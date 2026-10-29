import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from validate import validate  # noqa: E402

SECOES = ["Quando usar", "Quando não usar", "Componentes", "Combina com", "Notas"]


def ficha(tipo="plugin", dominios="[geral]", instalado_em="2026-10-15", omitir=None):
    corpo = "".join(f"## {s}\n- x\n\n" for s in SECOES if s != omitir)
    return (
        "---\n"
        "nome: X\n"
        f"tipo: {tipo}\n"
        f"dominios: {dominios}\n"
        "fonte: built-in\n"
        "superficies: [chat]\n"
        f"instalado_em: {instalado_em}\n"
        "---\n\n# X\n\nDescrição.\n\n" + corpo
    )


def index(secoes):
    """secoes: dict dominio -> lista de caminhos linkados."""
    linhas = ["# Índice", ""]
    for dom in ["geral", "desenvolvimento", "design", "pesquisa", "documentos", "engenharia-eletrica"]:
        linhas.append(f"## {dom}")
        for caminho in secoes.get(dom, []):
            linhas.append(f"- [X]({caminho}) · plugin · desc")
        linhas.append("")
    return "\n".join(linhas)


class ValidateTest(unittest.TestCase):
    def montar(self, arquivos, indice):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for pasta in ("plugins", "conectores", "agentes", "skills"):
            (root / pasta).mkdir()
        for caminho, conteudo in arquivos.items():
            (root / caminho).write_text(conteudo, encoding="utf-8")
        (root / "INDEX.md").write_text(indice, encoding="utf-8")
        return validate(root)

    def assertErro(self, erros, trecho):
        self.assertTrue(any(trecho in e for e in erros), f"{trecho!r} não está em {erros}")

    def test_repo_valido_sem_erros(self):
        erros = self.montar({"plugins/x.md": ficha()}, index({"geral": ["plugins/x.md"]}))
        self.assertEqual(erros, [])

    def test_dominio_invalido(self):
        erros = self.montar({"plugins/x.md": ficha(dominios="[dev]")}, index({}))
        self.assertErro(erros, "dominio invalido: dev")

    def test_ficha_ausente_no_indice(self):
        erros = self.montar(
            {"plugins/x.md": ficha(dominios="[geral, pesquisa]")},
            index({"geral": ["plugins/x.md"]}),
        )
        self.assertErro(erros, "x.md ausente em ## pesquisa")

    def test_ficha_em_secao_nao_declarada(self):
        erros = self.montar(
            {"plugins/x.md": ficha()},
            index({"geral": ["plugins/x.md"], "design": ["plugins/x.md"]}),
        )
        self.assertErro(erros, "x.md listada em ## design sem declarar")

    def test_link_quebrado(self):
        erros = self.montar({}, index({"geral": ["plugins/fantasma.md"]}))
        self.assertErro(erros, "link quebrado: plugins/fantasma.md")

    def test_secao_faltando(self):
        erros = self.montar(
            {"plugins/x.md": ficha(omitir="Notas")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "secao faltando: ## Notas")

    def test_sem_frontmatter(self):
        erros = self.montar({"plugins/x.md": "# X\n\nsem cabeçalho\n"}, index({}))
        self.assertErro(erros, "frontmatter ausente")

    def test_tipo_incoerente_com_pasta(self):
        erros = self.montar(
            {"plugins/x.md": ficha(tipo="conector")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "tipo conector nao combina com plugins/")

    def test_data_invalida(self):
        erros = self.montar(
            {"plugins/x.md": ficha(instalado_em="ontem")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "instalado_em invalido")
        ok = self.montar(
            {"plugins/x.md": ficha(instalado_em="desconhecido")},
            index({"geral": ["plugins/x.md"]}),
        )
        self.assertEqual(ok, [])

    def test_dominios_em_formato_nao_reconhecido(self):
        bloco = ficha(dominios="").replace("dominios: \n", "dominios:\n  - geral\n")
        erros = self.montar({"plugins/x.md": bloco}, index({}))
        self.assertErro(erros, "dominios deve ser lista [a, b] nao vazia")

    def test_dominios_vazio(self):
        erros = self.montar({"plugins/x.md": ficha(dominios="[]")}, index({}))
        self.assertErro(erros, "dominios deve ser lista [a, b] nao vazia")

    def test_link_quebrado_entre_fichas(self):
        conteudo = ficha().replace("## Combina com\n- x", "## Combina com\n- [Y](../conectores/y.md)")
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertErro(erros, "plugins/x.md: link quebrado: ../conectores/y.md")

    # --- robustez a edições realistas ---

    def test_heading_com_espaco_no_fim_e_aceito(self):
        conteudo = ficha().replace("## Notas\n", "## Notas   \n")
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertEqual(erros, [])

    def test_heading_dentro_de_bloco_de_codigo_nao_conta(self):
        conteudo = ficha(omitir="Notas") + "```\n## Notas\n```\n"
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertErro(erros, "secao faltando: ## Notas")

    def test_ordem_das_secoes(self):
        conteudo = ficha().replace("## Quando usar", "## TMP").replace(
            "## Quando não usar", "## Quando usar").replace("## TMP", "## Quando não usar")
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertErro(erros, "secoes fora de ordem")

    def test_bom_utf8_e_aceito(self):
        erros = self.montar({"plugins/x.md": "﻿" + ficha()}, index({"geral": ["plugins/x.md"]}))
        self.assertEqual(erros, [])

    def test_frontmatter_sem_quebra_final_e_lido(self):
        erros = self.montar({"plugins/x.md": "---\nnome: X\n---"}, index({}))
        self.assertFalse(any("frontmatter ausente" in e for e in erros), erros)

    def test_indice_aceita_prefixo_ponto_barra_e_ancora(self):
        erros = self.montar({"plugins/x.md": ficha()}, index({"geral": ["./plugins/x.md#notas"]}))
        self.assertEqual(erros, [])

    def test_indice_ignora_link_externo(self):
        erros = self.montar({}, index({"geral": ["https://github.com"]}))
        self.assertEqual(erros, [])

    def test_link_para_pasta_e_quebrado(self):
        erros = self.montar({}, index({"geral": ["plugins"]}))
        self.assertErro(erros, "link quebrado: plugins")

    def test_data_impossivel(self):
        erros = self.montar(
            {"plugins/x.md": ficha(instalado_em="2026-13-45")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "instalado_em invalido")

    def test_superficie_invalida(self):
        conteudo = ficha().replace("superficies: [chat]", "superficies: [web]")
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertErro(erros, "superficie invalida: web")

    def test_nome_vazio(self):
        conteudo = ficha().replace("nome: X", "nome:")
        erros = self.montar({"plugins/x.md": conteudo}, index({"geral": ["plugins/x.md"]}))
        self.assertErro(erros, "nome vazio")

    def test_dominio_duplicado(self):
        erros = self.montar(
            {"plugins/x.md": ficha(dominios="[geral, geral]")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "dominio duplicado: geral")

    def test_linha_duplicada_no_indice(self):
        erros = self.montar(
            {"plugins/x.md": ficha()}, index({"geral": ["plugins/x.md", "plugins/x.md"]})
        )
        self.assertErro(erros, "x.md duplicada em ## geral")

    def test_pasta_skills_e_validada(self):
        erros = self.montar(
            {"skills/x.md": ficha(tipo="skill", dominios="[dev]")}, index({"geral": ["skills/x.md"]})
        )
        self.assertErro(erros, "skills/x.md: dominio invalido: dev")

    def test_ficha_de_skill_valida(self):
        erros = self.montar(
            {"skills/x.md": ficha(tipo="skill")}, index({"geral": ["skills/x.md"]})
        )
        self.assertEqual(erros, [])

    def test_tipo_skill_fora_da_pasta_skills(self):
        erros = self.montar(
            {"plugins/x.md": ficha(tipo="skill")}, index({"geral": ["plugins/x.md"]})
        )
        self.assertErro(erros, "tipo skill nao combina com plugins/")


if __name__ == "__main__":
    unittest.main()

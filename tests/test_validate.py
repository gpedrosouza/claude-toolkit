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
        for pasta in ("plugins", "conectores", "agentes"):
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


if __name__ == "__main__":
    unittest.main()

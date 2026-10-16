"""Verifica a consistência entre as fichas e o INDEX.md. Não gera nada.

Uso: python3 scripts/validate.py [raiz]
"""
import re
import sys
from pathlib import Path

DOMINIOS = {"geral", "desenvolvimento", "design", "pesquisa", "documentos", "engenharia-eletrica"}
PASTAS = {"plugins": "plugin", "conectores": "conector", "agentes": "agente"}
CAMPOS = ["nome", "tipo", "dominios", "fonte", "superficies", "instalado_em"]
SECOES = ["Quando usar", "Quando não usar", "Componentes", "Combina com", "Notas"]
DATA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK = re.compile(r"\]\(([^)]+)\)")


def ler_frontmatter(texto):
    """Retorna dict do frontmatter, ou None se ausente."""
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    campos = {}
    for linha in m.group(1).splitlines():
        if ":" not in linha:
            continue
        chave, valor = linha.split(":", 1)
        valor = valor.split("#", 1)[0].strip()
        if valor.startswith("[") and valor.endswith("]"):
            valor = [v.strip() for v in valor[1:-1].split(",") if v.strip()]
        campos[chave.strip()] = valor
    return campos


def ler_indice(caminho):
    """Retorna dict dominio -> lista de caminhos linkados naquela seção."""
    secoes, atual = {}, None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            atual = linha[3:].strip()
            secoes.setdefault(atual, [])
        elif atual:
            secoes[atual].extend(LINK.findall(linha))
    return secoes


def validar_ficha(rel, texto):
    """Retorna (erros, dominios declarados)."""
    fm = ler_frontmatter(texto)
    if fm is None:
        return [f"{rel}: frontmatter ausente"], []
    erros = [f"{rel}: campo faltando: {c}" for c in CAMPOS if c not in fm]
    pasta = rel.split("/")[0]
    tipo = fm.get("tipo")
    if tipo and tipo != PASTAS[pasta]:
        erros.append(f"{rel}: tipo {tipo} nao combina com {pasta}/")
    dominios = fm.get("dominios") if isinstance(fm.get("dominios"), list) else []
    if "dominios" in fm and not dominios:
        erros.append(f"{rel}: dominios deve ser lista [a, b] nao vazia")
    erros += [f"{rel}: dominio invalido: {d}" for d in dominios if d not in DOMINIOS]
    data = fm.get("instalado_em")
    if data and data != "desconhecido" and not DATA.match(data):
        erros.append(f"{rel}: instalado_em invalido: {data}")
    erros += [f"{rel}: secao faltando: ## {s}" for s in SECOES if f"\n## {s}\n" not in texto]
    return erros, dominios


def validate(root):
    root = Path(root)
    erros, fichas = [], {}
    for pasta in PASTAS:
        for arquivo in sorted((root / pasta).glob("*.md")):
            rel = f"{pasta}/{arquivo.name}"
            texto = arquivo.read_text(encoding="utf-8")
            e, dominios = validar_ficha(rel, texto)
            erros += e
            erros += [
                f"{rel}: link quebrado: {l}"
                for l in LINK.findall(texto)
                if not l.startswith("http") and not (arquivo.parent / l).exists()
            ]
            fichas[rel] = dominios

    indice = root / "INDEX.md"
    if not indice.exists():
        return erros + ["INDEX.md ausente"]
    secoes = ler_indice(indice)

    for links in secoes.values():
        erros += [f"INDEX.md: link quebrado: {l}" for l in links if not (root / l).exists()]

    for rel, dominios in fichas.items():
        nome = rel.split("/")[-1]
        for d in dominios:
            if d in DOMINIOS and rel not in secoes.get(d, []):
                erros.append(f"INDEX.md: {nome} ausente em ## {d}")
        for secao, links in secoes.items():
            if rel in links and secao not in dominios:
                erros.append(f"INDEX.md: {nome} listada em ## {secao} sem declarar")
    return erros


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    erros = validate(root)
    if erros:
        print("\n".join(erros))
        sys.exit(1)
    n = sum(len(list((root / p).glob("*.md"))) for p in PASTAS)
    print(f"OK: {n} fichas")


if __name__ == "__main__":
    main()

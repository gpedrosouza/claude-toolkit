"""Verifica a consistência entre as fichas e o INDEX.md. Não gera nada.

Uso: python3 scripts/validate.py [raiz]
"""
import re
import sys
from datetime import date
from pathlib import Path

DOMINIOS = {"geral", "desenvolvimento", "design", "pesquisa", "documentos", "engenharia-eletrica"}
SUPERFICIES = {"chat", "claude-code"}
PASTAS = {"plugins": "plugin", "conectores": "conector", "agentes": "agente"}
CAMPOS = ["nome", "tipo", "dominios", "fonte", "superficies", "instalado_em"]
SECOES = ["Quando usar", "Quando não usar", "Componentes", "Combina com", "Notas"]
LINK = re.compile(r"\]\(([^)]+)\)")


def ler(arquivo):
    """Lê UTF-8 ignorando BOM."""
    return arquivo.read_text(encoding="utf-8-sig")


def alvo(link):
    """Caminho do link sem âncora; None para links externos."""
    if re.match(r"^[a-z]+:", link):
        return None
    return link.split("#", 1)[0]


def normalizar(link):
    """Forma canônica de um link do INDEX: sem './' nem âncora."""
    caminho = alvo(link)
    return caminho[2:] if caminho and caminho.startswith("./") else caminho


def data_valida(valor):
    try:
        date.fromisoformat(valor)
        return re.match(r"^\d{4}-\d{2}-\d{2}$", valor) is not None
    except ValueError:
        return False


def ler_frontmatter(texto):
    """Retorna dict do frontmatter, ou None se ausente."""
    m = re.match(r"^---\n(.*?)\n---(\n|$)", texto, re.S)
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


def headings(texto):
    """Títulos '## ' fora de blocos de código, sem espaços nas pontas."""
    titulos, em_codigo = [], False
    for linha in texto.splitlines():
        if linha.lstrip().startswith("```"):
            em_codigo = not em_codigo
        elif not em_codigo and linha.startswith("## "):
            titulos.append(linha[3:].strip())
    return titulos


def ler_indice(caminho):
    """Retorna dict dominio -> lista de links (crus) daquela seção."""
    secoes, atual = {}, None
    for linha in ler(caminho).splitlines():
        if linha.startswith("## "):
            atual = linha[3:].strip()
            secoes.setdefault(atual, [])
        elif atual:
            secoes[atual].extend(LINK.findall(linha))
    return secoes


def lista(fm, campo):
    valor = fm.get(campo)
    return valor if isinstance(valor, list) else []


def validar_ficha(rel, texto):
    """Retorna (erros, dominios declarados)."""
    fm = ler_frontmatter(texto)
    if fm is None:
        return [f"{rel}: frontmatter ausente"], []
    erros = [f"{rel}: campo faltando: {c}" for c in CAMPOS if c not in fm]
    if "nome" in fm and not fm["nome"]:
        erros.append(f"{rel}: nome vazio")

    pasta = rel.split("/")[0]
    tipo = fm.get("tipo")
    if tipo and tipo != PASTAS[pasta]:
        erros.append(f"{rel}: tipo {tipo} nao combina com {pasta}/")

    dominios = lista(fm, "dominios")
    if "dominios" in fm and not dominios:
        erros.append(f"{rel}: dominios deve ser lista [a, b] nao vazia")
    erros += [f"{rel}: dominio invalido: {d}" for d in dominios if d not in DOMINIOS]
    erros += [f"{rel}: dominio duplicado: {d}" for d in sorted(set(dominios)) if dominios.count(d) > 1]

    erros += [f"{rel}: superficie invalida: {s}" for s in lista(fm, "superficies") if s not in SUPERFICIES]

    data = fm.get("instalado_em")
    if data and data != "desconhecido" and not data_valida(data):
        erros.append(f"{rel}: instalado_em invalido: {data}")

    titulos = headings(texto)
    faltando = [s for s in SECOES if s not in titulos]
    erros += [f"{rel}: secao faltando: ## {s}" for s in faltando]
    if not faltando and [t for t in titulos if t in SECOES] != SECOES:
        erros.append(f"{rel}: secoes fora de ordem (esperado: {', '.join(SECOES)})")
    return erros, dominios


def validate(root):
    root = Path(root)
    erros, fichas = [], {}
    for pasta in PASTAS:
        for arquivo in sorted((root / pasta).glob("*.md")):
            rel = f"{pasta}/{arquivo.name}"
            texto = ler(arquivo)
            e, dominios = validar_ficha(rel, texto)
            erros += e
            for link in LINK.findall(texto):
                caminho = alvo(link)
                if caminho and not (arquivo.parent / caminho).is_file():
                    erros.append(f"{rel}: link quebrado: {link}")
            fichas[rel] = dominios

    indice = root / "INDEX.md"
    if not indice.exists():
        return erros + ["INDEX.md ausente"]
    secoes = {s: [normalizar(l) for l in links] for s, links in ler_indice(indice).items()}

    for secao, links in secoes.items():
        for l in links:
            if l is None:
                continue
            if not (root / l).is_file():
                erros.append(f"INDEX.md: link quebrado: {l}")
        for l in sorted({l for l in links if l and links.count(l) > 1}):
            erros.append(f"INDEX.md: {l.split('/')[-1]} duplicada em ## {secao}")

    for rel, dominios in fichas.items():
        nome = rel.split("/")[-1]
        for d in dict.fromkeys(dominios):
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

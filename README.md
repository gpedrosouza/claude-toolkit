# claude-toolkit

Dicionário dos plugins, conectores e agentes instalados no meu Claude, organizado por domínio. Serve para responder rápido: *neste projeto, quais ferramentas eu uso?*

Comece pelo [INDEX.md](INDEX.md). Cada linha leva a uma ficha curta.

## Estrutura

```
INDEX.md             uma linha por ferramenta, agrupado por domínio
plugins/             uma ficha por plugin
conectores/          uma ficha por conector MCP
agentes/             uma ficha por agente avulso
scripts/validate.py  verifica fichas × INDEX
```

Domínios: `geral`, `desenvolvimento`, `design`, `pesquisa`, `documentos`, `engenharia-eletrica`. Uma ferramenta pode ter vários.

Agentes que vêm dentro de um plugin ficam listados na ficha do plugin.

## Modelo da ficha

```markdown
---
nome: <nome de exibição>
tipo: plugin | conector | agente
dominios: [<domínio>, ...]
fonte: <URL do repo, "marketplace oficial" ou "built-in">
superficies: [chat, claude-code]
instalado_em: AAAA-MM-DD   # ou "desconhecido"
---

# <nome>

<1–2 frases: o que é>

## Quando usar
## Quando não usar
## Componentes
## Combina com
## Notas
```

Arquivo: slug do nome (`google-drive.md`). Ficha cabe numa tela.

## Regras para o Claude

1. **Instalação** — ao instalar algo a pedido do Guilherme: criar a ficha, adicionar a linha em cada domínio no INDEX e commitar, no mesmo pedido.
2. **Início de projeto** — ler só o INDEX, identificar os domínios do projeto e propor as ferramentas desse recorte mais as de `geral`. Abrir fichas só das escolhidas. Esperar aprovação antes de usar.
3. **Remoção** — ao desinstalar algo: apagar a ficha, suas linhas no INDEX e os links para ela em "Combina com" de outras fichas, e commitar. Exceção: `anthropic-skills` (vem com o Claude).
4. Rodar `python3 scripts/validate.py` antes de cada commit.

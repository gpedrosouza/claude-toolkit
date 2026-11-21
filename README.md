# claude-toolkit

> **EN —** My operating manual for working with AI agents. It catalogs every plugin, MCP connector, sub-agent and skill installed in my Claude setup, grouped by domain, so an agent can read a ~1.5k-token index at the start of a project and propose only the tools that fit. It also versions my global and per-project `CLAUDE.md` templates, and a validator keeps the index and the cards in sync.

Dicionário dos plugins, conectores e agentes instalados no meu Claude, organizado por domínio. Serve para responder rápido: *neste projeto, quais ferramentas eu uso?*

**Por que existe:** com dezenas de ferramentas instaladas, carregar tudo em cada sessão gasta contexto e confunde o agente. Aqui o agente lê só o `INDEX.md`, escolhe o recorte do projeto e abre a ficha apenas do que vai usar. Os modelos de `CLAUDE.md` padronizam como cada projeto meu começa com o Claude Code.

Comece pelo [INDEX.md](INDEX.md). Cada linha leva a uma ficha curta.

## Estrutura

```
INDEX.md             uma linha por ferramenta, agrupado por domínio
plugins/             uma ficha por plugin
conectores/          uma ficha por conector MCP
agentes/             uma ficha por agente avulso
skills/              uma ficha por skill avulsa (fora de plugin)
scripts/validate.py  verifica fichas × INDEX
modelos/             CLAUDE.md global (cópia versionada) e modelo para projetos novos
docs/ideias/         ideias para adotar em projetos futuros
```

**Projeto novo:** copie `modelos/CLAUDE.projeto.md` para a raiz do repo como `CLAUDE.md` e preencha. **Mudou o global?** Atualize `modelos/CLAUDE.global.md` junto com `~/.claude/CLAUDE.md`.

Domínios: `geral`, `desenvolvimento`, `design`, `pesquisa`, `documentos`, `engenharia-eletrica`. Uma ferramenta pode ter vários.

Agentes que vêm dentro de um plugin ficam listados na ficha do plugin.

## Modelo da ficha

```markdown
---
nome: <nome de exibição>
tipo: plugin | conector | agente | skill
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

Arquivo: slug do nome (`google-drive.md`). Ficha cabe numa tela. Seções nesta ordem.

## Linha do INDEX

```markdown
- [Superpowers](plugins/superpowers.md) · plugin · metodologia de dev: brainstorming → plano → TDD → revisão
```

A ficha aparece sob cada `## <domínio>` que declara. Ordem em cada seção: plugins, conectores, agentes; alfabética dentro de cada tipo.

## Regras para o Claude

1. **Instalação** — ao instalar algo a pedido do Guilherme: criar a ficha, adicionar a linha em cada domínio no INDEX e commitar, no mesmo pedido.
2. **Início de projeto** — ler só o INDEX, identificar os domínios do projeto e propor as ferramentas desse recorte mais as de `geral`. Abrir fichas só das escolhidas. Esperar aprovação antes de usar.
3. **Remoção** — ao desinstalar algo: apagar a ficha, suas linhas no INDEX e os links para ela em "Combina com" de outras fichas, e commitar. Exceção: `anthropic-skills` (vem com o Claude).
4. Rodar `python3 scripts/validate.py` antes de cada commit.

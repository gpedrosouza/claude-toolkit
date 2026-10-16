# Dicionário de plugins, conectores e agentes — Design

**Data:** 2026-10-15
**Repo:** `gpedrosouza/claude-toolkit` (GitHub)
**Status:** aguardando revisão

## Objetivo

Um catálogo em markdown de tudo que está instalado no Claude do Guilherme
(plugins, conectores MCP, agentes), organizado por domínio, para responder
rápido à pergunta: *"neste projeto, quais ferramentas eu uso?"*

Serve a dois leitores:

- **Guilherme** — consulta e decide o que ativar.
- **Claude** — lê o índice no início de um projeto e propõe as ferramentas
  daquele recorte.

### Critérios de sucesso

- Ler só o `INDEX.md` basta para escolher ferramentas (~1,5k tokens).
- Toda ferramenta instalada tem ficha; nenhuma ficha de coisa desinstalada.
- Uma ficha nova leva um commit, sem script nem build.

## Escopo

- **Entra:** apenas o que está instalado/conectado.
- **Não entra:** candidatos pesquisados, comparações entre ferramentas
  (revisitar se surgir necessidade real).

## Domínios

| Domínio | Para quê |
|---|---|
| `geral` | amadurecer ideias, planejar, verificar — vale para qualquer projeto |
| `desenvolvimento` | código: TDD, debug, review, arquitetura, git |
| `design` | UI/UX, Figma, crítica de design, acessibilidade |
| `pesquisa` | literatura acadêmica, busca de papers, revisão |
| `documentos` | Word, PDF, planilhas, apresentações, Drive |
| `engenharia-eletrica` | simulação e cálculo (começa vazio) |

Uma ferramenta pode ter vários domínios.

## Estrutura do repo

```
claude-toolkit/
├── README.md        regras do repo + como o Claude usa o dicionário
├── INDEX.md         uma linha por ferramenta, agrupado por domínio
├── plugins/         uma ficha por plugin
├── conectores/      uma ficha por conector MCP
├── agentes/         uma ficha por agente avulso (não vindo de plugin)
└── docs/superpowers/specs/   specs de design do próprio repo
```

Agentes que vêm dentro de um plugin (ex.: `research-superpowers:drafter`)
são listados na ficha do plugin, não em `agentes/`.

Quando um plugin e um conector têm o mesmo nome (Figma), cada um tem sua
ficha e uma aponta para a outra em "Combina com".

## Modelo da ficha

```markdown
---
nome: <nome de exibição>
tipo: plugin | conector | agente
dominios: [<domínio>, ...]
fonte: <URL do repo ou "marketplace oficial" / "built-in">
superficies: [chat, claude-code]
instalado_em: AAAA-MM-DD
---

# <nome>

<1–2 frases: o que é>

## Quando usar
- <gatilho concreto>

## Quando não usar
- <situação em que atrapalha>

## Componentes
| Skill / ferramenta | Para quê |
|---|---|

## Combina com
- <outra ferramenta do dicionário>

## Notas
- <aprendizados de uso; começa vazio ou com o essencial>
```

Nome do arquivo: slug do nome (`superpowers.md`, `google-drive.md`).

## Formato do INDEX

```markdown
## desenvolvimento
- [Superpowers](plugins/superpowers.md) · plugin · metodologia de dev: brainstorming → plano → TDD
```

Uma ferramenta aparece em cada domínio que declara. O INDEX é mantido à
mão pelo Claude; revisitar automação se passar de ~100 itens.

## Fluxos

1. **Instalação** — ao instalar algo a pedido do Guilherme: criar ficha,
   adicionar linhas no INDEX, commitar. Tudo no mesmo pedido.
2. **Início de projeto** — ler o INDEX, identificar domínios do projeto,
   propor as ferramentas do recorte + `geral`; Guilherme aprova.
3. **Remoção** — apagar ficha e linhas do INDEX, commitar. O git guarda
   o histórico.

### Como o Claude lembra de consultar

- **Chat:** entrada na memória do Claude apontando para o repo.
- **Claude Code:** uma linha no `~/.claude/CLAUDE.md` global apontando
  para o repo.

## Inventário inicial (catalogar na criação)

**Plugins (8):** Superpowers, research-superpowers, LR-AI (lit-review),
paper-search, Figma, design, engineering, cowork-plugin-management.

**Conectores (5):** Google Drive, Figma, Elicit, Consensus, Canva
(Canva está instalado mas precisa reconectar — registrar em Notas).

**Skills built-in da Anthropic:** uma ficha única `anthropic-skills`
(docx, pdf, xlsx, pptx, docs, deep-research etc.), em `plugins/`, com
`fonte: built-in`.

**Agentes avulsos:** Explore, Plan, general-purpose, claude-code-guide
— uma ficha cada em `agentes/`. `statusline-setup` e `claude` (genérico)
ficam de fora por não mudarem a escolha de ferramentas.

## Fora do escopo

- Script gerador de INDEX
- Status `candidato`/`descartado`
- Páginas de comparação
- Qualquer automação de instalação

## Pré-requisitos

- Guilherme cria o repo vazio `gpedrosouza/claude-toolkit` no GitHub
  (ou autoriza o Claude a criar, se o acesso permitir).

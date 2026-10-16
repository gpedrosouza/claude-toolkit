# Dicionário de ferramentas (claude-toolkit) — Plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar o repo `claude-toolkit` com README, INDEX e uma ficha por ferramenta instalada, validado por um script e publicado no GitHub.

**Architecture:** Markdown puro em pastas por tipo (`plugins/`, `conectores/`, `agentes/`), domínios como campo de frontmatter, `INDEX.md` mantido à mão. Um validador em Python stdlib garante que fichas e INDEX estão consistentes — é o "teste" de cada tarefa.

**Tech Stack:** Markdown, Python 3 (stdlib apenas: `pathlib`, `re`, `unittest`), git, `gh` CLI.

**Spec:** `docs/superpowers/specs/2026-10-15-dicionario-plugins-design.md`

## Global Constraints

- Idioma de todo o conteúdo: português.
- Domínios válidos (exatamente): `geral`, `desenvolvimento`, `design`, `pesquisa`, `documentos`, `engenharia-eletrica`.
- `tipo` ∈ {`plugin`, `conector`, `agente`} e deve casar com a pasta (`plugins/`→plugin, `conectores/`→conector, `agentes/`→agente).
- Campos obrigatórios do frontmatter: `nome`, `tipo`, `dominios`, `fonte`, `superficies`, `instalado_em`.
- `instalado_em`: `AAAA-MM-DD` ou `desconhecido` (instalações anteriores a hoje não têm data conhecida).
- Seções obrigatórias, nesta ordem: `## Quando usar`, `## Quando não usar`, `## Componentes`, `## Combina com`, `## Notas`.
- Nome de arquivo = slug do nome (minúsculas, hífens).
- Linha do INDEX: `- [<nome>](<pasta>/<slug>.md) · <tipo> · <descrição curta>`; a ficha aparece sob cada `## <domínio>` que declara, e só neles.
- Fichas curtas: corpo cabe numa tela (~40 linhas). Nada de reproduzir documentação.
- Validador não gera nada — só verifica (gerador de INDEX está fora do escopo).
- Commits terminam com:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_018PmR8ZZRL5DRCgZZDPR1mr
  ```

## Review Focus

1. Domínio escrito errado no frontmatter (`engenharia_eletrica`, `dev`) → validador acusa domínio inválido.
2. Ficha que declara um domínio mas não aparece naquela seção do INDEX (ou aparece numa seção não declarada) → erro.
3. Link no INDEX apontando para arquivo inexistente (renomeou/apagou ficha) → erro.
4. Ficha sem uma das seções obrigatórias ou sem frontmatter → erro, não crash.
5. `tipo` incoerente com a pasta (ficha de conector salva em `plugins/`) → erro.

Todos os cinco têm teste na Task 1.

---

### Task 1: Esqueleto do repo + validador

**Files:**
- Create: `README.md`, `INDEX.md`, `scripts/validate.py`, `tests/test_validate.py`
- Create: `plugins/.gitkeep`, `conectores/.gitkeep`, `agentes/.gitkeep`

**Interfaces:**
- Produces: `validate(root: Path) -> list[str]` (lista de mensagens de erro; vazia = ok) em `scripts/validate.py`. CLI: `python3 scripts/validate.py [root]` imprime erros e sai com código 1, ou imprime `OK: <n> fichas` e sai 0. Todas as tarefas seguintes usam esse comando como verificação.

- [ ] **Step 1: Escrever os testes que falham** (`tests/test_validate.py`, `unittest`, cada teste monta um repo mínimo em `tempfile.TemporaryDirectory`)

  - `test_repo_valido_sem_erros` — uma ficha válida em `plugins/x.md` com `dominios: [geral]` e linha correspondente sob `## geral` → `validate(root) == []`.
  - `test_dominio_invalido` — `dominios: [dev]` → algum erro contém `"dominio invalido: dev"`.
  - `test_ficha_ausente_no_indice` — ficha declara `[geral, pesquisa]`, INDEX só tem em `geral` → erro contém `"x.md ausente em ## pesquisa"`.
  - `test_ficha_em_secao_nao_declarada` — INDEX lista sob `## design` sem declarar → erro contém `"x.md listada em ## design sem declarar"`.
  - `test_link_quebrado` — INDEX aponta `plugins/fantasma.md` → erro contém `"link quebrado: plugins/fantasma.md"`.
  - `test_secao_faltando` — ficha sem `## Notas` → erro contém `"secao faltando: ## Notas"`.
  - `test_sem_frontmatter` — arquivo sem `---` → erro contém `"frontmatter ausente"` (não levanta exceção).
  - `test_tipo_incoerente_com_pasta` — `tipo: conector` em `plugins/` → erro contém `"tipo conector nao combina com plugins/"`.
  - `test_data_invalida` — `instalado_em: ontem` → erro contém `"instalado_em invalido"`; `desconhecido` é aceito.

- [ ] **Step 2: Rodar e ver falhar**

  Run: `python3 -m unittest discover -s tests -v`
  Expected: FAIL / ImportError (`validate` não existe)

- [ ] **Step 3: Implementar `validate(root: Path) -> list[str]` em `scripts/validate.py`**

  Frontmatter parseado com regex simples (`chave: valor`; listas no formato `[a, b]`) — sem PyYAML. INDEX parseado por seção `## <domínio>` e links `](caminho)`. Ignorar `.gitkeep` e `README.md`/`INDEX.md` ao varrer as pastas. Mensagens de erro prefixadas com o caminho relativo da ficha.

- [ ] **Step 4: Rodar e ver passar**

  Run: `python3 -m unittest discover -s tests -v`
  Expected: 9 testes OK

- [ ] **Step 5: Escrever `README.md` e `INDEX.md`**

  `INDEX.md`: título `# Índice`, uma linha explicando o formato, e as seis seções `## geral`, `## desenvolvimento`, `## design`, `## pesquisa`, `## documentos`, `## engenharia-eletrica` (vazias por ora; sob `engenharia-eletrica` uma linha `_Nada instalado ainda._`, que o validador deve ignorar por não ser link).

  `README.md` (curto) com: objetivo (1 parágrafo), estrutura de pastas, o modelo da ficha copiado da spec, formato da linha do INDEX, e as **regras para o Claude** — os três fluxos da spec (instalação → ficha + INDEX + commit no mesmo pedido; início de projeto → ler só o INDEX, propor recorte + `geral`, esperar aprovação; remoção → apagar ficha e linhas) e "rodar `python3 scripts/validate.py` antes de cada commit".

- [ ] **Step 6: Validar**

  Run: `python3 scripts/validate.py`
  Expected: `OK: 0 fichas`

- [ ] **Step 7: Commit** — `feat: esqueleto do repo e validador`

---

### Task 2: Fichas de desenvolvimento e geral

**Files:** Create `plugins/superpowers.md`, `plugins/engineering.md`, `plugins/cowork-plugin-management.md`; Modify `INDEX.md`

**Interfaces:** Consumes `python3 scripts/validate.py` (Task 1).

| Ficha | dominios | fonte | superficies | instalado_em |
|---|---|---|---|---|
| Superpowers | [desenvolvimento, geral] | https://github.com/obra/superpowers | [chat, claude-code] | 2026-10-15 |
| engineering | [desenvolvimento] | marketplace oficial | [chat, claude-code] | desconhecido |
| cowork-plugin-management | [geral] | marketplace oficial | [chat, claude-code] | desconhecido |

Conteúdo: Superpowers segue o exemplo aprovado no brainstorming (componentes = as 15 skills do plugin; Notas: "rende mais no Claude Code que no chat"; "brainstorming não serve para pesquisa acadêmica — usar brainstorming-research"). engineering: componentes = architecture, code-review, debug, deploy-checklist, documentation, incident-response, standup, system-design, tech-debt, testing-strategy; "Quando não usar": fluxo completo de feature nova → Superpowers. Combina com: Superpowers ↔ engineering.

- [ ] **Step 1:** Escrever as três fichas e as linhas no INDEX (Superpowers em `geral` e `desenvolvimento`).
- [ ] **Step 2:** `python3 scripts/validate.py` → `OK: 3 fichas`
- [ ] **Step 3:** Commit — `docs: fichas de desenvolvimento e geral`

---

### Task 3: Fichas de pesquisa

**Files:** Create `plugins/research-superpowers.md`, `plugins/lr-ai.md`, `plugins/paper-search.md`, `conectores/elicit.md`, `conectores/consensus.md`; Modify `INDEX.md`

| Ficha | dominios | superficies |
|---|---|---|
| research-superpowers | [pesquisa] | [chat, claude-code] |
| LR-AI | [pesquisa] | [chat, claude-code] |
| paper-search | [pesquisa] | [chat, claude-code] |
| Elicit | [pesquisa] | [chat] |
| Consensus | [pesquisa] | [chat] |

Todas `instalado_em: desconhecido`. research-superpowers: Componentes inclui as skills e os agentes do plugin (analyst, drafter, literature-scout, peer-reviewer, source-acquirer, source-ingester, wiki-linter); Notas: "foco original em teologia/arqueologia/humanidades digitais — fontes e checklists podem não servir para engenharia". LR-AI: Notas: "export para Google Sheets depende de Composio". Elicit vs Consensus vs paper-search: cada "Quando usar" diz o diferencial (Elicit = análise/relatórios/revisão sistemática; Consensus = resposta rápida baseada em evidência com citações; paper-search = busca e lookup por DOI via OpenAlex, sem conta).

- [ ] **Step 1:** Escrever as cinco fichas e linhas no INDEX.
- [ ] **Step 2:** `python3 scripts/validate.py` → `OK: 8 fichas`
- [ ] **Step 3:** Commit — `docs: fichas de pesquisa`

---

### Task 4: Fichas de design

**Files:** Create `plugins/figma.md`, `plugins/design.md`, `conectores/figma.md`, `conectores/canva.md`; Modify `INDEX.md`

| Ficha | dominios | superficies |
|---|---|---|
| Figma (plugin) | [design, desenvolvimento] | [chat, claude-code] |
| design | [design] | [chat, claude-code] |
| Figma (conector) | [design] | [chat] |
| Canva | [design, documentos] | [chat] |

Todas `instalado_em: desconhecido`. Plugin Figma: componentes = skills `figma-*`; "Combina com" aponta o conector e vice-versa ("o plugin traz as instruções; o conector traz o acesso aos arquivos"). Canva — Notas: "instalado, mas precisa reconectar (status em 2026-10-15)". Nomes no INDEX diferenciam: `Figma (plugin)` e `Figma (conector)`.

- [ ] **Step 1:** Escrever as quatro fichas e linhas no INDEX.
- [ ] **Step 2:** `python3 scripts/validate.py` → `OK: 12 fichas`
- [ ] **Step 3:** Commit — `docs: fichas de design`

---

### Task 5: Fichas de documentos

**Files:** Create `plugins/anthropic-skills.md`, `conectores/google-drive.md`; Modify `INDEX.md`

| Ficha | dominios | fonte | superficies |
|---|---|---|---|
| anthropic-skills | [documentos, geral] | built-in | [chat, claude-code] |
| Google Drive | [documentos, pesquisa] | marketplace oficial | [chat] |

`instalado_em: desconhecido`. anthropic-skills: Componentes agrupados em três linhas da tabela — arquivos (docx, pdf, pdf-reading, xlsx, pptx, file-reading), docs/artefatos (docs, google-workspace, artifact-design, dataviz), utilidades (deep-research, skill-creator, import-memory, morning). Notas: "vêm com o Claude, não precisam ser instaladas; não remover a ficha no fluxo de remoção".

- [ ] **Step 1:** Escrever as duas fichas e linhas no INDEX.
- [ ] **Step 2:** `python3 scripts/validate.py` → `OK: 14 fichas`
- [ ] **Step 3:** Commit — `docs: fichas de documentos`

---

### Task 6: Fichas de agentes

**Files:** Create `agentes/explore.md`, `agentes/plan.md`, `agentes/general-purpose.md`, `agentes/claude-code-guide.md`; Modify `INDEX.md`

| Ficha | dominios |
|---|---|
| Explore | [desenvolvimento] |
| Plan | [desenvolvimento, geral] |
| general-purpose | [geral] |
| claude-code-guide | [geral] |

Todas `tipo: agente`, `fonte: built-in`, `superficies: [chat, claude-code]`, `instalado_em: desconhecido`. Componentes = as ferramentas a que o agente tem acesso (ex.: Explore é só leitura). "Quando não usar" de todos: tarefas pequenas — cada agente começa sem contexto e custa mais tokens.

- [ ] **Step 1:** Escrever as quatro fichas e linhas no INDEX.
- [ ] **Step 2:** `python3 scripts/validate.py` → `OK: 18 fichas`
- [ ] **Step 3:** Commit — `docs: fichas de agentes`

---

### Task 7: Publicar e ligar ao Claude

**Files:** nenhum no repo (exceto se o push exigir ajuste)

- [ ] **Step 1:** `gh auth status` — se autenticado como `gpedrosouza`, `gh repo create gpedrosouza/claude-toolkit --private --source . --push`. Se não, parar e pedir ao Guilherme que crie o repo vazio; então `git remote add origin … && git push -u origin main`.
- [ ] **Step 2:** Verificar: `git ls-remote origin main` retorna o hash do último commit local.
- [ ] **Step 3:** Memória do Claude: atualizar `/areas/dicionario-plugins.md` com o link do repo e o status "publicado".
- [ ] **Step 4:** Claude Code: entregar ao Guilherme a linha para o `~/.claude/CLAUDE.md` global (ou escrever via pasta conectada, se ele conceder acesso):
  ```
  - Dicionário de ferramentas: github.com/gpedrosouza/claude-toolkit — ao iniciar um projeto, leia INDEX.md e proponha as ferramentas do recorte; ao instalar algo, crie a ficha conforme README.md.
  ```

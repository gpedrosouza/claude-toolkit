---
nome: Superpowers
tipo: plugin
dominios: [desenvolvimento, geral]
fonte: https://github.com/obra/superpowers
superficies: [chat, claude-code]
instalado_em: 2026-10-15
---

# Superpowers

Metodologia de desenvolvimento em skills encadeadas: ideia → design → plano → implementação com TDD → revisão. As skills disparam sozinhas conforme a etapa.

## Quando usar
- Começar qualquer projeto ou feature nova: `brainstorming` antes de escrever código
- Transformar um design aprovado em tarefas pequenas e executá-las
- Bug difícil de achar: `systematic-debugging`

## Quando não usar
- Tarefas fora de código (estudo, documentos, currículo): o fluxo fica pesado demais
- Pesquisa acadêmica: usar o `brainstorming-research` do research-superpowers

## Componentes
| Skill | Para quê |
|---|---|
| brainstorming | amadurecer a ideia e escrever a spec |
| writing-plans | quebrar a spec em tarefas com testes |
| executing-plans | executar o plano na própria sessão (mais barato) |
| subagent-driven-development | um agente por tarefa + revisor (mais rigoroso) |
| dispatching-parallel-agents | tarefas independentes em paralelo |
| test-driven-development | ciclo red-green-refactor |
| systematic-debugging | achar a causa raiz antes de corrigir |
| verification-before-completion | provar que funciona antes de dizer que terminou |
| requesting-code-review / receiving-code-review | pedir e responder revisão |
| using-git-worktrees / finishing-a-development-branch | isolar o trabalho e fechar a branch |
| writing-skills | criar skills novas |
| diagnosing-superpowers | entender por que uma sessão deu errado |
| using-superpowers | introdução ao sistema |

## Combina com
- [engineering](engineering.md): code-review, architecture, deploy-checklist avulsos

## Notas
- Rende mais no Claude Code do que no chat.
- Para mudanças pequenas, o brainstorming aceita um design curto no chat, sem spec.

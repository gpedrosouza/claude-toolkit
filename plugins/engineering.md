---
nome: engineering
tipo: plugin
dominios: [desenvolvimento]
fonte: marketplace oficial
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# engineering

Skills avulsas para o dia a dia de engenharia de software: revisão, debug, decisões de arquitetura, deploy e documentação. Cada uma resolve uma tarefa isolada.

## Quando usar
- Revisar um diff ou PR antes de mergear
- Registrar uma decisão de arquitetura (ADR) ou desenhar um sistema
- Preparar um deploy, responder a um incidente, escrever README/runbook

## Quando não usar
- Fluxo completo de feature nova: usar o Superpowers (brainstorming → plano → TDD)

## Componentes
| Skill | Para quê |
|---|---|
| architecture | ADR, comparar tecnologias |
| system-design | APIs, modelagem de dados, fronteiras de serviço |
| code-review | segurança, performance, correção de um diff |
| debug | reproduzir, isolar, diagnosticar, corrigir |
| testing-strategy | plano e estratégia de testes |
| tech-debt | levantar e priorizar dívida técnica |
| deploy-checklist | verificação antes de ir para produção |
| incident-response | triagem, comunicação e postmortem |
| documentation | README, docs de API, runbooks |
| standup | resumo de atividade para a daily |

## Combina com
- [Superpowers](superpowers.md): metodologia completa; engineering cobre tarefas soltas

## Notas
- Sobreposições com o Superpowers: `debug` ≈ `systematic-debugging`, `code-review` ≈ `requesting-code-review`.

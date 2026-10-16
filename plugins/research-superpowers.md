---
nome: research-superpowers
tipo: plugin
dominios: [pesquisa]
fonte: marketplace oficial
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# research-superpowers

Fluxo completo de pesquisa acadêmica, no estilo do Superpowers: ideia → plano pré-registrado → literatura → ingestão em wiki → análise → manuscrito → revisão por pares. Cada fonte vira uma página de wiki focada na pergunta de pesquisa.

## Quando usar
- Projeto de pesquisa longo, como o TCC ou um artigo: do recorte da pergunta até o texto
- Manter uma biblioteca de PDFs + BibTeX e uma wiki de fontes ao longo de meses

## Quando não usar
- Achar um paper ou responder uma pergunta pontual: Consensus ou paper-search
- Revisão de literatura que termina numa planilha: LR-AI é mais direto

## Componentes
| Skill / agente | Para quê |
|---|---|
| brainstorming-research → writing-research-plan → executing-research-plan | da ideia ao plano executado |
| literature-review, acquire-sources, add-to-library | buscar, baixar e catalogar fontes |
| ingest-source | fonte → página de wiki focada |
| wiki-lint, semantic-wiki-review, wiki-graph, drift-report | manter a wiki consistente |
| drafting-manuscript, requesting-peer-review | escrever e revisar o texto |
| finishing-a-research-project, grant-finder, scaffold-research-project | fechar, financiar, iniciar |
| agentes: analyst, drafter, literature-scout, peer-reviewer, source-acquirer, source-ingester, wiki-linter | executores chamados pelas skills acima |

## Combina com
- [paper-search](paper-search.md) e [Elicit](../conectores/elicit.md) para busca
- [Google Drive](../conectores/google-drive.md) para PDFs guardados

## Notas
- Foco original em teologia, arqueologia e humanidades digitais: as bases (IxTheo, Zenon-DAI…), o `grant-finder` (fomento alemão/europeu) e os checklists de revisão podem não servir para engenharia.

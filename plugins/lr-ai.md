---
nome: LR-AI
tipo: plugin
dominios: [pesquisa]
fonte: marketplace oficial
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# LR-AI

Revisão de literatura automatizada: papers-semente, busca booleana em bases, snowballing de citações, triagem por IA e categorização, entregues numa planilha.

## Quando usar
- Mapear o estado da arte de um tema (ex.: capítulo de revisão do TCC)
- Partir de poucos papers conhecidos e expandir por citações

## Quando não usar
- Pergunta pontual: Consensus responde mais rápido
- Projeto que também precisa de wiki e manuscrito: research-superpowers

## Componentes
| Skill | Para quê |
|---|---|
| lit-review | fluxo completo, de ponta a ponta |
| seed-search | definir tema, perguntas, critérios e papers-semente |
| database-search | busca booleana em OpenAlex, Semantic Scholar, arXiv |
| snowball | citações para frente e para trás |
| screen-papers | filtros + triagem por título/resumo |
| categorize-papers | taxonomia, resumos e prioridade de leitura |
| export-sheet | Google Sheet + Excel com abas de visão geral e método (PRISMA) |
| setup | diagnóstico de dependências e chaves de API |
| agente paper-screener | triagem de um lote de papers |

## Combina com
- [paper-search](paper-search.md) para lookups pontuais por DOI

## Notas
- O export para Google Sheets depende do Composio; o Excel funciona sem ele.

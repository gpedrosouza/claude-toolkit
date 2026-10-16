---
nome: Elicit
tipo: conector
dominios: [pesquisa]
fonte: marketplace oficial
superficies: [chat]
instalado_em: desconhecido
---

# Elicit

Conector com a sua conta Elicit: busca e análise de papers, relatórios gerados, revisões sistemáticas e uma biblioteca pessoal de fontes.

## Quando usar
- Relatório de pesquisa sobre uma pergunta, com extração de dados dos papers
- Revisão sistemática guiada
- Guardar e consultar uma coleção de papers, incluindo PDFs que você sobe

## Quando não usar
- Resposta rápida de "o que a evidência diz": Consensus
- Busca simples sem conta: paper-search

## Componentes
| Ferramentas | Para quê |
|---|---|
| search_papers, search_trials | buscar papers e ensaios clínicos |
| create_report, create_systematic_review | relatório e revisão sistemática |
| agent_session (create, send, get…) | sessão de pesquisa conduzida pelo agente do Elicit |
| library (save, search, import, collections) | biblioteca pessoal de fontes |

## Combina com
- [research-superpowers](../plugins/research-superpowers.md) para levar fontes à wiki

## Notas
- Usa a cota da sua conta Elicit (`get_usage` mostra o consumo).

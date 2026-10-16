---
nome: claude-code-guide
tipo: agente
dominios: [geral]
fonte: built-in
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# claude-code-guide

Agente que responde dúvidas sobre o próprio ecossistema Claude: Claude Code, API, Agent SDK e plugins, consultando a documentação.

## Quando usar
- "Como configuro hooks / MCP / slash commands no Claude Code?"
- Dúvidas de API (tool use, prompt caching, SDK) ou sobre avaliar plugins

## Quando não usar
- Dúvidas sobre o seu próprio código: Explore ou leitura direta
- Pergunta pequena que o Claude responde direto: o agente começa sem contexto e custa mais tokens

## Componentes
| Acesso | Detalhe |
|---|---|
| ferramentas | Glob, Grep, Read, WebFetch, WebSearch |

## Combina com
- [cowork-plugin-management](../plugins/cowork-plugin-management.md) ao criar plugins

## Notas
- Se já houver um em andamento na conversa, continuar o mesmo em vez de abrir outro.

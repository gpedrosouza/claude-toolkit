---
nome: general-purpose
tipo: agente
dominios: [geral]
fonte: built-in
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# general-purpose

Agente genérico com todas as ferramentas, para pesquisar ou executar uma tarefa de várias etapas num contexto separado.

## Quando usar
- Busca incerta, que vai exigir várias tentativas
- Tarefas independentes em paralelo (com `dispatching-parallel-agents` do Superpowers)

## Quando não usar
- Tarefa que você mesmo resolveria em poucos passos: o agente começa do zero e custa mais

## Componentes
| Acesso | Detalhe |
|---|---|
| ferramentas | todas |

## Combina com
- [Superpowers](../plugins/superpowers.md): `subagent-driven-development` e `dispatching-parallel-agents` usam agentes assim

## Notas
- O resultado volta só para o Claude; ele repassa o que importa.

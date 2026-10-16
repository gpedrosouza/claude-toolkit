---
nome: Plan
tipo: agente
dominios: [desenvolvimento, geral]
fonte: built-in
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# Plan

Agente arquiteto: estuda o código e devolve um plano de implementação passo a passo, com arquivos críticos e trade-offs.

## Quando usar
- Mudança grande num código existente, quando você quer uma segunda visão de arquitetura sem poluir a conversa

## Quando não usar
- Já está no fluxo do Superpowers: `writing-plans` faz esse papel com mais estrutura
- Mudança pequena

## Componentes
| Acesso | Detalhe |
|---|---|
| ferramentas | só leitura e busca; não edita arquivos |

## Combina com
- [Explore](explore.md) para localizar antes de planejar
- [Superpowers](../plugins/superpowers.md): alternativa mais completa

## Notas
- Começa sem contexto: o pedido precisa dizer objetivo e restrições.

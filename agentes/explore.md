---
nome: Explore
tipo: agente
dominios: [desenvolvimento]
fonte: built-in
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# Explore

Agente de busca somente leitura. Varre muitos arquivos e devolve só a conclusão, sem despejar o conteúdo no contexto principal.

## Quando usar
- "Onde está implementado X?" num repositório grande ou desconhecido
- Mapear convenções de nome e estrutura antes de mexer no código

## Quando não usar
- Arquivo ou função já conhecidos: ler direto sai mais barato
- Revisar ou auditar código: ele localiza, não avalia

## Componentes
| Acesso | Detalhe |
|---|---|
| ferramentas | todas, exceto editar/escrever arquivos e publicar artefatos |
| amplitude | pedir "medium" ou "very thorough" |

## Combina com
- [Plan](plan.md): Explore localiza, Plan desenha a mudança

## Notas
- Cada chamada começa sem contexto e custa tokens próprios; só vale quando a busca é ampla.

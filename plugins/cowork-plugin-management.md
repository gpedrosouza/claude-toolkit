---
nome: cowork-plugin-management
tipo: plugin
dominios: [geral]
fonte: marketplace oficial
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# cowork-plugin-management

Cria plugins do zero e customiza plugins instalados: skills, conectores MCP e comportamento.

## Quando usar
- Empacotar um fluxo que se repete (ex.: rotina da GR, padrão de relatório) como plugin próprio
- Ajustar um plugin instalado ao seu jeito de trabalhar

## Quando não usar
- Criar uma skill isolada: `skill-creator` (anthropic-skills) ou `writing-skills` (Superpowers) bastam

## Componentes
| Skill | Para quê |
|---|---|
| create-cowork-plugin | criar plugin novo |
| cowork-plugin-customizer | customizar plugin existente |

## Combina com
- [anthropic-skills](anthropic-skills.md): `skill-creator` para skills avulsas

## Notas
- Plugin novo criado aqui deve ganhar ficha neste dicionário.

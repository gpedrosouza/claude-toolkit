---
nome: Figma (plugin)
tipo: plugin
dominios: [design, desenvolvimento]
fonte: marketplace oficial
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# Figma (plugin)

As instruções de como trabalhar com o Figma: transformar design em código, levar uma tela do código para o Figma, montar design systems, diagramas no FigJam e slides.

## Quando usar
- Implementar uma tela a partir de um link do Figma
- Levar uma página existente para o Figma, ou montar um design system a partir do código
- Diagrama (fluxo, arquitetura, ERD) no FigJam

## Quando não usar
- Sem arquivo no Figma e sem intenção de editar lá: um mockup no próprio Claude basta

## Componentes
| Skill | Para quê |
|---|---|
| figma-design-to-code | design → código (obrigatória antes de ler o design) |
| figma-generate-design, figma-use | código/descrição → tela no Figma |
| figma-generate-library | design system com variáveis e componentes |
| figma-generate-diagram, figma-use-figjam | diagramas no FigJam |
| figma-use-slides, figma-spec | Figma Slides e specs/PRDs no Figma |
| figma-code-connect | mapear componentes do Figma ↔ código |
| figma-swiftui, figma-implement-motion, figma-use-motion | SwiftUI e animação |
| figma-shaders, figma-generative-plugins, figma-code-workflows, figma-create-new-file | casos específicos |

## Combina com
- [Figma (conector)](../conectores/figma.md): o plugin traz as instruções, o conector traz o acesso aos arquivos — um não funciona sem o outro
- [design](design.md) para criticar o resultado

## Notas
- Desinstalar o conector deixa este plugin sem uso.

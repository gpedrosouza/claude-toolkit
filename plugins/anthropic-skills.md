---
nome: anthropic-skills
tipo: plugin
dominios: [documentos, geral]
fonte: built-in
superficies: [chat, claude-code]
instalado_em: desconhecido
---

# anthropic-skills

Skills que vêm com o Claude: arquivos do Office e PDF, documentos e artefatos, e utilidades gerais. Não precisam ser instaladas.

## Quando usar
- Entregar ou editar um arquivo .docx, .pdf, .xlsx ou .pptx
- Pesquisa extensa com relatório (`deep-research`)
- Criar uma skill nova (`skill-creator`)

## Quando não usar
- Documento ou apresentação sem formato de arquivo exigido: os tipos nativos do Claude (Docs, Slides, Sheets) são editáveis e exportam depois

## Componentes
| Grupo | Skills |
|---|---|
| arquivos | docx, pdf, pdf-reading, xlsx, pptx, file-reading |
| documentos e artefatos | docs, google-workspace, artifact-design, artifact-capabilities, dataviz |
| utilidades | deep-research, skill-creator, import-memory, morning, product-self-knowledge |
| navegador e computador | chrome-browser, built-in-browser, computer-use |

## Combina com
- [Google Drive](../conectores/google-drive.md): `google-workspace` edita Docs/Sheets/Slides do Drive

## Notas
- Vêm com o Claude: no fluxo de remoção, esta ficha não é apagada.

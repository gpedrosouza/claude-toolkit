---
nome: Google Drive
tipo: conector
dominios: [documentos, pesquisa]
fonte: marketplace oficial
superficies: [chat]
instalado_em: desconhecido
---

# Google Drive

Acesso ao seu Google Drive: buscar, ler, baixar, criar, copiar e compartilhar arquivos.

## Quando usar
- Usar como fonte um arquivo que está no Drive (PDF de aula, planilha, contrato)
- Criar ou atualizar um Google Doc/Sheet/Slides quando você pedir explicitamente o formato Google

## Quando não usar
- Documento novo sem pedido de formato Google: Docs do Claude

## Componentes
| Ferramentas | Para quê |
|---|---|
| search_files, list_recent_files, get_file_metadata | achar arquivos |
| read_file_content, download_file_content | ler e baixar |
| create_file, update_file, copy_file | criar e alterar |
| share_file, get_file_permissions | compartilhamento |
| trash_file | mover para a lixeira |

## Combina com
- [anthropic-skills](../plugins/anthropic-skills.md): `google-workspace` para editar arquivos Google
- [research-superpowers](../plugins/research-superpowers.md) quando os PDFs da pesquisa estão no Drive

## Notas
- Compartilhar e excluir mexem na sua conta real: pedem confirmação.

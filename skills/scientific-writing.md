---
nome: scientific-writing
tipo: skill
dominios: [pesquisa]
fonte: https://github.com/K-Dense-AI/claude-scientific-writer/tree/main/skills/scientific-writing
superficies: [chat, claude-code]
instalado_em: 2026-10-29
---

# scientific-writing

Escrita e revisão de manuscritos científicos com rastreabilidade: cada afirmação ligada a uma fonte verificada,
nada de citação ou dado inventado, guias de relato (CONSORT, PRISMA, STROBE…) e autoria/declarações conferidas.
K-Dense, licença MIT, v2.1.

## Quando usar
- Escrever ou revisar seções de artigo, relatório técnico ou TCC em que a precisão das fontes importa
- Montar referências, declarações (ética, financiamento, uso de IA) e preparar submissão
- Responder a revisores de forma organizada

## Quando não usar
- Texto não acadêmico (proposta comercial, post, e-mail)
- Achar fontes: use paper-search, Consensus ou Elicit antes — esta skill não busca, só exige que a fonte seja verificada

## Componentes
| Parte | Para quê |
|---|---|
| Regras inegociáveis | confidencialidade, proibição de fabricar, ligação afirmação → evidência |
| Fluxo em 12 passos | registro de evidências → esboço → rascunho → conferências → aprovação humana |
| 8 scripts Python (só na versão completa) | scaffold, checagem de consistência, referências, autoria, lint — locais e sem rede |
| Referências e modelos (só na versão completa) | IMRAD, estilos de citação, guias de relato, modelos JSON/CSV |

## Combina com
- [research-superpowers](../plugins/research-superpowers.md): `drafting-manuscript` e `requesting-peer-review`
- [paper-search](../plugins/paper-search.md), [Consensus](../conectores/consensus.md) e [Elicit](../conectores/elicit.md) para achar as fontes

## Notas
- No chat ela foi instalada só com o SKILL.md (+ nota de que os arquivos de apoio podem faltar): regras e fluxo completos, sem scripts.
- Versão completa no Claude Code, rodando no PowerShell: `npx skillfish add k-dense-ai/claude-scientific-writer scientific-writing`.
- É exigente de propósito: trabalha com IDs de afirmação/evidência e só humanos aprovam a submissão.

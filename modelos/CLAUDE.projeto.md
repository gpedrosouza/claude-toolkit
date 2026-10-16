<!--
MODELO DE CLAUDE.md DE PROJETO — copie para a raiz do repo como CLAUDE.md e preencha.
Comentários HTML como este são removidos antes de o Claude ler o arquivo: não gastam contexto.

Regras do modelo (vêm da documentação oficial do Claude Code):
- Meta: 30–80 linhas; nunca passe de 200.
- Para cada linha, pergunte: "remover isto faria o Claude errar?" Se não, corte.
- Não repita o que já está no CLAUDE.md global (idioma, Windows, fuso, .env, LGPD, commits).
- Não descreva arquivo por arquivo nem coloque status de fase: isso muda e vai para o vault.
- "IMPORTANTE" em no máximo uma linha — se tudo é importante, nada é.
- Regra que não pode falhar nunca (ex.: bloquear commit de .env) pede hook, não só texto.
- Projeto grande com regras por área: veja docs/ideias/claude-rules-por-tema.md (.claude/rules/).
-->

# <Nome do projeto>

<1–2 linhas: o que o sistema faz e para quem.>

## Antes de qualquer tarefa
- Leia `<VAULT.md ou docs/vault/Home.md>` (índice) e abra só os docs que a tarefa exige.
- Sempre: `<histórico de sessões / status atual>`.

## Stack
<Linguagem + framework · banco · libs que importam>. Código em `<pasta>`.

## Comandos
<!-- Comandos exatos, copiáveis. Diga em que pasta rodar se não for a raiz. -->
- Testes: `<comando>`
- Lint / typecheck: `<comando>`
- Rodar: `<comando>`

## Regras do projeto
<!-- Só o que o código não revela: decisões, armadilhas, o que não pode quebrar. -->
- IMPORTANTE: <a regra que, se quebrada, causa o maior estrago>
- <armadilha conhecida>
- Pergunte antes de rodar: <scripts que mexem em dados reais, enviam mensagens ou custam dinheiro>

## Pronto =
`<comandos de verificação>` passando, com a saída mostrada.

## Fim de sessão
- <onde registrar o que foi feito, decisões e próximo passo>

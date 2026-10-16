# Ideia: regras do projeto em `.claude/rules/` (para projetos novos)

**Status:** ideia registrada em 2026-10-15 — usar ao começar o próximo projeto.
**Hoje usamos:** CLAUDE.md curto como porta de entrada + VAULT.md como memória (opção A).

## O que é

Em vez de um vault lido sob demanda, as regras ficam em arquivos por tema dentro de `.claude/rules/`. O Claude Code carrega:

- **sem `paths`** no cabeçalho → toda sessão (igual ao CLAUDE.md);
- **com `paths`** → só quando o Claude lê ou edita um arquivo que casa com o padrão.

```
projeto/
├── CLAUDE.md                 visão geral, comandos, definição de pronto
└── .claude/rules/
    ├── backend/api.md        paths: ["src/api/**"]
    ├── frontend/telas.md     paths: ["src/web/**/*.tsx"]
    ├── banco.md              paths: ["prisma/**", "src/db/**"]
    └── lgpd.md               (sem paths: vale sempre)
```

Exemplo de regra com escopo:

```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API
- Toda rota valida a entrada com zod antes de tocar no banco
- Erros respondem { erro: string } com status HTTP correto
```

## Por que vale para projetos novos

- **Gasta menos contexto:** regra de frontend não entra numa sessão que só mexe no banco.
- **Segue o código:** a regra mora ao lado do que ela governa e é versionada no git.
- **Regras compartilhadas:** `~/.claude/rules/` vale para todos os projetos; dá para criar links para regras comuns (ex.: LGPD).

## Por que não migrar os projetos atuais agora

- O vault (Obsidian) também é documentação para humanos — decisões, histórico, alinhamento com cliente. Isso não cabe em regras.
- Migrar duplicaria conteúdo e criaria duas fontes de verdade.

## Como dividir quando adotar

| Vai para `.claude/rules/` | Fica no vault |
|---|---|
| Regras de código por área (API, telas, banco) | Visão, contexto do cliente, glossário |
| Convenções que o Claude deve seguir sempre | Decisões (ADR) e histórico de sessões |
| Armadilhas de uma pasta específica | Fases, checklists, pendências |

## Como verificar que carregou

`/context` numa sessão lista os arquivos de memória e regras carregados. Uma regra com `paths` só aparece depois que o Claude abre um arquivo que casa.

## Referência

- [How Claude remembers your project — seção "Organize rules with .claude/rules/"](https://code.claude.com/docs/en/memory)

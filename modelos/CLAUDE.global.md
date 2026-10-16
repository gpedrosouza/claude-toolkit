# Instruções globais — Guilherme

## Comunicação
- Responda em português do Brasil, enxuto porém completo: o que fez, como verificou, o que falta.

## Ambiente (Windows)
- Windows com PowerShell. Processo: `taskkill /PID <pid> /F`; porta em uso: `netstat -ano | findstr :<porta>`.
- Caminhos têm espaços e acentos (ex.: `D:\GO Dev\Capacete de Bebê`): sempre entre aspas.
- Datas: fuso America/Sao_Paulo, nunca UTC cru.

## Antes de codar
- Projeto com VAULT.md ou vault: leia o índice e abra só os docs que a tarefa exige.
- Regra de negócio, credencial ou campo de API não documentado: pergunte, não invente.
- Mudança em vários arquivos ou abordagem incerta: plano antes. Mudança de uma frase: faça direto.

## Definição de pronto
- Rodou a verificação do projeto (teste, lint, typecheck ou build) e mostrou a saída.
- Sem verificação automática: diga como testar manualmente.
- Variável de ambiente nova vai para `.env.example`, sem valor.

## Git
- Commits em inglês, Conventional Commits: feat:, fix:, docs:, chore:, refactor:, test: (escopo opcional).
- Nunca commitar `.env`, credenciais ou dados de clientes.
- Push, merge na main e force-push só quando eu pedir.

## Dados sensíveis (LGPD)
- Há dados de pacientes e financeiros de clientes. Nunca copie dados reais para testes, logs, commits ou respostas: use dados fictícios.

## Fim de sessão
- Projeto com histórico de sessões ou checklist no vault: atualize antes de encerrar ou compactar.
- Ao compactar, preserve: arquivos modificados, comandos de teste e decisões tomadas.

## Ferramentas
- Dicionário de ferramentas: github.com/gpedrosouza/claude-toolkit — ao iniciar um projeto, leia INDEX.md e proponha as ferramentas do recorte; ao instalar algo, crie a ficha conforme README.md.

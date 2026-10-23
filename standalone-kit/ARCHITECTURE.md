# Arquitetura consolidada

## 1. Camadas

### Orientação operacional

Lida no início da sessão:

- `AGENTS.md`: protocolo de trabalho;
- `PROJECT.md`: contexto estável, escopo e restrições;
- `NOW.md`: situação atual e próximos passos;
- `TASKS.md`: atividades do projeto e fila dos agentes.

### Conhecimento

- `.wiki/INDEX.md`: mapa do conhecimento;
- demais páginas: abertas somente quando pertinentes.

### Histórico

- `history/`: registros de execuções, decisões, incidentes e mudanças relevantes;
- nunca deve ser lido integralmente por padrão.

## 2. Estrutura adaptativa

O projeto começa mínimo. Novos arquivos e pastas são criados durante a execução apenas quando houver conteúdo concreto.

Uma nova pasta deve surgir quando:

- houver dois ou mais arquivos relacionados;
- houver crescimento previsível;
- for necessária separação clara entre categorias.

Evite pastas profundas e categorias com um único arquivo. Toda nova página durável deve ser referenciada no índice correspondente.

## 3. Leitura progressiva

O agente deve:

1. ler `PROJECT.md`, `NOW.md` e `TASKS.md`;
2. identificar o que falta para a tarefa atual;
3. consultar `.wiki/INDEX.md` somente quando precisar de conhecimento adicional;
4. abrir apenas os arquivos pertinentes;
5. pesquisar `history/` apenas para recuperar precedente, decisão, erro ou execução específica.

## 4. Rastreabilidade

Execuções relevantes podem gerar um arquivo curto em `history/`, contendo:

- data e identificação da execução;
- solicitante;
- agente e versão, quando conhecidos;
- provedor e modelo, quando confirmados;
- tarefa relacionada;
- arquivos alterados;
- resultado, limitações e próximo passo.

Informações não confirmadas devem ser registradas como `unknown`. O agente não deve inferir o modelo.

## 5. Validação

Resultados produzidos por IA podem usar:

- `AI_PROPOSED`;
- `REQUIRES_REVIEW`;
- `HUMAN_VALIDATED`;
- `REJECTED`;
- `SUPERSEDED`.

Conclusão de execução não equivale a validação humana.

## 6. Fonte da verdade

- Markdown: estado, conhecimento e histórico legível;
- Git: alterações, autoria técnica e reversão;
- arquivos originais: evidência primária, sem sobrescrita.

Não há banco vetorial, SQLite, captura integral de prompts ou leitura automática de todo o repositório nesta versão.

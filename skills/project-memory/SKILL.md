---
name: project-memory
version: 3.1.0
description: Mantém memória operacional portátil e progressiva em projetos (PROJECT, NOW, TASKS, wiki, history), com registro automático ao fim de cada passo, destino certo para cada tipo de informação e nada apagado.
---

# Project Memory

Use esta skill quando o projeto adotar `PROJECT.md`, `NOW.md`, `TASKS.md`, `_wiki/INDEX.md` e `history/`.

## Objetivo

Preservar continuidade entre pessoas e agentes sem carregar todo o histórico no contexto, e sem que a pessoa precise pedir
"registre" a cada passo.

## Criação do projeto

Antes de rodar `scripts/init_project.py`, pergunte no chat, nesta ordem:

0. "Usar o padrão?" Se sim, pule as demais. O padrão é frontmatter com núcleo e perfil de trabalho (`--frontmatter perfil`),
   com os campos do perfil em `A definir`, para preencher quando forem conhecidos.
1. Quer frontmatter nas páginas da `_wiki/` e do `history/`? Se não, `--frontmatter nenhum`.
2. Inclui o perfil de trabalho (`domain`, `client`, `engagement`, `organization`)? Se não, `--frontmatter nucleo`.
3. Se incluir: cliente, contrato e organização (`--client`, `--engagement`, `--organization`).

A escolha fica gravada no `PROJECT.md`, na seção "Configuração da memória". Campos e modos: `references/formatos.md`.

Projeto criado com versão anterior (pasta `.wiki/` ou `wiki/`, sem "Configuração da memória"): continue usando a pasta que
existe. Renomear para `_wiki/` ou adotar frontmatter só com a pessoa.

## Início

1. Leia `AGENTS.md` (e o `CLAUDE.md` da subpasta em que for trabalhar, se houver).
2. Leia somente `PROJECT.md`, `NOW.md` e `TASKS.md`. As regras fixas ficam no topo do `PROJECT.md`: elas valem antes de tudo.
3. Não faça varredura integral do projeto.
4. Antes de propor algo sobre um tema já trabalhado, procure no `_wiki/INDEX.md` e no `history/` o que já foi decidido,
   achado ou descartado sobre ele. Propor de novo o que já foi feito ou descartado é a falha mais cara.

## Durante o trabalho

- Separe fato, inferência, sugestão e item pendente de validação.
- Preserve originais. Antes de alterar um arquivo que a pessoa está usando, pergunte e salve uma cópia datada.
- Premissa registrada não muda sem consulta. Se a tarefa pedir mudá-la, aponte o registro e pergunte.
- Não invente agente, versão, provedor, modelo, fonte ou resultado.
- Ao criar página na `_wiki/` ou registro no `history/`, siga a linha `Frontmatter:` do `PROJECT.md` (`perfil`, `nucleo` ou
  `nenhum`). Se a linha não existir, não escreva frontmatter e pergunte à pessoa se quer adotar.

## Encerramento de cada passo relevante (sem esperar pedido)

Um passo é relevante quando houve pelo menos um destes gatilhos:

- decisão da pessoa;
- mudança de direção ou parede (algo que não funcionou e mostrou alguma coisa);
- achado sobre o objeto de trabalho;
- regra ou padrão novo;
- pendência ou lembrete ("deixa anotado", "fazer na próxima vez");
- arquivo do projeto produzido ou alterado.

Sem gatilho, não registre. Com gatilho, registre na mesma rodada, cada coisa no seu destino (tabela completa em
`references/destinos.md`; a seção "Destinos deste projeto" do `AGENTS.md`, se houver, prevalece):

| O quê | Onde |
|---|---|
| Estado atual, bloqueios, próximo passo | `NOW.md` |
| Pendências, inclusive decisões que cabem à pessoa (`Usuário: ...`) | `TASKS.md` |
| Decisão, com premissa, motivo e o que foi descartado | `history/` |
| Trajetória: o que tentamos, onde batemos na parede, por que mudamos de direção | `history/` |
| Achado sobre o objeto de trabalho (dado, documento, modelo), com ID e evidência | registro de achados (local na linha `Achados:` do `PROJECT.md`; sem ela, `_wiki/achados.md`) |
| Regra durável ou explicação que vai ser reusada | página da `_wiki/` + linha no `INDEX.md` |
| Regra fixa da pessoa (inegociável) | topo do `PROJECT.md` + `AGENTS.md` + página única na wiki |
| Pergunta a terceiros | `PERGUNTAS.md` na raiz, criado na primeira pergunta, com motivo, o que fica assumido e prioridade |
| Plano aprovado para execução | `_wiki/planos/<assunto>.md` + linha em `_wiki/planos/INDEX.md` + link na tarefa do `TASKS.md` |
| Preferência sobre como o agente trabalha | memória do agente, como ponteiro |

Depois, feche com uma mensagem direta: o que foi feito, os links do que a pessoa deve abrir e o que ela precisa decidir.
A última linha é `Registrado em:` seguida dos links dos arquivos gravados nesta rodada. Se uma gravação falhou, diga que o
registro não foi feito e o que faltou.

## Quando a pessoa repete um pedido

Pedido feito duas vezes é regra que não foi registrada. Na segunda vez:

1. registre como regra no `AGENTS.md` (e no topo do `PROJECT.md`, se for regra do objeto do projeto);
2. crie ou atualize a página da wiki com as palavras da pessoa, entre aspas e com data;
3. deixe na memória do agente só um ponteiro para a página.

## Várias sessões e agentes

Mais de uma sessão ou agente pode editar os mesmos arquivos ao mesmo tempo.

- Releia o arquivo imediatamente antes de editar e preserve as entradas que não são suas.
- Mudança feita por outra sessão é deliberada: não reverta. Se parecer errada, aponte à pessoa.
- Prefira acrescentar uma entrada datada a reescrever a de outra sessão.
- Atualize só o que é da sua frente. Não assuma nem feche trabalho de outra sessão sem confirmação.

## Planos

Plano aprovado para execução é salvo em `_wiki/planos/<assunto>.md` antes ou junto do início da execução, com linha em
`_wiki/planos/INDEX.md` e link na tarefa do `TASKS.md`. Plano recusado ou substituído fica, marcado `REJECTED` ou `SUPERSEDED`.
A pasta só é criada no primeiro plano.

## Nada se apaga

- Texto ou análise superada fica e ganha, logo depois, a nota
  `> **Revisto mais à frente** (onde, data): o que vale agora`.
- Erro interno (resíduo de versão, valor digitado errado) se corrige no lugar e se registra no `history/`.
- Arquivos antigos vão para `z.old/`, espelhando a estrutura original. Apagar de `z.old/` é decisão da pessoa.
- Página da wiki ou do history substituída recebe a marca `SUPERSEDED` e o link da que vale.

## Tamanho do núcleo

`NOW.md` e `TASKS.md` são lidos em toda sessão. Quando um bloco do `NOW.md` deixar de ser atual, ou uma frente do `TASKS.md`
fechar, mova o texto para o `history/` do tema e deixe uma linha com o link. Meta: `NOW.md` com até cerca de 150 linhas.

## Organização adaptativa

Crie pasta nova só quando houver dois ou mais arquivos relacionados, crescimento previsível ou separação necessária. Evite pastas
profundas e categorias vazias. Separe o que é produto (análise, relatório) do que é operacional (script de inventário, limpeza,
conferência); o operacional não entra na numeração dos produtos.

## Formatos

Frontmatter da wiki, nomes do history, linha do índice, diário por frente e memória do agente: `references/formatos.md`.

## Validação

Conteúdo de IA não validado leva `REQUIRES_REVIEW` (ou `AI_PROPOSED`), no texto e na linha do índice, para ser listável com
uma busca. Só uma pessoa promove a `HUMAN_VALIDATED`. Use também `REJECTED` e `SUPERSEDED`.

# {{PROJECT_NAME}}

Responder em português.

## Ao começar

1. Ler só `PROJECT.md` (regras fixas no topo, propósito, pastas, fontes), `NOW.md` (situação atual) e `TASKS.md` (pendências).
2. Consultar `_wiki/INDEX.md` e `history/` quando a tarefa pedir, e sempre antes de propor algo sobre um tema já trabalhado.
3. Em subpastas com `CLAUDE.md` ou `AGENTS.md` próprio, seguir também esse arquivo.

## Ao encerrar cada passo relevante (sem esperar pedido)

Relevante: decisão da pessoa, mudança de direção ou parede, achado, regra ou padrão novo, pendência ou lembrete, arquivo do
projeto produzido ou alterado. Sem nenhum desses, não registrar.

- Atualizar `NOW.md` e `TASKS.md`.
- Registrar em `history/` a decisão (premissa, motivo, palavras da pessoa) e a trajetória (paredes, mudanças de direção).
- Achado sobre o objeto do trabalho vai para o registro de achados (linha `Achados:` do `PROJECT.md`), com ID e evidência.
- Pergunta a terceiros vai para `PERGUNTAS.md` (criar na primeira).
- Conhecimento durável vai para `_wiki/` (frontmatter com `related`) e ganha linha no `_wiki/INDEX.md`.
- Marcar o que é proposto por IA e não validado como `REQUIRES_REVIEW`.
- Fechar com os links do que a pessoa deve abrir e o que ela precisa decidir.
- Última linha da resposta: `Registrado em:` com os links do que foi gravado; se algo falhou, dizer que não foi registrado.

## Destinos deste projeto

Acrescentam ou substituem linhas da tabela de destinos da skill; em conflito, vale esta seção.

| O quê | Onde |
|---|---|
| Diário da frente ... | `history/AAAA-MM-DD-tema.md` (novas seções no fim) |

## Regras

- Nada se apaga: superado ganha nota "Revisto mais à frente"; arquivos antigos vão para `z.old/`; apagar é decisão da pessoa.
- Arquivo em uso pela pessoa: perguntar antes e salvar cópia datada.
- Premissa registrada só muda com consulta.
- Pedido repetido vira regra aqui, na mesma rodada.
- Plano aprovado: salvar em `_wiki/planos/<assunto>.md`, indexar em `_wiki/planos/INDEX.md` e ligar à tarefa no `TASKS.md`.
- Várias sessões ou agentes: reler o arquivo antes de editar, não reverter mudança de outra sessão, preferir entrada nova
  datada a reescrever, não assumir trabalho de outra sessão sem confirmação.
- Commit só quando a pessoa pedir; avisar antes.
- Não registrar senhas, tokens ou dados pessoais.

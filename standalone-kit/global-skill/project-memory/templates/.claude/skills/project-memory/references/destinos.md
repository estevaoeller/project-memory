# Onde registrar cada coisa

A regra geral: cada informação tem **um** lugar de origem. Os outros lugares apontam para ele com um link e uma linha.

| Tipo | Destino | Conteúdo mínimo | Exemplo de gatilho |
|---|---|---|---|
| Estado | `NOW.md`, seção datada no topo | o que está feito, o que está aberto, quem decide o quê, links | fim de qualquer passo |
| Pendência | `TASKS.md`, agrupada por frente | caixa de seleção, verbo, onde está a evidência, marca de validação | "deixa um lembrete", "fazer na próxima vez que..." |
| Decisão da pessoa | `history/AAAA-MM-DD-tema.md` | a decisão, as palavras da pessoa entre aspas, a premissa, o motivo, o que foi descartado | "como sempre, registre a decisão e a premissa" |
| Trajetória | `history/`, na mesma página do tema | onde estávamos, paredes (o que não funcionou e o que mostrou), mudança de direção e por quê | "o que batemos na parede e por que mudamos" |
| Achado sobre o objeto | registro de achados no local da linha `Achados:` do `PROJECT.md` (ex.: `analise/relatorios/ACHADOS.md` ou um `.csv`); sem essa linha, `_wiki/achados.md` | ID cumulativo, evidência, universo, período, status, próxima ação | número, quebra, anomalia, efeito de escopo |
| Conhecimento durável | `_wiki/<tema>.md` + linha no `INDEX.md` | explicação reutilizável, fontes, limites | "o texto poderia ficar na wiki" |
| Regra fixa | topo do `PROJECT.md` (bloco destacado) + `AGENTS.md` (uma linha) + `_wiki/` (página única com a íntegra) | as palavras da pessoa, a data, quem pode mudar | "isso precisa ficar registrado na raiz, registre forte" |
| Perguntas a terceiros | `PERGUNTAS.md` na raiz, criado na primeira pergunta | ID, pergunta, por que importa, o que fica assumido sem resposta, prioridade | "organizadas, não espalhadas, e por que importa" |
| Processo padrão | `AGENTS.md` ou `CLAUDE.md` da pasta + `_wiki/` se precisar de detalhe | regra curta e o porquê | "isso deve ser o padrão para os próximos" |
| Plano aprovado | `_wiki/planos/<assunto>.md` + linha em `_wiki/planos/INDEX.md` | contexto, desenho, mudanças, verificação, status | plano aceito para execução |
| Preferência sobre o agente | memória do agente | regra, **Why**, **How to apply**, link para a página do projeto | "não use X", "sempre faça Y" |

## Destinos deste projeto

A tabela acima é a base. O `AGENTS.md` do projeto pode ter a seção "Destinos deste projeto", que acrescenta linhas ou substitui
uma linha da base (ex.: diário de cada frente, relatório próprio de achados). Quando houver conflito, vale o `AGENTS.md`. Ao
criar um destino novo por pedido da pessoa, acrescente a linha ali na mesma rodada.

## Memória do agente × repositório

A memória do agente (ex.: `~/.claude/projects/.../memory/`) não é compartilhada com outras pessoas nem com outros agentes.
Fato do projeto mora no repositório. Na memória ficam preferências de trabalho e ponteiros para o repositório. Quando a pessoa
disser "anote na memória", grave no repositório e deixe o ponteiro na memória, e diga onde gravou.

## Qualidade do registro

- Decisão sem motivo não serve: escreva por que, nas palavras da pessoa quando houver.
- Número sempre com a contagem (linhas, entidades, volume), o universo e o período.
- Planilha ou saída registrada traz os dados de origem, os parâmetros e o cálculo, nunca só o resultado.
- Ao fazer um registro, confirme no fim do passo, na linha `Registrado em:`, onde gravou. Se uma ferramenta falhou no meio,
  diga que o registro não foi feito.

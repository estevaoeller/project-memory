# Formatos

## Frontmatter

Frontmatter portátil, para preservar o contexto quando a nota sair do repositório (ex.: Obsidian). Vale para as páginas da
`_wiki/` e os registros do `history/`. O modo do projeto está na linha `Frontmatter:` do `PROJECT.md`:

| Modo | Campos |
|---|---|
| `perfil` (padrão) | núcleo + perfil de trabalho |
| `nucleo` | só o núcleo |
| `nenhum` | sem frontmatter |

Núcleo: `type`, `date_created`, `date_modified`, `related`. Perfil de trabalho: `domain`, `client`, `engagement`,
`organization`. Exemplo no modo `perfil`:

```yaml
---
domain: Work
type: Project Wiki
client: Nome do cliente
engagement: Código do contrato
organization: Organização
date_created: DD/MM/AAAA
date_modified: DD/MM/AAAA
related:
  - "[[outra-pagina]]"
  - "[[mais-uma]]"
---
```

- `type`: `Project Wiki` na `_wiki/`, `Project History` no `history/`.
- Os valores do perfil vêm do `PROJECT.md` (seção "Configuração da memória"). Enquanto estiverem `A definir`, pergunte quando
  surgir a informação e atualize ali.
- Datas em DD/MM/AAAA.

## Página da wiki

- `date_created` não muda. `date_modified` muda só em alteração material.
- `related`: dois ou três wikilinks temáticos, pelo nome do arquivo sem extensão. Revise quando o assunto da página mudar.
- Os links Markdown no corpo continuam valendo. O `INDEX.md` é o ponto de entrada.
- Nome do arquivo em minúsculas, com hífens, pelo assunto (`regra-projecao.md`), não pela data.
- Logo abaixo do título, a marca de validação e a origem: `REQUIRES_REVIEW`. Criada em DD/MM/AAAA a pedido de ...

## Linha do `INDEX.md`

```markdown
- [Título](pagina.md): o que a página responde, em uma ou duas frases, com os números ou nomes que alguém buscaria. `REQUIRES_REVIEW`
```

Regras fixas e a questão central do projeto ficam no topo, em negrito. O índice também lista páginas de `history/` e relatórios
do trabalho quando forem a fonte de um tema.

## `history/`

- Nome: `AAAA-MM-DD-tema.md`, um arquivo por tema e dia.
- Frente longa (uma revisão, uma rodada de análise): **um diário único**, com seções novas no fim (`## AAAA-MM-DD: assunto`).
  O `AGENTS.md` diz qual é o diário de cada frente.
- Frontmatter conforme o modo do projeto, com `type: Project History`. Modelo: `history/_modelo-registro.md`.
- Roteiro de uma página de trajetória:

```markdown
# DD/MM/AAAA: tema

`REQUIRES_REVIEW`. Por que este registro existe e quais páginas ele complementa.

## 1. Onde estávamos
## 2. Paredes
| # | Parede | O que mostrou | O que fizemos |
## 3. Decisão da pessoa
> palavras da pessoa, com data
## 4. O que mudou (arquivos, regras, notas "Revisto mais à frente")
## 5. O que fica aberto e quem decide
```

- Texto longo colado pela pessoa (transcrição, áudio, e-mail) vai íntegro para `history/` e a wiki aponta para ele.

## Rastreabilidade (opcional)

Quando útil para auditoria, registre: solicitante, agente, modelo, arquivos alterados, resultado e limitações. Use `unknown`
quando não for possível confirmar. Nunca deduza o modelo.

## Memória do agente

Um arquivo por fato:

```markdown
---
name: feedback-slug
description: uma linha que ajuda a decidir se é relevante
metadata:
  type: user | feedback | project | reference
---

A regra ou o fato.

**Why:** o que a pessoa disse, entre aspas, com data.

**How to apply:** quando e como usar; link para a página do projeto. Ver [[outra-memoria]].
```

No `MEMORY.md`, uma linha por memória: `- [Título](arquivo.md): gancho`.

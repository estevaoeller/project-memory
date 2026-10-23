# Project Memory Wiki Kit — V3 Adaptive

Base portátil de memória operacional para projetos trabalhados por pessoas e agentes como Goose, Codex e Claude Code.

> `global-skill/project-memory/` (SKILL.md, scripts, templates) é gerado a partir de
> `plugins/project-memory/` na raiz do repositório — não edite esses arquivos aqui
> diretamente. Edite a fonte e rode `python scripts/build_wiki_kit.py`.

## Princípio

A base define um protocolo mínimo, não uma taxonomia fixa:

- poucos arquivos são lidos no início;
- conhecimento detalhado é consultado sob demanda;
- o histórico é preservado sem ser carregado automaticamente;
- pastas e páginas surgem conforme o projeto realmente precisa;
- agente, provedor e modelo são registrados apenas em execuções relevantes.

## Núcleo inicial

```text
AGENTS.md
PROJECT.md
NOW.md
TASKS.md
.wiki/INDEX.md
history/
```

Veja `INSTALL.md` para instalação e `ARCHITECTURE.md` para as regras consolidadas.

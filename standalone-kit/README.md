# Project Memory Wiki Kit, versão 3.1

Base portátil de memória operacional para projetos trabalhados por pessoas e agentes como Goose, Codex e Claude Code.

> `global-skill/project-memory/` (SKILL.md, references, scripts, templates) é gerado a partir
> da raiz do repositório (`skills/`, `scripts/`, `templates/`). Não edite esses arquivos aqui
> diretamente: edite a fonte e rode `python scripts/build_wiki_kit.py`.

## Princípio

A base define um protocolo mínimo, não uma taxonomia fixa:

- poucos arquivos são lidos no início;
- conhecimento detalhado é consultado sob demanda;
- o histórico é preservado sem ser carregado automaticamente;
- pastas e páginas surgem conforme o projeto realmente precisa;
- o registro acontece sem pedido, ao fim de cada passo relevante, cada coisa no seu destino;
- nada se apaga: o superado ganha nota ou vai para `z.old/`;
- agente, provedor e modelo são registrados só quando úteis para auditoria.

## Núcleo inicial

```text
AGENTS.md
PROJECT.md
NOW.md
TASKS.md
_wiki/INDEX.md
history/
```

Veja `INSTALL.md` para instalação e `ARCHITECTURE.md` para as regras consolidadas.

# Project Memory

Plugin de memoria operacional progressiva para projetos conduzidos por pessoas e agentes de IA.

## O que ele instala

A skill `project-memory`, contendo:

- protocolo de leitura minima;
- estado atual em `NOW.md`;
- tarefas em `TASKS.md`;
- conhecimento duravel em `.wiki/`;
- historico consultado apenas quando necessario;
- script de inicializacao;
- modelos para Claude Code, Codex, Goose e outros agentes.

## Instalar pelo marketplace

```text
/plugin marketplace add estevaoeller/Skills
/plugin install project-memory@estevaoeller-skills
```

## Invocar no Claude Code

```text
/project-memory:project-memory
```

Exemplo de solicitacao:

```text
Use project-memory para inicializar a memoria deste projeto.
```

## Inicializar manualmente um projeto

Localize a pasta do plugin instalado ou copie este diretorio e execute:

```bash
python scripts/init_project.py /caminho/do/projeto --name "Nome do projeto" --git
```

O script preserva arquivos existentes por padrao. Use `--force` somente quando quiser substitui-los.

## Estrutura criada no projeto

```text
AGENTS.md
CLAUDE.md
PROJECT.md
NOW.md
TASKS.md
.wiki/INDEX.md
history/README.md
```

A estrutura deve crescer conforme necessidades reais, sem criar antecipadamente categorias vazias.

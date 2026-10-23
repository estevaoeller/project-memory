# Instalação

## Criar um projeto

Windows:

```powershell
py global-skill/project-memory/scripts/init_project.py C:\caminho\do\projeto --name "Nome do projeto" --git
```

Linux/macOS:

```bash
python3 global-skill/project-memory/scripts/init_project.py /caminho/do/projeto --name "Nome do projeto" --git
```

O script não sobrescreve arquivos existentes, salvo com `--force`.

## Instalar a skill globalmente

Copie a pasta:

```text
global-skill/project-memory/
```

para:

```text
~/.agents/skills/project-memory/
```

Para Claude Code, também pode ser copiada para:

```text
~/.claude/skills/project-memory/
```

O projeto criado já inclui cópias locais da skill para facilitar portabilidade.

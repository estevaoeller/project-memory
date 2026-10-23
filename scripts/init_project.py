#!/usr/bin/env python3
"""Inicializa um projeto com o núcleo adaptativo de memória."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inicializa Project Memory V3")
    parser.add_argument("target", type=Path, help="Pasta de destino do projeto")
    parser.add_argument("--name", default=None, help="Nome do projeto")
    parser.add_argument("--git", action="store_true", help="Inicializa Git e configura template de commit")
    parser.add_argument("--force", action="store_true", help="Sobrescreve arquivos existentes")
    return parser.parse_args()


def copy_template(template: Path, target: Path, force: bool) -> tuple[int, int]:
    created = 0
    skipped = 0
    for source in template.rglob("*"):
        relative = source.relative_to(template)
        destination = target / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not force:
            skipped += 1
            continue
        shutil.copy2(source, destination)
        created += 1
    return created, skipped


def replace_placeholders(target: Path, project_name: str) -> None:
    replacements = {
        "{{PROJECT_NAME}}": project_name,
        "{{DATE}}": dt.date.today().isoformat(),
    }
    for path in target.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def init_git(target: Path) -> None:
    try:
        if not (target / ".git").exists():
            subprocess.run(["git", "init"], cwd=target, check=True)
        subprocess.run(
            ["git", "config", "commit.template", str(target / ".gitmessage")],
            cwd=target,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"Aviso: não foi possível configurar Git: {exc}", file=sys.stderr)


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    template = script_dir.parent / "templates"
    if not template.exists():
        print(f"Template não encontrado: {template}", file=sys.stderr)
        return 1

    target = args.target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    name = args.name or target.name

    created, skipped = copy_template(template, target, args.force)
    replace_placeholders(target, name)
    if args.git:
        init_git(target)

    print(f"Projeto inicializado em: {target}")
    print(f"Arquivos criados/atualizados: {created}")
    print(f"Arquivos preservados: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

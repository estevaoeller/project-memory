#!/usr/bin/env python3
"""Regenera standalone-kit/global-skill/project-memory/
a partir da raiz deste plugin, que e a fonte unica de verdade.

O kit standalone (README.md, INSTALL.md, ARCHITECTURE.md, CHANGELOG.md,
example-project/) continua mantido manualmente; apenas a copia da skill
(SKILL.md, references/, scripts/, templates/) e gerada por este script.

Antes do kit, atualiza as copias locais da skill dentro de templates/
(.claude/skills/ e .agents/skills/), que vao para cada projeto criado.
"""

from __future__ import annotations

import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_SKILL_DIR = ROOT / "skills" / "project-memory"
PLUGIN_SCRIPTS_DIR = ROOT / "scripts"
PLUGIN_TEMPLATES_DIR = ROOT / "templates"
KIT_SKILL_DIR = ROOT / "standalone-kit" / "global-skill" / "project-memory"
TEMPLATE_SKILL_COPIES = (
    PLUGIN_TEMPLATES_DIR / ".claude" / "skills" / "project-memory",
    PLUGIN_TEMPLATES_DIR / ".agents" / "skills" / "project-memory",
)


def sync_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def sync_dir(src: Path, dst: Path) -> None:
    # copytree(..., dirs_exist_ok=True) merges into an existing tree instead
    # of deleting it first; on OneDrive, rmtree on synced folders can fail
    # with PermissionError while the cloud client still holds a handle.
    shutil.copytree(src, dst, dirs_exist_ok=True)

    src_files = {p.relative_to(src) for p in src.rglob("*") if p.is_file()}
    dst_files = {p.relative_to(dst) for p in dst.rglob("*") if p.is_file()}
    for stale in dst_files - src_files:
        (dst / stale).unlink()

    # remove now-empty directories left behind by deleted files
    for dirpath in sorted(dst.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            try:
                dirpath.rmdir()
            except PermissionError:
                # mesmo caso do OneDrive acima; pasta vazia nao entra no git
                print(f"Aviso: pasta vazia nao removida: {dirpath}", file=sys.stderr)


def dirs_match(src: Path, dst: Path) -> bool:
    # comparacao recursiva: dircmp sozinho so olha o primeiro nivel
    if not dst.is_dir():
        return False
    src_files = {p.relative_to(src) for p in src.rglob("*") if p.is_file()}
    dst_files = {p.relative_to(dst) for p in dst.rglob("*") if p.is_file()}
    if src_files != dst_files:
        return False
    return all(filecmp.cmp(src / f, dst / f, shallow=False) for f in src_files)


def sync_skill(dst: Path) -> None:
    sync_file(PLUGIN_SKILL_DIR / "SKILL.md", dst / "SKILL.md")
    sync_dir(PLUGIN_SKILL_DIR / "references", dst / "references")


def skill_matches(dst: Path) -> bool:
    return filecmp.cmp(
        PLUGIN_SKILL_DIR / "SKILL.md", dst / "SKILL.md", shallow=False
    ) and dirs_match(PLUGIN_SKILL_DIR / "references", dst / "references")


def is_in_sync() -> bool:
    for dst in (*TEMPLATE_SKILL_COPIES, KIT_SKILL_DIR):
        if not (dst / "SKILL.md").exists() or not skill_matches(dst):
            return False
    return dirs_match(PLUGIN_SCRIPTS_DIR, KIT_SKILL_DIR / "scripts") and dirs_match(
        PLUGIN_TEMPLATES_DIR, KIT_SKILL_DIR / "templates"
    )


def main() -> int:
    check_only = "--check" in sys.argv[1:]

    if not PLUGIN_SKILL_DIR.exists():
        print(f"ERRO: fonte ausente: {PLUGIN_SKILL_DIR}", file=sys.stderr)
        return 1

    if check_only:
        if not KIT_SKILL_DIR.exists() or not is_in_sync():
            print(
                "Kit desatualizado: rode 'python scripts/build_wiki_kit.py' "
                "e faca commit do resultado.",
                file=sys.stderr,
            )
            return 1
        print("Kit em sincronia com a fonte do plugin.")
        return 0

    for copy in TEMPLATE_SKILL_COPIES:
        sync_skill(copy)
    sync_skill(KIT_SKILL_DIR)
    sync_dir(PLUGIN_SCRIPTS_DIR, KIT_SKILL_DIR / "scripts")
    sync_dir(PLUGIN_TEMPLATES_DIR, KIT_SKILL_DIR / "templates")

    print(f"Kit regenerado a partir de {PLUGIN_SKILL_DIR.relative_to(ROOT)}")
    print(f"Destino: {KIT_SKILL_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

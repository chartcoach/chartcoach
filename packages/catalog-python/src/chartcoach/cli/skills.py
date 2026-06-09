from __future__ import annotations

from collections.abc import Iterable, Sequence
import dataclasses as dc
from pathlib import Path
import os
import sysconfig
from typing import cast

import click
import yaml

from .common import CONTEXT_SETTINGS, emit_rows

SKILLS_ENV = "CHARTCOACH_SKILLS_DIR"
SKILL_DATA_DIR = "skill-data"
PACKAGED_DATA_DIR = "data"
SUPPLEMENTARY_DIRS = ("references", "templates")


@dc.dataclass(frozen=True)
class Skill:
    name: str
    description: str
    directory: Path
    hidden: bool = False

    @property
    def skill_file(self) -> Path:
        return self.directory / "SKILL.md"

    def to_row(self) -> dict[str, object]:
        return {
            "name": self.name,
            "description": self.description,
        }


@click.group(
    "skills",
    invoke_without_command=True,
    context_settings=CONTEXT_SETTINGS,
    help="List and print CLI-served ChartCoach agent skills.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("table", "json", "jsonl")),
    default="table",
    show_default=True,
    help="Output format for the default list view.",
)
@click.pass_context
def skills_command(ctx: click.Context, output_format: str) -> None:
    """List and print CLI-served ChartCoach agent skills."""

    if ctx.invoked_subcommand is None:
        _emit_skill_list(output_format)


@skills_command.command("list", context_settings=CONTEXT_SETTINGS)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("table", "json", "jsonl")),
    default="table",
    show_default=True,
    help="Output format.",
)
def list_command(output_format: str) -> None:
    """List available CLI-served skills."""

    _emit_skill_list(output_format)


@skills_command.command("get", context_settings=CONTEXT_SETTINGS)
@click.argument("name", required=False)
@click.option("--all", "get_all", is_flag=True, help="Print every visible skill.")
@click.option(
    "--full",
    is_flag=True,
    help="Include references and templates after each SKILL.md.",
)
def get_command(name: str | None, get_all: bool, full: bool) -> None:
    """Print one CLI-served skill or every visible skill."""

    skills = _discover_skills()
    if get_all:
        visible = [skill for skill in skills if not skill.hidden]
        if not visible:
            return
        click.echo("\n\n".join(_skill_content(skill, full=full) for skill in visible))
        return
    if name is None:
        raise click.ClickException("Pass a skill name or --all.")
    skill = _skill_by_name(skills, name)
    click.echo(_skill_content(skill, full=full).rstrip())


@skills_command.command("path", context_settings=CONTEXT_SETTINGS)
@click.argument("name", required=False)
def path_command(name: str | None) -> None:
    """Print the CLI-served skill-data path or one skill directory path."""

    if name is None:
        roots = _skill_roots()
        if not roots:
            raise click.ClickException("No CLI-served skill-data directory found.")
        click.echo(str(roots[0]))
        return
    click.echo(str(_skill_by_name(_discover_skills(), name).directory))


def _emit_skill_list(output_format: str) -> None:
    rows = [skill.to_row() for skill in _discover_skills() if not skill.hidden]
    if output_format == "table":
        rows = [
            {"name": row["name"], "description": row["description"]}
            for row in rows
        ]
    emit_rows(rows, output_format=output_format)


def _discover_skills() -> list[Skill]:
    skills: dict[str, Skill] = {}
    for root in _skill_roots():
        for path in sorted(root.iterdir()):
            if not path.is_dir():
                continue
            skill_file = path / "SKILL.md"
            if not skill_file.exists():
                continue
            skill = _read_skill(path)
            if skill is not None:
                skills.setdefault(skill.name, skill)
    return sorted(skills.values(), key=lambda skill: skill.name)


def _skill_roots() -> list[Path]:
    env = os.getenv(SKILLS_ENV)
    if env:
        path = Path(env)
        return [path] if path.is_dir() else []

    candidates: list[Path] = []
    candidates.extend(_walkup_skill_roots(Path.cwd()))
    candidates.extend(_walkup_skill_roots(Path(__file__).resolve()))
    data_root = Path(sysconfig.get_path("data")) / SKILL_DATA_DIR
    if data_root.is_dir():
        candidates.append(data_root)
    packaged_data_root = (
        Path(sysconfig.get_path("data")) / PACKAGED_DATA_DIR / SKILL_DATA_DIR
    )
    if packaged_data_root.is_dir():
        candidates.append(packaged_data_root)
    return _unique_paths(candidates)


def _walkup_skill_roots(start: Path) -> list[Path]:
    current = start if start.is_dir() else start.parent
    roots: list[Path] = []
    for directory in (current, *current.parents):
        for candidate in (
            directory / SKILL_DATA_DIR,
            directory / PACKAGED_DATA_DIR / SKILL_DATA_DIR,
        ):
            if candidate.is_dir():
                roots.append(candidate)
    return roots


def _unique_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[Path] = set()
    output: list[Path] = []
    for path in paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        output.append(path)
    return output


def _read_skill(directory: Path) -> Skill | None:
    content = (directory / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = _frontmatter(content)
    if frontmatter is None:
        return None
    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        return None
    description = frontmatter.get("description")
    return Skill(
        name=name.strip(),
        description=description if isinstance(description, str) else "",
        directory=directory,
        hidden=bool(frontmatter.get("hidden")),
    )


def _frontmatter(content: str) -> dict[str, object] | None:
    content = content.lstrip()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    raw = parts[1]
    parsed = yaml.safe_load(raw) or {}
    if not isinstance(parsed, dict):
        return None
    return cast(dict[str, object], parsed)


def _skill_by_name(skills: Sequence[Skill], name: str) -> Skill:
    for skill in skills:
        if skill.name == name:
            return skill
    available = ", ".join(skill.name for skill in skills if not skill.hidden)
    hint = f" Available CLI-served skills: {available}." if available else ""
    raise click.ClickException(f"Unknown CLI-served skill: {name}.{hint}")


def _skill_content(skill: Skill, *, full: bool) -> str:
    parts = [skill.skill_file.read_text(encoding="utf-8").rstrip()]
    if full:
        parts.extend(_supplementary_content(skill.directory))
    return "\n\n".join(parts)


def _supplementary_content(directory: Path) -> list[str]:
    parts: list[str] = []
    for subdir_name in SUPPLEMENTARY_DIRS:
        subdir = directory / subdir_name
        if not subdir.is_dir():
            continue
        for path in sorted(subdir.iterdir()):
            if path.is_file():
                relpath = f"{subdir_name}/{path.name}"
                content = path.read_text(encoding="utf-8").rstrip()
                parts.append(f"--- {relpath} ---\n{content}")
    return parts


__all__ = ["skills_command"]

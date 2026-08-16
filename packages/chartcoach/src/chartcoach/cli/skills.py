from __future__ import annotations

import dataclasses as dc
import os
import sysconfig
from collections.abc import Iterable, Sequence
from pathlib import Path, PurePosixPath

import click
import yaml

from .common import CONTEXT_SETTINGS, emit_rows

SKILLS_ENV = "CHARTCOACH_SKILLS_DIR"
SKILL_DATA_DIR = "skill-data"
PACKAGED_DATA_DIR = "data"
SUPPLEMENTARY_DIRS = ("references", "templates")
SKILL_ORDER = ("core", "discuss", "visfeedback", "visrec", "contribute")
SKILL_ORDER_INDEX = {name: index for index, name in enumerate(SKILL_ORDER)}


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
    help="List and print CLI-served chartcoach agent skills.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("table", "json")),
    default="table",
    show_default=True,
    help="Output format for the default list view.",
)
@click.pass_context
def skills_command(ctx: click.Context, output_format: str) -> None:
    """List and print CLI-served chartcoach agent skills."""

    if ctx.invoked_subcommand is None:
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
            {"name": row["name"], "description": row["description"]} for row in rows
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
    return sorted(skills.values(), key=_skill_sort_key)


def _skill_sort_key(skill: Skill) -> tuple[int, str]:
    return (SKILL_ORDER_INDEX.get(skill.name, len(SKILL_ORDER)), skill.name)


def _skill_roots() -> list[Path]:
    env = os.getenv(SKILLS_ENV)
    if env:
        path = Path(env)
        return [path] if path.is_dir() else []

    candidates: list[Path] = []
    candidates.extend(_walkup_skill_roots(Path.cwd()))
    candidates.extend(_walkup_skill_roots(Path(__file__).resolve()))
    source_roots = _unique_paths(candidates)
    if source_roots:
        return source_roots

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
    skill_file = directory / "SKILL.md"
    content = skill_file.read_text(encoding="utf-8")
    try:
        frontmatter = _frontmatter(content)
        hidden = _hidden(frontmatter.get("hidden")) if frontmatter else False
    except ValueError as exc:
        raise click.ClickException(
            f"Invalid skill front matter in {skill_file}: {exc}"
        ) from exc
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
        hidden=hidden,
    )


def _frontmatter(content: str) -> dict[str, object] | None:
    lines = content.lstrip().splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(
            index for index, line in enumerate(lines[1:], start=1) if line == "---"
        )
    except StopIteration as exc:
        raise ValueError("Front matter is missing its closing delimiter.") from exc
    try:
        values = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        raise ValueError(str(exc)) from exc
    if values is None:
        return {}
    if not isinstance(values, dict) or not all(isinstance(key, str) for key in values):
        raise ValueError("Front matter must be a YAML mapping.")
    return values


def _hidden(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    raise ValueError("The hidden value must be true or false.")


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
                relpath = PurePosixPath(subdir_name, path.name).as_posix()
                content = path.read_text(encoding="utf-8").rstrip()
                parts.append(f"--- {relpath} ---\n{content}")
    return parts


__all__ = ["skills_command"]

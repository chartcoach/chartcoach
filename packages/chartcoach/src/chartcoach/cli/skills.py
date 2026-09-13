from __future__ import annotations

import os
from pathlib import Path

import click
from agent_plugins import AgentPluginError, Skill

from chartcoach import _skills as skill_service

from .common import CONTEXT_SETTINGS, emit_rows

SKILLS_ENV = "CHARTCOACH_SKILLS_DIR"


@click.group(
    "skills",
    invoke_without_command=True,
    context_settings=CONTEXT_SETTINGS,
    help="List and print chartcoach Agent Skills.",
    epilog=("Set CHARTCOACH_SKILLS_DIR to read Agent Skills from another directory."),
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
    """List and print chartcoach Agent Skills."""

    if ctx.invoked_subcommand is None:
        _, skills = _resources()
        _emit_skill_list(skills, output_format)


@skills_command.command("get", context_settings=CONTEXT_SETTINGS)
@click.argument("name", required=False)
@click.option(
    "--all",
    "get_all",
    is_flag=True,
    help="Print every visible Agent Skill.",
)
@click.option(
    "--full",
    is_flag=True,
    help="Include references and templates after each SKILL.md.",
)
def get_command(name: str | None, get_all: bool, full: bool) -> None:
    """Print one Agent Skill or every visible Agent Skill."""

    _, skills = _resources()
    try:
        if get_all:
            visible = _visible_skills(skills)
            if visible:
                click.echo(
                    "\n\n".join(
                        skill_service.skill_markdown(skill, full=full)
                        for skill in visible
                    )
                )
            return
        if name is None:
            raise click.ClickException("Pass a skill name or --all.")
        skill = skill_service.select_agent_skill(skills, name)
        content = skill_service.skill_markdown(skill, full=full)
    except skill_service.UnknownAgentSkillError as error:
        raise _unknown_skill_error(error, skills) from error
    except AgentPluginError as error:
        raise _skill_error(error) from error
    click.echo(content.rstrip())


@skills_command.command("path", context_settings=CONTEXT_SETTINGS)
@click.argument("name", required=False)
def path_command(name: str | None) -> None:
    """Print the skills directory or one Agent Skill path."""

    root, skills = _resources()
    if name is None:
        click.echo(str(root))
        return
    try:
        skill = skill_service.select_agent_skill(skills, name)
    except skill_service.UnknownAgentSkillError as error:
        raise _unknown_skill_error(error, skills) from error
    except AgentPluginError as error:
        raise _skill_error(error) from error
    click.echo(str(skill.path))


def _emit_skill_list(
    skills: tuple[Skill, ...],
    output_format: str,
) -> None:
    try:
        rows = []
        for skill in _visible_skills(skills):
            rows.append(
                {
                    "name": skill.path.name,
                    "description": skill_service.skill_description(skill),
                }
            )
    except AgentPluginError as error:
        raise _skill_error(error) from error
    emit_rows(rows, output_format=output_format)


def _visible_skills(skills: tuple[Skill, ...]) -> tuple[Skill, ...]:
    return tuple(skill for skill in skills if not skill_service.skill_is_hidden(skill))


def _resources() -> tuple[Path, tuple[Skill, ...]]:
    configured = os.getenv(SKILLS_ENV)
    try:
        if configured:
            root = Path(configured).resolve(strict=True)
            if not root.is_dir():
                raise click.ClickException(
                    f"{SKILLS_ENV} is not a directory: {str(root)!r}"
                )
            skills = skill_service.skills_from_directory(root)
            if not skills:
                raise AgentPluginError(
                    f"{SKILLS_ENV} contains no Agent Skills: {str(root)!r}"
                )
            return root, skills
        plugin = skill_service.agent_plugin()
        return plugin.path / "skills", skill_service.agent_skills(plugin)
    except AgentPluginError as error:
        raise _skill_error(error) from error
    except (OSError, RuntimeError) as error:
        raise click.ClickException(
            f"{SKILLS_ENV} cannot be resolved: {configured!r}"
        ) from error


def _skill_error(error: BaseException) -> click.ClickException:
    return click.ClickException(f"Cannot load Agent Skills: {error}")


def _unknown_skill_error(
    error: skill_service.UnknownAgentSkillError,
    skills: tuple[Skill, ...],
) -> click.ClickException:
    try:
        available = ", ".join(skill.path.name for skill in _visible_skills(skills))
    except AgentPluginError as metadata_error:
        return _skill_error(metadata_error)
    hint = f" Available CLI-served skills: {available}." if available else ""
    return click.ClickException(f"Unknown CLI-served skill: {error.name}.{hint}")


__all__ = ["skills_command"]

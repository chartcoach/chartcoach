"""Access the Agent Skills installed with chartcoach."""

from __future__ import annotations

import os
from collections.abc import Sequence
from pathlib import Path, PurePosixPath

import agent_plugins
import yaml

_DISTRIBUTION_NAME = "chartcoach"
_SUPPLEMENTARY_DIRS = frozenset({"references", "templates"})
_SKILL_ORDER = ("core", "discuss", "visfeedback", "visrec", "contribute")
_SKILL_ORDER_INDEX = {name: index for index, name in enumerate(_SKILL_ORDER)}


class UnknownAgentSkillError(agent_plugins.AgentPluginError):
    """A requested chartcoach Agent Skill is unavailable."""

    def __init__(self, name: str, available: Sequence[str]) -> None:
        self.name = name
        self.available = tuple(available)
        hint = f" Choose from: {', '.join(self.available)}." if self.available else ""
        super().__init__(f"Unknown Agent Skill {name!r}.{hint}")


def agent_plugin() -> agent_plugins.Plugin:
    """Return the Agent Plugin installed with this chartcoach version."""

    try:
        plugin = agent_plugins.locate(_DISTRIBUTION_NAME)
    except agent_plugins.AgentPluginError as error:
        raise agent_plugins.AgentPluginError(
            f"{error}. Reinstall chartcoach to restore its Agent Plugin resources."
        ) from error
    if plugin.manifest.name != _DISTRIBUTION_NAME:
        raise agent_plugins.AgentPluginError(
            f"Expected Agent Plugin name {_DISTRIBUTION_NAME!r}, "
            f"found {plugin.manifest.name!r}"
        )
    return plugin


def agent_skills(
    plugin: agent_plugins.Plugin | None = None,
) -> tuple[agent_plugins.Skill, ...]:
    """Return packaged Agent Skill objects in chartcoach workflow order."""

    resources = agent_plugin() if plugin is None else plugin
    return tuple(sorted(resources.skills, key=_skill_sort_key))


def agent_skill(
    name: str = "core",
    *,
    plugin: agent_plugins.Plugin | None = None,
) -> agent_plugins.Skill:
    """Return one packaged Agent Skill by its directory name.

    Args:
        name: Skill name. Defaults to `core`.
        plugin: Existing plugin handle. The installed chartcoach plugin is
            located when this argument is omitted.

    Raises:
        AgentPluginError: The requested skill is unavailable.
    """

    resources = agent_plugin() if plugin is None else plugin
    return resources.skill(name)


def skills_from_directory(
    root: str | os.PathLike[str],
) -> tuple[agent_plugins.Skill, ...]:
    """Return Agent Skill objects discovered directly below `root`."""

    try:
        directory = Path(root).resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise agent_plugins.AgentPluginError(
            f"Agent Skills directory cannot be resolved: {Path(root)}"
        ) from error
    if not directory.is_dir():
        raise agent_plugins.AgentPluginError(
            f"Agent Skills path is not a directory: {directory}"
        )

    skills: list[agent_plugins.Skill] = []
    try:
        for path in sorted(directory.iterdir()):
            if path.is_symlink() and path.is_dir():
                raise agent_plugins.AgentPluginError(
                    f"Agent Skill directory cannot be a symlink: {path}"
                )
            if not path.is_dir() or not (path / "SKILL.md").is_file():
                continue
            skill = agent_plugins.Skill(path)
            if skill.path.parent != directory:
                raise agent_plugins.AgentPluginError(
                    f"Agent Skill directory escapes {directory}: {path}"
                )
            skills.append(skill)
    except OSError as error:
        raise agent_plugins.AgentPluginError(
            f"Cannot inspect Agent Skills in {directory}: {error}"
        ) from error
    return tuple(sorted(skills, key=_skill_sort_key))


def select_agent_skill(
    skills: Sequence[agent_plugins.Skill],
    name: str = "core",
) -> agent_plugins.Skill:
    """Return one named Agent Skill from an existing collection."""

    matches = tuple(skill for skill in skills if skill.path.name == name)
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        paths = ", ".join(str(skill.path) for skill in matches)
        raise agent_plugins.AgentPluginError(
            f"Multiple Agent Skills use directory name {name!r}: {paths}"
        )
    available = tuple(dict.fromkeys(skill.path.name for skill in skills))
    raise UnknownAgentSkillError(name, available)


def skill_description(skill: agent_plugins.Skill) -> str:
    """Return the description declared in an Agent Skill's frontmatter."""

    values = _skill_frontmatter(skill)
    description = values.get("description")
    if description is not None and not isinstance(description, str):
        raise agent_plugins.AgentPluginError(
            f"Invalid Agent Skill frontmatter in {skill.file('SKILL.md')}: "
            "description must be a string"
        )
    return description or ""


def skill_is_hidden(skill: agent_plugins.Skill) -> bool:
    """Return whether chartcoach hides an Agent Skill from discovery lists."""

    hidden = _skill_frontmatter(skill).get("hidden", False)
    if not isinstance(hidden, bool):
        raise agent_plugins.AgentPluginError(
            f"Invalid Agent Skill frontmatter in {skill.file('SKILL.md')}: "
            "hidden must be true or false"
        )
    return hidden


def skill_markdown(
    skill: agent_plugins.Skill,
    *,
    full: bool = False,
) -> str:
    """Return `SKILL.md` and optional UTF-8 reference and template resources."""

    parts = [skill.source.rstrip()]
    if full:
        for path in skill.files:
            relative = path.relative_to(skill.path)
            if len(relative.parts) < 2 or relative.parts[0] not in _SUPPLEMENTARY_DIRS:
                continue
            name = PurePosixPath(relative.as_posix())
            selected = skill.file(name)
            parts.append(f"--- {name} ---\n{_read_text(selected).rstrip()}")
    return "\n\n".join(parts)


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise agent_plugins.AgentPluginError(
            f"Cannot read Agent Skill resource {path}: {error}"
        ) from error


def _skill_frontmatter(skill: agent_plugins.Skill) -> dict[str, object]:
    skill_file = skill.file("SKILL.md")
    try:
        values = yaml.safe_load(skill.frontmatter)
    except (RecursionError, yaml.YAMLError) as error:
        raise agent_plugins.AgentPluginError(
            f"Invalid Agent Skill frontmatter in {skill_file}: {error}"
        ) from error
    if not isinstance(values, dict) or not all(isinstance(key, str) for key in values):
        raise agent_plugins.AgentPluginError(
            f"Invalid Agent Skill frontmatter in {skill_file}: expected a YAML mapping"
        )
    return values


def _skill_sort_key(skill: agent_plugins.Skill) -> tuple[int, str]:
    name = skill.path.name
    return (_SKILL_ORDER_INDEX.get(name, len(_SKILL_ORDER)), name)


__all__ = [
    "UnknownAgentSkillError",
    "agent_plugin",
    "agent_skill",
    "agent_skills",
    "select_agent_skill",
    "skill_description",
    "skill_is_hidden",
    "skill_markdown",
    "skills_from_directory",
]

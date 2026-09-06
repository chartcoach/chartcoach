from __future__ import annotations

import json
from pathlib import Path

import agent_plugins
import pytest
from chartcoach import skills as skill_service


def test_skill_services_return_agent_plugin_objects(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plugin = _plugin(tmp_path)
    monkeypatch.setattr(agent_plugins, "locate", lambda name: plugin)

    expected = (
        agent_plugins.Skill(plugin.path / "skills" / "core"),
        agent_plugins.Skill(plugin.path / "skills" / "extra"),
    )
    assert skill_service.agent_plugin() is plugin
    assert skill_service.agent_skills() == expected
    assert skill_service.skills_from_directory(plugin.path / "skills") == expected
    assert skill_service.agent_skill() == expected[0]
    assert skill_service.agent_skill("extra") == expected[1]


def test_skill_services_read_description_and_full_source(tmp_path: Path) -> None:
    plugin = _plugin(tmp_path)
    core = skill_service.agent_skill("core", plugin=plugin)

    assert skill_service.skill_description(core) == "Use core chartcoach operations."
    assert skill_service.skill_markdown(core) == (
        "---\nname: core\ndescription: Use core chartcoach operations.\n---\n\n# Core"
    )
    assert skill_service.skill_markdown(core, full=True).endswith(
        "--- references/query.md ---\nQuery reference."
    )


def test_agent_skill_selects_by_directory_without_parsing_sources(
    tmp_path: Path,
) -> None:
    plugin = _plugin(tmp_path)
    skill_file = plugin.path / "skills" / "core" / "SKILL.md"
    skill_file.write_text(
        "---\nname: other\ndescription: Frontmatter name.\n---\n",
        encoding="utf-8",
    )
    (plugin.path / "skills" / "extra" / "SKILL.md").write_text(
        "missing frontmatter\n",
        encoding="utf-8",
    )

    selected = skill_service.agent_skill(
        "core", plugin=agent_plugins.Plugin(plugin.path)
    )

    assert selected.path.name == "core"


def test_skills_from_directory_rejects_directory_symlinks(tmp_path: Path) -> None:
    plugin = _plugin(tmp_path)
    (plugin.path / "skills" / "alias").symlink_to(
        plugin.path / "skills" / "core",
        target_is_directory=True,
    )

    with pytest.raises(agent_plugins.AgentPluginError, match="cannot be a symlink"):
        skill_service.skills_from_directory(plugin.path / "skills")


def test_skills_from_directory_bounds_symlink_loops(tmp_path: Path) -> None:
    loop = tmp_path / "loop"
    loop.symlink_to(loop, target_is_directory=True)

    with pytest.raises(agent_plugins.AgentPluginError, match="cannot be resolved"):
        skill_service.skills_from_directory(loop)


def test_select_agent_skill_rejects_duplicate_directory_names(tmp_path: Path) -> None:
    plugin = _plugin(tmp_path)
    core = agent_plugins.Skill(plugin.path / "skills" / "core")

    with pytest.raises(agent_plugins.AgentPluginError, match="Multiple Agent Skills"):
        skill_service.select_agent_skill((core, core), "core")


def test_agent_plugin_errors_include_reinstall_recovery(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(_: str) -> agent_plugins.Plugin:
        raise agent_plugins.AgentPluginError("marker missing")

    monkeypatch.setattr(agent_plugins, "locate", fail)

    with pytest.raises(agent_plugins.AgentPluginError, match="Reinstall chartcoach"):
        skill_service.agent_plugin()


def test_skill_description_bounds_yaml_recursion(tmp_path: Path) -> None:
    plugin = _plugin(tmp_path)
    skill_file = plugin.path / "skills" / "core" / "SKILL.md"
    depth = 500
    skill_file.write_text(
        "---\nname: " + "[" * depth + "x" + "]" * depth + "\n---\n",
        encoding="utf-8",
    )

    with pytest.raises(agent_plugins.AgentPluginError, match="Invalid Agent Skill"):
        skill_service.skill_description(agent_plugins.Skill(skill_file.parent))


def test_skill_markdown_names_the_unreadable_resource(tmp_path: Path) -> None:
    plugin = _plugin(tmp_path)
    core = skill_service.agent_skill("core", plugin=plugin)
    binary = core.path / "references" / "binary.bin"
    binary.write_bytes(b"\xff\xfe")
    core = agent_plugins.Skill(core.path)

    with pytest.raises(agent_plugins.AgentPluginError, match=r"binary\.bin"):
        skill_service.skill_markdown(core, full=True)


def _plugin(tmp_path: Path) -> agent_plugins.Plugin:
    root = tmp_path / "chartcoach.agent-plugin"
    root.mkdir()
    (root / "plugin.json").write_text(
        json.dumps(
            {
                "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                "name": "chartcoach",
            }
        ),
        encoding="utf-8",
    )
    _write_skill(
        root,
        "extra",
        description="Use an extra workflow.",
        body="# Extra\n",
    )
    core = _write_skill(
        root,
        "core",
        description="Use core chartcoach operations.",
        body="# Core\n",
    )
    references = core / "references"
    references.mkdir()
    (references / "query.md").write_text("Query reference.\n", encoding="utf-8")
    return agent_plugins.Plugin(root)


def _write_skill(
    plugin_root: Path,
    name: str,
    *,
    description: str,
    body: str,
) -> Path:
    directory = plugin_root / "skills" / name
    directory.mkdir(parents=True)
    (directory / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n\n{body}",
        encoding="utf-8",
    )
    return directory

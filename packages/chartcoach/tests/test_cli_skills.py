from __future__ import annotations

import json
from pathlib import Path

import agent_plugins
import pytest
from chartcoach.cli.main import main as chartcoach_cli
from click.testing import CliRunner


@pytest.fixture
def agent_plugin(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> agent_plugins.Plugin:
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
    core = _write_skill(
        root,
        "core",
        description="Core chartcoach skill.",
        body="# Core\n\nUse chartcoach primitives.\n",
    )
    references = core / "references" / "catalog"
    references.mkdir(parents=True)
    (references / "commands.md").write_text("Command reference.\n", encoding="utf-8")
    _write_skill(
        root,
        "extra",
        description="Extra chartcoach skill.",
        body="# Extra\n",
    )
    _write_skill(
        root,
        "hidden",
        description="Hidden chartcoach skill.",
        body="# Hidden\n",
        hidden=True,
    )
    plugin = agent_plugins.Plugin(root)
    monkeypatch.setattr(agent_plugins, "locate", lambda name: plugin)
    return plugin


def test_skills_cli_lists_agent_plugin_skills(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert result.exit_code == 0, result.output
    assert json.loads(result.stdout) == [
        {"name": "core", "description": "Core chartcoach skill."},
        {"name": "extra", "description": "Extra chartcoach skill."},
    ]


def test_skills_cli_get_all_prints_every_visible_skill(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "--all"])

    assert result.exit_code == 0
    assert "# Core" in result.output
    assert "# Extra" in result.output
    assert "# Hidden" not in result.output


def test_skills_cli_gets_a_hidden_skill_by_name(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "hidden"])

    assert result.exit_code == 0
    assert "# Hidden" in result.output


def test_skills_cli_preserves_all_precedence_over_name(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "core", "--all"])

    assert result.exit_code == 0
    assert "# Core" in result.output
    assert "# Extra" in result.output


def test_skills_cli_full_includes_nested_resources(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "core", "--full"])

    assert result.exit_code == 0
    assert "--- references/catalog/commands.md ---" in result.output
    assert "Command reference." in result.output


def test_skills_cli_prints_paths_from_the_plugin_object(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    root_result = runner.invoke(chartcoach_cli, ["skills", "path"])
    skill_result = runner.invoke(chartcoach_cli, ["skills", "path", "core"])

    assert root_result.exit_code == 0
    assert root_result.output.strip() == str(agent_plugin.path / "skills")
    assert skill_result.exit_code == 0
    assert skill_result.output.strip() == str(agent_plugin.path / "skills" / "core")


def test_skills_cli_uses_the_configured_skills_directory(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    override_root = tmp_path / "override"
    _write_skill(
        override_root,
        "custom",
        description="Custom chartcoach skill.",
        body="# Custom\n",
    )
    configured = override_root / "skills"
    monkeypatch.setenv("CHARTCOACH_SKILLS_DIR", str(configured))

    list_result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])
    path_result = runner.invoke(chartcoach_cli, ["skills", "path"])

    assert list_result.exit_code == 0, list_result.output
    assert json.loads(list_result.stdout) == [
        {"name": "custom", "description": "Custom chartcoach skill."}
    ]
    assert path_result.output.strip() == str(configured.resolve())


@pytest.mark.parametrize("kind", ["missing", "empty", "file"])
def test_skills_cli_rejects_invalid_configured_directories(
    kind: str,
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configured = tmp_path / kind
    if kind == "empty":
        configured.mkdir()
    elif kind == "file":
        configured.write_text("not a directory\n", encoding="utf-8")
    monkeypatch.setenv("CHARTCOACH_SKILLS_DIR", str(configured))

    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert result.exit_code == 1
    assert "CHARTCOACH_SKILLS_DIR" in result.stderr
    assert str(configured) in result.stderr


def test_skills_cli_bounds_configured_symlink_loops(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    loop = tmp_path / "loop"
    loop.symlink_to(loop, target_is_directory=True)
    monkeypatch.setenv("CHARTCOACH_SKILLS_DIR", str(loop))

    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert result.exit_code == 1
    assert "CHARTCOACH_SKILLS_DIR cannot be resolved" in result.stderr


def test_skills_cli_preserves_installed_plugin_recovery(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(_: str) -> agent_plugins.Plugin:
        raise agent_plugins.AgentPluginError("marker missing")

    monkeypatch.setattr(agent_plugins, "locate", fail)

    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert result.exit_code == 1
    assert "marker missing" in result.stderr
    assert "Reinstall chartcoach" in result.stderr


def test_skills_cli_named_get_ignores_malformed_siblings(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    (agent_plugin.path / "skills" / "extra" / "SKILL.md").write_text(
        "missing frontmatter\n",
        encoding="utf-8",
    )

    result = runner.invoke(chartcoach_cli, ["skills", "get", "core"])

    assert result.exit_code == 0
    assert "# Core" in result.output


def test_skills_cli_translates_description_errors(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    (agent_plugin.path / "skills" / "core" / "SKILL.md").write_text(
        "---\nname: core\ndescription: [invalid]\n---\n",
        encoding="utf-8",
    )

    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert result.exit_code == 1
    assert "Error: Cannot load Agent Skills:" in result.stderr


def test_skills_cli_reports_unknown_skills(
    runner: CliRunner,
    agent_plugin: agent_plugins.Plugin,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "missing"])

    assert result.exit_code == 1
    assert result.stderr.endswith(
        "Error: Unknown CLI-served skill: missing. "
        "Available CLI-served skills: core, extra.\n"
    )


def _write_skill(
    plugin_root: Path,
    name: str,
    *,
    description: str,
    body: str,
    hidden: bool = False,
) -> Path:
    directory = plugin_root / "skills" / name
    directory.mkdir(parents=True)
    hidden_line = "hidden: true\n" if hidden else ""
    (directory / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n{hidden_line}---\n\n{body}",
        encoding="utf-8",
    )
    return directory

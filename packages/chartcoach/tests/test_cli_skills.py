from __future__ import annotations

from pathlib import Path
import json

from click.testing import CliRunner
import pytest

from chartcoach.cli.main import main as chartcoach_cli


@pytest.fixture
def skill_data_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    root = tmp_path / "skill-data"
    skill_dir = root / "core"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\n"
        'name: "core"\n'
        "description: 'Core chartcoach skill.'\n"
        "hidden: false\n"
        "---\n\n"
        "# Core\n\n"
        "Use chartcoach primitives.\n",
        encoding="utf-8",
    )
    references = skill_dir / "references"
    references.mkdir()
    (references / "commands.md").write_text("Command reference.\n", encoding="utf-8")
    hidden_dir = root / "hidden"
    hidden_dir.mkdir()
    (hidden_dir / "SKILL.md").write_text(
        "---\n"
        "name: hidden\n"
        "description: Hidden skill.\n"
        "hidden: true\n"
        "---\n\n"
        "# Hidden\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("CHARTCOACH_SKILLS_DIR", str(root))
    return skill_dir


def test_skills_cli_lists_visible_skills(
    runner: CliRunner,
    skill_data_root: Path,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "--format", "json"])

    assert json.loads(result.stdout) == [
        {
            "name": "core",
            "description": "Core chartcoach skill.",
        }
    ]


def test_skills_cli_gets_hidden_skill_by_name(
    runner: CliRunner,
    skill_data_root: Path,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "hidden"])

    assert result.exit_code == 0
    assert "# Hidden" in result.output


def test_skills_cli_full_includes_references(
    runner: CliRunner,
    skill_data_root: Path,
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "core", "--full"])

    assert result.exit_code == 0
    assert "--- references/commands.md ---" in result.output
    assert "Command reference." in result.output

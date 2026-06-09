from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error, jsonl_rows


def test_main_help_advertises_skills_command(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["--help"])

    assert result.exit_code == 0
    assert "Start here (for AI agents):" in result.output
    assert "chartcoach skills get core" in result.output
    assert "CLI-served skills ship with the CLI" in result.output
    assert "skills" in result.output
    assert "ChartCoach agent skills" in result.output


@pytest.fixture
def skill_data_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[Path, Path]:
    root = tmp_path / "skill-data"
    skill_dir = root / "core"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\n"
        "name: core\n"
        "description: Core ChartCoach skill.\n"
        "---\n\n"
        "# Core\n\n"
        "Use ChartCoach primitives.\n",
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
    return root, skill_dir


def test_skills_cli_lists_visible_skills(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "list", "--format", "jsonl"])

    assert jsonl_rows(result) == [
        {
            "name": "core",
            "description": "Core ChartCoach skill.",
        }
    ]


def test_skills_cli_gets_skill_content(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "core"])

    assert result.exit_code == 0
    assert "# Core" in result.output
    assert "Command reference" not in result.output


def test_skills_cli_full_includes_references(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "core", "--full"])

    assert result.exit_code == 0
    assert "--- references/commands.md ---" in result.output
    assert "Command reference." in result.output


def test_skills_cli_all_prints_visible_skills(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "--all"])

    assert result.exit_code == 0
    assert "# Core" in result.output
    assert "# Hidden" not in result.output


def test_skills_cli_hidden_skill_is_addressable_by_name(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "get", "hidden"])

    assert result.exit_code == 0
    assert "# Hidden" in result.output


def test_skills_cli_prints_skill_paths(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    _, skill_dir = skill_data_root

    result = runner.invoke(chartcoach_cli, ["skills", "path", "core"])

    assert result.exit_code == 0
    assert result.output.strip() == str(skill_dir)


def test_packaged_skills_exclude_top_level_repo_skill(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)

    list_result = runner.invoke(chartcoach_cli, ["skills", "list", "--format", "jsonl"])
    assert list_result.exit_code == 0
    visible_names = {row["name"] for row in jsonl_rows(list_result)}
    assert visible_names == {"core", "visfeedback"}

    get_result = runner.invoke(chartcoach_cli, ["skills", "get", "chartcoach"])
    assert_cli_error(get_result, "Unknown CLI-served skill: chartcoach")
    assert "Available CLI-served skills: core, visfeedback" in get_result.output
    assert (repo_root / "skills" / "chartcoach" / "SKILL.md").exists()

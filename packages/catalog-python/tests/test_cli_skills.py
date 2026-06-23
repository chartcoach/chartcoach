from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.constants import CHARTCOACH_DEFAULTS

from helpers import assert_cli_error, jsonl_rows


def test_main_help_exits_successfully(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["--help"])

    assert result.exit_code == 0


def test_main_without_command_exits_successfully(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, [])

    assert result.exit_code == 0


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
        "description: Core chartcoach skill.\n"
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
    return root, skill_dir


def test_skills_cli_lists_visible_skills(
    runner: CliRunner,
    skill_data_root: tuple[Path, Path],
) -> None:
    result = runner.invoke(chartcoach_cli, ["skills", "list", "--format", "jsonl"])

    assert jsonl_rows(result) == [
        {
            "name": "core",
            "description": "Core chartcoach skill.",
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


def test_packaged_skills_are_served_from_package_data(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)

    list_result = runner.invoke(chartcoach_cli, ["skills", "list", "--format", "jsonl"])
    assert list_result.exit_code == 0
    visible_names = [row["name"] for row in jsonl_rows(list_result)]
    assert visible_names == ["core", "discuss", "visfeedback", "visrec", "contribute"]

    for name in ("discuss", "contribute", "visrec"):
        skill_result = runner.invoke(chartcoach_cli, ["skills", "get", name])
        assert skill_result.exit_code == 0
        assert f"name: {name}" in skill_result.output

    get_result = runner.invoke(chartcoach_cli, ["skills", "get", "chartcoach"])
    assert_cli_error(get_result, "Unknown CLI-served skill: chartcoach")
    assert (
        "Available CLI-served skills: core, discuss, visfeedback, visrec, contribute"
        in get_result.output
    )


def test_packaged_core_skill_teaches_default_resolution_for_citations(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)

    result = runner.invoke(chartcoach_cli, ["skills", "get", "core"])

    assert result.exit_code == 0
    assert "## Package Defaults" in result.output
    assert "CHARTCOACH_DEFAULTS" in result.output
    assert "GUIDELINE_URL_TEMPLATE" in result.output
    assert "CATALOG_RELEASE_ROOT_URL" in result.output
    assert '--url-template "$GUIDELINE_URL_TEMPLATE"' in result.output


def test_packaged_core_skill_distinguishes_academic_source_scope(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)

    result = runner.invoke(chartcoach_cli, ["skills", "get", "core"])

    assert result.exit_code == 0
    assert "academically published sources" in result.output
    assert "article`, `inproceedings`, and `incollection`" in result.output
    assert (
        "Queries over all reference types include the full catalog evidence trail"
        in (result.output)
    )
    assert "Do not treat `source_type` as a hard trust ranking" in result.output


def test_packaged_skills_do_not_hardcode_package_default_values(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)
    copied_values = {
        CHARTCOACH_DEFAULTS.catalog_artifact_base_url,
        CHARTCOACH_DEFAULTS.guideline_url_template,
        CHARTCOACH_DEFAULTS.catalog_digest,
        CHARTCOACH_DEFAULTS.catalog_version,
        CHARTCOACH_DEFAULTS.lance_document_table,
    }
    outputs: list[str] = []
    for name in ("core", "discuss", "visfeedback", "visrec", "contribute"):
        result = runner.invoke(chartcoach_cli, ["skills", "get", name])
        assert result.exit_code == 0
        outputs.append(result.output)
    skill_text = "\n".join(outputs)

    for value in copied_values:
        assert value not in skill_text


def test_packaged_contribute_skill_describes_catalog_issue_paths(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SKILLS_DIR", raising=False)

    result = runner.invoke(chartcoach_cli, ["skills", "get", "contribute"])

    assert result.exit_code == 0
    assert (
        "https://github.com/chartcoach/catalog/issues/new?body=<encoded-body>"
        in result.output
    )
    assert "`missing-guideline.md`" in result.output
    assert "`improve-guideline.md`" in result.output
    assert "`catalog-curation.md`" in result.output
    assert "command -v gh" in result.output
    assert "gh auth status --hostname github.com" in result.output
    assert "gh issue create --repo chartcoach/catalog" in result.output
    assert "ask for explicit approval" in result.output

    for heading in (
        "## Issue Type",
        "## Summary",
        "## Evidence From Use",
        "## Related Guideline Records",
        "## Suggested Catalog Change",
        "## Public Disclosure Check",
        "## Uncertainty",
    ):
        assert heading in result.output

    for checklist_item in (
        "- [ ] No private user data.",
        "- [ ] No local filesystem paths.",
        "- [ ] Any referenced guideline ids were verified with exact reads.",
    ):
        assert checklist_item in result.output

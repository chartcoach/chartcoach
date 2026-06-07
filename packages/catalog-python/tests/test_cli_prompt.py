from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error


def test_prompt_cli_prints_parameterized_codex_prompt(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    source = tmp_path / "guidelines"
    index_path = tmp_path / "index"

    result = runner.invoke(
        chartcoach_cli,
        [
            "prompt",
            "--codex",
            "--source",
            str(source),
            "--index",
            str(index_path),
            "--guidance-mode",
            "feedback",
            "--task",
            "Review a dashboard for misleading bar axes.",
        ],
    )

    assert result.exit_code == 0
    assert "Target agent: Codex." in result.output
    assert "Installed skill: `chartcoach/catalog`." in result.output
    assert f"Catalog source: `{source}`." in result.output
    assert f"LanceDB index: `{index_path}`." in result.output
    assert "Guidance mode: `feedback`." in result.output
    assert "Review a dashboard for misleading bar axes." in result.output
    assert "Read `MANIFEST.md`" in result.output
    assert "Guideline Use Report" in result.output
    assert "http://localhost:4321/guidelines/<guideline-id>/" in result.output


def test_prompt_cli_uses_public_site_url_env(runner: CliRunner) -> None:
    result = runner.invoke(
        chartcoach_cli,
        ["prompt", "--codex"],
        env={"CHARTCOACH_SITE_URL": "https://example.org/chartcoach/"},
    )

    assert result.exit_code == 0
    assert "https://example.org/chartcoach/guidelines/<guideline-id>/" in result.output


def test_prompt_cli_requires_one_target_agent(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["prompt"])

    assert_cli_error(result, "Pass exactly one agent flag")

    result = runner.invoke(chartcoach_cli, ["prompt", "--codex", "--claude"])

    assert_cli_error(result, "Pass exactly one agent flag")


def test_prompt_cli_prints_unresolved_catalog_source(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    missing_source = tmp_path / "missing-catalog"

    result = runner.invoke(
        chartcoach_cli,
        ["prompt", "--opencode", "--source", str(missing_source)],
    )

    assert result.exit_code == 0
    assert f"Catalog source: `{missing_source}`." in result.output

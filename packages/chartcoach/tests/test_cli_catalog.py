from __future__ import annotations

import json
from pathlib import Path

from chartcoach import Catalog
from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.curation import build_release
from click.testing import CliRunner


def test_catalog_describe_reports_local_catalog_identity(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "describe",
            "--source",
            str(sample_catalog_path),
        ],
    )

    assert result.exit_code == 0, result.output
    description = json.loads(result.stdout)
    assert description["resolved_location"] == str(sample_catalog_path)
    assert description["release_digest"] is None
    assert len(description["entries_digest"]) == 64
    assert len(description["manifest_digest"]) == 64
    assert {row["name"] for row in description["tables"]} == {
        "guidelines",
        "sections",
        "guideline_labels",
        "references",
        "guideline_references",
        "guideline_sources",
    }


def test_catalog_describe_preserves_the_resolved_release_digest(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    release = build_release(sample_catalog, release_root)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "describe",
            "--source",
            str(release_root),
        ],
    )

    assert result.exit_code == 0, result.output
    description = json.loads(result.stdout)
    assert description["resolved_location"] == str(release_root / "release.json")
    assert description["release_digest"] == release.digest


def test_catalog_list_json_reports_truncation_and_successful_empty_results(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    truncated = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
        ],
    )
    empty = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "no-such-guideline-text",
        ],
    )

    assert truncated.exit_code == 0, truncated.output
    assert json.loads(truncated.stdout)["truncated"] is True
    assert empty.exit_code == 0, empty.output
    assert json.loads(empty.stdout)["rows"] == []
    assert "Guidance:" in empty.stderr

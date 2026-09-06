from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation import build_release
from chartcoach.cli.main import main as chartcoach_cli


def test_catalog_overview_reports_local_content_identity(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "overview",
            "--source",
            str(sample_catalog_path),
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    overview = json.loads(result.stdout)
    assert overview["source"] == str(sample_catalog_path)
    assert overview["release_digest"] is None
    assert len(overview["content_digest"]) == 64
    assert {row["name"] for row in overview["tables"]} == {
        "guidelines",
        "sections",
        "guideline_labels",
    }


def test_catalog_overview_preserves_the_resolved_release_digest(
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
            "overview",
            "--source",
            str(release_root),
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    overview = json.loads(result.stdout)
    assert overview["source"] == str(release_root)
    assert overview["release_digest"] == release.digest

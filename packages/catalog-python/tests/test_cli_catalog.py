from __future__ import annotations

import json
from pathlib import Path
import shutil
from typing import cast

from click.testing import CliRunner
import pytest

import chartcoach.cli.common as common_cli
from chartcoach import Catalog
from chartcoach.catalog import remote as catalog_remote
from chartcoach.catalog.remote import read_release_metadata
from chartcoach.cli.main import main as chartcoach_cli

from helpers import jsonl_rows


def cache_default_catalog(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    catalog: Catalog,
) -> None:
    bundle_path = catalog.write_bundle(tmp_path / "default-bundle")
    metadata = read_release_metadata(bundle_path)
    cache_root = tmp_path / "cache"
    target = cache_root / "catalog" / "releases" / metadata.version / metadata.digest
    target.parent.mkdir(parents=True)
    shutil.copytree(bundle_path, target)
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_VERSION", metadata.version)
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_DIGEST", metadata.digest)


def test_catalog_schema_and_values_report_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "schema",
            "--source",
            str(sample_catalog_path),
            "--format",
            "jsonl",
        ],
    )
    schema = jsonl_rows(result)
    assert {"table": "guidelines", "column": "title", "type": "String"} in schema
    assert {"table": "labels", "column": "family", "type": "String"} in schema
    assert {
        "table": "guideline_sources",
        "column": "source_title",
        "type": "String",
    } in schema

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "guideline_labels.label",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "chart:",
            "--format",
            "jsonl",
        ],
    )
    values = {row["value"]: row["rows"] for row in jsonl_rows(result)}
    assert values == {"chart:bar": 1, "chart:line": 1}


def test_catalog_table_format_uses_readable_columns(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--label",
            "chart:bar",
            "--format",
            "table",
        ],
    )

    assert result.exit_code == 0
    assert result.output.splitlines()[0].split() == [
        "id",
        "title",
        "description",
        "labels",
    ]
    assert "chart:bar, component:axis" in result.output


def test_cache_download_notice_redacts_credential_url(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    common_cli.report_cache_download(
        "catalog",
        "https://user:secret@example.test/private/token/metadata.json?sig=hidden#frag",
        tmp_path / "cache",
    )

    captured = capsys.readouterr()
    assert "https://example.test/.../metadata.json" in captured.err
    assert "secret" not in captured.err
    assert "sig=hidden" not in captured.err


def test_catalog_overview_labels_and_roles_are_composable(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    overview_result = runner.invoke(
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
    overview = cast(dict[str, object], json.loads(overview_result.output))
    assert overview["section_roles"] == ["advice"]
    assert overview["label_families"] == ["chart", "component", "task"]

    labels_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "labels",
            "--source",
            str(sample_catalog_path),
            "--family",
            "chart",
            "--format",
            "jsonl",
        ],
    )
    labels = {row["label"] for row in jsonl_rows(labels_result)}
    assert labels == {"chart:bar", "chart:line"}

    roles_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "roles",
            "--source",
            str(sample_catalog_path),
            "--format",
            "jsonl",
        ],
    )
    assert jsonl_rows(roles_result)[0]["role"] == "advice"


def test_catalog_overview_reports_navigation_tables(
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
    overview = cast(dict[str, object], json.loads(result.output))
    tables = {
        str(row["name"]) for row in cast(list[dict[str, object]], overview["tables"])
    }
    assert tables == {"guidelines", "sections", "labels", "guideline_labels"}


def test_read_commands_use_cached_default_source(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)
    cache_default_catalog(monkeypatch, tmp_path, sample_catalog)

    result = runner.invoke(
        chartcoach_cli,
        ["catalog", "schema", "--tables", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    rows = jsonl_rows(result)
    assert {row["name"] for row in rows} >= {"guidelines", "sections", "labels"}


def test_default_catalog_downloads_once_without_fetching_indexes(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    metadata = read_release_metadata(bundle_path)
    cache_root = tmp_path / "cache"
    release_url = f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/metadata.json"
    downloads: list[str] = []

    def read_url_text(url: str) -> str:
        if url == release_url:
            return json.dumps(metadata.to_record())
        raise AssertionError(f"Unexpected metadata URL: {url}")

    def download_file(url: str, path: Path) -> None:
        downloads.append(url)
        if url.endswith("/MANIFEST.md"):
            shutil.copyfile(bundle_path / "MANIFEST.md", path)
            return
        if url.endswith("/entries.parquet"):
            shutil.copyfile(bundle_path / "entries.parquet", path)
            return
        raise AssertionError(f"Unexpected artifact URL: {url}")

    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setenv("CHARTCOACH_ARTIFACT_BASE_URL", "https://example.test")
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_VERSION", metadata.version)
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_DIGEST", metadata.digest)
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    first = runner.invoke(chartcoach_cli, ["catalog", "overview", "--format", "json"])
    second = runner.invoke(chartcoach_cli, ["catalog", "labels", "--format", "jsonl"])

    assert first.exit_code == 0, first.output
    assert second.exit_code == 0, second.output
    assert "Downloading ChartCoach catalog" in first.stderr
    assert "Cache" in first.stderr
    assert second.stderr == ""
    assert downloads == [
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/MANIFEST.md",
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/entries.parquet",
    ]
    cached_release = (
        cache_root / "catalog" / "releases" / metadata.version / metadata.digest
    )
    assert (cached_release / "metadata.json").exists()
    assert (cached_release / "MANIFEST.md").exists()
    assert (cached_release / "entries.parquet").exists()
    assert not (cached_release / "indexes").exists()


def test_catalog_validate_uses_cached_default_source(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)
    cache_default_catalog(monkeypatch, tmp_path, sample_catalog)

    result = runner.invoke(chartcoach_cli, ["catalog", "validate", "--format", "json"])

    payload = cast(list[dict[str, object]], json.loads(result.output))
    rows = {row["name"]: row["rows"] for row in payload}
    assert rows["guidelines"] == 2
    assert rows["manifest_section_roles"] == 1


def test_catalog_values_and_sql_report_empty_results(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    values_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "guideline_labels.label",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert values_result.exit_code == 0
    assert values_result.output.strip() == "0 rows"

    sql_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "sql",
            "--source",
            str(sample_catalog_path),
            "select id from guidelines where id = 'not-present'",
        ],
    )
    assert sql_result.exit_code == 0
    assert sql_result.output.strip() == "0 rows"


def test_catalog_values_reports_truncated_value_lists(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "guideline_labels.label",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "chart:",
            "--limit",
            "1",
        ],
    )

    assert result.exit_code == 0
    assert result.output.splitlines()[0].split() == ["table", "column", "value", "rows"]
    assert "Returned 1 values. Increase --limit to inspect more." in result.stderr

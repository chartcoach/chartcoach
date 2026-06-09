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

from helpers import assert_cli_error, jsonl_rows


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
        ["catalog", "schema", "--source", str(sample_catalog_path), "--format", "jsonl"],
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


def test_catalog_overview_does_not_build_reference_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_reference_table(_catalog: Catalog) -> object:
        raise AssertionError("overview should not parse BibTeX reference tables")

    monkeypatch.setattr(Catalog, "references", fail_reference_table)
    monkeypatch.setattr(Catalog, "guideline_references", fail_reference_table)
    monkeypatch.setattr(Catalog, "guideline_sources", fail_reference_table)

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
        str(row["name"])
        for row in cast(list[dict[str, object]], overview["tables"])
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
    release_url = (
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/metadata.json"
    )
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
    cached_release = cache_root / "catalog" / "releases" / metadata.version / metadata.digest
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


def test_catalog_validate_uses_source_env(
    runner: CliRunner,
    sample_workspace_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CHARTCOACH_SOURCE", str(sample_workspace_path))

    result = runner.invoke(chartcoach_cli, ["catalog", "validate", "--format", "jsonl"])

    rows = {row["name"]: row["rows"] for row in jsonl_rows(result)}
    assert rows["guidelines"] == 2
    assert rows["manifest_section_roles"] == 1

def test_catalog_sql_queries_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "sql",
            "--source",
            str(sample_catalog_path),
            "select id, title from guidelines where list_contains(labels, 'chart:bar')",
            "--format",
            "jsonl",
        ],
    )

    assert jsonl_rows(result) == [
        {"id": "full-axis-bars", "title": "Use full value axes for bars"}
    ]


def test_catalog_sql_rejects_non_select_statements(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "sql",
            "--source",
            str(sample_catalog_path),
            "create table x as select 1",
        ],
    )

    assert_cli_error(result, "Only SELECT queries are allowed")


def test_catalog_validate_rejects_empty_workspace(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    (empty / "entries").mkdir()
    (empty / "MANIFEST.md").write_text(
        """# Empty

## Section Roles

### advice

Actionable guidance.

## Label Families

### chart

Chart-family labels such as `chart:bar`.
"""
    )
    result = runner.invoke(chartcoach_cli, ["catalog", "validate", "--source", str(empty)])
    assert_cli_error(result, "No guideline entries found")


def test_catalog_build_dry_run_reports_without_writing_bundle(
    runner: CliRunner,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "bundle"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "build",
            "--source",
            str(sample_workspace_path),
            "--out",
            str(output_path),
            "--dry-run",
        ],
    )
    assert result.exit_code == 0
    assert "catalog bundle" in result.output
    assert not (output_path / "entries.parquet").exists()
    assert not (output_path / "metadata.json").exists()


def test_catalog_build_writes_bundle(
    runner: CliRunner,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "bundle"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "build",
            "--source",
            str(sample_workspace_path),
            "--out",
            str(output_path),
        ],
    )
    assert result.exit_code == 0
    assert (output_path / "entries.parquet").exists()
    assert (output_path / "MANIFEST.md").exists()
    assert (output_path / "metadata.json").exists()


def test_catalog_build_requires_overwrite_for_existing_bundle(
    runner: CliRunner,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "bundle"
    first_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "build",
            "--source",
            str(sample_workspace_path),
            "--out",
            str(output_path),
        ],
    )
    assert first_result.exit_code == 0

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "build",
            "--source",
            str(sample_workspace_path),
            "--out",
            str(output_path),
        ],
    )
    assert_cli_error(result, "Pass --overwrite")


def test_catalog_validate_accepts_bundle(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "validate",
            "--source",
            str(bundle_path),
            "--format",
            "jsonl",
        ],
    )

    rows = {row["name"]: row["rows"] for row in jsonl_rows(result)}
    assert rows["guidelines"] == 2
    assert rows["manifest_section_roles"] == 1


def test_catalog_export_duckdb_writes_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    import duckdb

    duckdb_path = tmp_path / "duckdb" / "catalog.duckdb"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "export",
            "duckdb",
            "--source",
            str(sample_catalog_path),
            "--out",
            str(duckdb_path),
        ],
    )

    assert result.exit_code == 0
    assert duckdb_path.exists()
    assert "Wrote DuckDB catalog" in result.output

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        guidelines_count = conn.execute("select count(*) from guidelines").fetchone()
        labels_count = conn.execute("select count(*) from labels").fetchone()
    finally:
        conn.close()
    assert guidelines_count == (2,)
    assert labels_count == (5,)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "export",
            "duckdb",
            "--source",
            str(sample_catalog_path),
            "--out",
            str(duckdb_path),
        ],
    )
    assert_cli_error(result, "Pass --overwrite")


def test_duckdb_overwrite_preserves_existing_file_on_failure(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import duckdb

    import chartcoach.duckdb as duckdb_module

    duckdb_path = tmp_path / "duckdb" / "catalog.duckdb"
    duckdb_module.write_duckdb(sample_catalog, duckdb_path)

    def fail_register(*_: object, **__: object) -> None:
        raise RuntimeError("register failed")

    monkeypatch.setattr(duckdb_module, "register_catalog", fail_register)

    with pytest.raises(RuntimeError, match="register failed"):
        duckdb_module.write_duckdb(sample_catalog, duckdb_path, overwrite=True)

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        row = conn.execute("select count(*) from guidelines").fetchone()
    finally:
        conn.close()
    assert row == (2,)


def test_catalog_manifest_cli_prints_manifest(
    runner: CliRunner,
    sample_workspace_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "manifest",
            "--source",
            str(sample_workspace_path),
            "--format",
            "jsonl",
        ],
    )

    payload = jsonl_rows(result)[0]
    assert payload["section_roles"] == ["advice"]
    assert payload["label_families"] == ["chart", "component", "task"]


def test_catalog_manifest_cli_explains_manifestless_sources(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "manifest",
            "--source",
            str(sample_catalog_path),
            "--format",
            "jsonl",
        ],
    )

    assert_cli_error(result, "Catalog source has no manifest")
    assert "Omit --source to use the package-pinned default catalog artifact." in result.output
    assert "Use standalone parquet files for records, tables, SQL, and indexing." in result.output


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

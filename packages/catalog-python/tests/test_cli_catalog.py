from __future__ import annotations

import json
from pathlib import Path
import shutil
import tarfile
from typing import cast

from click.testing import CliRunner
import pytest

import chartcoach.cli.common as common_cli
from chartcoach import Catalog
from chartcoach.catalog import remote as catalog_remote
from chartcoach.catalog.remote import read_release_metadata
from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.constants import (
    CHARTCOACH_DEFAULTS,
    DEFAULT_CATALOG_DIGEST,
    DEFAULT_CATALOG_VERSION,
)

from helpers import jsonl_rows
from catalog_testkit import sha256


def test_catalog_defaults_exports_package_pinned_values(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["catalog", "defaults", "--format", "json"])

    assert result.exit_code == 0
    assert json.loads(result.output) == {
        **CHARTCOACH_DEFAULTS.to_record(),
        "catalogReleaseRootUrl": CHARTCOACH_DEFAULTS.catalog_release_root_url,
    }


def test_catalog_defaults_exports_shell_variables(runner: CliRunner) -> None:
    result = runner.invoke(chartcoach_cli, ["catalog", "defaults", "--format", "sh"])

    assert result.exit_code == 0
    lines = result.output.splitlines()
    assert (
        f"export DEFAULT_CATALOG_VERSION={CHARTCOACH_DEFAULTS.catalog_version}" in lines
    )
    assert (
        f"export GUIDELINE_URL_TEMPLATE='{CHARTCOACH_DEFAULTS.guideline_url_template}'"
    ) in lines
    assert (
        f"export CATALOG_RELEASE_ROOT_URL={CHARTCOACH_DEFAULTS.catalog_release_root_url}"
        in lines
    )


def cache_default_catalog(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    catalog: Catalog,
) -> None:
    bundle_path = catalog.write_bundle(tmp_path / "default-bundle")
    metadata = read_release_metadata(bundle_path)
    cache_root = tmp_path / "cache"
    target = (
        cache_root
        / "artifacts"
        / "catalog"
        / "releases"
        / metadata.version
        / metadata.digest
    )
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


def test_catalog_schema_accepts_positional_table_names(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "schema",
            "guidelines",
            "--source",
            str(sample_catalog_path),
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert {row["table"] for row in rows} == {"guidelines"}
    assert {"table": "guidelines", "column": "title", "type": "String"} in rows


def test_catalog_schema_table_listing_rejects_table_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "schema",
            "guidelines",
            "--source",
            str(sample_catalog_path),
            "--tables",
        ],
    )

    assert result.exit_code == 1
    assert "`catalog schema --tables` lists table names" in result.output
    assert "catalog schema TABLE" in result.output


def test_catalog_values_unknown_field_explains_field_shape(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "chart",
            "--source",
            str(sample_catalog_path),
        ],
    )

    assert result.exit_code == 1
    assert "FIELD names the value dimension to count" in result.output
    assert "catalog values labels --contains TEXT" in result.output
    assert "catalog labels --family FAMILY" in result.output


def test_catalog_values_labels_table_column_points_to_full_label_field(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "values",
            "labels.label",
            "--source",
            str(sample_catalog_path),
        ],
    )

    assert result.exit_code == 1
    assert "Unknown column for table labels: label" in result.output
    assert "catalog values labels" in result.output
    assert "catalog values guideline_labels.label" in result.output
    assert "catalog values label.family" in result.output


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
    assert "ID" in result.output
    assert "Title" in result.output
    assert "Description" in result.output
    assert "Labels" in result.output
    assert "chart:bar, component:axis" in result.output


def test_catalog_query_empty_table_output_prints_status_once(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "zzzzunlikelyagentquery",
            "--format",
            "table",
        ],
    )

    assert result.exit_code == 0, result.output
    assert result.output.count("No entries matched.") == 1
    assert "Guidance:" in result.output
    assert "Relax one text predicate" in result.output


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
    assert "Downloading chartcoach catalog" in first.stderr
    assert "Cache" in first.stderr
    assert second.stderr == ""
    assert downloads == [
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/MANIFEST.md",
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/entries.parquet",
    ]
    cached_release = (
        cache_root
        / "artifacts"
        / "catalog"
        / "releases"
        / metadata.version
        / metadata.digest
    )
    assert (cached_release / "metadata.json").exists()
    assert (cached_release / "MANIFEST.md").exists()
    assert (cached_release / "entries.parquet").exists()
    assert not (cached_release / "indexes").exists()


def test_catalog_cache_versions_reads_artifact_index(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    artifact_index = {
        "kind": "chartcoach-artifact-index",
        "version": 1,
        "catalogs": [
            {
                "name": "chartcoach/catalog",
                "version": "0.0.0",
                "digest": "old-digest",
                "root": "catalog/releases/0.0.0/old-digest/",
                "metadata": "catalog/releases/0.0.0/old-digest/metadata.json",
                "artifacts": [],
            },
            {
                "name": "chartcoach/catalog",
                "version": "0.1.2",
                "digest": "new-digest",
                "root": "catalog/releases/0.1.2/new-digest/",
                "metadata": "catalog/releases/0.1.2/new-digest/metadata.json",
                "artifacts": [],
            },
        ],
    }

    def read_url_text(url: str) -> str:
        assert url == "https://example.test/index.json"
        return json.dumps(artifact_index)

    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cache",
            "versions",
            "--index-url",
            "https://example.test/index.json",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert [row["version"] for row in rows] == ["0.0.0", "0.1.2"]
    assert rows[1]["metadata"] == "catalog/releases/0.1.2/new-digest/metadata.json"


def test_catalog_cache_clear_deletes_default_release(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_path = (
        tmp_path
        / "cache"
        / "artifacts"
        / "catalog"
        / "releases"
        / DEFAULT_CATALOG_VERSION
        / DEFAULT_CATALOG_DIGEST
    )
    release_path.mkdir(parents=True)
    (release_path / "metadata.json").write_text("{}")

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))

    result = runner.invoke(chartcoach_cli, ["catalog", "cache", "clear"])

    assert result.exit_code == 0, result.output
    assert "Deleted cached artifacts" in result.output
    assert not release_path.exists()


def test_catalog_cache_pull_downloads_latest_catalog_and_index(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    metadata = read_release_metadata(bundle_path)
    archive_source = tmp_path / "index.tar.gz"
    table_dir = tmp_path / "index-source" / "catalog_documents.lance"
    table_dir.mkdir(parents=True)
    (table_dir / "data.txt").write_text("indexed rows")
    with tarfile.open(archive_source, "w:gz") as archive:
        archive.add(table_dir, arcname="catalog_documents.lance")
    metadata = catalog_remote.CatalogReleaseMetadata(
        version="9.0.0",
        digest=metadata.digest,
        artifacts=(
            *metadata.artifacts,
            catalog_remote.ArtifactDescriptor(
                kind="lancedb-index",
                path="indexes/lancedb/openrouter/model/index.tar.gz",
                digest=sha256(archive_source),
                bytes=archive_source.stat().st_size,
                format="tar+gzip",
                extra={"table": "catalog_documents"},
            ),
        ),
    )
    artifact_index = {
        "kind": "chartcoach-artifact-index",
        "version": 1,
        "catalogs": [
            {
                "name": "chartcoach/catalog",
                "version": "9.0.0",
                "digest": metadata.digest,
                "root": f"catalog/releases/9.0.0/{metadata.digest}/",
                "metadata": f"catalog/releases/9.0.0/{metadata.digest}/metadata.json",
                "artifacts": [
                    {
                        **artifact.to_record(),
                        "path": f"catalog/releases/9.0.0/{metadata.digest}/{artifact.path}",
                    }
                    for artifact in metadata.artifacts
                ],
            }
        ],
    }
    metadata_url = (
        f"https://example.test/catalog/releases/9.0.0/{metadata.digest}/metadata.json"
    )
    downloads: list[str] = []

    def read_url_text(url: str) -> str:
        if url == "https://example.test/index.json":
            return json.dumps(artifact_index)
        if url == metadata_url:
            return json.dumps(metadata.to_record())
        raise AssertionError(f"Unexpected URL: {url}")

    def download_file(url: str, path: Path) -> None:
        downloads.append(url)
        if url.endswith("/MANIFEST.md"):
            shutil.copyfile(bundle_path / "MANIFEST.md", path)
            return
        if url.endswith("/entries.parquet"):
            shutil.copyfile(bundle_path / "entries.parquet", path)
            return
        if url.endswith("/index.tar.gz"):
            shutil.copyfile(archive_source, path)
            return
        raise AssertionError(f"Unexpected artifact URL: {url}")

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cache",
            "pull",
            "--index-url",
            "https://example.test/index.json",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    assert "Downloading chartcoach catalog" in result.stderr
    assert "Downloading chartcoach LanceDB index" in result.stderr
    payload = cast(list[dict[str, object]], json.loads(result.stdout))
    catalog_path = Path(cast(str, payload[0]["catalog_path"]))
    index_path = Path(cast(str, payload[0]["index_path"]))
    assert (catalog_path / "MANIFEST.md").is_file()
    assert (catalog_path / "entries.parquet").is_file()
    assert (
        index_path / "catalog_documents.lance" / "data.txt"
    ).read_text() == "indexed rows"
    assert (index_path.parent / "index.tar.gz").is_file()
    assert downloads == [
        f"https://example.test/catalog/releases/9.0.0/{metadata.digest}/MANIFEST.md",
        f"https://example.test/catalog/releases/9.0.0/{metadata.digest}/entries.parquet",
        f"https://example.test/catalog/releases/9.0.0/{metadata.digest}/indexes/lancedb/openrouter/model/index.tar.gz",
    ]


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
    assert values_result.stdout.strip() == "0 rows"
    assert "Try a shorter or broader --contains value." in values_result.stderr

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
    assert "Table" in result.output
    assert "Column" in result.output
    assert "Value" in result.output
    assert "Rows" in result.output
    assert "guideline_labels" in result.output
    assert "chart:" in result.output
    assert "Returned 1 values. Increase --limit to inspect more." in result.stderr

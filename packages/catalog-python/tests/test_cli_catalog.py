from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from click.testing import CliRunner, Result
import pytest

from chartcoach import Catalog
from chartcoach.cli import guidelines as guidelines_cli
from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error, csv_rows, json_value, jsonl_rows


GUIDELINE_SEARCH_RESULT: dict[str, object] = {
    "query": "direct labels",
    "rows": [
        {
            "rank": 1,
            "id": "direct-labels",
            "title": "Use direct labels",
            "description": "Label marks directly when space permits.",
            "labels": ["chart:line"],
            "matched_document_id": "direct-labels---overview",
            "matched_role": "overview",
            "score": 0.125,
            "matched_text": "Use direct labels\n\nLabel marks directly.",
        }
    ],
    "row_count": 1,
    "limit": 8,
}


def patch_guideline_search(
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, object]:
    captured_guideline_kwargs: dict[str, object] = {}

    def fake_search_guidelines(
        self: object, query_text: str, **kwargs: object
    ) -> dict[str, object]:
        captured_guideline_kwargs["query_text"] = query_text
        captured_guideline_kwargs.update(kwargs)
        return GUIDELINE_SEARCH_RESULT

    monkeypatch.setattr(
        guidelines_cli.CatalogTools,
        "search_guidelines",
        fake_search_guidelines,
    )
    return captured_guideline_kwargs


def guideline_search_args(sample_catalog_path: Path, index_dir: Path) -> list[str]:
    return [
        "guidelines",
        "search",
        "--source",
        str(sample_catalog_path),
        "--index-dir",
        str(index_dir),
        "direct labels",
    ]


def test_guidelines_cli_list_filters_catalog(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "list",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "axis",
            "--format",
            "jsonl",
        ],
    )
    assert [row["id"] for row in jsonl_rows(result)] == ["full-axis-bars"]


def test_guidelines_cli_show_emits_complete_guideline_record(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "show",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--format",
            "jsonl",
        ],
    )
    guideline = jsonl_rows(result)
    assert len(guideline) == 1
    assert guideline[0]["id"] == "direct-labels"
    assert guideline[0]["guideline"]["title"] == "Use direct labels"


def test_tables_cli_reports_schema_and_values(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        ["tables", "schema", "--source", str(sample_catalog_path), "--format", "jsonl"],
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
            "tables",
            "values",
            "guideline_labels",
            "label",
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


def test_read_commands_require_explicit_source(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)

    result = runner.invoke(chartcoach_cli, ["tables", "list", "--format", "jsonl"])

    assert_cli_error(result, "Pass --source PATH")


def test_sql_cli_queries_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
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


def test_sql_cli_rejects_non_select_statements(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "sql",
            "--source",
            str(sample_catalog_path),
            "create table x as select 1",
        ],
    )

    assert_cli_error(result, "Only SELECT queries are allowed")


def test_catalog_check_rejects_empty_workspace(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
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
    result = runner.invoke(chartcoach_cli, ["catalog", "check", "--source", str(empty)])
    assert_cli_error(result, "No guideline entries found")


def test_catalog_build_is_workspace_scoped(
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
    assert not (output_path / "catalog.parquet").exists()

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
    assert (output_path / "catalog.parquet").exists()
    assert (output_path / "MANIFEST.md").exists()

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


def test_catalog_check_accepts_artifact_bundle(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "check",
            "--source",
            str(bundle_path),
            "--format",
            "jsonl",
        ],
    )

    rows = {row["name"]: row["rows"] for row in jsonl_rows(result)}
    assert rows["guidelines"] == 2
    assert rows["manifest_section_roles"] == 1


def test_catalog_duckdb_writes_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    import duckdb

    duckdb_path = tmp_path / "artifacts" / "catalog.duckdb"

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
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

    duckdb_path = tmp_path / "artifacts" / "catalog.duckdb"
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


@pytest.mark.search
def test_artifacts_cli_lists_native_paths(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    index_dir = tmp_path / "index"

    result = runner.invoke(
        chartcoach_cli,
        [
            "artifacts",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(index_dir),
            "--format",
            "jsonl",
        ],
    )

    rows = {row["name"]: row for row in jsonl_rows(result)}
    assert set(rows) == {
        "catalog_manifest",
        "catalog_source",
        "catalog_parquet",
        "duckdb_catalog",
        "index_root",
        "index_table",
    }
    assert rows["catalog_manifest"]["path"] == str(
        sample_catalog_path.parent / "MANIFEST.md"
    )
    assert rows["catalog_source"]["path"] == str(sample_catalog_path)
    index_root = Path(str(rows["index_root"]["path"]))
    assert index_root.is_relative_to(index_dir)
    assert Path(str(rows["index_table"]["path"])) == (
        index_root / "catalog_documents.lance"
    )
    assert rows["index_table"]["table_name"] == "catalog_documents"


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


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (
            ["guidelines", "retrieve", "--id", "missing-guideline"],
            "Unknown guideline id: missing-guideline",
        ),
        (["guidelines", "list", "--label", "chart:missing"], "Unknown label"),
        (["guidelines", "retrieve", "--section", "missing"], "Unknown section role"),
    ],
)
def test_guidelines_cli_renders_error_hints(
    runner: CliRunner,
    sample_catalog_path: Path,
    argv: list[str],
    expected: str,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [*argv[:2], "--source", str(sample_catalog_path), *argv[2:]],
    )

    assert_cli_error(result, expected)


def test_guidelines_cli_retrieves_section_specific_evidence(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "retrieve",
            "--source",
            str(sample_catalog_path),
            "--id",
            "full-axis-bars",
            "--section",
            "advice",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert result.exit_code == 0
    assert rows == [
        {
            "id": "full-axis-bars",
            "title": "Use full value axes for bars",
            "description": "Keep bar axes on the honest baseline.",
            "labels": ["chart:bar", "component:axis"],
            "references": [],
            "sections": [
                {
                    "role": "advice",
                    "title": "Advice",
                    "content": "Start bar value axes at zero.",
                }
            ],
        }
    ]


@pytest.mark.search
def test_guidelines_search_requires_existing_index_with_actionable_error(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(
        guidelines_cli.CatalogTools,
        "search_guidelines",
        raise_missing_index,
    )

    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "search",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(tmp_path / "index"),
            "axis",
        ],
    )

    assert_cli_error(result, "missing search index")
    assert "Build or provide a search index" in result.output
    assert "Inspect catalog artifacts" in result.output


@pytest.mark.search
@pytest.mark.parametrize(
    ("output_format", "reader"),
    [
        ("json", lambda result: json_value(result)["rows"][0]["id"]),
        ("jsonl", lambda result: jsonl_rows(result)[0]["id"]),
        ("csv", lambda result: csv_rows(result)[0]["id"]),
    ],
)
def test_guidelines_search_structured_formats_return_guideline_rows(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    output_format: str,
    reader: Callable[[Result], object],
) -> None:
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *guideline_search_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            output_format,
        ],
    )

    assert reader(result) == "direct-labels"


@pytest.mark.search
def test_guidelines_search_markdown_keeps_stable_evidence(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *guideline_search_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "direct-labels" in result.output
    assert "score: `0.125`" in result.output


@pytest.mark.search
def test_guidelines_search_forwards_native_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured_guideline_kwargs = patch_guideline_search(monkeypatch)
    result = runner.invoke(
        chartcoach_cli,
        [
            *guideline_search_args(sample_catalog_path, tmp_path / "index"),
            "--where",
            "role = 'section.advice'",
            "--format",
            "json",
        ],
    )
    payload = json_value(result)
    assert payload["rows"][0]["id"] == "direct-labels"
    assert captured_guideline_kwargs["where"] == "role = 'section.advice'"
    assert captured_guideline_kwargs["limit"] == 8


@pytest.mark.search
def test_index_cli_queries_documents_with_native_options(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    fake_index_root = tmp_path / "index" / "digest"

    monkeypatch.setattr(
        "chartcoach.tools.catalog.CatalogTools.query_documents",
        lambda _self, query, *, limit, where: (
            captured.update({"query": query, "limit": limit, "where": where})
            or {
                "query": query,
                "rows": [{"id": "doc", "parent_id": "direct-labels", "_score": 1.2}],
                "row_count": 1,
                "limit": limit,
                "where": where,
                "index_root": str(fake_index_root),
                "table_name": "catalog_documents",
            }
        ),
    )

    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "query",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(tmp_path / "index"),
            "axis labels",
            "--limit",
            "2",
            "--where",
            "role = 'overview'",
        ],
    )

    assert result.exit_code == 0
    payload = json_value(result)
    assert payload["rows"] == [
        {"id": "doc", "parent_id": "direct-labels", "_score": 1.2}
    ]
    assert payload["table_name"] == "catalog_documents"
    assert captured == {
        "query": "axis labels",
        "limit": 2,
        "where": "role = 'overview'",
    }


@pytest.mark.search
def test_index_cli_queries_built_lance_index(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    pytest.importorskip("lancedb")
    index_dir = tmp_path / "index"

    build_result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "build",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(index_dir),
        ],
    )
    assert build_result.exit_code == 0

    query_result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "query",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(index_dir),
            "direct labels",
            "--limit",
            "5",
            "--where",
            "parent_id = 'direct-labels'",
        ],
    )

    assert query_result.exit_code == 0
    payload = json_value(query_result)
    assert payload["table_name"] == "catalog_documents"
    assert payload["row_count"] >= 1
    assert {row["parent_id"] for row in payload["rows"]} == {"direct-labels"}


@pytest.mark.search
def test_index_cli_rejects_invalid_limit_before_opening_index(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "query",
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(tmp_path / "index"),
            "axis labels",
            "--limit",
            "0",
        ],
    )

    assert_cli_error(result, "Invalid value for '--limit'", exit_code=2)

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from click.testing import CliRunner, Result
import pytest

from chartcoach import Catalog
from chartcoach.cli import guidelines as guidelines_cli
from chartcoach.cli.main import main as chartcoach_cli

from helpers import csv_rows, json_value, jsonl_rows


class FakeGuidelineSearchResult:
    def to_dict(self) -> dict[str, object]:
        return {
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
                    "distance": 0.125,
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
        *_: object, **kwargs: object
    ) -> FakeGuidelineSearchResult:
        captured_guideline_kwargs.update(kwargs)
        return FakeGuidelineSearchResult()

    monkeypatch.setattr(
        guidelines_cli.ChromaIndex,
        "from_cache",
        staticmethod(lambda *_args, **_kwargs: object()),
    )
    monkeypatch.setattr(guidelines_cli, "search_guidelines", fake_search_guidelines)
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


def test_guidelines_cli_show_emits_wire_record(
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

    assert result.exit_code == 1
    assert "Pass --source PATH" in result.output


def test_catalog_check_rejects_empty_workspace(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    result = runner.invoke(chartcoach_cli, ["catalog", "check", "--source", str(empty)])
    assert result.exit_code == 1
    assert "No guideline entries found" in result.output


def test_catalog_build_is_workspace_scoped(
    runner: CliRunner,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "catalog.parquet"

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
    assert not output_path.exists()

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
    assert output_path.exists()

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
    assert result.exit_code == 1
    assert "Pass --overwrite" in result.output


@pytest.mark.duckdb
def test_catalog_duckdb_writes_catalog_tables(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    duckdb = pytest.importorskip("duckdb")
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
    assert result.exit_code == 1
    assert "Pass --overwrite" in result.output


@pytest.mark.duckdb
def test_duckdb_overwrite_preserves_existing_file_on_failure(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    duckdb = pytest.importorskip("duckdb")
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
    pytest.importorskip("chromadb")
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
        "catalog_source",
        "catalog_parquet",
        "duckdb_catalog",
        "index_root",
        "chroma",
    }
    assert rows["catalog_source"]["path"] == str(sample_catalog_path)
    assert rows["index_root"]["path"] == str(index_dir)
    assert rows["chroma"]["collection_name"] == "catalog"


def test_feedback_prompt_cli_uses_local_image_and_deterministic_evidence(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    image_path = tmp_path / "chart.jpg"
    image_path.write_bytes(b"not a real jpeg")

    result = runner.invoke(
        chartcoach_cli,
        [
            "feedback",
            "prompt",
            "--source",
            str(sample_catalog_path),
            "--image",
            str(image_path),
            "--situation",
            "Quick public comparison.",
            "--label",
            "chart:bar",
            "--section",
            "advice",
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "# Chart Feedback Prompt" in result.output
    assert str(image_path) in result.output
    assert "Quick public comparison." in result.output
    assert "full-axis-bars" in result.output
    assert "Start bar value axes at zero." in result.output


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

    assert result.exit_code == 1
    assert expected in result.output
    assert "Traceback" not in result.output


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
        ],
    )

    assert result.exit_code == 0
    assert "Use full value axes for bars" in result.output
    assert "Start bar value axes at zero." in result.output
    assert "direct-labels" not in result.output


@pytest.mark.search
def test_guidelines_search_validates_filters_before_opening_index(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "search",
            "--source",
            str(sample_catalog_path),
            "--where",
            "{",
            "axis labels",
        ],
    )

    assert result.exit_code == 1
    assert "--where must be valid JSON" in result.output
    assert "chartcoach index build" not in result.output
    assert "Traceback" not in result.output


@pytest.mark.search
def test_guidelines_search_requires_existing_index_without_traceback(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(
        guidelines_cli.ChromaIndex,
        "from_cache",
        staticmethod(raise_missing_index),
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

    assert result.exit_code == 1
    assert "missing search index" in result.output
    assert "chartcoach index build --source PATH" in result.output
    assert "Traceback" not in result.output


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
    assert "distance: `0.125`" in result.output


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
            '{"role":"section.advice"}',
            "--format",
            "json",
        ],
    )
    payload = json_value(result)
    assert payload["rows"][0]["id"] == "direct-labels"
    assert captured_guideline_kwargs["where"] == {"role": "section.advice"}
    assert captured_guideline_kwargs["limit"] == 8


@pytest.mark.search
@pytest.mark.parametrize(
    ("command", "payload", "expected_params"),
    [
        (
            "query",
            '{"query_texts":["axis","labels"],"n_results":2,"include":["documents"]}',
            {
                "query_texts": ["axis", "labels"],
                "n_results": 2,
                "include": ["documents"],
            },
        ),
        (
            "get",
            '{"ids":["doc"],"include":["metadatas"]}',
            {"ids": ["doc"], "include": ["metadatas"]},
        ),
    ],
)
def test_index_cli_passes_native_chroma_params(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    command: str,
    payload: str,
    expected_params: dict[str, object],
) -> None:
    import chartcoach.search.chroma as chroma

    captured: dict[str, object] = {}

    class FakeCollection:
        def count(self) -> int:
            return 1

        def query(self, **params: object) -> dict[str, object]:
            captured.update(params)
            return {"ids": [["doc"]]}

        def get(self, **params: object) -> dict[str, object]:
            captured.update(params)
            return {"ids": ["doc"]}

    class FakeIndex:
        collection = FakeCollection()

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "from_cache",
        staticmethod(lambda *_args, **_kwargs: FakeIndex()),
    )

    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            command,
            "--source",
            str(sample_catalog_path),
            "--index-dir",
            str(tmp_path / "index"),
            payload,
        ],
    )

    assert result.exit_code == 0
    assert captured == expected_params

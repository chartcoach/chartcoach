from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogEntry, Guideline, Section
from chartcoach.cli import artifacts as artifacts_cli
from chartcoach.cli import catalog as catalog_cli
from chartcoach.cli import feedback as feedback_cli
from chartcoach.cli import guidelines as guidelines_cli
from chartcoach.cli import index as index_cli
from chartcoach.cli import tables as tables_cli


def _source_path(tmp_path: Path) -> Path:
    catalog = Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line", "task:lookup"),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Place labels near marks.",
                        ),
                    ),
                )
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="full-axis-bars",
                    title="Use full value axes for bars",
                    description="Keep bar axes on the honest baseline.",
                    body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                    labels=("chart:bar", "component:axis"),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Start bar value axes at zero.",
                        ),
                    ),
                )
            ),
        ]
    )
    path = tmp_path / "catalog.parquet"
    catalog.write_parquet(path)
    return path


def _workspace_path(tmp_path: Path) -> Path:
    workspace = tmp_path / "workspace"
    Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line",),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Place labels near marks.",
                        ),
                    ),
                )
            )
        ]
    ).write_folder(workspace)
    return workspace


def test_guidelines_cli_lists_and_shows_guidelines(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["list", "--source", str(path), "--contains", "axis", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert "full-axis-bars" in result.output
    assert "direct-labels" not in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["show", "--source", str(path), "direct-labels"],
    )

    assert result.exit_code == 0
    assert "Use direct labels" in result.output
    assert "Place labels near marks." in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["show", "--source", str(path), "direct-labels", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert result.output.count("\n") == 1
    assert '"id": "direct-labels"' in result.output


def test_read_commands_require_explicit_source(monkeypatch: pytest.MonkeyPatch) -> None:
    repo_root = Path(__file__).parents[3]
    monkeypatch.chdir(repo_root)
    monkeypatch.delenv("CHARTCOACH_SOURCE", raising=False)

    result = CliRunner().invoke(
        tables_cli.tables_command,
        ["list", "--format", "jsonl"],
    )

    assert result.exit_code == 1
    assert "Pass --source PATH" in result.output


def test_catalog_build_and_check_are_workspace_scoped(tmp_path: Path) -> None:
    workspace = _workspace_path(tmp_path)
    output_path = tmp_path / "catalog.parquet"

    empty = tmp_path / "empty"
    empty.mkdir()
    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["check", "--source", str(empty)],
    )
    assert result.exit_code == 1
    assert "No guideline entries found" in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["build", "--source", str(workspace), "--out", str(output_path), "--dry-run"],
    )
    assert result.exit_code == 0
    assert not output_path.exists()

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["build", "--source", str(workspace), "--out", str(output_path)],
    )
    assert result.exit_code == 0
    assert output_path.exists()

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["build", "--source", str(workspace), "--out", str(output_path)],
    )
    assert result.exit_code == 1
    assert "Pass --overwrite" in result.output



def test_catalog_duckdb_writes_catalog_tables(tmp_path: Path) -> None:
    pytest.importorskip("duckdb")
    path = _source_path(tmp_path)
    duckdb_path = tmp_path / "artifacts" / "catalog.duckdb"

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "duckdb",
            "--source",
            str(path),
            "--out",
            str(duckdb_path),
        ],
    )

    assert result.exit_code == 0
    assert duckdb_path.exists()
    assert "Wrote DuckDB catalog" in result.output

    import duckdb

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        guidelines_count = conn.execute("select count(*) from guidelines").fetchone()
        labels_count = conn.execute("select count(*) from labels").fetchone()
        assert guidelines_count is not None
        assert labels_count is not None
        assert guidelines_count[0] == 2
        assert labels_count[0] == 4
    finally:
        conn.close()

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["duckdb", "--source", str(path), "--out", str(duckdb_path)],
    )
    assert result.exit_code == 1
    assert "Pass --overwrite" in result.output


def test_duckdb_overwrite_preserves_existing_file_on_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    duckdb = pytest.importorskip("duckdb")
    import chartcoach.duckdb as duckdb_module

    path = _source_path(tmp_path)
    catalog = Catalog.from_parquet(path)
    duckdb_path = tmp_path / "artifacts" / "catalog.duckdb"
    duckdb_module.write_duckdb(catalog, duckdb_path)

    def fail_register(*_: object, **__: object) -> None:
        raise RuntimeError("register failed")

    monkeypatch.setattr(duckdb_module, "register_catalog", fail_register)

    with pytest.raises(RuntimeError, match="register failed"):
        duckdb_module.write_duckdb(catalog, duckdb_path, overwrite=True)

    conn = duckdb.connect(duckdb_path, read_only=True)
    try:
        row = conn.execute("select count(*) from guidelines").fetchone()
    finally:
        conn.close()
    assert row == (2,)


def test_tables_cli_lists_and_describes_schema(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        tables_cli.tables_command,
        ["schema", "--source", str(path), "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"table": "guidelines"' in result.output
    assert '"column": "title"' in result.output

    result = CliRunner().invoke(
        tables_cli.tables_command,
        ["list", "--source", str(path), "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"name": "sections"' in result.output
    assert '"name": "labels"' in result.output


def test_artifacts_cli_lists_native_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    path = _source_path(tmp_path)
    index_dir = tmp_path / "index"
    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(
            lambda _catalog, **_kwargs: chroma.ChromaIndexPaths(
                index_root=index_dir,
                cache_path=index_dir / "digest" / "embedding",
                chroma_path=index_dir / "digest" / "embedding" / "chroma_db",
                catalog_digest="digest",
                documents_version="documents-v1",
                embedding_name="tiny",
                collection_name="catalog",
            )
        ),
    )

    result = CliRunner().invoke(
        artifacts_cli.artifacts_command,
        [
            "--source",
            str(path),
            "--index-dir",
            str(index_dir),
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert '"name": "catalog_parquet"' in result.output
    assert '"name": "duckdb_catalog"' in result.output
    assert '"name": "chroma"' in result.output
    assert '"collection_name": "catalog"' in result.output
    assert f"--source {path.as_posix()!r}" in result.output


def test_artifacts_cli_does_not_require_index_dir(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        artifacts_cli.artifacts_command,
        ["--source", str(path), "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"name": "catalog_parquet"' in result.output
    assert '"name": "duckdb_catalog"' in result.output
    assert '"name": "index_root"' in result.output
    assert '"name": "chroma"' in result.output


def test_artifacts_cli_survives_missing_search_extras(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    path = _source_path(tmp_path)

    def raise_missing_search_extra(*_: object, **__: object) -> object:
        raise ModuleNotFoundError("missing polars_hash", name="polars_hash")

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "cache_paths",
        staticmethod(raise_missing_search_extra),
    )

    result = CliRunner().invoke(
        artifacts_cli.artifacts_command,
        ["--source", str(path), "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"name": "catalog_parquet"' in result.output
    assert '"name": "duckdb_catalog"' in result.output
    assert '"name": "index_root"' in result.output
    assert '"name": "chroma"' not in result.output
    assert "Search extras are required" in result.output


def test_feedback_prompt_cli_uses_local_image_and_deterministic_evidence(
    tmp_path: Path,
) -> None:
    path = _source_path(tmp_path)
    image_path = tmp_path / "chart.jpg"
    image_path.write_bytes(b"not a real jpeg")

    result = CliRunner().invoke(
        feedback_cli.feedback_command,
        [
            "prompt",
            "--source",
            str(path),
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


def test_tables_cli_counts_values(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        tables_cli.tables_command,
        [
            "values",
            "guideline_labels",
            "label",
            "--source",
            str(path),
            "--contains",
            "chart:",
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert '"value": "chart:bar"' in result.output
    assert '"value": "chart:line"' in result.output


def test_guidelines_cli_retrieves_section_specific_evidence(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        [
            "retrieve",
            "--source",
            str(path),
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


def test_guidelines_cli_retrieve_fails_on_unknown_id(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["retrieve", "--source", str(path), "--id", "missing-guideline"],
    )

    assert result.exit_code == 1
    assert "Unknown guideline id: missing-guideline" in result.output
    assert "guidelines list --source PATH --format jsonl" in result.output
    assert "Traceback" not in result.output


def test_guidelines_cli_list_validates_labels(tmp_path: Path) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["list", "--source", str(path), "--label", "chart:missing"],
    )

    assert result.exit_code == 1
    assert "Unknown label" in result.output
    assert "chartcoach tables values guideline_labels label" in result.output
    assert "Traceback" not in result.output


def test_guidelines_search_invalid_where_json_does_not_emit_index_hint(
    tmp_path: Path,
) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["search", "--source", str(path), "--where", "{", "axis labels"],
    )

    assert result.exit_code == 1
    assert "--where must be valid JSON" in result.output
    assert "chartcoach index build" not in result.output
    assert "Traceback" not in result.output


def test_guidelines_cli_retrieve_validates_labels_and_sections(
    tmp_path: Path,
) -> None:
    path = _source_path(tmp_path)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["retrieve", "--source", str(path), "--label", "chart:missing"],
    )

    assert result.exit_code == 1
    assert "Unknown label" in result.output
    assert "chartcoach tables values guideline_labels label" in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["retrieve", "--source", str(path), "--section", "advice"],
    )

    assert result.exit_code == 0
    assert "Place labels near marks." in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["retrieve", "--source", str(path), "--section", "missing"],
    )

    assert result.exit_code == 1
    assert "Unknown section role" in result.output
    assert "DuckDB or Polars" in result.output


def test_guidelines_search_requires_existing_index_without_traceback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = _source_path(tmp_path)

    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(
        guidelines_cli.ChromaIndex,
        "from_cache",
        staticmethod(raise_missing_index),
    )

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        ["search", "--source", str(path), "--index-dir", str(tmp_path / "index"), "axis"],
    )

    assert result.exit_code == 1
    assert "missing search index" in result.output
    assert "chartcoach index build --source PATH" in result.output
    assert "Traceback" not in result.output


def test_guidelines_search_flattens_guideline_results(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = _source_path(tmp_path)
    captured_guideline_kwargs: dict[str, object] = {}

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

    def fake_search_guidelines(*_: object, **kwargs: object) -> FakeGuidelineSearchResult:
        captured_guideline_kwargs.update(kwargs)
        return FakeGuidelineSearchResult()

    monkeypatch.setattr(
        guidelines_cli.ChromaIndex,
        "from_cache",
        staticmethod(lambda *_args, **_kwargs: object()),
    )
    monkeypatch.setattr(guidelines_cli, "search_guidelines", fake_search_guidelines)

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        [
            "search",
            "--source",
            str(path),
            "--index-dir",
            str(tmp_path / "index"),
            "direct labels",
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "direct-labels" in result.output
    assert "distance: `0.125`" in result.output
    assert "Use direct labels" in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        [
            "search",
            "--source",
            str(path),
            "--index-dir",
            str(tmp_path / "index"),
            "direct labels",
            "--format",
            "csv",
        ],
    )

    assert result.exit_code == 0
    assert "rank,id,title" in result.output
    assert "direct-labels" in result.output

    result = CliRunner().invoke(
        guidelines_cli.guidelines_command,
        [
            "search",
            "--source",
            str(path),
            "--index-dir",
            str(tmp_path / "index"),
            "direct labels",
            "--where",
            '{"role":"section.advice"}',
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert captured_guideline_kwargs["where"] == {"role": "section.advice"}
    assert captured_guideline_kwargs["limit"] == 8


def test_index_cli_passes_native_chroma_params(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.search.chroma as chroma

    path = _source_path(tmp_path)
    captured_query: dict[str, object] = {}
    captured_get: dict[str, object] = {}

    class FakeCollection:
        def count(self) -> int:
            return 1

        def query(self, **params: object) -> dict[str, object]:
            captured_query.update(params)
            return {"ids": [["doc"]]}

        def get(self, **params: object) -> dict[str, object]:
            captured_get.update(params)
            return {"ids": ["doc"]}

    class FakeIndex:
        collection = FakeCollection()

    monkeypatch.setattr(
        chroma.ChromaIndex,
        "from_cache",
        staticmethod(lambda *_args, **_kwargs: FakeIndex()),
    )

    result = CliRunner().invoke(
        index_cli.index_command,
        [
            "query",
            "--source",
            str(path),
            "--index-dir",
            str(tmp_path / "index"),
            '{"query_texts":["axis","labels"],"n_results":2,"include":["documents"]}',
        ],
    )

    assert result.exit_code == 0
    assert captured_query == {
        "query_texts": ["axis", "labels"],
        "n_results": 2,
        "include": ["documents"],
    }

    result = CliRunner().invoke(
        index_cli.index_command,
        [
            "get",
            "--source",
            str(path),
            "--index-dir",
            str(tmp_path / "index"),
            '{"ids":["doc"],"include":["metadatas"]}',
        ],
    )

    assert result.exit_code == 0
    assert captured_get == {"ids": ["doc"], "include": ["metadatas"]}

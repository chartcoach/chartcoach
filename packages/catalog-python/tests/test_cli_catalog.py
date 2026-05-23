from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach import Catalog, CatalogEntry, Guideline
from chartcoach.cli import catalog as catalog_cli


def _catalog_path(tmp_path: Path) -> Path:
    catalog = Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line", "task:lookup"),
                )
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="full-axis-bars",
                    title="Use full value axes for bars",
                    description="Keep bar axes on the honest baseline.",
                    body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                    labels=("chart:bar", "component:axis"),
                )
            ),
        ]
    )
    path = tmp_path / "catalog.parquet"
    catalog.write_parquet(path)
    return path


def test_catalog_cli_lists_and_shows_guidelines(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "list", "--contains", "axis", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert "full-axis-bars" in result.output
    assert "direct-labels" not in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "show", "direct-labels"],
    )

    assert result.exit_code == 0
    assert "Use direct labels" in result.output
    assert "Place labels near marks." in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "show", "direct-labels", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert result.output.count("\n") == 1
    assert '"id": "direct-labels"' in result.output


def test_catalog_cli_runs_sql_without_search(tmp_path: Path) -> None:
    pytest.importorskip("duckdb")
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "sql",
            "select id, title from guidelines order by id",
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert '"id": "direct-labels"' in result.output
    assert '"id": "full-axis-bars"' in result.output


def test_catalog_cli_registers_the_same_relations_it_advertises(tmp_path: Path) -> None:
    pytest.importorskip("duckdb")
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "sql",
            "select category, subcategory from labels order by category limit 1",
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert '"category": "chart"' in result.output


def test_catalog_cli_renders_sql_errors_without_traceback(tmp_path: Path) -> None:
    pytest.importorskip("duckdb")
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "sql",
            "select nope from guidelines",
        ],
    )

    assert result.exit_code == 1
    assert "nope" in result.output
    assert "Try:" in result.output
    assert "schema --format jsonl" in result.output
    assert "Traceback" not in result.output


def test_catalog_cli_rejects_mutating_sql(tmp_path: Path) -> None:
    pytest.importorskip("duckdb")
    path = _catalog_path(tmp_path)
    external_csv = tmp_path / "external.csv"
    external_csv.write_text("value\n1\n", encoding="utf-8")

    for sql in [
        "create table scratch as select 1",
        "copy guidelines to 'scratch.csv'",
        "select 1; select 2",
        f"select * from read_csv_auto('{external_csv.as_posix()}') limit 1",
    ]:
        result = CliRunner().invoke(
            catalog_cli.catalog_command,
            [
                "--catalog",
                str(path),
                "sql",
                sql,
            ],
        )

        assert result.exit_code == 1
        assert "Traceback" not in result.output


def test_catalog_cli_lists_sql_schema(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "schema", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"relation": "guidelines"' in result.output
    assert '"column": "title"' in result.output


def test_catalog_cli_discovers_relations_and_values(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "relations", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"name": "sections"' in result.output
    assert '"name": "labels"' in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "values", "sections", "role", "--format", "jsonl"],
    )

    assert result.exit_code == 0
    assert '"relation": "sections"' in result.output
    assert '"column": "role"' in result.output
    assert '"value": "advice"' in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "values",
            "guidelines",
            "labels",
            "--explode",
            "--contains",
            "chart:",
            "--format",
            "jsonl",
        ],
    )

    assert result.exit_code == 0
    assert '"value": "chart:bar"' in result.output
    assert '"value": "chart:line"' in result.output


def test_catalog_cli_value_errors_are_actionable(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "values", "missing", "role"],
    )

    assert result.exit_code == 1
    assert "Unknown relation" in result.output
    assert "relations --format jsonl" in result.output
    assert "Traceback" not in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "values", "sections", "missing"],
    )

    assert result.exit_code == 1
    assert "Unknown column" in result.output
    assert "schema --relation sections --format jsonl" in result.output
    assert "Traceback" not in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "values", "guidelines", "labels"],
    )

    assert result.exit_code == 1
    assert "list-valued" in result.output
    assert "--explode" in result.output


def test_catalog_cli_retrieves_role_specific_evidence(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "retrieve",
            "--id",
            "full-axis-bars",
            "--role",
            "advice",
        ],
    )

    assert result.exit_code == 0
    assert "Use full value axes for bars" in result.output
    assert "Start bar value axes at zero." in result.output
    assert "direct-labels" not in result.output


def test_catalog_cli_retrieve_fails_on_unknown_id(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "retrieve", "--id", "missing-guideline"],
    )

    assert result.exit_code == 1
    assert "Unknown guideline id: missing-guideline" in result.output
    assert "list --format jsonl" in result.output
    assert "Traceback" not in result.output


def test_catalog_cli_retrieve_validates_labels_and_roles(tmp_path: Path) -> None:
    path = _catalog_path(tmp_path)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "retrieve", "--label", "chart:missing"],
    )

    assert result.exit_code == 1
    assert "Unknown label" in result.output
    assert "values guideline_labels label" in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "retrieve", "--role", "section.advice"],
    )

    assert result.exit_code == 0
    assert "Place labels near marks." in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "retrieve", "--role", "missing"],
    )

    assert result.exit_code == 1
    assert "Unknown section role" in result.output
    assert "values sections role" in result.output


def test_catalog_cli_search_renders_missing_cache_without_traceback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = _catalog_path(tmp_path)

    def raise_missing_cache(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing Chroma cache")

    monkeypatch.setattr(catalog_cli, "_open_search_session", raise_missing_cache)

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "search",
            "axis",
            "--cache-mode",
            "reuse_only",
        ],
    )

    assert result.exit_code == 1
    assert "missing Chroma cache" in result.output
    assert "reuse_or_create" in result.output
    assert "Traceback" not in result.output


def test_catalog_cli_search_flattens_chroma_results(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = _catalog_path(tmp_path)
    captured_guideline_kwargs: dict[str, object] = {}

    class FakeTools:
        def search_guidelines(self, *_: object, **kwargs: object) -> dict[str, object]:
            captured_guideline_kwargs.update(kwargs)
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

        def search(self, *_: object, **__: object) -> dict[str, object]:
            return {
                "ids": [["direct-labels---overview"]],
                "documents": [["Use direct labels\n\nLabel marks directly."]],
                "metadatas": [
                    [
                        {
                            "parent_id": "direct-labels",
                            "role": "overview",
                            "labels": ["chart:line"],
                        }
                    ]
                ],
                "distances": [[0.125]],
            }

    class FakeSession:
        tools = FakeTools()

        def __enter__(self) -> "FakeSession":
            return self

        def __exit__(self, *_: object) -> None:
            return None

    monkeypatch.setattr(
        catalog_cli,
        "_open_search_session",
        lambda *_args, **_kwargs: FakeSession(),
    )

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        ["--catalog", str(path), "search", "direct labels", "--format", "markdown"],
    )

    assert result.exit_code == 0
    assert "direct-labels" in result.output
    assert "distance: `0.125`" in result.output
    assert "Use direct labels" in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "search",
            "direct labels",
            "--format",
            "csv",
        ],
    )

    assert result.exit_code == 0
    assert "rank,id,title" in result.output
    assert "direct-labels" in result.output

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "search",
            "direct labels",
            "--role",
            "overview",
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert captured_guideline_kwargs["roles"] == ("overview",)


def test_catalog_cli_guideline_search_rejects_document_filters_with_hint(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = _catalog_path(tmp_path)

    class FakeSession:
        def __enter__(self) -> "FakeSession":
            return self

        def __exit__(self, *_: object) -> None:
            return None

    monkeypatch.setattr(
        catalog_cli,
        "_open_search_session",
        lambda *_args, **_kwargs: FakeSession(),
    )

    result = CliRunner().invoke(
        catalog_cli.catalog_command,
        [
            "--catalog",
            str(path),
            "search",
            "direct labels",
            "--where",
            '{"role":"overview"}',
        ],
    )

    assert result.exit_code == 1
    assert "--level document" in result.output
    assert "--label" in result.output
    assert "Traceback" not in result.output

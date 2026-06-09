from __future__ import annotations

from collections.abc import Callable
import dataclasses as dc
import json
from pathlib import Path
from typing import cast

from click.testing import CliRunner, Result
import pytest

from chartcoach import Catalog, CatalogManifest
import chartcoach.cli.catalog as catalog_cli
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


@dc.dataclass(frozen=True)
class FakeGuidelineSearchResult:
    payload: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return self.payload


def patch_guideline_search(
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, object]:
    captured_guideline_kwargs: dict[str, object] = {}

    def fake_search(
        catalog: object, table: object, text: str, **kwargs: object
    ) -> FakeGuidelineSearchResult:
        captured_guideline_kwargs["catalog"] = catalog
        captured_guideline_kwargs["table"] = table
        captured_guideline_kwargs["text"] = text
        captured_guideline_kwargs.update(kwargs)
        return FakeGuidelineSearchResult(GUIDELINE_SEARCH_RESULT)

    monkeypatch.setattr(catalog_cli, "search_guidelines", fake_search)
    return captured_guideline_kwargs


def catalog_find_args(sample_catalog_path: Path, index_path: Path) -> list[str]:
    return [
        "catalog",
        "find",
        "--source",
        str(sample_catalog_path),
        "--index",
        str(index_path),
        "direct labels",
    ]


def json_result_rows(result: Result) -> list[dict[str, object]]:
    return cast(list[dict[str, object]], json_value(result)["rows"])


def test_catalog_query_filters_entries(
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
            "--label",
            "chart:bar",
            "--format",
            "jsonl",
        ],
    )

    assert [row["id"] for row in jsonl_rows(result)] == ["full-axis-bars"]


def test_catalog_query_composes_base_filters(
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
            "--any-label",
            "chart:bar",
            "--any-label",
            "chart:line",
            "--label-prefix",
            "component:",
            "--section-contains",
            "zero",
            "--format",
            "jsonl",
        ],
    )

    assert [row["id"] for row in jsonl_rows(result)] == ["full-axis-bars"]


def test_catalog_read_emits_entry_sections_and_sources(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows == [
        {
            "id": "direct-labels",
            "title": "Use direct labels",
            "description": "Label marks directly when space permits.",
            "labels": ["chart:line", "component:label", "task:lookup"],
            "sections": [
                {
                    "role": "advice",
                    "title": "Advice",
                    "content": "Place labels near marks.",
                }
            ],
            "sources": [],
        }
    ]


def test_catalog_read_can_include_full_source_detail(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--source-detail",
            "full",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows[0]["sources"] == []
    assert rows[0]["references"] == []


def test_catalog_read_markdown_renders_source_metadata(
    runner: CliRunner,
    sample_manifest: CatalogManifest,
    tmp_path: Path,
) -> None:
    catalog = Catalog.from_entries(
        [
            {
                "id": "direct-labels",
                "title": "Use direct labels",
                "description": "Label marks directly.",
                "body": "## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                "labels": ["chart:line"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Place labels near marks.",
                    }
                ],
                "references": [
                    """@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""
                ],
            }
        ],
        manifest=sample_manifest,
    )
    source_path = tmp_path / "entries.parquet"
    catalog.write_parquet(source_path)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(source_path),
            "direct-labels",
            "--section",
            "advice",
            "--source-detail",
            "minimal",
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "### Sources" in result.output
    assert "Smith, Ada" in result.output
    assert "Readable charts" in result.output


def test_catalog_read_can_select_section_roles(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "full-axis-bars",
            "--section",
            "advice",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(result)
    assert rows == [
        {
            "id": "full-axis-bars",
            "title": "Use full value axes for bars",
            "description": "Keep bar axes on the honest baseline.",
            "labels": ["chart:bar", "component:axis"],
            "sections": [
                {
                    "role": "advice",
                    "title": "Advice",
                    "content": "Start bar value axes at zero.",
                }
            ],
            "sources": [],
        }
    ]


def test_catalog_read_accepts_manifest_role_with_no_matching_sections(
    runner: CliRunner,
    tmp_path: Path,
) -> None:
    manifest = CatalogManifest.from_text(
        """# Sample Catalog

## Section Roles

### advice

Actionable guidance.

### review

Review notes.

## Label Families

### chart

Chart labels such as `chart:line`.
"""
    )
    catalog = Catalog.from_entries(
        [
            {
                "id": "direct-labels",
                "title": "Use direct labels",
                "description": "Label marks directly.",
                "body": "## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                "labels": ["chart:line"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Place labels near marks.",
                    }
                ],
            }
        ],
        manifest=manifest,
    )
    source_path = catalog.write_bundle(tmp_path / "bundle")

    roles_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "roles",
            "--source",
            str(source_path),
            "--format",
            "jsonl",
        ],
    )
    role_rows = {row["role"]: row["entries"] for row in jsonl_rows(roles_result)}
    assert role_rows == {"advice": 1, "review": 0}

    read_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(source_path),
            "direct-labels",
            "--section",
            "review",
            "--format",
            "jsonl",
        ],
    )

    rows = jsonl_rows(read_result)
    assert rows[0]["sections"] == []


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (
            ["catalog", "read", "missing-guideline"],
            "Unknown entry id: missing-guideline",
        ),
        (
            ["catalog", "query", "--label", "chart:missing"],
            "Unknown label",
        ),
        (
            ["catalog", "read", "direct-labels", "--section", "missing"],
            "Unknown section role",
        ),
    ],
)
def test_catalog_entry_commands_render_recovery_hints(
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


def test_catalog_unknown_section_lists_valid_roles(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-labels",
            "--section",
            "missing",
        ],
    )

    assert_cli_error(result, "Unknown section role(s): missing")
    assert "Valid roles: advice" in result.output
    assert "chartcoach catalog roles" in result.output


def test_catalog_unknown_id_suggests_nearest_valid_id(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "read",
            "--source",
            str(sample_catalog_path),
            "direct-lables",
        ],
    )

    assert_cli_error(result, "Unknown entry id: direct-lables")
    assert "Nearest entry ids: direct-labels" in result.output
    assert "chartcoach catalog read ID" in result.output
    assert "chartcoach catalog query" in result.output


@pytest.mark.search
def test_catalog_find_requires_existing_index_with_actionable_error(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(catalog_cli, "open_index", raise_missing_index)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "find",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "axis",
        ],
    )

    assert_cli_error(result, "missing search index")
    assert "chartcoach catalog index create --source PATH --index PATH" in result.output
    assert "chartcoach catalog find --mode fts" in result.output


@pytest.mark.search
def test_catalog_find_suggests_child_index_directory(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    parent = tmp_path / "index"
    child = parent / "fts"
    (child / "catalog_documents.lance").mkdir(parents=True)

    def raise_missing_table(*_: object, **__: object) -> object:
        raise FileNotFoundError("Table catalog_documents was not found")

    monkeypatch.setattr(catalog_cli, "open_index", raise_missing_table)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "find",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(parent),
            "axis",
        ],
    )

    assert_cli_error(result, "Table catalog_documents was not found")
    assert f"Found table 'catalog_documents' under {child}" in result.output
    assert f"Pass `--index {child}`" in result.output


@pytest.mark.search
def test_catalog_find_without_index_shows_recovery(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "find",
            "--source",
            str(sample_catalog_path),
            "axis",
        ],
    )

    assert_cli_error(result, "Pass --index PATH")
    assert (
        f"chartcoach catalog index create --source {sample_catalog_path} --index PATH"
        in result.output
    )
    assert "Use `--mode fts`" in result.output


@pytest.mark.search
def test_catalog_find_uses_default_index_for_default_catalog(
    runner: CliRunner,
    sample_catalog: object,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    default_index = tmp_path / "cached-index"

    def fake_open_index(index_path: str, *, table_name: str) -> object:
        captured["index_path"] = index_path
        captured["table_name"] = table_name
        return object()

    monkeypatch.setattr(
        "chartcoach.cli.common.default_index_path",
        lambda *, table_name, reporter=None: default_index,
    )
    monkeypatch.setattr(catalog_cli, "load_catalog", lambda _ctx: sample_catalog)
    monkeypatch.setattr(catalog_cli, "open_index", fake_open_index)
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        ["catalog", "find", "direct labels", "--format", "json"],
    )

    assert json_result_rows(result)[0]["id"] == "direct-labels"
    assert captured == {
        "index_path": str(default_index),
        "table_name": "catalog_documents",
    }


@pytest.mark.search
@pytest.mark.parametrize(
    ("output_format", "reader"),
    [
        ("json", lambda result: json_result_rows(result)[0]["id"]),
        ("jsonl", lambda result: jsonl_rows(result)[0]["id"]),
        ("csv", lambda result: csv_rows(result)[0]["id"]),
    ],
)
def test_catalog_find_structured_formats_return_guideline_rows(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    output_format: str,
    reader: Callable[[Result], object],
) -> None:
    monkeypatch.setattr(catalog_cli, "open_index", lambda *_args, **_kwargs: object())
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *catalog_find_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            output_format,
        ],
    )

    assert reader(result) == "direct-labels"


@pytest.mark.search
def test_catalog_find_markdown_keeps_ranking_evidence(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(catalog_cli, "open_index", lambda *_args, **_kwargs: object())
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *catalog_find_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            "markdown",
        ],
    )

    assert result.exit_code == 0
    assert "direct-labels" in result.output
    assert "score: `0.125`" in result.output
    assert "matched document role: `overview`" in result.output
    assert "retrieval hint: retrieve by guideline id" in result.output


@pytest.mark.search
def test_catalog_find_compact_format_keeps_citation_fields(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(catalog_cli, "open_index", lambda *_args, **_kwargs: object())
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *catalog_find_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            "compact",
        ],
    )

    assert result.exit_code == 0
    assert "1. `direct-labels` - Use direct labels" in result.output
    assert (
        "match: document role `overview` (retrieve by guideline id or a manifest section role), "
        "from `direct-labels---overview`, score `0.125`"
    ) in result.output
    assert "text: Use direct labels Label marks directly." in result.output


def test_catalog_commands_report_no_matches(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    list_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert list_result.exit_code == 0
    assert list_result.output.strip() == "No entries matched."

    query_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "query",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert query_result.exit_code == 0
    assert query_result.output.strip() == ""


def test_catalog_list_table_compacts_list_cells_and_machine_formats_preserve_lists(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    table_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "table",
        ],
    )
    assert table_result.exit_code == 0
    assert "chart:line, component:label, task:lookup" in table_result.output

    json_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "json",
        ],
    )
    payload = cast(list[dict[str, object]], json.loads(json_result.output))
    assert payload[0]["labels"] == [
        "chart:line",
        "component:label",
        "task:lookup",
    ]

    jsonl_result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "jsonl",
        ],
    )
    assert jsonl_rows(jsonl_result)[0]["labels"] == [
        "chart:line",
        "component:label",
        "task:lookup",
    ]


@pytest.mark.search
def test_catalog_find_forwards_native_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(catalog_cli, "open_index", lambda *_args, **_kwargs: object())
    captured_guideline_kwargs = patch_guideline_search(monkeypatch)
    result = runner.invoke(
        chartcoach_cli,
        [
            *catalog_find_args(sample_catalog_path, tmp_path / "index"),
            "--where",
            "role = 'section.advice'",
            "--format",
            "json",
        ],
    )
    payload = json_value(result)
    rows = cast(list[dict[str, object]], payload["rows"])
    assert rows[0]["id"] == "direct-labels"
    assert captured_guideline_kwargs["where"] == "role = 'section.advice'"
    assert captured_guideline_kwargs["limit"] == 8

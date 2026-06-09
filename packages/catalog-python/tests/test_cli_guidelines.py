from __future__ import annotations

from collections.abc import Callable
import dataclasses as dc
import json
from pathlib import Path
from typing import cast

from click.testing import CliRunner, Result
import pytest

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

    monkeypatch.setattr(
        guidelines_cli,
        "search",
        fake_search,
    )
    return captured_guideline_kwargs

def guideline_search_args(sample_catalog_path: Path, index_path: Path) -> list[str]:
    return [
        "guidelines",
        "search",
        "--source",
        str(sample_catalog_path),
        "--index",
        str(index_path),
        "direct labels",
    ]


def json_result_rows(result: Result) -> list[dict[str, object]]:
    return cast(list[dict[str, object]], json_value(result)["rows"])

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
    assert guideline[0]["title"] == "Use direct labels"
    assert guideline[0]["references"] == []

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


def test_guidelines_cli_unknown_section_lists_valid_roles(
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
            "--section",
            "missing",
        ],
    )

    assert_cli_error(result, "Unknown section role(s): missing")
    assert "Valid roles: advice" in result.output
    assert "chartcoach catalog manifest --source PATH" in result.output


def test_guidelines_show_suggests_nearest_valid_id(
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
            "direct-lables",
        ],
    )

    assert_cli_error(result, "Unknown guideline id: direct-lables")
    assert "Nearest guideline ids: direct-labels" in result.output
    assert (
        "Copy ids exactly from `chartcoach guidelines search --format compact QUERY`"
        in result.output
    )
    assert "chartcoach guidelines show ID" in result.output


def test_guidelines_retrieve_suggests_nearest_valid_id(
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
            "full-axis-bar",
        ],
    )

    assert_cli_error(result, "Unknown guideline id: full-axis-bar")
    assert "Nearest guideline ids: full-axis-bars" in result.output
    assert "chartcoach guidelines retrieve --id ID" in result.output


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
def test_search_command_requires_existing_index_with_actionable_error(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(guidelines_cli, "open_index", raise_missing_index)

    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "search",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "axis",
        ],
    )

    assert_cli_error(result, "missing search index")
    assert "chartcoach index --source PATH --index PATH" in result.output
    assert "Pass the same index path" in result.output
    assert "--mode fts" in result.output


@pytest.mark.search
def test_search_command_suggests_child_index_directory(
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

    monkeypatch.setattr(guidelines_cli, "open_index", raise_missing_table)

    result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "search",
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
def test_search_command_without_index_shows_first_run_recovery(
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
            "axis",
        ],
    )

    assert_cli_error(result, "Pass --index PATH")
    assert (
        f"chartcoach index --source {sample_catalog_path} --index PATH"
        in result.output
    )
    assert "Use `--mode fts`" in result.output


@pytest.mark.search
@pytest.mark.parametrize(
    ("output_format", "reader"),
    [
        ("json", lambda result: json_result_rows(result)[0]["id"]),
        ("jsonl", lambda result: jsonl_rows(result)[0]["id"]),
        ("csv", lambda result: csv_rows(result)[0]["id"]),
    ],
)
def test_search_command_structured_formats_return_guideline_rows(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    output_format: str,
    reader: Callable[[Result], object],
) -> None:
    monkeypatch.setattr(guidelines_cli, "open_index", lambda *_args, **_kwargs: object())
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
def test_search_command_markdown_keeps_stable_evidence(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(guidelines_cli, "open_index", lambda *_args, **_kwargs: object())
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
    assert "matched document role: `overview`" in result.output
    assert "retrieval hint: retrieve by guideline id" in result.output


@pytest.mark.search
def test_search_command_compact_format_keeps_citation_fields(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(guidelines_cli, "open_index", lambda *_args, **_kwargs: object())
    patch_guideline_search(monkeypatch)

    result = runner.invoke(
        chartcoach_cli,
        [
            *guideline_search_args(sample_catalog_path, tmp_path / "index"),
            "--format",
            "compact",
        ],
    )

    assert result.exit_code == 0
    assert "1. `direct-labels` - Use direct labels" in result.output
    assert (
        "match: document role `overview` (retrieve by guideline id or a manifest section role), from `direct-labels---overview`, score `0.125`"
        in result.output
    )
    assert "text: Use direct labels Label marks directly." in result.output


def test_guideline_commands_report_no_matches(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    list_result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "list",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert list_result.exit_code == 0
    assert list_result.output.strip() == "No guidelines matched."

    retrieve_result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "retrieve",
            "--source",
            str(sample_catalog_path),
            "--contains",
            "not-present",
        ],
    )
    assert retrieve_result.exit_code == 0
    assert retrieve_result.output.strip() == "No guidelines matched."


def test_guidelines_list_table_compacts_list_cells_and_machine_formats_preserve_lists(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    table_result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
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
    header, row = table_result.output.strip().splitlines()
    table_row = dict(zip(header.split("\t"), row.split("\t"), strict=True))
    assert table_row["labels"] == "chart:line, component:label, task:lookup"

    json_result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
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
            "guidelines",
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

    csv_result = runner.invoke(
        chartcoach_cli,
        [
            "guidelines",
            "list",
            "--source",
            str(sample_catalog_path),
            "--limit",
            "1",
            "--format",
            "csv",
        ],
    )
    assert csv_rows(csv_result)[0]["labels"] == (
        '["chart:line", "component:label", "task:lookup"]'
    )


@pytest.mark.search
def test_search_command_forwards_native_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(guidelines_cli, "open_index", lambda *_args, **_kwargs: object())
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
    rows = cast(list[dict[str, object]], payload["rows"])
    assert rows[0]["id"] == "direct-labels"
    assert captured_guideline_kwargs["where"] == "role = 'section.advice'"
    assert captured_guideline_kwargs["limit"] == 8

from __future__ import annotations

from collections.abc import Callable
import dataclasses as dc
from pathlib import Path
from typing import cast

from click.testing import CliRunner, Result
import pytest

import chartcoach.cli.catalog_index as catalog_index_cli
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

    monkeypatch.setattr(catalog_index_cli, "search_guidelines", fake_search)
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


@pytest.mark.search
def test_catalog_find_requires_existing_index_with_actionable_error(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_missing_index(*_: object, **__: object) -> object:
        raise FileNotFoundError("missing search index")

    monkeypatch.setattr(catalog_index_cli, "open_index", raise_missing_index)

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

    monkeypatch.setattr(catalog_index_cli, "open_index", raise_missing_table)

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
    monkeypatch.setattr(catalog_index_cli, "load_catalog", lambda _ctx: sample_catalog)
    monkeypatch.setattr(catalog_index_cli, "open_index", fake_open_index)
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
    monkeypatch.setattr(
        catalog_index_cli, "open_index", lambda *_args, **_kwargs: object()
    )
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
    monkeypatch.setattr(
        catalog_index_cli, "open_index", lambda *_args, **_kwargs: object()
    )
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
    monkeypatch.setattr(
        catalog_index_cli, "open_index", lambda *_args, **_kwargs: object()
    )
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


@pytest.mark.search
def test_catalog_find_forwards_native_filters(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        catalog_index_cli, "open_index", lambda *_args, **_kwargs: object()
    )
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

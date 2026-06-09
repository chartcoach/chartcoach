from __future__ import annotations

from collections.abc import Sized
import dataclasses as dc
from pathlib import Path
import sys
from types import ModuleType
from typing import cast

from click.testing import CliRunner
import pytest

from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error, json_value


@pytest.mark.search
def test_index_cli_queries_documents_with_native_options(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    fake_index_path = tmp_path / "index"

    @dc.dataclass(frozen=True)
    class FakeTable:
        name: str = "catalog_documents"

    fake_table = FakeTable()
    monkeypatch.setattr(
        "chartcoach.cli.index.open_index",
        lambda *_args, **_kwargs: fake_table,
    )

    monkeypatch.setattr(
        "chartcoach.cli.index.query_table",
        lambda table, query, *, limit, where, mode: (
            captured.update(
                {
                    "table": table,
                    "query": query,
                    "limit": limit,
                    "where": where,
                    "mode": mode,
                }
            )
            or [
                {
                    "id": "direct-labels---overview",
                    "parent_id": "direct-labels",
                    "text": "Use direct labels",
                    "_score": 1.2,
                }
            ]
        ),
    )

    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--index",
            str(fake_index_path),
            "documents",
            "axis labels",
            "--limit",
            "2",
            "--where",
            "role = 'overview'",
            "--mode",
            "fts",
        ],
    )

    assert result.exit_code == 0
    payload = json_value(result)
    rows = cast(list[dict[str, object]], payload["rows"])
    assert rows == [
        {
            "id": "direct-labels---overview",
            "parent_id": "direct-labels",
            "text": "Use direct labels",
            "_score": 1.2,
        }
    ]
    assert payload["mode"] == "fts"
    assert payload["table_name"] == "catalog_documents"
    assert captured == {
        "table": fake_table,
        "query": "axis labels",
        "limit": 2,
        "where": "role = 'overview'",
        "mode": "fts",
    }


@pytest.mark.search
def test_index_documents_suggests_child_index_directory(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    parent = tmp_path / "index"
    child = parent / "fts"
    (child / "catalog_documents.lance").mkdir(parents=True)

    def raise_missing_table(*_: object, **__: object) -> object:
        raise FileNotFoundError("Table catalog_documents was not found")

    monkeypatch.setattr("chartcoach.cli.index.open_index", raise_missing_table)

    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--index",
            str(parent),
            "documents",
            "axis labels",
        ],
    )

    assert_cli_error(result, "Table catalog_documents was not found")
    assert f"Found table 'catalog_documents' under {child}" in result.output
    assert f"Pass `--index {child}`" in result.output


def test_index_documents_help_does_not_require_index(
    runner: CliRunner,
) -> None:
    result = runner.invoke(chartcoach_cli, ["index", "documents", "--help"])

    assert result.exit_code == 0
    assert "Run LanceDB search over indexed document rows." in result.output


def test_index_help_describes_default_action(
    runner: CliRunner,
) -> None:
    result = runner.invoke(chartcoach_cli, ["index", "--help"])

    assert result.exit_code == 0
    assert "Running without a subcommand creates or replaces the table." in result.output


@pytest.mark.search
def test_index_cli_queries_built_lance_index(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    pytest.importorskip("lancedb")
    index_path = tmp_path / "index"

    build_result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(index_path),
        ],
    )
    assert build_result.exit_code == 0

    query_result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--index",
            str(index_path),
            "documents",
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
    row_count = payload["row_count"]
    assert isinstance(row_count, int)
    assert row_count >= 1
    rows = cast(list[dict[str, object]], payload["rows"])
    assert {row["parent_id"] for row in rows} == {"direct-labels"}


def test_index_cli_passes_lancedb_embedding_options(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from chartcoach.cli import index as index_cli

    captured: dict[str, object] = {}

    class FakeEmbedding:
        pass

    class FakeEmbeddingClass:
        @classmethod
        def create(cls, **kwargs: object) -> FakeEmbedding:
            captured["embedding_kwargs"] = kwargs
            return FakeEmbedding()

    class FakeRegistry:
        def set_var(self, key: str, value: str) -> None:
            cast(dict[str, str], captured.setdefault("vars", {}))[key] = value

        def get(self, name: str) -> type[FakeEmbeddingClass]:
            captured["embedding_name"] = name
            return FakeEmbeddingClass

    def get_registry() -> FakeRegistry:
        return FakeRegistry()

    class FakeTable:
        name = "catalog_documents"

        def count_rows(self) -> int:
            return 2

    def fake_index(
        catalog: object,
        index_path: Path,
        *,
        table_name: str,
        embedding: object,
    ) -> FakeTable:
        captured["catalog_len"] = len(cast(Sized, catalog))
        captured["index_path"] = index_path
        captured["table_name"] = table_name
        captured["embedding"] = embedding
        return FakeTable()

    fake_lancedb = ModuleType("lancedb")
    fake_embeddings = ModuleType("lancedb.embeddings")
    setattr(fake_embeddings, "get_registry", get_registry)
    setattr(fake_lancedb, "embeddings", fake_embeddings)
    monkeypatch.setitem(sys.modules, "lancedb", fake_lancedb)
    monkeypatch.setitem(sys.modules, "lancedb.embeddings", fake_embeddings)
    monkeypatch.setattr(index_cli, "index", fake_index)

    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "--embedding",
            "sentence-transformers",
            "--embedding-option",
            "name=all-MiniLM-L6-v2",
            "--embedding-option",
            "normalize=false",
            "--embedding-var",
            "token=secret",
        ],
    )

    assert result.exit_code == 0
    assert captured["embedding_name"] == "sentence-transformers"
    assert captured["embedding_kwargs"] == {
        "name": "all-MiniLM-L6-v2",
        "normalize": False,
    }
    assert captured["vars"] == {"token": "secret"}
    assert isinstance(captured["embedding"], FakeEmbedding)
    assert captured["table_name"] == "catalog_documents"


def test_index_cli_rejects_embedding_options_without_embedding(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "index",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "--embedding-option",
            "name=all-MiniLM-L6-v2",
        ],
    )

    assert_cli_error(result, "Pass --embedding before --embedding-option")


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
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "documents",
            "axis labels",
            "--limit",
            "0",
        ],
    )

    assert_cli_error(result, "Invalid value for '--limit'", exit_code=2)

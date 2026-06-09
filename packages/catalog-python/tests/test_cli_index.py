from __future__ import annotations

from collections.abc import Sized
import json
from pathlib import Path
import sys
from types import ModuleType
from typing import cast

from click.testing import CliRunner
import pytest

import chartcoach.cli.catalog_index as catalog_index_cli
import chartcoach.cli.common as common_cli
from chartcoach.cli.main import main as chartcoach_cli

from helpers import assert_cli_error


def test_catalog_index_create_passes_lancedb_embedding_options(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
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
        index_path: str,
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
    monkeypatch.setattr(catalog_index_cli, "index", fake_index)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "index",
            "create",
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
    assert captured["index_path"] == str(tmp_path / "index")
    assert captured["table_name"] == "catalog_documents"


def test_catalog_index_create_rejects_embedding_options_without_embedding(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "index",
            "create",
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
def test_catalog_find_without_index_extra_does_not_resolve_default_archive(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_default_index_path(*_: object, **__: object) -> Path:
        raise AssertionError("default index archive should not be resolved")

    monkeypatch.setattr(catalog_index_cli, "load_catalog", lambda _ctx: object())
    monkeypatch.setattr(common_cli.importlib.util, "find_spec", lambda name: None)
    monkeypatch.setattr(common_cli, "default_index_path", fail_default_index_path)

    result = runner.invoke(chartcoach_cli, ["catalog", "find", "axis"])

    assert_cli_error(
        result, "LanceDB indexing requires the optional `chartcoach[index]`"
    )
    assert "Install `chartcoach[index]` to use indexed discovery." in result.output


@pytest.mark.search
def test_catalog_index_info_preserves_object_store_uri(
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    class FakeTable:
        name = "catalog_documents"

        def count_rows(self) -> int:
            return 0

    def fake_open_index(index_path: str, *, table_name: str) -> FakeTable:
        captured["index_path"] = index_path
        captured["table_name"] = table_name
        return FakeTable()

    monkeypatch.setattr(catalog_index_cli, "open_index", fake_open_index)

    uri = "s3://chartcoach/catalog/releases/0.0.0/digest/indexes/lancedb/openrouter/model/db"
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "index",
            "info",
            "--index",
            uri,
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    payload = cast(list[dict[str, object]], json.loads(result.output))
    assert payload[0]["index_path"] == uri
    assert captured == {
        "index_path": uri,
        "table_name": "catalog_documents",
    }


@pytest.mark.search
def test_catalog_index_info_tolerates_unreadable_embedding_metadata(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class FakeTable:
        name = "catalog_documents"

        @property
        def embedding_functions(self) -> object:
            raise ValueError("missing registry variable")

        def count_rows(self) -> int:
            return 3

    monkeypatch.setattr(
        catalog_index_cli, "open_index", lambda *_args, **_kwargs: FakeTable()
    )

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "index",
            "info",
            "--index",
            str(tmp_path / "index"),
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0
    payload = cast(list[dict[str, object]], json.loads(result.output))
    assert payload[0]["embedding_functions"] == "unknown"
    assert payload[0]["documents"] == 3


@pytest.mark.search
def test_catalog_index_info_uses_default_index_when_omitted(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    default_index = tmp_path / "cached-index"

    class FakeTable:
        name = "catalog_documents"

        def count_rows(self) -> int:
            return 3

    def fake_open_index(index_path: str, *, table_name: str) -> FakeTable:
        captured["index_path"] = index_path
        captured["table_name"] = table_name
        return FakeTable()

    monkeypatch.setattr(
        "chartcoach.cli.common.default_index_path",
        lambda *, table_name, reporter=None: default_index,
    )
    monkeypatch.setattr(catalog_index_cli, "open_index", fake_open_index)

    result = runner.invoke(
        chartcoach_cli,
        ["catalog", "index", "info", "--format", "json"],
    )

    assert result.exit_code == 0
    payload = cast(list[dict[str, object]], json.loads(result.output))
    assert payload[0]["index_path"] == str(default_index)
    assert payload[0]["documents"] == 3
    assert captured == {
        "index_path": str(default_index),
        "table_name": "catalog_documents",
    }


@pytest.mark.search
def test_catalog_find_rejects_invalid_limit_before_opening_index(
    runner: CliRunner,
    sample_catalog_path: Path,
    tmp_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "find",
            "--source",
            str(sample_catalog_path),
            "--index",
            str(tmp_path / "index"),
            "axis labels",
            "--limit",
            "0",
        ],
    )

    assert_cli_error(result, "Invalid value for '--limit'", exit_code=2)

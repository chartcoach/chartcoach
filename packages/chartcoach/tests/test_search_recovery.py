from __future__ import annotations

import asyncio
import json
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Literal

import lancedb
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogError, open_catalog
from chartcoach._catalog.search import catalog_search
from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.curation import EmbeddingProfile, build_release
from chartcoach.mcp import _build_server, _register_tools
from click.testing import CliRunner
from lancedb.embeddings import get_registry
from lancedb.query import (
    LanceHybridQueryBuilder,
    LanceQueryBuilder,
    LanceVectorQueryBuilder,
)
from lancedb.table import LanceTable
from mcp.types import CallToolResult

pytestmark = [pytest.mark.curation, pytest.mark.search, pytest.mark.mcp]
_PROFILE = "test-search-recovery"
_ALIAS = "chartcoach-search-recovery-test"
SearchMode = Literal["fts", "vector", "hybrid"]


@pytest.fixture
def indexed_catalog(
    sample_catalog: Catalog, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> Catalog:
    embedding = deterministic_embedding(
        _ALIAS,
        lambda text, _index: (
            float("direct" in text.lower()),
            float("label" in text.lower()),
            1.0,
            1.0,
        ),
    )
    embedding = type(embedding).create(max_retries=0)
    release = tmp_path / "release"
    build_release(
        sample_catalog,
        release,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding, python_requirements={"numpy": version("numpy")}
            )
        },
    )
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    return open_catalog(release)


@pytest.mark.parametrize("mode", ["fts", "vector", "hybrid"])
def test_compact_search_projects_native_hits_and_preserves_scores(
    indexed_catalog: Catalog, mode: SearchMode, monkeypatch: pytest.MonkeyPatch
) -> None:
    table = indexed_catalog.index(_PROFILE)
    native = table.search(
        "direct labels",
        query_type=mode,
        fts_columns="text",
        vector_column_name="vector",
    )
    if mode != "fts":
        assert isinstance(native, LanceVectorQueryBuilder | LanceHybridQueryBuilder)
        native = native.distance_type("cosine")
    expected = native.limit(3).to_list()
    converted: list[list[dict[str, Any]]] = []
    original = LanceQueryBuilder.to_list

    def observe_conversion(self: LanceQueryBuilder, *args: Any, **kwargs: Any):
        rows = original(self, *args, **kwargs)
        converted.append(rows)
        return rows

    monkeypatch.setattr(LanceQueryBuilder, "to_list", observe_conversion)

    result = catalog_search(
        indexed_catalog, "direct labels", profile=_PROFILE, mode=mode, limit=2
    )

    score_column = {
        "fts": "_score",
        "vector": "_distance",
        "hybrid": "_relevance_score",
    }[mode]
    assert len(converted) == 1
    assert converted[0] == [
        {
            column: row[column]
            for column in ("id", "parent_id", "role", "text", score_column)
        }
        for row in expected
    ]
    assert result["documents_considered"] == 2
    assert result["documents_truncated"] is True
    match = result["matches"][0]
    assert match["id"] == "direct-labels"
    assert match["matched_document_id"] == expected[0]["id"]
    assert match["score"] == expected[0][score_column]
    assert match["score_kind"] == ("distance" if mode == "vector" else "relevance")


@pytest.mark.parametrize("mode", ["fts", "vector", "hybrid"])
@pytest.mark.parametrize("where", ["category = 'line'", "role ="])
def test_search_filter_errors_precede_row_execution_and_embedding(
    indexed_catalog: Catalog,
    mode: SearchMode,
    where: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def unexpected_work(*_args: Any, **_kwargs: Any) -> None:
        pytest.fail("Invalid filter executed rows or invoked an embedding function")

    with monkeypatch.context() as preparation:
        preparation.setattr(LanceTable, "_execute_query", unexpected_work)
        preparation.setattr(
            get_registry().get(_ALIAS), "compute_query_embeddings", unexpected_work
        )
        with pytest.raises(CatalogError) as exc_info:
            catalog_search(
                indexed_catalog,
                "direct labels",
                profile=_PROFILE,
                mode=mode,
                where=where,
            )

    error = exc_info.value
    assert error.code == "invalid_input"
    columns = error.details["columns"]
    assert isinstance(columns, list)
    assert {"id", "parent_id", "role", "text"} <= set(columns)
    assert "catalog.index(profile).schema" in str(error)
    recovered = catalog_search(
        indexed_catalog,
        "direct labels",
        profile=_PROFILE,
        mode=mode,
        where="length(parent_id) > 0 and role in ('overview', 'section.advice')",
    )
    assert recovered["matches"][0]["id"] == "direct-labels"


def test_mcp_search_recovers_from_filter_and_provider_failures(
    indexed_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    marker = "private-provider-diagnostic"

    def fail_embedding(*_args: Any, **_kwargs: Any) -> None:
        raise RuntimeError(marker)

    async def exercise() -> None:
        server = _build_server(log_level="INFO")
        _register_tools(server, catalog=indexed_catalog, profile=_PROFILE)
        invalid = await server.call_tool(
            "search", {"text": "direct labels", "where": "category = 'line'"}
        )
        assert isinstance(invalid, CallToolResult)
        assert invalid.is_error is True
        assert invalid.structured_content["error"]["code"] == "invalid_input"
        assert "parent_id" in invalid.structured_content["error"]["details"]["columns"]
        assert invalid.structured_content["error"]["hints"]

        with monkeypatch.context() as provider:
            provider.setattr(
                get_registry().get(_ALIAS), "compute_query_embeddings", fail_embedding
            )
            for mode in ("vector", "hybrid"):
                failed = await server.call_tool(
                    "search", {"text": "direct labels", "mode": mode}
                )
                assert isinstance(failed, CallToolResult)
                assert failed.is_error is True
                assert failed.structured_content["error"]["code"] == "operation_failed"
                assert marker not in failed.model_dump_json()

        recovered = await server.call_tool("search", {"text": "direct labels"})
        assert isinstance(recovered, CallToolResult)
        assert recovered.is_error is False
        assert recovered.structured_content["matches"][0]["id"] == "direct-labels"

    asyncio.run(exercise())


def test_cli_search_redacts_upstream_provider_diagnostics(
    indexed_catalog: Catalog,
    runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    marker = "private-provider-diagnostic"

    def fail_embedding(*_args: Any, **_kwargs: Any) -> None:
        raise RuntimeError(marker)

    monkeypatch.setattr(
        get_registry().get(_ALIAS), "compute_query_embeddings", fail_embedding
    )
    location = indexed_catalog.describe()["resolved_location"]
    assert location is not None
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "search",
            "direct labels",
            "--source",
            location,
            "--profile",
            _PROFILE,
            "--mode",
            "vector",
        ],
    )

    assert result.exit_code == 1
    assert marker not in result.output
    assert "LanceDB search failed" in result.stderr
    assert "FTS" in result.stderr


def test_index_open_failure_preserves_cache_repair_and_recovery(
    indexed_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    attempts: list[object] = []

    def fail_connection(path: object, *_args: Any, **_kwargs: Any) -> None:
        attempts.append(path)
        raise OSError("private-storage-diagnostic")

    with monkeypatch.context() as storage:
        storage.setattr(lancedb, "connect", fail_connection)
        with pytest.raises(CatalogError) as exc_info:
            indexed_catalog.index(_PROFILE)

    assert exc_info.value.code == "operation_failed"
    assert exc_info.value.details["operation"] == "open_index"
    assert "private-storage-diagnostic" not in str(exc_info.value)
    assert len(attempts) == 2
    assert indexed_catalog.index(_PROFILE).count_rows() > 0


def test_native_index_binding_mismatch_remains_a_profile_error(
    indexed_catalog: Catalog, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    directory = tmp_path / "changed-binding"
    table = indexed_catalog.index(_PROFILE, directory=directory)
    rows = table.to_arrow()
    metadata = dict(rows.schema.metadata or {})
    binding = json.loads(metadata[b"embedding_functions"])
    binding[0]["model"]["max_retries"] = 1
    metadata[b"embedding_functions"] = json.dumps(binding).encode()
    connect = lancedb.connect
    connect(directory).create_table(
        "documents", rows.replace_schema_metadata(metadata), mode="overwrite"
    )
    monkeypatch.setattr(
        lancedb, "connect", lambda *_args, **_kwargs: connect(directory)
    )

    with pytest.raises(CatalogError) as exc_info:
        indexed_catalog.index(_PROFILE)

    assert exc_info.value.code == "incompatible_profile"
    assert "embedding binding disagrees" in str(exc_info.value)


def test_compact_search_reports_missing_parents_as_an_index_mismatch(
    indexed_catalog: Catalog, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    table = indexed_catalog.index(_PROFILE, directory=tmp_path / "changed-parent")
    table.update(
        where="parent_id = 'direct-labels'", values={"parent_id": "missing-guideline"}
    )
    monkeypatch.setattr(indexed_catalog, "_index_loader", lambda *_args: table)

    with pytest.raises(CatalogError) as exc_info:
        catalog_search(indexed_catalog, "direct labels", profile=_PROFILE)

    assert exc_info.value.code == "incompatible_profile"
    assert exc_info.value.details["guideline_id"] == "missing-guideline"


def test_embedding_initialization_failure_is_a_redacted_embedding_error(
    indexed_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    marker = "private-embedding-configuration"

    def fail_creation(_cls: object, **_kwargs: Any) -> None:
        raise RuntimeError(marker)

    monkeypatch.setattr(
        get_registry().get(_ALIAS), "create", classmethod(fail_creation)
    )

    with pytest.raises(CatalogError) as exc_info:
        catalog_search(
            indexed_catalog, "direct labels", profile=_PROFILE, mode="vector"
        )

    assert exc_info.value.code == "embedding_failure"
    assert exc_info.value.details["operation"] == "initialize_embedding"
    assert marker not in str(exc_info.value)
    assert catalog_search(indexed_catalog, "direct labels", profile=_PROFILE)["matches"]


@pytest.mark.parametrize(
    "unavailable", ["alias", "missing_requirement", "incompatible_requirement"]
)
def test_semantic_setup_reports_capability_failures_and_keeps_fts_available(
    indexed_catalog: Catalog, unavailable: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    def missing_alias(name: str) -> None:
        raise KeyError(name)

    def missing_distribution(name: str) -> str:
        raise PackageNotFoundError(name)

    if unavailable == "alias":
        monkeypatch.setattr(get_registry(), "get", missing_alias)
    else:
        monkeypatch.setattr(
            "chartcoach._catalog.search.version",
            missing_distribution
            if unavailable == "missing_requirement"
            else lambda _name: "0.0.0",
        )

    with pytest.raises(CatalogError) as exc_info:
        catalog_search(
            indexed_catalog, "direct labels", profile=_PROFILE, mode="vector"
        )

    assert exc_info.value.code == "unavailable_capability"
    assert exc_info.value.hints
    if unavailable == "alias":
        assert exc_info.value.details["alias"] == _ALIAS
    else:
        assert exc_info.value.details["actual"] == {
            "numpy": "missing" if unavailable == "missing_requirement" else "0.0.0"
        }
    assert catalog_search(indexed_catalog, "direct labels", profile=_PROFILE)["matches"]

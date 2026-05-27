from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from chartcoach import Catalog
from chartcoach.mcp import server as mcp_server
from chartcoach.paths import default_index_dir
from chartcoach.tools.catalog import CatalogTools

pytestmark = pytest.mark.mcp


def test_mcp_settings_support_index_dir() -> None:
    config = mcp_server.resolve_config(
        source="catalog.parquet",
        index_dir="index",
    )

    assert config.settings == {
        "source": "catalog.parquet",
        "index_dir": Path("index"),
    }


def test_mcp_settings_use_default_index_dir(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CHARTCOACH_INDEX_DIR", raising=False)

    config = mcp_server.resolve_config(source="catalog.parquet")

    assert config.settings["source"] == "catalog.parquet"
    assert config.settings["index_dir"] == default_index_dir()


def test_mcp_settings_support_env_index_dir(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CHARTCOACH_INDEX_DIR", "env-index")

    config = mcp_server.resolve_config(source="catalog.parquet")

    assert config.settings["index_dir"] == "env-index"


def test_mcp_server_exposes_native_tool_contracts(
    sample_catalog: Catalog,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mcp_module = pytest.importorskip("mcp.server")

    class FakeCollection:
        def __init__(self) -> None:
            self.query_params: dict[str, Any] | None = None
            self.get_params: dict[str, Any] | None = None

        def query(self, **params: object) -> dict[str, object]:
            self.query_params = dict(params)
            return {"ids": [[]]}

        def get(self, **params: object) -> dict[str, object]:
            self.get_params = dict(params)
            return {"ids": []}

    collection = FakeCollection()
    search = mcp_server._ChromaTools(
        sample_catalog,
        cache_dir="index",
        cache_mode="reuse_only",
    )
    monkeypatch.setattr(
        search,
        "open_index",
        lambda: SimpleNamespace(collection=collection),
    )

    async def exercise_server() -> None:
        server = mcp_module.FastMCP("chartcoach", json_response=True)
        mcp_server._register_tools(
            server,
            catalog_tools=CatalogTools(sample_catalog),
            artifact_tools=mcp_server._ArtifactTools(
                sample_catalog,
                source="catalog.parquet",
                index_dir="index",
            ),
            search=search,
        )
        tools = {tool.name: tool for tool in await server.list_tools()}

        assert set(tools) == {
            "catalog_artifacts",
            "tables_list",
            "tables_schema",
            "tables_values",
            "sql_query",
            "guidelines_list",
            "guidelines_get",
            "guidelines_retrieve",
            "guidelines_search",
            "chroma_query",
            "chroma_get",
        }
        for tool in tools.values():
            assert tool.annotations is not None
            assert tool.annotations.readOnlyHint is True
            assert tool.annotations.destructiveHint is False
            assert tool.annotations.idempotentHint is True
            assert tool.annotations.openWorldHint is False
            assert tool.description

        assert {"query_texts", "n_results", "where", "include"} <= set(
            tools["chroma_query"].inputSchema["properties"]
        )
        assert {"ids", "where", "limit", "include"} <= set(
            tools["chroma_get"].inputSchema["properties"]
        )
        assert {"query", "limit"} <= set(tools["sql_query"].inputSchema["properties"])

        query_result = await server.call_tool(
            "chroma_query",
            {
                "query_texts": ["axis", "labels"],
                "n_results": 2,
                "include": ["documents"],
            },
        )
        get_result = await server.call_tool(
            "chroma_get",
            {"ids": ["doc"], "include": ["metadatas"]},
        )
        sql_result = await server.call_tool(
            "sql_query",
            {
                "query": "select id from guidelines order by id",
                "limit": 1,
            },
        )

        assert cast(tuple[object, dict[str, object]], query_result)[1] == {"ids": [[]]}
        assert cast(tuple[object, dict[str, object]], get_result)[1] == {"ids": []}
        sql_payload = cast(tuple[object, dict[str, object]], sql_result)[1]
        assert sql_payload["rows"] == [{"id": "direct-labels"}]
        assert sql_payload["truncated"] is True
        assert collection.query_params == {
            "query_texts": ["axis", "labels"],
            "n_results": 2,
            "include": ["documents"],
        }
        assert collection.get_params == {"ids": ["doc"], "include": ["metadatas"]}

    asyncio.run(exercise_server())


def test_mcp_main_registers_catalog_tools_without_opening_search(
    sample_catalog_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    added_tools: list[str] = []

    class FakeServer:
        def __init__(self) -> None:
            self.settings = SimpleNamespace(host=None, port=None, log_level=None)

        def add_tool(self, tool: object, **_: object) -> None:
            added_tools.append(getattr(tool, "__name__"))

        def run(self, *, transport: str) -> None:
            assert transport == "stdio"

    fake_server = FakeServer()
    monkeypatch.setattr(
        mcp_server,
        "_load_fast_mcp",
        lambda: lambda *_, **__: fake_server,
    )
    monkeypatch.setattr(
        mcp_server.ChromaIndex,
        "from_cache",
        staticmethod(
            lambda *_args, **_kwargs: (_ for _ in ()).throw(
                AssertionError("search cache should open lazily")
            )
        ),
    )

    mcp_server.main(
        settings={"source": sample_catalog_path},
        runtime=mcp_server.RuntimeConfig(),
    )

    assert set(added_tools) == {
        "catalog_artifacts",
        "list_tables",
        "describe_tables",
        "count_values",
        "sql_query",
        "list_guidelines",
        "get_guideline",
        "retrieve_guidelines",
        "search_guidelines",
        "chroma_query",
        "chroma_get",
    }

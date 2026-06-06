from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import cast

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

    class FakeIndex:
        index_root = Path("index/root")
        table_name = "catalog_documents"

        def __init__(self) -> None:
            self.query_params: dict[str, object] | None = None

        def query_documents(
            self,
            query: str,
            *,
            limit: int,
            where: str | None = None,
        ) -> list[dict[str, object]]:
            self.query_params = {"query": query, "limit": limit, "where": where}
            return [{"id": "doc", "parent_id": "direct-labels", "_score": 1.2}]

    index = FakeIndex()
    catalog_tools = CatalogTools(
        sample_catalog,
        index_dir="index",
    )
    monkeypatch.setattr(catalog_tools, "open_index", lambda: index)

    async def exercise_server() -> None:
        server = mcp_module.FastMCP("chartcoach", json_response=True)
        mcp_server._register_tools(
            server,
            catalog_tools=catalog_tools,
            artifact_tools=mcp_server._ArtifactTools(
                sample_catalog,
                source="catalog.parquet",
                index_dir="index",
            ),
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
            "index_query",
        }
        for tool in tools.values():
            assert tool.annotations is not None
            assert tool.annotations.readOnlyHint is True
            assert tool.annotations.destructiveHint is False
            assert tool.annotations.idempotentHint is True
            assert tool.annotations.openWorldHint is False
            assert tool.description

        assert {"query", "limit", "where"} <= set(
            tools["index_query"].inputSchema["properties"]
        )
        assert {"query", "limit"} <= set(tools["sql_query"].inputSchema["properties"])

        query_result = await server.call_tool(
            "index_query",
            {
                "query": "axis labels",
                "limit": 2,
                "where": "role = 'overview'",
            },
        )
        sql_result = await server.call_tool(
            "sql_query",
            {
                "query": "select id from guidelines order by id",
                "limit": 1,
            },
        )

        query_payload = cast(tuple[object, dict[str, object]], query_result)[1]
        assert query_payload["rows"] == [
            {"id": "doc", "parent_id": "direct-labels", "_score": 1.2}
        ]
        assert query_payload["table_name"] == "catalog_documents"
        sql_payload = cast(tuple[object, dict[str, object]], sql_result)[1]
        assert sql_payload["rows"] == [{"id": "direct-labels"}]
        assert sql_payload["truncated"] is True
        assert index.query_params == {
            "query": "axis labels",
            "limit": 2,
            "where": "role = 'overview'",
        }

    asyncio.run(exercise_server())


def test_mcp_main_registers_catalog_tools_without_opening_search(
    sample_catalog_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    added_tools: list[str] = []

    class FakeServer:
        def __init__(self) -> None:
            self.settings = SimpleNamespace(host=None, port=None, log_level=None)

        def add_tool(self, tool: object, **kwargs: object) -> None:
            added_tools.append(str(kwargs["name"]))

        def run(self, *, transport: str) -> None:
            assert transport == "stdio"

    fake_server = FakeServer()
    monkeypatch.setattr(
        mcp_server,
        "_load_fast_mcp",
        lambda: lambda *_, **__: fake_server,
    )
    monkeypatch.setattr(
        CatalogTools,
        "open_index",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("search cache should open lazily")
        ),
    )

    mcp_server.main(
        settings={"source": sample_catalog_path},
        runtime=mcp_server.RuntimeConfig(),
    )

    assert set(added_tools) == {
        "catalog_artifacts",
        "tables_list",
        "tables_schema",
        "tables_values",
        "sql_query",
        "guidelines_list",
        "guidelines_get",
        "guidelines_retrieve",
        "guidelines_search",
        "index_query",
    }

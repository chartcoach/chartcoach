from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import cast

import pytest

from chartcoach import Catalog
import chartcoach.mcp as mcp_server
from chartcoach.tools import Tools

pytestmark = pytest.mark.mcp


def test_mcp_config_supports_explicit_index() -> None:
    config = mcp_server.configure(
        source="entries.parquet",
        index="index",
        table="docs",
    )

    assert config.settings == {
        "source": "entries.parquet",
        "index": "index",
        "table": "docs",
    }


def test_mcp_config_preserves_object_store_index_uri() -> None:
    uri = "s3://chartcoach/catalog/releases/0.0.0/digest/indexes/lancedb/openrouter/model/db"
    config = mcp_server.configure(index=uri)

    assert config.settings["index"] == uri


def test_mcp_config_omits_index_when_unconfigured(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("CHARTCOACH_INDEX", raising=False)

    config = mcp_server.configure(source="entries.parquet")

    assert config.settings["source"] == "entries.parquet"
    assert "index" not in config.settings
    assert config.settings["table"] == "catalog_documents"


def test_mcp_config_supports_env_index(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CHARTCOACH_INDEX", "env-index")

    config = mcp_server.configure(source="entries.parquet")

    assert config.settings["index"] == "env-index"


def test_mcp_server_exposes_raw_tool_contracts(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    mcp_module = pytest.importorskip("mcp.server")
    from chartcoach.search import index

    table = index(sample_catalog, tmp_path / "index")
    server_tools = Tools(sample_catalog, table=table, index_path=tmp_path / "index")

    async def exercise_server() -> None:
        server = mcp_module.FastMCP("chartcoach", json_response=True)
        mcp_server._register_tools(
            server,
            tools=server_tools,
            include_search=True,
        )
        tools = {tool.name: tool for tool in await server.list_tools()}

        assert set(tools) == {"sql", "search"}
        for tool in tools.values():
            assert tool.annotations is not None
            assert tool.annotations.readOnlyHint is True
            assert tool.annotations.destructiveHint is False
            assert tool.annotations.idempotentHint is True
            assert tool.annotations.openWorldHint is False
            assert tool.description

        assert {"search_query", "limit", "where", "mode"} <= set(
            tools["search"].inputSchema["properties"]
        )
        assert {"statement", "limit"} <= set(tools["sql"].inputSchema["properties"])

        search_result = await server.call_tool(
            "search",
            {
                "search_query": "axis labels",
                "limit": 2,
                "where": "role = 'overview'",
                "mode": "fts",
            },
        )
        sql_result = await server.call_tool(
            "sql",
            {
                "statement": "select id from guidelines order by id",
                "limit": 1,
            },
        )

        search_payload = cast(tuple[object, dict[str, object]], search_result)[1]
        search_rows = cast(list[dict[str, object]], search_payload["rows"])
        assert search_rows[0]["parent_id"] == "direct-labels"
        assert search_payload["mode"] == "fts"
        assert search_payload["table_name"] == "catalog_documents"
        sql_payload = cast(tuple[object, dict[str, object]], sql_result)[1]
        assert sql_payload["rows"] == [{"id": "direct-labels"}]
        assert sql_payload["truncated"] is True

    asyncio.run(exercise_server())


def test_mcp_main_registers_sql_without_index(
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
        "FastMCP",
        lambda *_, **__: fake_server,
    )
    mcp_server.main(
        settings={"source": sample_catalog_path},
        runtime=mcp_server.Runtime(),
    )

    assert added_tools == ["sql"]

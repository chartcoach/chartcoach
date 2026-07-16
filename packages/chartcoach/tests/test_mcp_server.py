from __future__ import annotations

import asyncio
from pathlib import Path
from typing import cast

import pytest

from chartcoach.catalog.collection import Catalog
import chartcoach.mcp as mcp_server
from chartcoach.tools import Tools
from catalog_testkit import deterministic_embedding

pytestmark = pytest.mark.mcp


@pytest.mark.search
def test_mcp_registers_real_fastmcp_sql_and_search_tools(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.catalog.curation.lancedb_index import build_lancedb_index

    async def exercise() -> None:
        digest = "a" * 64
        index_path = tmp_path / "index"
        table = build_lancedb_index(
            sample_catalog,
            index_path,
            embedding=deterministic_embedding("chartcoach-mcp-test"),
        )
        server = mcp_server.FastMCP("chartcoach-test", json_response=True)
        mcp_server._register_tools(
            server,
            tools=Tools(
                sample_catalog,
                table=table,
                index_path=index_path,
                release_digest=digest,
            ),
            include_search=True,
        )

        tool_map = {tool.name: tool for tool in await server.list_tools()}
        assert set(tool_map) == {"sql", "search"}

        sql_result = await server.call_tool(
            "sql",
            {
                "statement": "select id from guidelines order by id limit 1",
                "limit": 1,
            },
        )
        assert isinstance(sql_result, tuple)
        _sql_content, sql_payload = sql_result
        sql_payload = cast(dict[str, object], sql_payload)
        sql_rows = cast(list[dict[str, object]], sql_payload["rows"])
        assert sql_payload["row_count"] == 1
        assert sql_payload["release_digest"] == digest
        assert sql_rows[0]["id"] == "direct-labels"

        search_result = await server.call_tool(
            "search",
            {"search_query": "direct labels", "limit": 1, "mode": "fts"},
        )
        assert isinstance(search_result, tuple)
        _search_content, search_payload = search_result
        search_payload = cast(dict[str, object], search_payload)
        search_rows = cast(list[dict[str, object]], search_payload["rows"])
        assert search_payload["mode"] == "fts"
        assert search_payload["index_path"] == str(index_path)
        assert search_rows[0]["id"] == "direct-labels"

    asyncio.run(exercise())

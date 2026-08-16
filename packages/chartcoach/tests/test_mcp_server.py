from __future__ import annotations

import asyncio
from pathlib import Path
from typing import cast

import chartcoach.mcp as mcp_server
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest
from chartcoach.tools import Tools
from mcp.types import CallToolResult

pytestmark = pytest.mark.mcp


@pytest.mark.search
def test_mcp_registers_sql_and_search_tools(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.catalog.curation.lancedb_index import build_lancedb_index

    async def exercise() -> None:
        catalog = _released_catalog(sample_catalog)
        assert catalog.release is not None
        index_path = tmp_path / "index"
        table = build_lancedb_index(
            sample_catalog,
            index_path,
            embedding=deterministic_embedding("chartcoach-mcp-test"),
        )
        server = mcp_server.MCPServer("chartcoach-test")
        mcp_server._register_tools(
            server,
            tools=Tools(
                catalog,
                table=table,
                source=tmp_path / "release",
                profile="test/deterministic",
            ),
            include_search=True,
        )

        tool_map = {tool.name: tool for tool in await server.list_tools()}
        assert set(tool_map) == {"sql", "search"}
        assert tool_map["sql"].annotations is not None
        assert tool_map["sql"].annotations.read_only_hint is True
        assert tool_map["sql"].annotations.destructive_hint is False
        assert tool_map["sql"].annotations.idempotent_hint is True
        assert tool_map["sql"].annotations.open_world_hint is False
        assert tool_map["search"].annotations is not None
        assert tool_map["search"].annotations.open_world_hint is True

        sql_result = await server.call_tool(
            "sql",
            {
                "statement": "select id from guidelines order by id limit 1",
                "limit": 1,
            },
        )
        assert isinstance(sql_result, CallToolResult)
        assert sql_result.is_error is False
        sql_payload = cast(dict[str, object], sql_result.structured_content)
        sql_rows = cast(list[dict[str, object]], sql_payload["rows"])
        assert sql_payload["row_count"] == 1
        assert sql_payload["release_digest"] == catalog.release.digest
        assert sql_rows[0]["id"] == "direct-labels"

        search_result = await server.call_tool(
            "search",
            {"search_query": "direct labels", "limit": 1, "mode": "fts"},
        )
        assert isinstance(search_result, CallToolResult)
        assert search_result.is_error is False
        search_payload = cast(dict[str, object], search_result.structured_content)
        search_rows = cast(list[dict[str, object]], search_payload["rows"])
        assert search_payload["mode"] == "fts"
        assert search_payload["source"] == str(tmp_path / "release")
        assert search_payload["profile"] == "test/deterministic"
        assert search_rows[0]["id"] == "direct-labels"

    asyncio.run(exercise())


def _released_catalog(catalog: Catalog) -> Catalog:
    artifacts = {
        "MANIFEST.md": ReleaseArtifact("1" * 64, 1),
        "entries.parquet": ReleaseArtifact("2" * 64, 1),
    }
    release = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    return Catalog(
        catalog.to_frame(),
        manifest=catalog.manifest,
        release=release,
    )

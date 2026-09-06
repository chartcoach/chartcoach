from __future__ import annotations

import asyncio
from pathlib import Path
from typing import cast

import chartcoach.mcp as mcp_server
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import open_catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release
from chartcoach.catalog.model import Catalog
from mcp.types import CallToolResult

pytestmark = [pytest.mark.mcp, pytest.mark.search, pytest.mark.curation]


def test_mcp_exposes_bounded_discovery_read_cite_and_search(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def exercise() -> None:
        profile = "test-deterministic"
        release_root = tmp_path / "release"
        build_release(
            sample_catalog,
            release_root,
            profiles={
                profile: EmbeddingProfile(
                    deterministic_embedding("chartcoach-mcp-test")
                )
            },
        )
        monkeypatch.setattr(
            "chartcoach.catalog.runtime.cache._cache_root",
            lambda: tmp_path / "cache",
        )
        catalog = open_catalog(release_root)
        assert catalog.release is not None
        server = mcp_server._build_server(log_level="INFO")
        mcp_server._register_tools(server, catalog=catalog, profile=profile)

        assert server.instructions is not None
        assert "Call describe first" in server.instructions
        tool_map = {tool.name: tool for tool in await server.list_tools()}
        assert set(tool_map) == {"describe", "sql", "read", "cite", "search"}
        for tool in tool_map.values():
            assert tool.annotations is not None
            assert tool.annotations.read_only_hint is True
            assert tool.annotations.destructive_hint is False
            assert tool.output_schema is not None
            assert "ErrorToolResult" in tool.output_schema["$defs"]
        assert "source_title" in str(tool_map["read"].output_schema)
        assert "citation" in str(tool_map["cite"].output_schema)

        sql_input = tool_map["sql"].input_schema["properties"]
        search_input = tool_map["search"].input_schema["properties"]
        read_input = tool_map["read"].input_schema["properties"]
        assert sql_input["limit"]["minimum"] == 1
        assert sql_input["limit"]["maximum"] == 100
        assert search_input["limit"]["maximum"] == 100
        assert read_input["ids"]["minItems"] == 1
        assert read_input["ids"]["maxItems"] == 100

        description = await server.call_tool("describe", {"profile": profile})
        assert isinstance(description, CallToolResult)
        assert description.is_error is False
        description_data = cast(dict[str, object], description.structured_content)
        assert description_data["release_digest"] == catalog.release.digest
        assert (
            cast(dict[str, object], description_data["profile"])["distance_metric"]
            == "cosine"
        )

        sql = await server.call_tool(
            "sql",
            {"statement": "select id from guidelines order by id", "limit": 1},
        )
        assert isinstance(sql, CallToolResult)
        assert sql.is_error is False
        sql_data = cast(dict[str, object], sql.structured_content)
        assert sql_data["truncated"] is True
        assert sql_data["release_digest"] == catalog.release.digest

        read = await server.call_tool("read", {"ids": ["direct-labels"]})
        cite = await server.call_tool("cite", {"ids": ["direct-labels"]})
        assert isinstance(read, CallToolResult)
        assert isinstance(cite, CallToolResult)
        assert read.is_error is False
        assert cite.is_error is False
        assert (
            cast(list[dict[str, object]], read.structured_content["records"])[0]["id"]
            == "direct-labels"
        )
        assert (
            cast(list[dict[str, object]], cite.structured_content["records"])[0]["id"]
            == "direct-labels"
        )

        search = await server.call_tool(
            "search",
            {"text": "direct labels", "limit": 1, "mode": "fts"},
        )
        assert isinstance(search, CallToolResult)
        assert search.is_error is False
        search_data = cast(dict[str, object], search.structured_content)
        assert search_data["score_kind"] == "relevance"
        assert search_data["documents_considered"] == 1
        assert cast(list[dict[str, object]], search_data["matches"])[0]["id"] == (
            "direct-labels"
        )

        missing = await server.call_tool("read", {"ids": ["missing"]})
        assert isinstance(missing, CallToolResult)
        assert missing.is_error is True
        assert missing.structured_content == {
            "error": {
                "code": "lookup",
                "message": "Unknown guideline entry ID: missing",
                "details": {
                    "id": "missing",
                    "suggestions": ["full-axis-bars", "direct-labels"],
                },
            }
        }

        oversized = await server.call_tool(
            "sql",
            {"statement": "select repeat('x', 70000) as text"},
        )
        assert isinstance(oversized, CallToolResult)
        assert oversized.is_error is True
        assert oversized.structured_content["error"]["code"] == "response_too_large"

    asyncio.run(exercise())

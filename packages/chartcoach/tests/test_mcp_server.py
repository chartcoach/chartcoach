from __future__ import annotations

import asyncio
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import cast

import chartcoach.mcp as mcp_server
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, Guideline, open_catalog
from chartcoach.curation import EmbeddingProfile, build_release
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.types import CallToolResult, TextContent

pytestmark = [pytest.mark.mcp, pytest.mark.search, pytest.mark.curation]


def test_stdio_client_discovers_tools_and_receives_structured_results(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    contract = Path(__file__).parents[3] / "fixtures/catalog-contract/operations.json"
    reference = json.loads(contract.read_text())["bibliography_urls"][0]["reference"]
    catalog = Catalog.from_guidelines(
        [
            replace(Guideline.from_mapping(row), references=(reference,))
            for row in sample_catalog.to_frame().iter_rows(named=True)
        ],
        manifest=sample_catalog.manifest,
    )
    release_root = tmp_path / "release"
    build_release(catalog, release_root)

    async def exercise() -> None:
        parameters = StdioServerParameters(
            command=sys.executable,
            args=[
                "-c",
                "from chartcoach.cli.main import main; main()",
                "mcp",
                "--source",
                str(release_root),
            ],
        )
        async with (
            stdio_client(parameters) as (reader, writer),
            ClientSession(reader, writer) as session,
        ):
            await session.initialize()
            listing = await session.list_tools()
            assert {tool.name for tool in listing.tools} == {
                "describe",
                "sql",
                "read",
                "cite",
            }
            result = await session.call_tool("read", {"ids": ["direct-labels"]})
            assert result.is_error is False
            assert result.structured_content["records"][0]["id"] == "direct-labels"
            missing = await session.call_tool("read", {"ids": ["missing"]})
            assert missing.is_error is True
            assert missing.structured_content["error"]["code"] == "lookup"
            wrong_role = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["recommendations"]}
            )
            assert wrong_role.is_error is True
            assert wrong_role.structured_content["error"]["code"] == "lookup"
            assert any(
                "advice" in hint
                for hint in wrong_role.structured_content["error"]["hints"]
            )
            assert "advice" in _text(wrong_role)

            invalid_limit = await session.call_tool(
                "sql", {"statement": "select 1", "limit": 0}
            )
            assert invalid_limit.is_error is True
            assert "limit" in _text(invalid_limit)

            oversized_error = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["é" * 40_000]}
            )
            assert oversized_error.is_error is True
            assert (
                oversized_error.structured_content["error"]["code"]
                == "response_too_large"
            )
            assert (
                len(
                    json.dumps(
                        oversized_error.structured_content, ensure_ascii=False
                    ).encode()
                )
                <= 65_536
            )
            assert "Narrow" in _text(oversized_error)
            assert oversized_error.structured_content["error"]["message"] in _text(
                oversized_error
            )

            recovered = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["advice"]}
            )
            assert recovered.is_error is False
            citation = await session.call_tool("cite", {"ids": ["direct-labels"]})
            source = citation.structured_content["records"][0]["sources"][0]
            assert (
                source["url"] == "https://www.datawrapper.de/blog/colorblindness-part2"
            )
            assert source["url"] in source["citation"]

    asyncio.run(exercise())


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
            "chartcoach._catalog.runtime.cache._cache_root",
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
        error = missing.structured_content["error"]
        assert error["code"] == "lookup"
        assert error["details"]["id"] == "missing"
        assert "direct-labels" in error["details"]["suggestions"]
        assert error["hints"]
        assert all(hint in _text(missing) for hint in error["hints"])

        missing_profile = await server.call_tool("describe", {"profile": "missing"})
        assert isinstance(missing_profile, CallToolResult)
        assert missing_profile.is_error is True
        assert missing_profile.structured_content["error"]["details"]["available"] == [
            profile
        ]
        assert profile in _text(missing_profile)

        oversized = await server.call_tool(
            "sql",
            {"statement": "select repeat('é', 33000) as text"},
        )
        assert isinstance(oversized, CallToolResult)
        assert oversized.is_error is True
        assert oversized.structured_content["error"]["code"] == "response_too_large"
        assert oversized.structured_content["error"]["details"]["bytes"] > 65_536
        assert "Narrow" in _text(oversized)
        recovered = await server.call_tool("sql", {"statement": "select 1 as value"})
        assert isinstance(recovered, CallToolResult)
        assert recovered.structured_content["rows"] == [{"value": 1}]

    asyncio.run(exercise())


def _text(result: CallToolResult) -> str:
    return "\n".join(
        item.text for item in result.content if isinstance(item, TextContent)
    )

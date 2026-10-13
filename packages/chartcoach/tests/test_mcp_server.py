from __future__ import annotations

import asyncio
import json
import sys
from dataclasses import replace
from importlib.metadata import version
from pathlib import Path
from typing import Any, cast

import chartcoach.mcp as mcp_server
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, Guideline, Section, open_catalog
from chartcoach.curation import EmbeddingProfile, build_release
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.types import CallToolResult, TextContent

pytestmark = [pytest.mark.mcp, pytest.mark.search, pytest.mark.curation]


def test_stdio_client_can_enumerate_read_and_cite_using_only_text_results(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    contract = Path(__file__).parents[3] / "fixtures/catalog-contract/operations.json"
    reference = json.loads(contract.read_text())["bibliography_urls"][0]["reference"]
    records = [
        replace(Guideline.from_mapping(row), references=(reference,))
        for row in sample_catalog.to_frame().iter_rows(named=True)
    ]
    records.append(replace(records[0], id="legend-labels"))
    catalog = Catalog.from_guidelines(records, manifest=sample_catalog.manifest)
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
            described = _payload(await session.call_tool("describe"))
            assert described["mcp"]["search"] is None
            assert described["mcp"]["sql_engine"] == "DuckDB"
            assert {table["name"] for table in described["tables"]} >= {
                "guidelines",
                "sections",
                "guideline_sources",
            }
            probe = _payload(
                await session.call_tool(
                    "sql", {"statement": "SELECT 1 AS probe", "limit": 1}
                )
            )
            assert probe["rows"] == [{"probe": 1}]

            ids: list[str] = []
            offset = 0
            while True:
                page = _payload(
                    await session.call_tool(
                        "sql",
                        {
                            "statement": f"SELECT id, title, description FROM guidelines ORDER BY id LIMIT 2 OFFSET {offset}",
                            "limit": 2,
                        },
                    )
                )
                assert page["row_count"] == len(page["rows"])
                assert page["truncated"] is False
                ids.extend(row["id"] for row in page["rows"])
                offset += page["row_count"]
                if page["row_count"] < 2:
                    break
            assert ids == ["direct-labels", "full-axis-bars", "legend-labels"]
            assert offset == 3
            for guideline_id in ids:
                evidence = _payload(
                    await session.call_tool("read", {"ids": [guideline_id]})
                )
                assert evidence["records"][0]["sections"][0]["content"]
                citation = _payload(
                    await session.call_tool("cite", {"ids": [guideline_id]})
                )
                assert citation["records"][0]["url"].endswith(guideline_id)

            result = await session.call_tool("read", {"ids": ["direct-labels"]})
            assert result.is_error is False
            assert _payload(result)["records"][0]["id"] == "direct-labels"
            missing = await session.call_tool("read", {"ids": ["missing"]})
            assert missing.is_error is True
            assert _payload(missing)["error"]["code"] == "lookup"
            wrong_role = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["recommendations"]}
            )
            assert wrong_role.is_error is True
            assert _payload(wrong_role)["error"]["code"] == "lookup"
            assert any(
                "advice" in hint for hint in _payload(wrong_role)["error"]["hints"]
            )
            assert "advice" in _text(wrong_role)

            invalid_limit = await session.call_tool(
                "sql", {"statement": "select 1", "limit": 0}
            )
            assert invalid_limit.is_error is True
            assert "limit" in _text(invalid_limit)

            large_error = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["é" * 40_000]}
            )
            assert large_error.is_error is True
            assert _payload(large_error)["error"]["code"] == "lookup"
            assert "é" * 40_000 in _payload(large_error)["error"]["message"]
            assert len(_text(large_error).encode("utf-8")) > 65_536

            recovered = await session.call_tool(
                "read", {"ids": ["direct-labels"], "roles": ["advice"]}
            )
            assert recovered.is_error is False
            assert (
                _payload(recovered)["records"][0]["sections"][0]["content"]
                == "Place labels near marks."
            )
            citation = await session.call_tool("cite", {"ids": ["direct-labels"]})
            source = _payload(citation)["records"][0]["sources"][0]
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
                ),
                "test-inspected": EmbeddingProfile(
                    deterministic_embedding("chartcoach-mcp-test")
                ),
            },
        )
        monkeypatch.setattr(
            "chartcoach._catalog.runtime.cache._cache_root",
            lambda: tmp_path / "cache",
        )
        catalog = open_catalog(release_root)
        assert catalog.release is not None
        server = mcp_server.create_server(catalog, profile=profile)

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
        assert search_input["limit"]["minimum"] == 1
        assert "matches[].id" in read_input["ids"]["description"]
        assert "BibTeX" in read_input["source_detail"]["description"]
        assert "LanceDB SQL" in search_input["where"]["description"]
        assert "DESCRIBE guidelines" in sql_input["statement"]["description"]
        assert "exceptions" in read_input["roles"]["description"]
        assert tool_map["search"].description is not None
        assert tool_map["describe"].description is not None
        assert tool_map["read"].description is not None

        def unexpected_index_or_provider(*_args: object, **_kwargs: object) -> None:
            pytest.fail("Discovery must keep the index and embedding provider idle.")

        with monkeypatch.context() as lazy:
            lazy.setattr(catalog, "_search_table", unexpected_index_or_provider)
            lazy.setattr(
                "chartcoach._catalog.search.SearchEmbeddings.get",
                unexpected_index_or_provider,
            )
            description = await server.call_tool(
                "describe", {"profile": "test-inspected"}
            )
        assert isinstance(description, CallToolResult)
        assert description.is_error is False
        description_data = _payload(description)
        assert description_data["profile"]["name"] == "test-inspected"
        assert description_data["release_digest"] == catalog.release.digest
        assert (
            cast(dict[str, object], description_data["profile"])["distance_metric"]
            == "cosine"
        )
        search_info = description_data["mcp"]["search"]
        assert search_info["profile"] == profile
        assert set(search_info["filter_columns"]) == {
            "row_id",
            "id",
            "parent_id",
            "role",
            "labels",
            "content_hash",
            "text",
            "vector",
        }
        assert set(search_info["document_roles"]) == {
            "document",
            "overview",
            "section.advice",
        }

        sql = await server.call_tool(
            "sql",
            {"statement": "select id from guidelines order by id", "limit": 1},
        )
        assert isinstance(sql, CallToolResult)
        assert sql.is_error is False
        sql_data = _payload(sql)
        assert sql_data["truncated"] is True
        assert sql_data["release_digest"] == catalog.release.digest

        read = await server.call_tool("read", {"ids": ["direct-labels"]})
        cite = await server.call_tool("cite", {"ids": ["direct-labels"]})
        assert isinstance(read, CallToolResult)
        assert isinstance(cite, CallToolResult)
        assert read.is_error is False
        assert cite.is_error is False
        assert _payload(read)["records"][0]["id"] == "direct-labels"
        assert _payload(cite)["records"][0]["id"] == "direct-labels"

        types = _payload(
            await server.call_tool("sql", {"statement": "DESCRIBE guidelines"})
        )
        assert {row["column_name"]: row["column_type"] for row in types["rows"]}[
            "labels"
        ] == "VARCHAR[]"

        search = await server.call_tool(
            "search",
            {"text": "direct labels", "limit": 1, "mode": "fts"},
        )
        assert isinstance(search, CallToolResult)
        assert search.is_error is False
        search_data = _payload(search)
        assert search_data["score_kind"] == "relevance"
        assert search_data["documents_considered"] == 1
        assert cast(list[dict[str, object]], search_data["matches"])[0]["id"] == (
            "direct-labels"
        )
        wide_search = _payload(
            await server.call_tool("search", {"text": "direct labels", "limit": 150})
        )
        assert wide_search["limit"] == 150
        assert wide_search["matches"][0]["id"] == "direct-labels"
        for mode in ("vector", "hybrid"):
            semantic = await server.call_tool(
                "search", {"text": "direct labels", "mode": mode, "limit": 3}
            )
            assert isinstance(semantic, CallToolResult)
            assert semantic.is_error is False
            semantic_data = _payload(semantic)
            assert semantic_data["matches"]
            assert semantic_data["score_kind"] == (
                "distance" if mode == "vector" else "relevance"
            )

        filtered = _payload(
            await server.call_tool(
                "search", {"text": "direct labels", "where": "role = 'section.advice'"}
            )
        )
        assert filtered["matches"]
        assert all(
            match["matched_role"] == "section.advice" for match in filtered["matches"]
        )
        parent = _payload(
            await server.call_tool(
                "search",
                {"text": "direct labels", "where": "parent_id = 'direct-labels'"},
            )
        )
        assert [match["id"] for match in parent["matches"]] == ["direct-labels"]
        empty = _payload(
            await server.call_tool("search", {"text": "absentuniqueterm74298651"})
        )
        assert empty["matches"] == []
        assert empty["match_count"] == 0

        invalid_filter_result = await server.call_tool(
            "search", {"text": "clutter", "where": "invalid_column_probe = 1"}
        )
        assert isinstance(invalid_filter_result, CallToolResult)
        invalid_filter = _payload(invalid_filter_result)
        assert invalid_filter["error"]["code"] == "invalid_input"
        assert "parent_id" in invalid_filter["error"]["details"]["columns"]
        assert "invalid_column_probe" in invalid_filter["error"]["details"]["reason"]
        assert any("describe" in hint for hint in invalid_filter["error"]["hints"])

        blank = _payload(await server.call_tool("search", {"text": "   "}))
        assert blank["error"]["code"] == "invalid_input"
        assert "non-empty string" in blank["error"]["message"]
        assert blank["error"]["hints"] == []

        missing = await server.call_tool("read", {"ids": ["missing"]})
        assert isinstance(missing, CallToolResult)
        assert missing.is_error is True
        error = _payload(missing)["error"]
        assert error["code"] == "lookup"
        assert error["details"]["id"] == "missing"
        assert "direct-labels" in error["details"]["suggestions"]
        assert error["hints"]
        assert any("sql(" in hint for hint in error["hints"])

        missing_profile = await server.call_tool("describe", {"profile": "missing"})
        assert isinstance(missing_profile, CallToolResult)
        assert missing_profile.is_error is True
        assert _payload(missing_profile)["error"]["details"]["available"] == [
            profile,
            "test-inspected",
        ]
        assert profile in _text(missing_profile)

        large_sql = await server.call_tool(
            "sql",
            {"statement": "select repeat('é', 33000) as text"},
        )
        assert isinstance(large_sql, CallToolResult)
        assert large_sql.is_error is False
        assert _payload(large_sql)["rows"] == [{"text": "é" * 33_000}]
        assert len(_text(large_sql).encode("utf-8")) > 65_536
        recovered = await server.call_tool("sql", {"statement": "select 1 as value"})
        assert isinstance(recovered, CallToolResult)
        assert _payload(recovered)["rows"] == [{"value": 1}]

    asyncio.run(exercise())


def test_mcp_accepts_caller_selected_row_and_batch_sizes(
    sample_catalog: Catalog,
) -> None:
    record = Guideline.from_mapping(sample_catalog.to_frame().row(0, named=True))
    ids = [f"chart-label-{index:03d}" for index in range(150)]
    catalog = Catalog.from_guidelines(
        [replace(record, id=guideline_id) for guideline_id in ids],
        manifest=sample_catalog.manifest,
    )

    async def exercise() -> None:
        server = mcp_server.create_server(catalog)
        page = _payload(
            await server.call_tool(
                "sql",
                {"statement": "SELECT id FROM guidelines ORDER BY id", "limit": 150},
            )
        )
        assert page["row_count"] == 150
        assert page["truncated"] is False
        assert [row["id"] for row in page["rows"]] == ids

        for tool in ("read", "cite"):
            result = _payload(await server.call_tool(tool, {"ids": ids}))
            assert [row["id"] for row in result["records"]] == ids
            empty = _payload(await server.call_tool(tool, {"ids": []}))
            assert empty["records"] == []

        roles = _payload(
            await server.call_tool("read", {"ids": ids[:1], "roles": ["advice"] * 150})
        )
        assert [section["role"] for section in roles["records"][0]["sections"]] == [
            "advice"
        ]

    asyncio.run(exercise())


def test_mcp_search_retains_dependency_repair_and_fts_recovery(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    profile = "test-dependencies"
    release_root = tmp_path / "release"
    build_release(
        sample_catalog,
        release_root,
        profiles={
            profile: EmbeddingProfile(
                deterministic_embedding("chartcoach-mcp-deps"),
                python_requirements={"lancedb": version("lancedb")},
            )
        },
    )
    monkeypatch.setattr(
        "chartcoach._catalog.search._installed", lambda _distribution: False
    )

    async def exercise() -> None:
        server = mcp_server.create_server(open_catalog(release_root), profile=profile)
        failed = _payload(
            await server.call_tool(
                "search", {"text": "direct labels", "mode": "vector"}
            )
        )
        assert failed["error"]["code"] == "unavailable_capability"
        assert failed["error"]["details"]["missing"] == ["lancedb"]
        assert any(
            "Install the listed packages" in hint for hint in failed["error"]["hints"]
        )
        assert any("mode='fts'" in hint for hint in failed["error"]["hints"])
        recovered = _payload(
            await server.call_tool("search", {"text": "direct labels"})
        )
        assert recovered["matches"][0]["id"] == "direct-labels"

    asyncio.run(exercise())


@pytest.mark.parametrize(
    "statement,repaired,rows,hint",
    [
        (
            "SELECT 1 AS value, 2 AS value",
            "SELECT 1 AS first, 2 AS second",
            [{"first": 1, "second": 2}],
            "alias",
        ),
        (
            "SELECT CAST('abc' AS BLOB) AS value",
            "SELECT CAST(CAST('abc' AS BLOB) AS VARCHAR) AS value",
            [{"value": "abc"}],
            "VARCHAR",
        ),
    ],
)
def test_sql_input_recovery_keeps_actionable_guidance(
    sample_catalog: Catalog,
    statement: str,
    repaired: str,
    rows: list[dict[str, object]],
    hint: str,
) -> None:
    async def exercise() -> None:
        server = mcp_server.create_server(sample_catalog)
        failed = _payload(await server.call_tool("sql", {"statement": statement}))
        assert failed["error"]["code"] == "invalid_input"
        assert any(hint in guidance for guidance in failed["error"]["hints"])
        recovered = _payload(await server.call_tool("sql", {"statement": repaired}))
        assert recovered["rows"] == rows

    asyncio.run(exercise())


def test_citation_template_recovery_keeps_argument_guidance(
    sample_catalog: Catalog,
) -> None:
    async def exercise() -> None:
        server = mcp_server.create_server(sample_catalog)
        failed = _payload(
            await server.call_tool(
                "cite",
                {"ids": ["direct-labels"], "url_template": "https://example.com"},
            )
        )
        assert failed["error"]["code"] == "invalid_input"
        assert any("{id}" in hint for hint in failed["error"]["hints"])
        recovered = _payload(
            await server.call_tool(
                "cite",
                {"ids": ["direct-labels"], "url_template": "https://example.com/{id}"},
            )
        )
        assert recovered["records"][0]["url"] == "https://example.com/direct-labels"

    asyncio.run(exercise())


def test_large_read_and_search_results_are_complete(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    content = "é" * 20_000
    catalog = Catalog.from_guidelines(
        [
            replace(
                Guideline.from_mapping(row),
                description="large result probe " + content,
                sections=(Section(role="advice", title="Advice", content=content),),
            )
            for row in sample_catalog.to_frame().iter_rows(named=True)
        ],
        manifest=sample_catalog.manifest,
    )

    async def exercise() -> None:
        profile = "test-large-results"
        release = tmp_path / "release"
        build_release(
            catalog,
            release,
            profiles={
                profile: EmbeddingProfile(
                    deterministic_embedding("chartcoach-large-results")
                )
            },
        )
        server = mcp_server.create_server(open_catalog(release), profile=profile)
        ids = ["direct-labels", "full-axis-bars"]
        result = await server.call_tool("read", {"ids": ids})
        assert isinstance(result, CallToolResult)
        assert result.is_error is False
        assert len(_text(result).encode("utf-8")) > 65_536
        assert [row["id"] for row in _payload(result)["records"]] == ids
        assert all(
            row["sections"][0]["content"] == content
            for row in _payload(result)["records"]
        )

        search = await server.call_tool(
            "search", {"text": "large result probe", "limit": 100}
        )
        assert isinstance(search, CallToolResult)
        assert search.is_error is False
        assert len(_text(search).encode("utf-8")) > 65_536
        assert {match["id"] for match in _payload(search)["matches"]} == set(ids)
        assert all(
            match["description"] == "large result probe " + content
            for match in _payload(search)["matches"]
        )

    asyncio.run(exercise())


def _payload(result: object) -> dict[str, Any]:
    assert isinstance(result, CallToolResult)
    assert len(result.content) == 1
    payload = json.loads(_text(result))
    assert payload == result.structured_content
    return payload


def _text(result: CallToolResult) -> str:
    return "\n".join(
        item.text for item in result.content if isinstance(item, TextContent)
    )

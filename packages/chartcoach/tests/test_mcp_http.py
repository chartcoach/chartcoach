from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager

import httpx2
import pytest
from chartcoach import Catalog
from chartcoach.mcp import MCPConfig, create_app, create_server, register_tools
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.server import MCPServer
from mcp.types import CallToolResult
from starlette.applications import Starlette
from starlette.routing import Mount

pytestmark = pytest.mark.mcp


@pytest.mark.parametrize("streaming", [False, True])
@pytest.mark.parametrize(
    "public_url,base_url",
    [
        ("https://mcp.example.test", "https://mcp.example.test"),
        ("https://MCP.EXAMPLE.TEST:443/", "https://mcp.example.test"),
        ("https://[2001:0db8:0:0:0:0:0:1]:443/", "https://[2001:db8::1]"),
        ("https://xn--fa-hia.example", "https://xn--fa-hia.example"),
    ],
)
def test_http_client_tools_auth_origin_policy_and_readiness(
    sample_catalog: Catalog, streaming: bool, public_url: str, base_url: str
) -> None:
    async def exercise() -> None:
        config = MCPConfig(
            transport="streamable-http",
            public_url=public_url,
            path="/catalog/mcp",
            token="http-test-token",
            json_response=not streaming,
        )
        server = create_server(sample_catalog)
        app = create_app(server, config=config)
        async with httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=app), base_url=base_url
        ) as client:
            assert (await client.get("/healthz")).status_code == 503
            async with app.router.lifespan_context(app):
                assert (await client.get("/healthz")).json() == {"ok": True}
                assert (await client.post(config.path)).status_code == 401
                client.headers["Authorization"] = "bEaReR   http-test-token"
                assert (
                    await client.post(
                        config.path, json={}, headers={"Host": "attacker.example"}
                    )
                ).status_code == 421
                assert (
                    await client.post(
                        config.path,
                        json={},
                        headers={"Origin": "https://attacker.example"},
                    )
                ).status_code == 403
                client.headers["Origin"] = base_url
                async with (
                    streamable_http_client(
                        str(client.base_url.join(config.path)), http_client=client
                    ) as streams,
                    ClientSession(*streams[:2]) as session,
                ):
                    await session.initialize()
                    tools = await session.list_tools()
                    assert {tool.name for tool in tools.tools} == {
                        "describe",
                        "sql",
                        "read",
                        "cite",
                    }
                    result = await session.call_tool("read", {"ids": ["direct-labels"]})
                    assert result.is_error is False
                    assert (
                        result.structured_content["records"][0]["id"] == "direct-labels"
                    )
                    sql = await session.call_tool(
                        "sql", {"statement": "select 1 as value"}
                    )
                    assert sql.is_error is False
                    assert sql.structured_content["rows"] == [{"value": 1}]
            assert (await client.get("/healthz")).status_code == 503

    asyncio.run(exercise())


def test_mounted_app_keeps_readiness_public_and_tools_authenticated(
    sample_catalog: Catalog,
) -> None:
    async def exercise() -> None:
        child = create_app(
            create_server(sample_catalog), config=MCPConfig(token="mount-token")
        )

        @asynccontextmanager
        async def lifespan(parent: Starlette):
            async with child.router.lifespan_context(child):
                yield

        parent = Starlette(routes=[Mount("/catalog", app=child)], lifespan=lifespan)
        async with httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=parent), base_url="http://localhost"
        ) as client:
            assert (await client.get("/catalog/healthz")).status_code == 503
            async with parent.router.lifespan_context(parent):
                assert (await client.get("/catalog/healthz")).json() == {"ok": True}
                assert (await client.post("/catalog/mcp", json={})).status_code == 401
                client.headers["Authorization"] = "Bearer mount-token"
                async with (
                    streamable_http_client(
                        "http://localhost/catalog/mcp", http_client=client
                    ) as streams,
                    ClientSession(*streams[:2]) as session,
                ):
                    await session.initialize()
                    assert (await session.list_tools()).tools
            assert (await client.get("/catalog/healthz")).status_code == 503

    asyncio.run(exercise())


def test_register_tools_composes_with_a_caller_owned_sdk_server(
    sample_catalog: Catalog,
) -> None:
    async def exercise() -> None:
        server = MCPServer("custom")
        server.add_tool(lambda: "application", name="application")
        register_tools(server, catalog=sample_catalog)
        assert {tool.name for tool in await server.list_tools()} == {
            "application",
            "describe",
            "sql",
            "read",
            "cite",
        }

    asyncio.run(exercise())


def test_mcp_sql_deadline_interrupts_work_and_allows_recovery(
    sample_catalog: Catalog,
) -> None:
    async def exercise() -> None:
        server = create_server(sample_catalog, sql_timeout=0.05)
        result = await server.call_tool(
            "sql",
            {"statement": "select sum(sin(i)) as total from range(1000000000) t(i)"},
        )
        assert isinstance(result, CallToolResult)
        assert result.is_error is True
        assert result.structured_content["error"]["code"] == "operation_failed"
        assert "deadline" in result.structured_content["error"]["message"]
        recovered = await server.call_tool("sql", {"statement": "select 1 as value"})
        assert isinstance(recovered, CallToolResult)
        assert recovered.is_error is False

    asyncio.run(exercise())


def test_sql_deadline_still_applies_when_interrupt_arrives_during_idle_planning(
    sample_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    from threading import Event

    from chartcoach._catalog.errors import CatalogOperationError
    from chartcoach._catalog.sql import catalog_sql

    connection = sample_catalog.duckdb(
        config={"enable_external_access": False, "threads": 1}
    )
    interrupted = Event()

    class DelayedConnection:
        def sql(self, statement: str):
            assert interrupted.wait(timeout=2), (
                "Deadline never interrupted idle connection"
            )
            return connection.sql(statement)

        def interrupt(self) -> None:
            connection.interrupt()
            interrupted.set()

        def close(self) -> None:
            connection.close()

    monkeypatch.setattr(sample_catalog, "duckdb", lambda **_kwargs: DelayedConnection())
    with pytest.raises(CatalogOperationError, match="execution deadline"):
        catalog_sql(
            sample_catalog,
            "select sum(sin(i)) as total from range(1000000) t(i)",
            timeout=0.01,
        )

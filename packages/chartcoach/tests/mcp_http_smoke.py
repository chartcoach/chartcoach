"""Exercise an installed wheel through uvx, dotenv, HTTP, and stdio clients."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import httpx2
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client


async def check_tools(session: ClientSession) -> None:
    await session.initialize()
    tools = await session.list_tools()
    assert {tool.name for tool in tools.tools} == {"describe", "sql", "read", "cite"}
    described = await session.call_tool("describe")
    assert not described.is_error
    identity = described.structured_content["release_digest"]
    assert identity
    read = await session.call_tool("read", {"ids": ["direct-labels"]})
    assert not read.is_error
    assert read.structured_content["records"][0]["id"] == "direct-labels"
    assert read.structured_content["release_digest"] == identity
    sql = await session.call_tool(
        "sql", {"statement": "SELECT count(*) AS entries FROM guidelines"}
    )
    assert not sql.is_error
    assert sql.structured_content["rows"][0]["entries"] > 0
    assert sql.structured_content["release_digest"] == identity


async def check_http(url: str) -> None:
    async with (
        httpx2.AsyncClient(
            headers={"Authorization": "Bearer smoke-token", "Host": "mcp.example.test"}
        ) as client,
        streamable_http_client(url, http_client=client) as (read, write),
        ClientSession(read, write) as session,
    ):
        await check_tools(session)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wheel", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    args = parser.parse_args()
    command = [
        os.environ.get("UV", "uv"),
        "tool",
        "run",
        "--isolated",
        "--python",
        sys.executable,
        "--from",
        f"{args.wheel.resolve()}[mcp]",
        "chartcoach",
        "mcp",
    ]
    environment = {
        name: value
        for name, value in os.environ.items()
        if not name.startswith("CHARTCOACH_") and name != "PYTHONPATH"
    }
    with tempfile.TemporaryDirectory(prefix="chartcoach-mcp-smoke-") as directory:
        root = Path(directory)
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
        (root / ".env").write_text(
            f"CHARTCOACH_SOURCE={json.dumps(args.source.resolve().as_posix(), ensure_ascii=False)}\n"
            f"CHARTCOACH_MCP_PORT={port}\n"
            "CHARTCOACH_MCP_TRANSPORT=streamable-http\n"
            "CHARTCOACH_MCP_HOST=127.0.0.1\n"
            "CHARTCOACH_MCP_PUBLIC_URL=https://mcp.example.test\n"
            "CHARTCOACH_MCP_PATH=/catalog/mcp\n"
            "CHARTCOACH_MCP_TOKEN=smoke-token\n",
            encoding="utf-8",
        )
        url = f"http://127.0.0.1:{port}"
        with (root / "server.log").open("w+") as log:
            process = subprocess.Popen(
                command, cwd=root, env=environment, stdout=log, stderr=log
            )
            try:
                deadline = time.monotonic() + 90
                with httpx2.Client(timeout=2) as client:
                    while True:
                        if process.poll() is not None:
                            raise AssertionError(
                                f"uvx MCP exited with {process.returncode}"
                            )
                        try:
                            response = client.get(url + "/healthz")
                            if response.status_code == 200:
                                assert response.json() == {"ok": True}
                                break
                        except httpx2.TransportError:
                            pass
                        if time.monotonic() > deadline:
                            raise AssertionError("uvx MCP did not become ready")
                        time.sleep(0.1)
                    assert client.post(url + "/catalog/mcp", json={}).status_code == 401
                    assert (
                        client.post(
                            url + "/catalog/mcp",
                            json={},
                            headers={
                                "Authorization": "Bearer smoke-token",
                                "Origin": "https://foreign.example.test",
                            },
                        ).status_code
                        == 403
                    )
                asyncio.run(
                    asyncio.wait_for(check_http(url + "/catalog/mcp"), timeout=90)
                )
            finally:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=10)

            async def check_stdio() -> None:
                async with (
                    stdio_client(
                        StdioServerParameters(
                            command=command[0],
                            args=[*command[1:], "--transport", "stdio"],
                            cwd=root,
                            env=environment,
                        )
                    ) as (read, write),
                    ClientSession(read, write) as session,
                ):
                    await check_tools(session)

            asyncio.run(asyncio.wait_for(check_stdio(), timeout=90))
    print(
        "Verified uvx MCP startup, dotenv, readiness, authentication, HTTP and stdio tools"
    )


if __name__ == "__main__":
    main()

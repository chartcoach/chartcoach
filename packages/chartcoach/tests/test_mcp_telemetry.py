from __future__ import annotations

import asyncio
import contextlib
import gzip
import json
import logging
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from collections.abc import Callable, Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from typing import Any

import pytest
from chartcoach import Catalog, open_catalog
from chartcoach.cli.main import main
from chartcoach.curation import build_release
from chartcoach.mcp import create_server
from click.testing import CliRunner
from langfuse import Langfuse
from mcp import Client, ClientSession
from mcp.client.stdio import (
    StdioServerParameters,
    get_default_environment,
    stdio_client,
)
from opentelemetry.proto.collector.trace.v1.trace_service_pb2 import (
    ExportTraceServiceRequest,
)
from opentelemetry.sdk.trace import ReadableSpan
from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
    InMemorySpanExporter,
)
from opentelemetry.trace import StatusCode, format_trace_id

pytestmark = [pytest.mark.mcp, pytest.mark.tracing, pytest.mark.curation]

METADATA = "langfuse.observation.metadata"
Spans = Callable[[], tuple[ReadableSpan, ...]]


@pytest.fixture(scope="module")
def exported() -> Iterator[Spans]:
    # Langfuse registers its span processor on the process-wide tracer provider
    # that the MCP SDK records into, so one client serves the whole module.
    exporter = InMemorySpanExporter()
    langfuse = Langfuse(
        public_key="pk-lf-telemetry-test",
        secret_key="sk-lf-telemetry-test",
        base_url="http://127.0.0.1:9",
        span_exporter=exporter,
    )

    def finished() -> tuple[ReadableSpan, ...]:
        langfuse.flush()
        spans = exporter.get_finished_spans()
        exporter.clear()
        return spans

    yield finished
    langfuse.shutdown()


@pytest.fixture
def release(sample_catalog: Catalog, tmp_path: Path) -> Catalog:
    build_release(sample_catalog, tmp_path / "release")
    return open_catalog(tmp_path / "release")


def test_tool_spans_carry_arguments_results_and_host_identity(
    release: Catalog, exported: Spans
) -> None:
    async def exercise() -> dict[str, Any] | None:
        async with Client(create_server(release)) as client:
            result = await client.call_tool(
                "read",
                {"ids": ["direct-labels"]},
                meta={"openai/session": "chat-7", "openai/subject": "person-3"},
            )
            return result.structured_content

    payload = asyncio.run(exercise())

    [span] = exported()
    attributes = span.attributes or {}
    assert release.release is not None
    assert span.name == "tools/call read"
    assert json.loads(str(attributes["gen_ai.tool.call.arguments"])) == {
        "ids": ["direct-labels"]
    }
    assert json.loads(str(attributes["gen_ai.tool.call.result"])) == payload
    assert attributes["gen_ai.conversation.id"] == "chat-7"
    assert attributes["user.id"] == "person-3"
    assert attributes["langfuse.observation.type"] == "retriever"
    assert attributes["langfuse.trace.tags"] == ("chartcoach", "mcp")
    assert attributes[f"{METADATA}.sessionSource"] == "openai/session"
    assert attributes[f"{METADATA}.catalogId"] == release.release.digest
    assert attributes[f"{METADATA}.catalogReleaseId"] == release.release.digest
    assert attributes[f"{METADATA}.client"] == "mcp"


@pytest.mark.parametrize("host", [None, "claude-session-1"])
def test_stdio_calls_share_the_launching_session(
    release: Catalog,
    exported: Spans,
    monkeypatch: pytest.MonkeyPatch,
    host: str | None,
) -> None:
    if host is None:
        monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    else:
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", host)

    # The in-process client, like stdio, carries no HTTP request.
    async def exercise() -> None:
        async with Client(create_server(release)) as client:
            await client.call_tool("describe")
            await client.call_tool("sql", {"statement": "SELECT 1 AS probe"})

    asyncio.run(exercise())

    spans = exported()
    assert len(spans) == 2
    attributes = [span.attributes or {} for span in spans]
    assert len({item["gen_ai.conversation.id"] for item in attributes}) == 1
    if host is not None:
        assert attributes[0]["gen_ai.conversation.id"] == host
    assert {item[f"{METADATA}.sessionSource"] for item in attributes} == {
        "CLAUDE_CODE_SESSION_ID" if host else "process"
    }


def test_tool_errors_and_log_records_name_the_outcome(
    release: Catalog, exported: Spans, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.INFO, logger="chartcoach.mcp")

    async def exercise() -> None:
        async with Client(create_server(release)) as client:
            await client.call_tool("read", {"ids": ["private-missing-id"]})
            await client.call_tool("unknown", {})

    asyncio.run(exercise())

    spans = {span.name: span for span in exported()}
    assert set(spans) == {"tools/call read", "tools/call unknown"}
    assert all(span.status.status_code is StatusCode.ERROR for span in spans.values())
    read = spans["tools/call read"].attributes or {}
    unknown = spans["tools/call unknown"].attributes or {}
    assert read[f"{METADATA}.errorCode"] == "lookup"
    assert read["langfuse.observation.status_message"] == (
        "Unknown guideline entry ID: private-missing-id"
    )
    assert unknown[f"{METADATA}.errorCode"] == "tool_error"
    assert unknown["gen_ai.tool.call.result"] == "Unknown tool: unknown"

    [message] = [
        record.getMessage()
        for record in caplog.records
        if record.name == "chartcoach.mcp" and "tool=read" in record.getMessage()
    ]
    trace_id = format_trace_id(spans["tools/call read"].context.trace_id)
    assert message.startswith("tool=read outcome=lookup duration_ms=")
    assert message.endswith(f"trace_id={trace_id}")
    assert "private-missing-id" not in message


def test_caller_trace_context_sets_the_parent_session_and_user(
    release: Catalog, exported: Spans
) -> None:
    async def exercise() -> None:
        async with Client(create_server(release)) as client:
            await client.call_tool(
                "describe",
                meta={
                    "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
                    "baggage": "langfuse_session_id=agent-run-9,langfuse_user_id=analyst-2",
                },
            )

    asyncio.run(exercise())

    [span] = exported()
    attributes = span.attributes or {}
    assert span.parent is not None
    assert format_trace_id(span.context.trace_id) == "0af7651916cd43dd8448eb211c80319c"
    assert span.parent.span_id == 0xB7AD6B7169203331
    assert attributes["session.id"] == attributes["gen_ai.conversation.id"]
    assert attributes["gen_ai.conversation.id"] == "agent-run-9"
    assert attributes["user.id"] == "analyst-2"
    assert attributes[f"{METADATA}.sessionSource"] == "baggage"


@pytest.mark.parametrize("transport", ["stdio", "streamable-http"])
def test_cli_exports_tool_traces_to_langfuse_before_exit(
    sample_catalog: Catalog, tmp_path: Path, transport: str
) -> None:
    build_release(sample_catalog, tmp_path / "release")
    received: list[tuple[str, ExportTraceServiceRequest]] = []

    class Langfuse(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            pass

        def do_POST(self) -> None:
            body = self.rfile.read(int(self.headers["Content-Length"]))
            if self.headers.get("Content-Encoding") == "gzip":
                body = gzip.decompress(body)
            request = ExportTraceServiceRequest()
            request.ParseFromString(body)
            received.append((self.path, request))
            self.send_response(200)
            self.send_header("Content-Type", "application/x-protobuf")
            self.send_header("Content-Length", "0")
            self.end_headers()

    endpoint = ThreadingHTTPServer(("127.0.0.1", 0), Langfuse)
    Thread(target=endpoint.serve_forever, daemon=True).start()
    command = [
        sys.executable,
        "-c",
        "from chartcoach.cli.main import main; main()",
        "mcp",
        "--source",
        str(tmp_path / "release"),
    ]
    environment = {
        "CHARTCOACH_MCP_TRACING": "true",
        "LANGFUSE_PUBLIC_KEY": "pk-lf-cli-test",
        "LANGFUSE_SECRET_KEY": "sk-lf-cli-test",
        "LANGFUSE_BASE_URL": f"http://127.0.0.1:{endpoint.server_port}",
    }
    arguments = {"statement": "SELECT 1 AS probe"}

    async def over_stdio() -> None:
        parameters = StdioServerParameters(
            command=command[0], args=command[1:], env=environment, cwd=tmp_path
        )
        async with (
            stdio_client(parameters) as (reader, writer),
            ClientSession(reader, writer) as session,
        ):
            await session.initialize()
            await session.call_tool("sql", arguments)

    def over_http() -> int:
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        server = subprocess.Popen(
            [*command, "--transport", "streamable-http", "--port", str(port)],
            env=get_default_environment() | environment,
            cwd=tmp_path,
        )
        try:
            url = f"http://127.0.0.1:{port}"
            for _ in range(100):
                with contextlib.suppress(OSError):
                    urllib.request.urlopen(f"{url}/healthz", timeout=1).close()
                    break
                time.sleep(0.2)

            async def call() -> None:
                async with Client(f"{url}/mcp") as client:
                    await client.call_tool("sql", arguments)

            asyncio.run(call())
            # Container runtimes stop the server with SIGTERM.
            server.send_signal(signal.SIGTERM)
            return server.wait(timeout=30)
        finally:
            if server.poll() is None:
                server.kill()

    try:
        if transport == "stdio":
            asyncio.run(over_stdio())
        else:
            assert over_http() == 128 + signal.SIGTERM
    finally:
        endpoint.shutdown()
        endpoint.server_close()

    spans = [
        span
        for _, request in received
        for resource in request.resource_spans
        for scope in resource.scope_spans
        for span in scope.spans
    ]
    assert {path for path, _ in received} == {"/api/public/otel/v1/traces"}
    assert [span.name for span in spans] == ["tools/call sql"]
    attributes = {item.key: item.value.string_value for item in spans[0].attributes}
    assert json.loads(attributes["gen_ai.tool.call.arguments"]) == arguments
    assert json.loads(attributes["gen_ai.tool.call.result"])["rows"] == [{"probe": 1}]


def test_tracing_requires_langfuse_keys_before_opening_the_catalog(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("LANGFUSE_PUBLIC_KEY", raising=False)
    monkeypatch.delenv("LANGFUSE_SECRET_KEY", raising=False)

    result = CliRunner().invoke(
        main, ["mcp", "--tracing", "--source", str(tmp_path / "absent")]
    )

    assert result.exit_code == 1
    assert (
        "CHARTCOACH_MCP_TRACING requires LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY."
        in result.output
    )

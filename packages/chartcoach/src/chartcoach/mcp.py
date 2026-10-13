"""Compose catalog tools, an MCP server, or an ASGI app independently of the CLI."""

from __future__ import annotations

import logging
import signal
import sys
from collections.abc import Mapping

try:
    from mcp.server import MCPServer
except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
    if exc.name == "mcp" or (exc.name is not None and exc.name.startswith("mcp.")):
        add_note = getattr(exc, "add_note", None)
        if callable(add_note):
            add_note("Install chartcoach[mcp] to use the chartcoach MCP server.")
    raise

from ._catalog import Catalog, open_catalog
from ._mcp.config import MCPConfig, load_config
from ._mcp.http import create_app
from ._mcp.settings import DEFAULT_LOG_LEVEL, DEFAULT_SQL_TIMEOUT
from ._mcp.telemetry import ToolTelemetry, start_langfuse
from ._mcp.tools import register_tools


def create_server(
    catalog: Catalog,
    *,
    profile: str | None = None,
    embedding_variables: Mapping[str, str] | None = None,
    embedding_environment: Mapping[str, str] | None = None,
    sql_timeout: float = DEFAULT_SQL_TIMEOUT,
    log_level: str = DEFAULT_LOG_LEVEL,
) -> MCPServer:
    """Bind a caller-owned catalog and native LanceDB profile to a new server.

    Only variables declared by the selected profile are read from the environment.
    Explicit variables take precedence. No model, index, or credential is needed
    for full-text search. Extend the returned SDK server with your own tools.
    Tool calls are logged and annotate the SDK's OpenTelemetry spans for any
    tracer provider the process configures.
    """
    settings = MCPConfig(profile=profile, sql_timeout=sql_timeout, log_level=log_level)
    server = MCPServer(
        "chartcoach",
        description="Inspect one source-traced Guideline Catalog.",
        instructions=(
            "Call describe first for schemas, vocabulary and active search configuration. "
            "Use sql for candidate selection and catalog enumeration, or configured search "
            "for ranked topic candidates. Read guideline IDs to inspect context and exceptions, "
            "then cite their sources."
        ),
        log_level=settings.log_level,
        middleware=[ToolTelemetry(catalog)],
    )
    register_tools(
        server,
        catalog=catalog,
        profile=profile,
        embedding_variables=embedding_variables,
        embedding_environment=embedding_environment,
        sql_timeout=settings.sql_timeout,
    )
    return server


def run(config: MCPConfig) -> None:
    """Open one catalog, compose its server, and run the selected transport.

    With tracing enabled, Langfuse exports tool spans until the transport stops.
    """
    logging.basicConfig(
        level=config.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    langfuse = start_langfuse() if config.tracing else None
    if langfuse is not None:
        # uvicorn re-raises SIGTERM after its graceful shutdown. Exiting through
        # SystemExit runs the finally block, which flushes buffered spans.
        signal.signal(signal.SIGTERM, lambda signum, _: sys.exit(128 + signum))
    try:
        _serve(config)
    finally:
        if langfuse is not None:
            langfuse.shutdown()


def _serve(config: MCPConfig) -> None:
    catalog = open_catalog(config.source)
    server = create_server(
        catalog,
        profile=config.profile,
        embedding_variables=config.embedding_variables,
        embedding_environment=config.embedding_environment,
        sql_timeout=config.sql_timeout,
        log_level=config.log_level,
    )
    logging.getLogger(__name__).info(
        "Starting chartcoach MCP transport=%s host=%s port=%s release=%s tracing=%s",
        config.transport,
        config.host,
        config.port,
        catalog.release.digest if catalog.release else None,
        config.tracing,
    )
    if config.transport == "stdio":
        server.run()
    else:
        import uvicorn

        uvicorn.run(
            create_app(server, config=config),
            host=config.host,
            port=config.port,
            log_level=config.log_level.lower(),
        )


__all__ = [
    "MCPConfig",
    "create_app",
    "create_server",
    "load_config",
    "register_tools",
    "run",
]

"""Compose catalog tools, an MCP server, or an ASGI app independently of the CLI."""

from __future__ import annotations

import logging
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
    """
    settings = MCPConfig(profile=profile, sql_timeout=sql_timeout, log_level=log_level)
    server = MCPServer(
        "chartcoach",
        description="Inspect one source-traced Guideline Catalog.",
        instructions=(
            "Call describe first to inspect catalog identity, tables, vocabulary, and profiles. "
            "Use sql for compact discovery, then read selected guideline entry IDs and cite their sources. "
            "Example: SELECT id, title FROM guidelines ORDER BY id LIMIT 5"
        ),
        log_level=settings.log_level,
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
    """Open one catalog, compose its server, and run the selected transport."""
    logging.basicConfig(
        level=config.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
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
        "Starting chartcoach MCP transport=%s host=%s port=%s release=%s",
        config.transport,
        config.host,
        config.port,
        catalog.release.digest if catalog.release else None,
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

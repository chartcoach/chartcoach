from __future__ import annotations

import logging
from collections.abc import Callable
from os import PathLike
from typing import Literal

try:
    from mcp.server import FastMCP
    from mcp.types import ToolAnnotations
except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
    name = exc.name
    if name == "mcp" or (name is not None and name.startswith("mcp.")):
        exc.add_note("Install `chartcoach[mcp]` to use the chartcoach MCP server.")
    raise

from .catalog import open_catalog, open_index
from .tools import Tools, search_error

Transport = Literal["stdio", "sse", "streamable-http"]
Level = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

DEFAULT_TRANSPORT = "stdio"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL = "INFO"
TRANSPORT_CHOICES: tuple[Transport, ...] = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES: tuple[Level, ...] = (
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
)

logger = logging.getLogger(__name__)


def _transport(value: str) -> Transport:
    resolved_transport = value.lower()
    if resolved_transport not in TRANSPORT_CHOICES:
        choices = ", ".join(TRANSPORT_CHOICES)
        raise ValueError(
            f"Unsupported MCP transport {resolved_transport!r}. Expected one of: {choices}."
        )
    return resolved_transport


def _level(value: str) -> Level:
    resolved_log_level = value.upper()
    if resolved_log_level not in LOG_LEVEL_CHOICES:
        choices = ", ".join(LOG_LEVEL_CHOICES)
        raise ValueError(
            f"Unsupported MCP log level {resolved_log_level!r}. Expected one of: {choices}."
        )
    return resolved_log_level


def _configure_logging(log_level: Level) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


def _build_server(*, host: str, port: int, log_level: Level) -> FastMCP:
    return FastMCP(
        "chartcoach",
        json_response=True,
        host=host,
        port=port,
        log_level=log_level,
    )


def _add_tool(
    server: FastMCP,
    func: Callable[..., object],
    *,
    name: str,
    description: str,
    open_world: bool,
) -> None:
    server.add_tool(
        func,
        name=name,
        description=description,
        annotations=ToolAnnotations(
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=open_world,
        ),
    )


def _register_tools(
    server: FastMCP,
    *,
    tools: Tools,
    include_search: bool = False,
) -> None:
    _add_tool(
        server,
        tools.sql,
        name="sql",
        description="Run one read-only SQL query over catalog tables.",
        open_world=False,
    )
    if include_search:
        _add_tool(
            server,
            tools.search,
            name="search",
            description="Run LanceDB search over indexed catalog document rows.",
            open_world=True,
        )


def main(
    *,
    source: str | PathLike[str] | None = None,
    profile: str | None = None,
    transport: str = DEFAULT_TRANSPORT,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    log_level: str = DEFAULT_LOG_LEVEL,
) -> None:
    resolved_transport = _transport(transport)
    resolved_log_level = _level(log_level)
    if not 1 <= port <= 65535:
        raise ValueError("MCP port must be between 1 and 65535.")
    _configure_logging(resolved_log_level)

    catalog = open_catalog(source)

    logger.info(
        "Starting chartcoach MCP server with transport=%s host=%s port=%s",
        resolved_transport,
        host,
        port,
    )
    table = None
    if profile is not None:
        try:
            table = open_index(
                source,
                profile=profile,
            )
        except ModuleNotFoundError:
            raise
        except Exception as exc:
            raise ValueError(search_error(str(exc))) from exc
    server_tools = Tools(
        catalog,
        table=table,
        source=source,
        profile=profile,
    )
    server = _build_server(host=host, port=port, log_level=resolved_log_level)
    _register_tools(
        server,
        tools=server_tools,
        include_search=table is not None,
    )
    server.run(transport=resolved_transport)


__all__ = ["main"]

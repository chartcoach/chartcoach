from __future__ import annotations

import dataclasses as dc
import logging
import os
from collections.abc import Callable
from pathlib import Path
from typing import Literal, Protocol, TypedDict, Unpack, cast

try:
    from mcp.server import FastMCP
    from mcp.types import ToolAnnotations
except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
    name = exc.name
    if name == "mcp" or (name is not None and name.startswith("mcp.")):
        exc.add_note("Install `chartcoach[mcp]` to use the chartcoach MCP server.")
    raise

from .catalog.collection import Catalog
from .constants import INDEX_ENV, LANCE_DOCUMENT_TABLE, SOURCE_ENV
from .search import open as open_index
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


class Settings(TypedDict, total=False):
    source: str | Path
    index: str | Path
    table: str


@dc.dataclass(frozen=True)
class Runtime:
    transport: Transport = DEFAULT_TRANSPORT
    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT
    log_level: Level = DEFAULT_LOG_LEVEL


@dc.dataclass(frozen=True)
class Config:
    settings: Settings
    runtime: Runtime


class _AddToolKwargs(TypedDict):
    name: str
    description: str
    annotations: object


class _MCPSettings(Protocol):
    host: str
    port: int
    log_level: str


class _MCPServer(Protocol):
    settings: _MCPSettings

    def add_tool(
        self,
        tool: Callable[..., object],
        /,
        **kwargs: Unpack[_AddToolKwargs],
    ) -> None: ...

    def run(self, *, transport: str) -> None: ...


def configure(
    *,
    index: str | Path | None = None,
    table: str | None = None,
    source: str | Path | None = None,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> Config:
    return Config(
        settings=_settings(index=index, table=table, source=source),
        runtime=_runtime(
            transport=transport,
            host=host,
            port=port,
            log_level=log_level,
        ),
    )


def _settings(
    *,
    index: str | Path | None = None,
    table: str | None = None,
    source: str | Path | None = None,
) -> Settings:
    settings: Settings = {}
    if index is not None:
        settings["index"] = index
    elif raw_index := os.getenv(INDEX_ENV):
        settings["index"] = raw_index
    settings["table"] = table or LANCE_DOCUMENT_TABLE
    if source is not None:
        settings["source"] = source
    elif raw_source := os.getenv(SOURCE_ENV):
        settings["source"] = raw_source
    return settings


def _runtime(
    *,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> Runtime:
    resolved_transport = (
        transport or os.getenv("CHARTCOACH_MCP_TRANSPORT") or DEFAULT_TRANSPORT
    ).lower()
    if resolved_transport not in TRANSPORT_CHOICES:
        choices = ", ".join(TRANSPORT_CHOICES)
        raise ValueError(
            f"Unsupported MCP transport {resolved_transport!r}. Expected one of: {choices}."
        )

    raw_port = port if port is not None else os.getenv("CHARTCOACH_MCP_PORT")
    resolved_log_level = (
        log_level or os.getenv("CHARTCOACH_MCP_LOG_LEVEL") or DEFAULT_LOG_LEVEL
    ).upper()
    if resolved_log_level not in LOG_LEVEL_CHOICES:
        choices = ", ".join(LOG_LEVEL_CHOICES)
        raise ValueError(
            f"Unsupported MCP log level {resolved_log_level!r}. Expected one of: {choices}."
        )

    return Runtime(
        transport=cast(Transport, resolved_transport),
        host=host or os.getenv("CHARTCOACH_MCP_HOST") or DEFAULT_HOST,
        port=int(raw_port) if raw_port is not None else DEFAULT_PORT,
        log_level=cast(Level, resolved_log_level),
    )


def _configure_logging(log_level: Level) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


def _build_server(runtime: Runtime) -> _MCPServer:
    server = cast(_MCPServer, FastMCP("chartcoach", json_response=True))
    server.settings.host = runtime.host
    server.settings.port = runtime.port
    server.settings.log_level = runtime.log_level
    return server


def _add_tool(
    server: _MCPServer,
    func: Callable[..., object],
    *,
    name: str,
    description: str,
) -> None:
    server.add_tool(
        func,
        name=name,
        description=description,
        annotations=ToolAnnotations(
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=False,
        ),
    )


def _register_tools(
    server: _MCPServer,
    *,
    tools: Tools,
    include_search: bool = False,
) -> None:
    _add_tool(
        server,
        tools.sql,
        name="sql",
        description="Run one read-only SQL query over catalog tables.",
    )
    if include_search:
        _add_tool(
            server,
            tools.search,
            name="search",
            description="Run LanceDB search over indexed catalog document rows.",
        )


def main(
    *,
    settings: Settings | None = None,
    runtime: Runtime | None = None,
) -> None:
    requested_settings = settings or {}
    resolved_settings = _settings(
        index=requested_settings.get("index"),
        table=requested_settings.get("table"),
        source=requested_settings.get("source"),
    )
    resolved_runtime = runtime if runtime is not None else _runtime()
    _configure_logging(resolved_runtime.log_level)

    source = resolved_settings.get("source")

    logger.info(
        "Starting chartcoach MCP server with transport=%s host=%s port=%s",
        resolved_runtime.transport,
        resolved_runtime.host,
        resolved_runtime.port,
    )
    catalog = Catalog.open(source)
    index_path = resolved_settings.get("index")
    table = None
    if index_path is not None:
        try:
            table = open_index(
                index_path,
                table_name=resolved_settings.get("table", LANCE_DOCUMENT_TABLE),
            )
        except ModuleNotFoundError:
            raise
        except Exception as exc:
            raise ValueError(search_error(str(exc))) from exc
    server_tools = Tools(
        catalog,
        table=table,
        index_path=index_path,
    )
    server = _build_server(resolved_runtime)
    _register_tools(
        server,
        tools=server_tools,
        include_search=table is not None,
    )
    server.run(transport=resolved_runtime.transport)


__all__ = ["Config", "Runtime", "Settings", "configure", "main"]

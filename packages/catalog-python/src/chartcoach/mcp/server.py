from __future__ import annotations

import dataclasses as dc
import logging
import os
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Literal, Protocol, cast

from ..coach import Coach
from ..create import Settings, create

TransportName = Literal["stdio", "sse", "streamable-http"]
LogLevelName = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

DEFAULT_TRANSPORT = "stdio"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL = "INFO"

TRANSPORT_CHOICES: tuple[TransportName, ...] = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES: tuple[LogLevelName, ...] = (
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
)


@dc.dataclass(frozen=True)
class RuntimeConfig:
    """Network and logging options for the MCP server."""

    transport: TransportName = DEFAULT_TRANSPORT
    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT
    log_level: LogLevelName = DEFAULT_LOG_LEVEL


logger = logging.getLogger(__name__)


class _MCPSettings(Protocol):
    host: str
    port: int
    log_level: str
    transport_security: Any | None


class _MCPServer(Protocol):
    settings: _MCPSettings

    def add_tool(self, tool: Any, /) -> None: ...

    def run(self, *, transport: str) -> None: ...


def _is_missing_mcp_dependency(exc: ModuleNotFoundError) -> bool:
    name = exc.name
    return name == "mcp" or (name is not None and name.startswith("mcp."))


def _load_fast_mcp() -> Callable[..., _MCPServer]:
    """Load the optional MCP dependency lazily so static analysis stays install-agnostic."""

    try:
        return cast(Callable[..., _MCPServer], import_module("mcp.server").FastMCP)
    except ModuleNotFoundError as exc:
        if _is_missing_mcp_dependency(exc):
            exc.add_note("Install `chartcoach[mcp]` to use the ChartCoach MCP server.")
        raise


def _resolve_settings(
    *,
    cache_dir: str | Path | None = None,
    catalog: str | None = None,
) -> Settings:
    settings: Settings = {}
    if cache_dir is not None:
        settings["cache_dir"] = Path(cache_dir)
    if catalog is not None:
        settings["catalog"] = catalog
    return settings


def _resolve_runtime(
    *,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> RuntimeConfig:
    resolved_transport = (
        transport or os.getenv("MCP_TRANSPORT") or DEFAULT_TRANSPORT
    ).lower()
    if resolved_transport not in TRANSPORT_CHOICES:
        choices = ", ".join(TRANSPORT_CHOICES)
        raise ValueError(
            f"Unsupported MCP transport {resolved_transport!r}. Expected one of: {choices}."
        )

    resolved_host = host or os.getenv("MCP_HOST") or DEFAULT_HOST

    raw_port = port if port is not None else os.getenv("MCP_PORT")
    resolved_port = int(raw_port) if raw_port is not None else DEFAULT_PORT

    resolved_log_level = (
        log_level or os.getenv("MCP_LOG_LEVEL") or DEFAULT_LOG_LEVEL
    ).upper()
    if resolved_log_level not in LOG_LEVEL_CHOICES:
        choices = ", ".join(LOG_LEVEL_CHOICES)
        raise ValueError(
            f"Unsupported MCP log level {resolved_log_level!r}. Expected one of: {choices}."
        )

    return RuntimeConfig(
        transport=cast(TransportName, resolved_transport),
        host=resolved_host,
        port=resolved_port,
        log_level=cast(LogLevelName, resolved_log_level),
    )


def _configure_logging(log_level: LogLevelName) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


def _build_server(coach: Coach, runtime: RuntimeConfig) -> _MCPServer:
    server = _load_fast_mcp()("chartcoach", json_response=True)
    server.settings.host = runtime.host
    server.settings.port = runtime.port
    server.settings.log_level = runtime.log_level
    server.settings.transport_security = None

    tools = coach.tools
    server.add_tool(tools.sql)
    server.add_tool(tools.search)
    server.add_tool(tools.get)
    return server


def main(
    *,
    settings: Settings | None = None,
    runtime: RuntimeConfig | None = None,
) -> None:
    """Create a coach and serve its tools over MCP."""

    resolved_settings = settings or {}
    resolved_runtime = runtime if runtime is not None else _resolve_runtime()
    _configure_logging(resolved_runtime.log_level)

    try:
        logger.info(
            "Starting ChartCoach MCP server with transport=%s host=%s port=%s",
            resolved_runtime.transport,
            resolved_runtime.host,
            resolved_runtime.port,
        )
        coach = create(**resolved_settings)
        server = _build_server(coach, resolved_runtime)
        server.run(transport=resolved_runtime.transport)
    except Exception:
        logger.exception("ChartCoach MCP startup failed")
        raise


__all__ = ["RuntimeConfig", "main"]

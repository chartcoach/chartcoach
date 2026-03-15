from __future__ import annotations

import logging
import os
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Literal, cast

from mcp.server import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from ..coach import ChartCoach, ChartCoachConfig

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
LOCALHOST_HOSTS = {"127.0.0.1", "localhost", "::1"}


@dataclass(frozen=True)
class RuntimeConfig:
    transport: TransportName = DEFAULT_TRANSPORT
    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT
    log_level: LogLevelName = DEFAULT_LOG_LEVEL


mcp = FastMCP("chartcoach", json_response=True)
_coach: ChartCoach | None = None
_resolved_config: ChartCoachConfig | None = None
logger = logging.getLogger(__name__)


def _config() -> ChartCoachConfig:
    global _resolved_config
    if _resolved_config is None:
        _resolved_config = ChartCoachConfig.from_env()
    return _resolved_config


def _set_config(config: ChartCoachConfig) -> None:
    global _resolved_config
    _resolved_config = config


def _coach_from_cache() -> ChartCoach:
    global _coach
    if _coach is None:
        _coach = ChartCoach.from_cache(config=_config())
    return _coach


def _reset_cached_state() -> None:
    global _coach, _resolved_config
    _coach = None
    _resolved_config = None


def _resolve_config(
    *,
    cache_dir: str | Path | None = None,
    collection_name: str | None = None,
    catalog_uri: str | None = None,
) -> ChartCoachConfig:
    config = ChartCoachConfig.from_env()
    overrides: dict[str, str | Path] = {}

    if cache_dir is not None:
        overrides["cache_dir"] = Path(cache_dir)
    if collection_name is not None:
        overrides["collection_name"] = collection_name
    if catalog_uri is not None:
        overrides["catalog_uri"] = catalog_uri

    return replace(config, **overrides) if overrides else config


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


def _transport_security_for_host(host: str) -> TransportSecuritySettings | None:
    if host not in LOCALHOST_HOSTS:
        return None

    return TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=["127.0.0.1:*", "localhost:*", "[::1]:*"],
        allowed_origins=["http://127.0.0.1:*", "http://localhost:*", "http://[::1]:*"],
    )


def _configure_logging(log_level: LogLevelName) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


@mcp.tool()
def duckdb_query(sql: str, row_limit: int | None = None) -> dict[str, Any]:
    """Run one read-only DuckDB statement against the persisted catalog relations."""
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .duckdb_query(
            sql,
            row_limit=row_limit,
        )
    )


@mcp.tool()
def chroma_query(
    query_texts: list[str],
    n_results: int | None = None,
    where: dict[str, Any] | None = None,
    where_document: dict[str, Any] | None = None,
    include: list[str] | None = None,
) -> dict[str, Any]:
    """Run semantic search over the ChartCoach Chroma collection."""
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .chroma_query(
            query_texts,
            n_results=n_results,
            where=where,
            where_document=where_document,
            include=include,
        )
    )


@mcp.tool()
def chroma_get(
    ids: list[str] | None = None,
    where: dict[str, Any] | None = None,
    where_document: dict[str, Any] | None = None,
    include: list[str] | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> dict[str, Any]:
    """Fetch Chroma documents directly by id or metadata filter."""
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .chroma_get(
            ids=ids,
            where=where,
            where_document=where_document,
            include=include,
            limit=limit,
            offset=offset,
        )
    )


def main(
    *,
    cache_dir: str | Path | None = None,
    collection_name: str | None = None,
    catalog_uri: str | None = None,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> None:
    """Ensure frozen artifacts exist, then run the ChartCoach MCP server."""
    global _coach

    _reset_cached_state()
    config = _resolve_config(
        cache_dir=cache_dir,
        collection_name=collection_name,
        catalog_uri=catalog_uri,
    )
    runtime = _resolve_runtime(
        transport=transport,
        host=host,
        port=port,
        log_level=log_level,
    )
    _set_config(config)

    mcp.settings.host = runtime.host
    mcp.settings.port = runtime.port
    mcp.settings.log_level = runtime.log_level
    mcp.settings.transport_security = _transport_security_for_host(runtime.host)
    _configure_logging(runtime.log_level)

    try:
        logger.info(
            "Starting ChartCoach MCP server with cache_dir=%s collection_name=%s catalog_uri=%s transport=%s host=%s port=%s",
            config.cache_dir,
            config.collection_name,
            config.catalog_uri,
            runtime.transport,
            runtime.host,
            runtime.port,
        )

        logger.info("Ensuring ChartCoach cache artifacts exist before server start")
        ChartCoach.ensure_cache(config=config)

        logger.info("Loading ChartCoach cache-backed runtime")
        _coach = ChartCoach.from_cache(config=config)

        logger.info("Loading cached ChartCoach index into memory")
        _coach.load_index()

        logger.info("ChartCoach MCP startup complete; entering FastMCP run loop")
        mcp.run(transport=runtime.transport)
    except Exception:
        logger.exception("ChartCoach MCP startup failed")
        raise

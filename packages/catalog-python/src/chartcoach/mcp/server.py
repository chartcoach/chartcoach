from __future__ import annotations

import dataclasses as dc
import logging
import os
from collections.abc import Sequence
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Literal, Protocol, TypedDict, cast

from ..catalog.collection import Catalog
from ..tools.catalog import CatalogTools, format_tool_error
from ..constants import CACHE_DIR_ENV, CATALOG_PATH_ENV
from ..search.chroma import CacheMode
from ..search.registry import ToolSafety, ToolSpec, tool_specs
from ..search.session import SearchSession, open_search_session
from ..search.sql import connect_catalog
from ..search.sql_tools import SqlTools
from ..search.tools import DocumentFilter, IncludeFields, MetadataFilter, QueryInput

TransportName = Literal["stdio", "sse", "streamable-http"]
LogLevelName = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

DEFAULT_TRANSPORT = "stdio"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_CACHE_MODE: CacheMode = "reuse_only"

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


@dc.dataclass(frozen=True)
class MCPConfig:
    """Resolved MCP startup configuration."""

    settings: SearchSettings
    runtime: RuntimeConfig


logger = logging.getLogger(__name__)


class SearchSettings(TypedDict, total=False):
    catalog: str | Path
    cache_dir: str | Path
    cache_mode: CacheMode


class _MCPSettings(Protocol):
    host: str
    port: int
    log_level: str


class _MCPServer(Protocol):
    settings: _MCPSettings

    def add_tool(self, tool: Any, /, **kwargs: Any) -> None: ...

    def run(self, *, transport: str) -> None: ...


class _CatalogSqlTools:
    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog
        self._conn: Any | None = None
        self._tools: SqlTools | None = None

    @property
    def tools(self) -> SqlTools:
        if self._tools is None:
            self._conn = connect_catalog(self._catalog)
            self._tools = SqlTools(self._conn)
        return self._tools

    def sql(self, sql: str, *, row_limit: int | None = None) -> dict[str, Any]:
        """Run DuckDB SQL against the prepared catalog tables."""

        return self.tools.sql(sql, row_limit=row_limit)

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None
            self._tools = None


class _LazySearchTools:
    def __init__(
        self,
        catalog: Catalog,
        *,
        cache_dir: str | Path | None,
        cache_mode: CacheMode,
    ) -> None:
        self._catalog = catalog
        self._cache_dir = cache_dir
        self._cache_mode = cache_mode
        self._session: SearchSession | None = None

    @property
    def session(self) -> SearchSession:
        if self._session is None:
            self._session = open_search_session(
                self._catalog,
                cache_dir=self._cache_dir,
                cache_mode=self._cache_mode,
                cache_embeddings=False,
            )
        return self._session

    def search(
        self,
        query_texts: QueryInput,
        *,
        limit: int | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
    ) -> dict[str, Any]:
        """Semantically search the indexed catalog documents."""

        return self.session.tools.search(
            query_texts,
            limit=limit,
            where=where,
            where_document=where_document,
            include=include,
        )

    def search_guidelines(
        self,
        query_text: str,
        *,
        limit: int | None = None,
        roles: Sequence[str] | None = None,
        labels: Sequence[str] | None = None,
        label_prefixes: Sequence[str] | None = None,
        candidate_limit: int | None = None,
    ) -> dict[str, Any]:
        """Semantically search and return deduplicated guideline-level rows."""

        return self.session.tools.search_guidelines(
            query_text,
            limit=limit,
            roles=roles,
            labels=labels,
            label_prefixes=label_prefixes,
            candidate_limit=candidate_limit,
        )

    def get(
        self,
        *,
        ids: list[str] | None = None,
        where: MetadataFilter | None = None,
        where_document: DocumentFilter | None = None,
        include: IncludeFields | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch exact indexed documents by id or exact metadata filter."""

        return self.session.tools.get(
            ids=ids,
            where=where,
            where_document=where_document,
            include=include,
            limit=limit,
            offset=offset,
        )

    def close(self) -> None:
        if self._session is not None:
            self._session.close()
            self._session = None


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
    cache_mode: str | None = None,
) -> SearchSettings:
    settings: SearchSettings = {}
    if cache_dir is not None:
        settings["cache_dir"] = Path(cache_dir)
    elif raw_cache_dir := os.getenv(CACHE_DIR_ENV):
        settings["cache_dir"] = raw_cache_dir
    if catalog is not None:
        settings["catalog"] = catalog
    elif raw_catalog := os.getenv(CATALOG_PATH_ENV):
        settings["catalog"] = raw_catalog
    raw_cache_mode = (
        cache_mode or os.getenv("CHARTCOACH_CACHE_MODE") or DEFAULT_CACHE_MODE
    )
    if raw_cache_mode != DEFAULT_CACHE_MODE:
        raise ValueError(
            format_tool_error(
                f"Unsupported MCP cache mode {raw_cache_mode!r}.",
                [
                    "The MCP server only supports --cache-mode reuse_only so tool calls do not create or rebuild cache state.",
                    "Build or refresh the cache outside the server with the catalog search CLI.",
                ],
            )
        )
    settings["cache_mode"] = cast(CacheMode, raw_cache_mode)
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


def resolve_config(
    *,
    cache_dir: str | Path | None = None,
    catalog: str | None = None,
    cache_mode: str | None = None,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> MCPConfig:
    """Resolve environment and CLI options into MCP startup config."""

    return MCPConfig(
        settings=_resolve_settings(
            cache_dir=cache_dir,
            catalog=catalog,
            cache_mode=cache_mode,
        ),
        runtime=_resolve_runtime(
            transport=transport,
            host=host,
            port=port,
            log_level=log_level,
        ),
    )


def _configure_logging(log_level: LogLevelName) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


def _build_server(specs: tuple[ToolSpec, ...], runtime: RuntimeConfig) -> _MCPServer:
    server = _load_fast_mcp()("chartcoach", json_response=True)
    server.settings.host = runtime.host
    server.settings.port = runtime.port
    server.settings.log_level = runtime.log_level

    for spec in specs:
        server.add_tool(spec.func, annotations=_tool_annotations(spec.safety))
    return server


def _tool_annotations(safety: ToolSafety) -> Any:
    annotations = import_module("mcp.types").ToolAnnotations
    return annotations(
        readOnlyHint=safety.read_only,
        destructiveHint=safety.destructive,
        idempotentHint=safety.idempotent,
        openWorldHint=safety.open_world,
    )


def main(
    *,
    settings: SearchSettings | None = None,
    runtime: RuntimeConfig | None = None,
) -> None:
    """Create a search session and serve its tools over MCP."""

    resolved_settings = settings or {}
    resolved_runtime = runtime if runtime is not None else _resolve_runtime()
    _configure_logging(resolved_runtime.log_level)

    logger.info(
        "Starting ChartCoach MCP server with transport=%s host=%s port=%s",
        resolved_runtime.transport,
        resolved_runtime.host,
        resolved_runtime.port,
    )
    catalog = resolved_settings.get("catalog")
    if catalog is None:
        raise ValueError(
            format_tool_error(
                f"catalog must be provided with --catalog-path or {CATALOG_PATH_ENV}.",
                [
                    "Pass --catalog-path guidelines/catalog.parquet.",
                    f"Or export {CATALOG_PATH_ENV}=guidelines/catalog.parquet.",
                ],
            )
        )
    catalog_obj = Catalog.from_parquet(catalog)
    sql_tools = _CatalogSqlTools(catalog_obj)
    search_tools = _LazySearchTools(
        catalog_obj,
        cache_dir=resolved_settings.get("cache_dir"),
        cache_mode=resolved_settings.get("cache_mode", DEFAULT_CACHE_MODE),
    )
    specs = tool_specs(
        catalog_tools=CatalogTools(catalog_obj),
        sql_tools=sql_tools,
        search_tools=search_tools,
    )
    server = _build_server(specs, resolved_runtime)
    try:
        server.run(transport=resolved_runtime.transport)
    finally:
        sql_tools.close()
        search_tools.close()


__all__ = ["MCPConfig", "RuntimeConfig", "SearchSettings", "main", "resolve_config"]

from __future__ import annotations

import dataclasses as dc
import logging
import os
from collections.abc import Callable, Mapping
from importlib import import_module
from pathlib import Path
from typing import Any, Literal, Protocol, TypedDict, cast

from ..artifacts import catalog_artifact_rows
from ..catalog.collection import Catalog
from ..constants import INDEX_DIR_ENV, SOURCE_ENV
from ..paths import default_index_dir
from ..search.chroma import CacheMode, ChromaIndex
from ..search.guidelines import search_guidelines
from ..tools.catalog import CatalogTools, format_tool_error

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

logger = logging.getLogger(__name__)


@dc.dataclass(frozen=True)
class RuntimeConfig:
    transport: TransportName = DEFAULT_TRANSPORT
    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT
    log_level: LogLevelName = DEFAULT_LOG_LEVEL


@dc.dataclass(frozen=True)
class MCPConfig:
    settings: SearchSettings
    runtime: RuntimeConfig


class SearchSettings(TypedDict, total=False):
    source: str | Path
    index_dir: str | Path


class _MCPSettings(Protocol):
    host: str
    port: int
    log_level: str


class _MCPServer(Protocol):
    settings: _MCPSettings

    def add_tool(self, tool: Any, /, **kwargs: Any) -> None: ...

    def run(self, *, transport: str) -> None: ...


class _SearchTools(Protocol):
    def search_guidelines(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...

    def chroma_query(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...

    def chroma_get(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...


class _ArtifactTools:
    def __init__(
        self,
        catalog: Catalog,
        *,
        source: str | Path,
        index_dir: str | Path,
    ) -> None:
        self._catalog = catalog
        self._source = source
        self._index_dir = index_dir

    def catalog_artifacts(self) -> dict[str, Any]:
        rows = catalog_artifact_rows(
            self._catalog,
            source_path=self._source,
            index_dir=self._index_dir,
        )
        return {"rows": rows, "row_count": len(rows)}


class _ChromaTools:
    def __init__(
        self,
        catalog: Catalog,
        *,
        cache_dir: str | Path,
        cache_mode: CacheMode,
    ) -> None:
        self._catalog = catalog
        self._cache_dir = cache_dir
        self._cache_mode = cache_mode
        self._index: ChromaIndex | None = None

    def open_index(self) -> ChromaIndex:
        if self._index is None:
            self._index = ChromaIndex.from_cache(
                self._catalog,
                cache_dir=self._cache_dir,
                cache_mode=self._cache_mode,
            )
        return self._index

    def search_guidelines(
        self,
        query_text: str,
        *,
        limit: int | None = None,
        candidate_limit: int | None = None,
        where: dict[str, Any] | None = None,
        where_document: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        kwargs: dict[str, Any] = {}
        if limit is not None:
            kwargs["limit"] = limit
        if candidate_limit is not None:
            kwargs["candidate_limit"] = candidate_limit
        result = search_guidelines(
            self.open_index(),
            query_text,
            where=where,
            where_document=where_document,
            **kwargs,
        )
        return result.to_dict()

    def chroma_query(
        self,
        query_embeddings: Any | None = None,
        query_texts: Any | None = None,
        query_images: Any | None = None,
        query_uris: Any | None = None,
        ids: Any | None = None,
        n_results: int = 10,
        where: dict[str, Any] | None = None,
        where_document: dict[str, Any] | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        """Run collection.query with Chroma parameters."""

        params = _non_null_params(
            {
                "query_embeddings": query_embeddings,
                "query_texts": query_texts,
                "query_images": query_images,
                "query_uris": query_uris,
                "ids": ids,
                "n_results": n_results,
                "where": where,
                "where_document": where_document,
                "include": include,
            }
        )
        return cast(
            dict[str, Any],
            self.open_index().collection.query(**params),
        )

    def chroma_get(
        self,
        ids: Any | None = None,
        where: dict[str, Any] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        where_document: dict[str, Any] | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        """Run collection.get with Chroma parameters."""

        params = _non_null_params(
            {
                "ids": ids,
                "where": where,
                "limit": limit,
                "offset": offset,
                "where_document": where_document,
                "include": include,
            }
        )
        return cast(
            dict[str, Any],
            self.open_index().collection.get(**params),
        )

    def close(self) -> None:
        self._index = None


def _is_missing_mcp_dependency(exc: ModuleNotFoundError) -> bool:
    name = exc.name
    return name == "mcp" or (name is not None and name.startswith("mcp."))


def _non_null_params(params: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in params.items() if value is not None}


def _load_fast_mcp() -> Callable[..., _MCPServer]:
    try:
        return cast(Callable[..., _MCPServer], import_module("mcp.server").FastMCP)
    except ModuleNotFoundError as exc:
        if _is_missing_mcp_dependency(exc):
            exc.add_note("Install `chartcoach[mcp]` to use the ChartCoach MCP server.")
        raise


def _resolve_settings(
    *,
    index_dir: str | Path | None = None,
    source: str | Path | None = None,
) -> SearchSettings:
    settings: SearchSettings = {}
    if index_dir is not None:
        settings["index_dir"] = Path(index_dir)
    elif raw_index_dir := os.getenv(INDEX_DIR_ENV):
        settings["index_dir"] = raw_index_dir
    else:
        settings["index_dir"] = default_index_dir()
    if source is not None:
        settings["source"] = source
    elif raw_source := os.getenv(SOURCE_ENV):
        settings["source"] = raw_source
    return settings


def _resolve_runtime(
    *,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> RuntimeConfig:
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

    return RuntimeConfig(
        transport=cast(TransportName, resolved_transport),
        host=host or os.getenv("CHARTCOACH_MCP_HOST") or DEFAULT_HOST,
        port=int(raw_port) if raw_port is not None else DEFAULT_PORT,
        log_level=cast(LogLevelName, resolved_log_level),
    )


def resolve_config(
    *,
    index_dir: str | Path | None = None,
    source: str | Path | None = None,
    transport: str | None = None,
    host: str | None = None,
    port: int | None = None,
    log_level: str | None = None,
) -> MCPConfig:
    return MCPConfig(
        settings=_resolve_settings(index_dir=index_dir, source=source),
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


def _load_source(source: str | Path) -> Catalog:
    path = Path(source)
    if path.is_dir():
        return Catalog.from_folder(path)
    return Catalog.from_parquet(path)


def _build_server(runtime: RuntimeConfig) -> _MCPServer:
    server = _load_fast_mcp()("chartcoach", json_response=True)
    server.settings.host = runtime.host
    server.settings.port = runtime.port
    server.settings.log_level = runtime.log_level
    return server


def _add_tool(
    server: _MCPServer,
    func: Callable[..., Any],
    *,
    name: str,
    description: str,
) -> None:
    annotations = import_module("mcp.types").ToolAnnotations
    server.add_tool(
        func,
        name=name,
        description=description,
        annotations=annotations(
            readOnlyHint=True,
            destructiveHint=False,
            idempotentHint=True,
            openWorldHint=False,
        ),
    )


def _register_tools(
    server: _MCPServer,
    *,
    catalog_tools: CatalogTools,
    artifact_tools: _ArtifactTools,
    search: _SearchTools,
) -> None:
    _add_tool(
        server,
        artifact_tools.catalog_artifacts,
        name="catalog_artifacts",
        description="List native catalog, DuckDB, and Chroma artifact paths.",
    )
    _add_tool(
        server,
        catalog_tools.list_tables,
        name="tables_list",
        description="List queryable structured catalog tables and row counts.",
    )
    _add_tool(
        server,
        catalog_tools.describe_tables,
        name="tables_schema",
        description="List columns for structured catalog tables.",
    )
    _add_tool(
        server,
        catalog_tools.count_values,
        name="tables_values",
        description="Count distinct values in a structured catalog table column.",
    )
    _add_tool(
        server,
        catalog_tools.list_guidelines,
        name="guidelines_list",
        description="List guideline ids and summaries with deterministic filters.",
    )
    _add_tool(
        server,
        catalog_tools.get_guideline,
        name="guidelines_get",
        description="Return one complete guideline entry by id.",
    )
    _add_tool(
        server,
        catalog_tools.retrieve_guidelines,
        name="guidelines_retrieve",
        description="Return guideline records with optional label and section filters.",
    )
    _add_tool(
        server,
        search.search_guidelines,
        name="guidelines_search",
        description="Guideline-level semantic search over the Chroma artifact.",
    )
    _add_tool(
        server,
        search.chroma_query,
        name="chroma_query",
        description="Run native Chroma query against the catalog collection.",
    )
    _add_tool(
        server,
        search.chroma_get,
        name="chroma_get",
        description="Run native Chroma get against the catalog collection.",
    )


def main(
    *,
    settings: SearchSettings | None = None,
    runtime: RuntimeConfig | None = None,
) -> None:
    requested_settings = settings or {}
    resolved_settings = _resolve_settings(
        index_dir=requested_settings.get("index_dir"),
        source=requested_settings.get("source"),
    )
    resolved_runtime = runtime if runtime is not None else _resolve_runtime()
    _configure_logging(resolved_runtime.log_level)

    source = resolved_settings.get("source")
    if source is None:
        raise ValueError(
            format_tool_error(
                f"source must be provided with --source or {SOURCE_ENV}.",
                [
                    "Pass --source PATH.",
                    f"Or export {SOURCE_ENV}=PATH.",
                ],
            )
        )

    index_dir = resolved_settings["index_dir"]
    logger.info(
        "Starting ChartCoach MCP server with transport=%s host=%s port=%s",
        resolved_runtime.transport,
        resolved_runtime.host,
        resolved_runtime.port,
    )
    catalog_obj = _load_source(source)
    search = _ChromaTools(
        catalog_obj,
        cache_dir=index_dir,
        cache_mode=DEFAULT_CACHE_MODE,
    )
    server = _build_server(resolved_runtime)
    _register_tools(
        server,
        catalog_tools=CatalogTools(catalog_obj),
        artifact_tools=_ArtifactTools(
            catalog_obj,
            source=source,
            index_dir=index_dir,
        ),
        search=search,
    )
    try:
        server.run(transport=resolved_runtime.transport)
    finally:
        search.close()


__all__ = ["MCPConfig", "RuntimeConfig", "SearchSettings", "main", "resolve_config"]

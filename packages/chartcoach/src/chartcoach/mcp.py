from __future__ import annotations

import json
import logging
from collections.abc import Callable
from pathlib import Path
from typing import Annotated, Literal

try:
    from mcp.server import MCPServer
    from mcp.types import CallToolResult, TextContent, ToolAnnotations
    from pydantic import BaseModel, ConfigDict, Field, RootModel
except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
    name = exc.name
    if name == "mcp" or (name is not None and name.startswith("mcp.")):
        add_note = getattr(exc, "add_note", None)
        if callable(add_note):
            add_note("Install `chartcoach[mcp]` to use the chartcoach MCP server.")
    raise

from .catalog import Catalog, SourceDetail, open_catalog
from .catalog.embedding import apply_embedding_variables
from .catalog.errors import CatalogError, CatalogResponseTooLargeError
from .catalog.identity import catalog_identity
from .constants import DEFAULT_GUIDELINE_URL_TEMPLATE

Transport = Literal["stdio", "sse", "streamable-http"]
Level = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

DEFAULT_TRANSPORT = "stdio"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL = "INFO"
MAX_STRUCTURED_RESPONSE_BYTES = 65_536
TRANSPORT_CHOICES: tuple[Transport, ...] = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES: tuple[Level, ...] = (
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
)

McpLimit = Annotated[int, Field(ge=1, le=100, strict=True)]
McpId = Annotated[str, Field(min_length=1)]
McpIds = Annotated[list[McpId], Field(min_length=1, max_length=100)]
McpRoles = Annotated[list[McpId], Field(max_length=100)]

logger = logging.getLogger(__name__)


class _ResultModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class TableColumnInfo(_ResultModel):
    name: str
    type: str


class TableInfo(_ResultModel):
    name: str
    rows: int
    columns: list[TableColumnInfo]


class VocabularyInfo(_ResultModel):
    name: str
    description: str
    examples: list[str]


class ProfileInfo(_ResultModel):
    name: str
    profile_schema_version: int
    documents_version: int
    embedding_functions: list[dict[str, object]]
    dimensions: int
    distance_metric: Literal["cosine", "l2", "dot"]
    python_requirements: dict[str, str]
    lancedb_version: str
    projection: dict[str, object] | None


class DescribeToolResult(_ResultModel):
    resolved_location: str | None
    release_digest: str | None
    entries_digest: str
    manifest_digest: str
    tables: list[TableInfo]
    section_roles: list[VocabularyInfo]
    label_families: list[VocabularyInfo]
    profiles: list[str]
    profile: ProfileInfo | None


class SqlColumn(_ResultModel):
    name: str
    type: str


class SqlToolResult(_ResultModel):
    columns: list[SqlColumn]
    rows: list[dict[str, object]]
    row_count: int
    truncated: bool
    limit: int
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class SectionRecord(_ResultModel):
    role: str
    title: str
    content: str


class SourceRecord(_ResultModel):
    reference_id: str
    authors_text: str | None = None
    year: str | None = None
    source_title: str | None = None
    doi: str | None = None
    url: str | None = None
    guideline_id: str | None = None
    source_type: str | None = None
    authors: list[str] | None = None
    journal: str | None = None
    booktitle: str | None = None
    publisher: str | None = None


class GuidelineEntryRecord(_ResultModel):
    id: str
    title: str
    description: str
    labels: list[str]
    sections: list[SectionRecord]
    sources: list[SourceRecord]
    references: list[str] | None = None


class CitationSource(_ResultModel):
    reference_id: str
    source_type: str | None
    authors_text: str | None
    year: str | None
    source_title: str | None
    journal: str | None
    booktitle: str | None
    publisher: str | None
    doi: str | None
    url: str | None
    citation: str


class CitationRecord(_ResultModel):
    id: str
    title: str
    url: str
    guideline_citation: str
    sources: list[CitationSource]


class ReadToolResult(_ResultModel):
    records: list[GuidelineEntryRecord]
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class CiteToolResult(_ResultModel):
    records: list[CitationRecord]
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class GuidelineMatch(_ResultModel):
    rank: int
    id: str
    title: str
    description: str
    labels: list[str]
    matched_document_id: str
    matched_role: str
    matched_excerpt: str
    excerpt_truncated: bool
    score: float | None
    score_kind: Literal["distance", "relevance"]


class SearchToolResult(_ResultModel):
    query: str
    profile: str
    mode: Literal["fts", "vector", "hybrid"]
    score_kind: Literal["distance", "relevance"]
    matches: list[GuidelineMatch]
    match_count: int
    documents_considered: int
    documents_truncated: bool
    limit: int
    where: str | None
    resolved_location: str | None
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class ErrorBody(_ResultModel):
    code: Literal[
        "lookup",
        "invalid_input",
        "integrity",
        "unavailable_capability",
        "incompatible_profile",
        "embedding_failure",
        "response_too_large",
    ]
    message: str
    details: dict[str, object]


class ErrorToolResult(_ResultModel):
    error: ErrorBody


class DescribeOutput(RootModel[DescribeToolResult | ErrorToolResult]):
    pass


class SqlOutput(RootModel[SqlToolResult | ErrorToolResult]):
    pass


class ReadOutput(RootModel[ReadToolResult | ErrorToolResult]):
    pass


class CiteOutput(RootModel[CiteToolResult | ErrorToolResult]):
    pass


class SearchOutput(RootModel[SearchToolResult | ErrorToolResult]):
    pass


DescribeCallResult = Annotated[CallToolResult, DescribeOutput]
SqlCallResult = Annotated[CallToolResult, SqlOutput]
ReadCallResult = Annotated[CallToolResult, ReadOutput]
CiteCallResult = Annotated[CallToolResult, CiteOutput]
SearchCallResult = Annotated[CallToolResult, SearchOutput]


def _transport(value: str) -> Transport:
    resolved = value.lower()
    if resolved not in TRANSPORT_CHOICES:
        choices = ", ".join(TRANSPORT_CHOICES)
        raise ValueError(
            f"Unsupported MCP transport {resolved!r}. Expected: {choices}."
        )
    return resolved


def _level(value: str) -> Level:
    resolved = value.upper()
    if resolved not in LOG_LEVEL_CHOICES:
        choices = ", ".join(LOG_LEVEL_CHOICES)
        raise ValueError(
            f"Unsupported MCP log level {resolved!r}. Expected: {choices}."
        )
    return resolved


def _configure_logging(log_level: Level) -> None:
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().setLevel(getattr(logging, log_level))


def _build_server(*, log_level: Level) -> MCPServer:
    return MCPServer(
        "chartcoach",
        description="Inspect one source-traced Guideline Catalog.",
        instructions=(
            "Call describe first to inspect catalog identity, tables, vocabulary, and profiles. "
            "Use sql for compact discovery, then read selected guideline entry IDs and cite their sources. "
            "Example: SELECT id, title FROM guidelines ORDER BY id LIMIT 5"
        ),
        log_level=log_level,
    )


def _add_tool(
    server: MCPServer,
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
            read_only_hint=True,
            destructive_hint=False,
            idempotent_hint=True,
            open_world_hint=open_world,
        ),
    )


def _register_tools(
    server: MCPServer,
    *,
    catalog: Catalog,
    profile: str | None = None,
    embedding_vars: Path | None = None,
) -> None:
    search_profile = profile
    embedding_variables_loaded = False

    def describe(profile: str | None = None) -> DescribeCallResult:
        try:
            return _success(
                catalog.describe(profile=profile),
                DescribeToolResult,
                "Returned catalog description.",
            )
        except CatalogError as exc:
            return _failure(exc)

    def sql(statement: str, *, limit: McpLimit = 100) -> SqlCallResult:
        try:
            return _success(
                catalog.sql(statement, limit=limit),
                SqlToolResult,
                "Returned bounded SQL rows.",
            )
        except CatalogError as exc:
            return _failure(exc)

    def read(
        ids: McpIds,
        *,
        roles: McpRoles | None = None,
        source_detail: SourceDetail = "minimal",
    ) -> ReadCallResult:
        try:
            return _success(
                {
                    "records": catalog.read(
                        ids=ids, roles=roles or (), source_detail=source_detail
                    ),
                    **catalog_identity(catalog),
                },
                ReadToolResult,
                "Returned complete guideline entry records.",
            )
        except CatalogError as exc:
            return _failure(exc)

    def cite(
        ids: McpIds,
        *,
        url_template: str = DEFAULT_GUIDELINE_URL_TEMPLATE,
    ) -> CiteCallResult:
        try:
            return _success(
                {
                    "records": catalog.cite(ids=ids, url_template=url_template),
                    **catalog_identity(catalog),
                },
                CiteToolResult,
                "Returned guideline and source citations.",
            )
        except CatalogError as exc:
            return _failure(exc)

    _add_tool(
        server,
        describe,
        name="describe",
        description="Describe the catalog identity, tables, vocabulary, and index profiles.",
        open_world=False,
    )
    _add_tool(
        server,
        sql,
        name="sql",
        description=(
            "Run one read-only SELECT over the catalog tables. Returns typed columns, bounded rows, "
            "truncation state, and catalog identity. Inspect table columns with describe."
        ),
        open_world=False,
    )
    _add_tool(
        server,
        read,
        name="read",
        description="Read 1 through 100 exact guideline entry IDs with complete selected sections and source metadata.",
        open_world=False,
    )
    _add_tool(
        server,
        cite,
        name="cite",
        description="Return public guideline links and source citations for 1 through 100 exact guideline entry IDs.",
        open_world=False,
    )

    if search_profile is not None:

        def search(
            text: McpId,
            *,
            limit: McpLimit = 10,
            where: str | None = None,
            mode: Literal["fts", "vector", "hybrid"] = "fts",
        ) -> SearchCallResult:
            nonlocal embedding_variables_loaded
            try:
                if (
                    mode != "fts"
                    and embedding_vars is not None
                    and not embedding_variables_loaded
                ):
                    apply_embedding_variables(embedding_vars)
                    embedding_variables_loaded = True
                return _success(
                    catalog.search(
                        text,
                        profile=search_profile,
                        mode=mode,
                        limit=limit,
                        where=where,
                    ),
                    SearchToolResult,
                    "Returned ranked guideline matches.",
                )
            except CatalogError as exc:
                return _failure(exc)

        _add_tool(
            server,
            search,
            name="search",
            description=(
                "Search the startup index profile. FTS returns relevance scores. Vector returns distances. "
                "Hybrid returns relevance scores. The limit counts document hits before guideline deduplication."
            ),
            open_world=True,
        )


def _success(payload: object, model: type[BaseModel], text: str) -> CallToolResult:
    validated = model.model_validate(payload)
    structured = validated.model_dump(mode="json", exclude_unset=True)
    size = _structured_size(structured)
    if size > MAX_STRUCTURED_RESPONSE_BYTES:
        return _failure(
            CatalogResponseTooLargeError(
                "Complete tool result exceeds the 64 KiB response limit.",
                details={"bytes": size, "limit": MAX_STRUCTURED_RESPONSE_BYTES},
                hints=[
                    "Narrow the SQL query, requested guideline entry IDs, source detail, or search limit."
                ],
            )
        )
    return CallToolResult(
        content=[TextContent(type="text", text=text)],
        structured_content=structured,
        is_error=False,
    )


def _failure(error: CatalogError) -> CallToolResult:
    payload = ErrorToolResult(
        error=ErrorBody(
            code=error.code,
            message=error.message,
            details=dict(error.details),
        )
    ).model_dump(mode="json")
    if _structured_size(payload) > MAX_STRUCTURED_RESPONSE_BYTES:
        error = CatalogResponseTooLargeError(
            "Tool error details exceed the 64 KiB response limit.",
            details={"limit": MAX_STRUCTURED_RESPONSE_BYTES},
            hints=["Narrow the request before retrying."],
        )
        payload = ErrorToolResult(
            error=ErrorBody(
                code=error.code,
                message=error.message,
                details=dict(error.details),
            )
        ).model_dump(mode="json")
    return CallToolResult(
        content=[TextContent(type="text", text=error.message)],
        structured_content=payload,
        is_error=True,
    )


def _structured_size(value: object) -> int:
    return len(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )


def _run_server(
    server: MCPServer,
    *,
    transport: Transport,
    host: str,
    port: int,
) -> None:
    if transport == "stdio":
        server.run()
    elif transport == "sse":
        server.run("sse", host=host, port=port)
    else:
        server.run(
            "streamable-http",
            host=host,
            port=port,
            json_response=True,
        )


def main(
    *,
    location: str | Path | None = None,
    profile: str | None = None,
    embedding_vars: Path | None = None,
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
    catalog = open_catalog(location)
    if profile is not None:
        catalog.describe(profile=profile)
    logger.info(
        "Starting chartcoach MCP server with transport=%s host=%s port=%s",
        resolved_transport,
        host,
        port,
    )
    server = _build_server(log_level=resolved_log_level)
    _register_tools(
        server,
        catalog=catalog,
        profile=profile,
        embedding_vars=embedding_vars,
    )
    _run_server(
        server,
        transport=resolved_transport,
        host=host,
        port=port,
    )


__all__ = ["main"]

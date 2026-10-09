from __future__ import annotations

import json
import os
from collections.abc import Callable, Mapping
from typing import Literal

from mcp.server import MCPServer
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from pydantic import BaseModel

from chartcoach._catalog import Catalog, SourceDetail
from chartcoach._catalog.embedding import embedding_environment as resolve_environment
from chartcoach._catalog.errors import CatalogError, CatalogResponseTooLargeError
from chartcoach._catalog.identity import catalog_identity
from chartcoach._catalog.search import SearchEmbeddings, catalog_search
from chartcoach._catalog.sql import catalog_sql
from chartcoach._constants import DEFAULT_GUIDELINE_URL_TEMPLATE

from .config import MCPConfig
from .models import (
    CiteCallResult,
    CiteToolResult,
    DescribeCallResult,
    DescribeToolResult,
    ErrorBody,
    ErrorToolResult,
    McpId,
    McpIds,
    McpLimit,
    McpRoles,
    ReadCallResult,
    ReadToolResult,
    SearchCallResult,
    SearchToolResult,
    SqlCallResult,
    SqlToolResult,
)
from .settings import DEFAULT_SQL_TIMEOUT

MAX_STRUCTURED_RESPONSE_BYTES = 65_536


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


def register_tools(
    server: MCPServer,
    *,
    catalog: Catalog,
    profile: str | None = None,
    embedding_variables: Mapping[str, str] | None = None,
    embedding_environment: Mapping[str, str] | None = None,
    sql_timeout: float = DEFAULT_SQL_TIMEOUT,
) -> None:
    """Attach catalog tools to a caller-configured MCP SDK server."""
    settings = MCPConfig(
        profile=profile,
        sql_timeout=sql_timeout,
        embedding_variables=dict(embedding_variables or {}),
    )
    variables: dict[str, str] = {}
    if profile:
        metadata = catalog._profile_metadata(profile)
        environment = resolve_environment(
            os.environ if embedding_environment is None else embedding_environment
        )
        for binding in metadata.embedding_functions:
            for value in binding.model.values():
                if isinstance(value, str) and value.startswith("$var:"):
                    name = value.removeprefix("$var:")
                    if environment.get(name):
                        variables[name] = environment[name]
    variables.update(settings.embedding_variables)
    embedding_context = SearchEmbeddings(variables)
    search_profile = settings.profile

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
                catalog_sql(
                    catalog, statement, limit=limit, timeout=settings.sql_timeout
                ),
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
            try:
                return _success(
                    catalog_search(
                        catalog,
                        text,
                        profile=search_profile,
                        mode=mode,
                        limit=limit,
                        where=where,
                        embedding_context=embedding_context,
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
            hints=list(error.hints),
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
                hints=list(error.hints),
            )
        ).model_dump(mode="json")
    return CallToolResult(
        content=[TextContent(type="text", text=str(error))],
        structured_content=payload,
        is_error=True,
    )


def _structured_size(value: object) -> int:
    return len(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )

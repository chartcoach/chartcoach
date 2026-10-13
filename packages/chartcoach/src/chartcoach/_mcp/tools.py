from __future__ import annotations

import json
import os
from collections.abc import Callable, Mapping, Sequence
from typing import Annotated, Literal

from mcp.server import MCPServer
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from pydantic import BaseModel, Field

from chartcoach._catalog import Catalog, SourceDetail
from chartcoach._catalog.embedding import profile_variables
from chartcoach._catalog.errors import CatalogError
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
    ReadCallResult,
    ReadToolResult,
    SearchCallResult,
    SearchToolResult,
    SqlCallResult,
    SqlToolResult,
)
from .settings import DEFAULT_SQL_TIMEOUT


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
        variables = profile_variables(
            catalog._profile_metadata(profile).embedding_functions,
            os.environ if embedding_environment is None else embedding_environment,
        )
    variables.update(settings.embedding_variables)
    embedding_context = SearchEmbeddings(variables)
    search_profile = settings.profile

    def failure(tool: str, error: CatalogError) -> CallToolResult:
        return _failure(
            error,
            hints=_recovery_hints(error, tool=tool, catalog=catalog),
        )

    def describe(
        profile: Annotated[
            str | None,
            Field(
                description="Profile name to inspect from profiles. Omit to list profiles. Inspection leaves the active search profile unchanged.",
            ),
        ] = None,
    ) -> DescribeCallResult:
        try:
            description = catalog.describe(profile=profile)
            search_info: dict[str, object] | None = None
            if search_profile is not None:
                documents = catalog.documents()
                search_info = {
                    "profile": search_profile,
                    "filter_columns": [*documents.columns, "vector"],
                    "document_roles": sorted(
                        documents.get_column("role").unique().to_list()
                    ),
                }
            return _success(
                {
                    **description,
                    "mcp": {
                        "sql_engine": "DuckDB",
                        "sql_timeout_seconds": settings.sql_timeout,
                        "search": search_info,
                    },
                },
                DescribeToolResult,
            )
        except CatalogError as exc:
            return failure("describe", exc)

    def sql(
        statement: Annotated[
            str,
            Field(
                description="One read-only DuckDB query using tables and columns from describe. DESCRIBE guidelines returns native SQL types.",
            ),
        ],
        *,
        limit: Annotated[McpLimit, Field(description="Maximum returned rows.")] = 100,
    ) -> SqlCallResult:
        try:
            return _success(
                catalog_sql(
                    catalog, statement, limit=limit, timeout=settings.sql_timeout
                ),
                SqlToolResult,
            )
        except CatalogError as exc:
            return failure("sql", exc)

    def read(
        ids: McpIds,
        *,
        roles: Annotated[
            list[McpId] | None,
            Field(
                description="Section names from describe.section_roles[].name, such as advice or exceptions. Null or [] retains all sections.",
            ),
        ] = None,
        source_detail: Annotated[
            SourceDetail,
            Field(
                description="none: empty sources. minimal: reference ID, authors, year, title, DOI and URL. full: all parsed fields and raw BibTeX references. Use cite for formatted citations.",
            ),
        ] = "minimal",
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
            )
        except CatalogError as exc:
            return failure("read", exc)

    def cite(
        ids: McpIds,
        *,
        url_template: Annotated[
            str,
            Field(
                description="Public guideline URL template containing {id}. Keep the default for official catalog links.",
            ),
        ] = DEFAULT_GUIDELINE_URL_TEMPLATE,
    ) -> CiteCallResult:
        try:
            return _success(
                {
                    "records": catalog.cite(ids=ids, url_template=url_template),
                    **catalog_identity(catalog),
                },
                CiteToolResult,
            )
        except CatalogError as exc:
            return failure("cite", exc)

    _add_tool(
        server,
        describe,
        name="describe",
        description=(
            "Inspect catalog identity, table schemas and row counts, section roles, label families, "
            "and available profiles. mcp.search reports the active search profile and its "
            "filter columns and document roles, or null when search is unconfigured."
        ),
        open_world=False,
    )
    _add_tool(
        server,
        sql,
        name="sql",
        description=(
            "Query catalog tables with read-only DuckDB SQL. Returns typed rows. "
            "truncated reports the tool's row cap, not completion of SQL pagination. "
            "Enumerate with SELECT id, title, description FROM guidelines ORDER BY id "
            "LIMIT 100 OFFSET 0. Set the tool limit to at least the SQL page size, advance "
            "OFFSET by row_count, and stop when row_count is smaller than the page size."
        ),
        open_world=False,
    )
    _add_tool(
        server,
        read,
        name="read",
        description=(
            "Read guideline entries by ID. Returns records with title, description, labels, "
            "complete selected sections and sources. Inspect context and exceptions before "
            "applying advice."
        ),
        open_world=False,
    )
    _add_tool(
        server,
        cite,
        name="cite",
        description=(
            "Return guideline links and formatted source citations for entry IDs. "
            "Each record includes its title, URL, guideline_citation and sources "
            "with bibliographic fields, citation text, DOI and URL."
        ),
        open_world=False,
    )

    if search_profile is not None:

        def search(
            text: Annotated[
                McpId,
                Field(
                    description="Keywords for fts, or a natural-language topic for vector/hybrid."
                ),
            ],
            *,
            limit: Annotated[
                McpLimit,
                Field(
                    description="Maximum document hits before grouping by guideline. Increase to retrieve more distinct guideline candidates."
                ),
            ] = 10,
            where: Annotated[
                str | None,
                Field(
                    description="LanceDB SQL predicate over describe.mcp.search.filter_columns. parent_id is the guideline ID, id is the document ID. Examples: role = 'section.advice', array_has(labels, 'basis:empirical') AND role = 'overview'. Omit to search all documents."
                ),
            ] = None,
            mode: Annotated[
                Literal["fts", "vector", "hybrid"],
                Field(
                    description="fts: keyword relevance, higher is better. vector: semantic distance, lower is better. hybrid: combined relevance, higher is better. Vector/hybrid require the profile's provider dependencies and variables."
                ),
            ] = "fts",
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
                )
            except CatalogError as exc:
                return failure("search", exc)

        _add_tool(
            server,
            search,
            name="search",
            description=(
                "Find ranked guideline candidates in the active profile from describe.mcp.search. "
                "Returns matches with guideline IDs, matched document roles, excerpts and scores. "
                "Several document hits may match one guideline. Use matches[].id with read/cite, "
                "or sql to enumerate the catalog."
            ),
            open_world=True,
        )


def _recovery_hints(error: CatalogError, *, tool: str, catalog: Catalog) -> list[str]:
    if tool == "describe" and error.code == "lookup":
        return [
            "Call describe with profile=null, then select an exact name from profiles."
        ]
    if tool in {"read", "cite"} and error.code == "lookup":
        if tool == "read" and "id" not in error.details:
            return [
                "Use roles=null for all sections, or choose from: "
                + ", ".join(catalog.manifest.section_roles)
                + "."
            ]
        return [
            "Use guideline IDs from sql rows or search matches[].id.",
            'Discover IDs with sql(statement="SELECT id, title FROM guidelines ORDER BY id LIMIT 100").',
        ]
    if tool == "sql":
        hints = [hint for hint in error.hints if "chartcoach.duckdb." not in hint]
        if error.code == "invalid_input":
            hints.append(
                "Use describe.tables for table and column names, or sql with DESCRIBE guidelines for native SQL types."
            )
        return hints
    if tool != "search":
        return list(error.hints)
    if "columns" in error.details:
        return [
            "Use document columns from describe.mcp.search.filter_columns. Quote string values, such as role = 'overview', or set where=null."
        ]
    if "variables" in error.details:
        hints = [
            "Set the listed variables in the server environment or CHARTCOACH_EMBEDDING_VARS, then restart the server."
        ]
    else:
        hints = [
            hint.replace("catalog.describe(profile=...)", "describe(profile=...)")
            for hint in error.hints
        ]
    if error.code in {
        "unavailable_capability",
        "embedding_failure",
        "operation_failed",
        "incompatible_profile",
        "integrity",
    }:
        hints.append(
            "Try search with mode='fts' and where=null, or use sql over guidelines if the index is unavailable."
        )
    return hints


def _success(payload: object, model: type[BaseModel]) -> CallToolResult:
    return _result(model.model_validate(payload), is_error=False)


def _failure(error: CatalogError, *, hints: Sequence[str]) -> CallToolResult:
    return _result(
        ErrorToolResult(
            error=ErrorBody(
                code=error.code,
                message=error.message,
                details=dict(error.details),
                hints=list(hints),
            )
        ),
        is_error=True,
    )


def _result(payload: BaseModel, *, is_error: bool) -> CallToolResult:
    structured = payload.model_dump(mode="json", exclude_unset=True)
    return CallToolResult(
        content=[
            TextContent(
                type="text",
                text=json.dumps(structured, ensure_ascii=False, separators=(",", ":")),
            )
        ],
        structured_content=structured,
        is_error=is_error,
    )

from __future__ import annotations

from collections.abc import Sequence
from os import PathLike, fspath
from typing import TYPE_CHECKING

import duckdb

from .catalog.collection import Catalog
from .search import Mode, Query, query

if TYPE_CHECKING:
    from lancedb import Table

_SEARCH_HINTS = (
    "Build a full-text LanceDB table with `chartcoach catalog index create --source PATH --index PATH`.",
    "Pass the same index path to `chartcoach catalog find --mode fts`.",
    "Use `chartcoach catalog index create --embedding ...` when vector or hybrid search is required.",
)

MCP_TOOL_SPECS: tuple[dict[str, object], ...] = (
    {
        "name": "sql",
        "registered_when": "always",
        "description": "Run one read-only SQL query over catalog tables.",
        "arguments": [
            {
                "name": "statement",
                "type": "string",
                "required": True,
                "description": "One SELECT statement over catalog tables.",
            },
            {
                "name": "limit",
                "type": "integer",
                "required": False,
                "default": 100,
                "description": "Maximum rows to return. The value must be at least 1.",
            },
        ],
        "returns": {
            "type": "object",
            "fields": [
                {
                    "name": "columns",
                    "type": "array",
                    "description": "Returned column names and Polars data types.",
                },
                {
                    "name": "rows",
                    "type": "array",
                    "description": "Query rows as JSON objects.",
                },
                {
                    "name": "row_count",
                    "type": "integer",
                    "description": "Number of returned rows.",
                },
                {
                    "name": "truncated",
                    "type": "boolean",
                    "description": "True when more rows matched than the limit returned.",
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "description": "Applied row limit.",
                },
                {
                    "name": "catalog_digest",
                    "type": "string",
                    "description": "Digest for the catalog instance that served the query.",
                },
            ],
        },
    },
    {
        "name": "search",
        "registered_when": "only when --index or CHARTCOACH_INDEX is set",
        "description": "Run LanceDB search over indexed catalog document rows.",
        "arguments": [
            {
                "name": "search_query",
                "type": "string",
                "required": True,
                "description": "Text query for FTS, vector, hybrid, or automatic indexed discovery.",
            },
            {
                "name": "limit",
                "type": "integer",
                "required": False,
                "default": 10,
                "description": "Maximum candidate rows to return.",
            },
            {
                "name": "where",
                "type": "string or null",
                "required": False,
                "default": None,
                "description": "Optional LanceDB filter expression.",
            },
            {
                "name": "mode",
                "type": "auto | fts | vector | hybrid",
                "required": False,
                "default": "auto",
                "description": "Search mode. Use fts when no embedding function is configured.",
            },
        ],
        "returns": {
            "type": "object",
            "fields": [
                {
                    "name": "query",
                    "type": "string",
                    "description": "Original search query.",
                },
                {
                    "name": "mode",
                    "type": "string",
                    "description": "Applied search mode.",
                },
                {
                    "name": "rows",
                    "type": "array",
                    "description": "Candidate rows with ids, labels, matched roles, snippets, and scores.",
                },
                {
                    "name": "row_count",
                    "type": "integer",
                    "description": "Number of returned candidates.",
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "description": "Applied row limit.",
                },
                {
                    "name": "where",
                    "type": "string or null",
                    "description": "Applied LanceDB filter expression.",
                },
                {
                    "name": "index_path",
                    "type": "string or null",
                    "description": "Configured index path or URI.",
                },
                {
                    "name": "table_name",
                    "type": "string",
                    "description": "LanceDB table that served the query.",
                },
            ],
        },
    },
)


def mcp_tool_specs() -> list[dict[str, object]]:
    """Return MCP tool contracts without importing MCP runtime dependencies."""

    return [dict(spec) for spec in MCP_TOOL_SPECS]


class ToolError(ValueError):
    """Error that carries a message plus recovery hints."""

    def __init__(self, message: str, *, hints: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.message = message
        self.hints = tuple(hints)

    def __str__(self) -> str:
        return format_error(self.message, self.hints)


class Tools:
    """Raw catalog tools shared by CLI and MCP transports."""

    def __init__(
        self,
        catalog: Catalog,
        *,
        table: "Table | None" = None,
        index_path: str | PathLike[str] | None = None,
    ) -> None:
        self._catalog = catalog
        self._table = table
        self._index_path = fspath(index_path) if index_path is not None else None

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    def sql(self, statement: str, *, limit: int = 100) -> dict[str, object]:
        """Run one read-only SQL query over catalog tables."""

        if limit < 1:
            raise ToolError("SQL query limit must be at least 1.")
        _validate_select_query(statement)
        conn = self.catalog.duckdb(config={"enable_external_access": False})
        try:
            try:
                frame = conn.sql(statement).limit(limit + 1).pl()
            except duckdb.Error as exc:
                raise ToolError(
                    str(exc),
                    hints=[
                        "Query the catalog tables with one read-only SELECT statement.",
                    ],
                ) from exc
        finally:
            conn.close()

        visible = frame.head(limit)
        return {
            "columns": [
                {"name": name, "type": str(dtype)}
                for name, dtype in visible.schema.items()
            ],
            "rows": visible.to_dicts(),
            "row_count": visible.height,
            "truncated": frame.height > limit,
            "limit": limit,
            "catalog_digest": self.catalog.digest(),
        }

    def search(
        self,
        search_query: Query,
        *,
        limit: int = 10,
        where: str | None = None,
        mode: Mode = "auto",
    ) -> dict[str, object]:
        """Run LanceDB search over indexed catalog document rows."""

        table = self._require_table()
        rows = query(
            table,
            search_query,
            limit=limit,
            where=where,
            mode=mode,
        )
        return {
            "query": search_query,
            "mode": mode,
            "rows": rows,
            "row_count": len(rows),
            "limit": limit,
            "where": where,
            "index_path": self._index_path,
            "table_name": table.name,
        }

    def _require_table(self) -> "Table":
        if self._table is None:
            raise ToolError(
                "LanceDB table is required.",
                hints=_SEARCH_HINTS,
            )
        return self._table


def format_error(message: str, hints: Sequence[str]) -> str:
    """Render an error message and recovery hints for CLI and MCP transports."""

    if not hints:
        return message
    joined_hints = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nGuidance:\n{joined_hints}"


def search_error(message: str) -> str:
    """Return a search error message with recovery guidance."""

    return format_error(
        message,
        _SEARCH_HINTS,
    )


def _validate_select_query(statement: str) -> None:
    try:
        statements = duckdb.extract_statements(statement)
    except duckdb.ParserException as exc:
        raise ToolError(
            str(exc),
            hints=["Pass one SELECT query against the catalog tables."],
        ) from exc
    if len(statements) != 1:
        raise ToolError(
            "SQL queries must contain exactly one statement.",
            hints=["Pass one SELECT query. Multiple statements are rejected."],
        )
    statement_obj = statements[0]
    if str(statement_obj.type) != "StatementType.SELECT":
        raise ToolError(
            "Only SELECT queries are allowed.",
            hints=[
                "Run `chartcoach catalog export duckdb` when another tool needs mutable SQL tables.",
            ],
        )


__all__ = [
    "MCP_TOOL_SPECS",
    "ToolError",
    "Tools",
    "format_error",
    "mcp_tool_specs",
    "search_error",
]

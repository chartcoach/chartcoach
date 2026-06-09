from __future__ import annotations

from collections.abc import Sequence
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

import duckdb

from .catalog.collection import Catalog
from .search import Mode, Query, query

if TYPE_CHECKING:
    from lancedb import Table

_SEARCH_HINTS = (
    "Build a full-text LanceDB table with `chartcoach index --source PATH --index PATH`.",
    "Pass the same index path to search commands with `--mode fts`.",
    "Use `chartcoach index --embedding ...` when vector or hybrid search is required.",
)


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
        self._index_path = Path(index_path) if index_path is not None else None

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
            "index_path": str(self._index_path) if self._index_path is not None else None,
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
                "Run `chartcoach catalog duckdb` when another tool needs mutable SQL tables.",
            ],
        )


__all__ = [
    "ToolError",
    "Tools",
    "format_error",
    "search_error",
]

from __future__ import annotations

import math
from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from .errors import CatalogValidationError
from .identity import catalog_identity

if TYPE_CHECKING:
    from .model import Catalog


class SqlColumn(TypedDict):
    """One named SQL result column."""

    name: str
    type: str


class SqlResult(TypedDict):
    """One bounded SQL result with catalog identity."""

    columns: list[SqlColumn]
    rows: list[dict[str, object]]
    row_count: int
    truncated: bool
    limit: int
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


def catalog_sql(catalog: Catalog, statement: str, *, limit: int = 100) -> SqlResult:
    """Run one read-only query with external access disabled."""

    import duckdb

    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise CatalogValidationError("SQL query limit must be at least 1.")
    _validate_select_query(statement)
    connection = catalog.duckdb(config={"enable_external_access": False})
    try:
        try:
            relation = connection.sql(statement).limit(limit + 1)
            description = relation.description
            query_rows = relation.fetchall()
        except duckdb.Error as exc:
            raise CatalogValidationError(
                str(exc),
                hints=["Query the catalog tables with one read-only SELECT statement."],
            ) from exc
    finally:
        connection.close()

    columns = tuple(item[0] for item in description)
    if len(columns) != len(set(columns)):
        raise CatalogValidationError(
            "SQL query returned duplicate column names.",
            hints=["Give every SELECT expression a distinct alias."],
        )
    rows = [
        {
            column: _json_value(value)
            for column, value in zip(columns, values, strict=True)
        }
        for values in query_rows[:limit]
    ]
    identity = catalog_identity(catalog)
    return {
        "columns": [{"name": item[0], "type": str(item[1])} for item in description],
        "rows": rows,
        "row_count": len(rows),
        "truncated": len(query_rows) > limit,
        "limit": limit,
        "entries_digest": identity["entries_digest"],
        "manifest_digest": identity["manifest_digest"],
        "release_digest": identity["release_digest"],
    }


def _json_value(value: object) -> object:
    if value is None or isinstance(value, str | bool | int):
        return value
    if isinstance(value, float):
        if math.isfinite(value):
            return value
        raise _json_value_error()
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, datetime | date | time):
        return value.isoformat()
    if isinstance(value, list | tuple):
        return [_json_value(item) for item in value]
    if isinstance(value, Mapping) and all(isinstance(key, str) for key in value):
        return {str(key): _json_value(item) for key, item in value.items()}
    raise _json_value_error()


def _json_value_error() -> CatalogValidationError:
    return CatalogValidationError(
        "SQL query returned a value that cannot be represented as JSON.",
        hints=["Cast binary and custom values to VARCHAR in the SELECT list."],
    )


def _validate_select_query(statement: str) -> None:
    import duckdb

    try:
        statements = duckdb.extract_statements(statement)
    except duckdb.ParserException as exc:
        raise CatalogValidationError(
            str(exc),
            hints=["Pass one SELECT query against the catalog tables."],
        ) from exc
    if len(statements) != 1:
        raise CatalogValidationError(
            "SQL queries must contain exactly one statement.",
            hints=["Pass one SELECT query. Multiple statements are rejected."],
        )
    if str(statements[0].type) != "StatementType.SELECT":
        raise CatalogValidationError(
            "Only SELECT queries are allowed.",
            hints=[
                "Use chartcoach.duckdb.write_duckdb when another tool needs mutable SQL tables."
            ],
        )


__all__ = ["SqlColumn", "SqlResult", "catalog_sql"]

from __future__ import annotations

from typing import Any

from ..constants import DEFAULT_DUCKDB_ROW_LIMIT
from .json import normalize_for_json


class SqlTools:
    """Read-only SQL tools over a prepared DuckDB catalog connection."""

    def __init__(
        self,
        conn: Any,
        *,
        default_row_limit: int = DEFAULT_DUCKDB_ROW_LIMIT,
    ) -> None:
        self._conn = conn
        self._default_row_limit = default_row_limit

    @property
    def conn(self) -> Any:
        """Return the DuckDB connection behind these tools."""

        return self._conn

    def schema(
        self,
        relations: tuple[str, ...] = (),
    ) -> list[dict[str, object]]:
        """List columns for SQL-visible relations."""

        selected = set(relations)
        relation_rows = self.sql("show all tables", row_limit=10_000)["rows"]
        available_relations = tuple(
            row["name"] for row in relation_rows if isinstance(row.get("name"), str)
        )
        unknown = sorted(selected - set(available_relations))
        if unknown:
            available = ", ".join(available_relations)
            raise ValueError(
                f"Unknown SQL relation(s): {', '.join(unknown)}. Available relations: {available}"
            )

        rows: list[dict[str, object]] = []
        for relation in available_relations:
            if selected and relation not in selected:
                continue
            describe = self.sql(f"describe {relation}", row_limit=10_000)
            rows.extend(
                {
                    "relation": relation,
                    "column": row["column_name"],
                    "type": row["column_type"],
                }
                for row in describe["rows"]
            )
        return rows

    def sql(
        self,
        sql: str,
        *,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        """Run one read-only DuckDB statement and return JSON-safe rows."""

        normalized_sql = sql.strip()
        if not normalized_sql:
            raise ValueError("SQL cannot be empty.")
        _validate_read_only_sql(normalized_sql)
        applied_row_limit = self._default_row_limit if row_limit is None else row_limit
        cursor = self.conn.execute(normalized_sql)
        if cursor.description is None:
            return {
                "sql": normalized_sql,
                "columns": [],
                "rows": [],
                "row_count": 0,
                "row_limit": applied_row_limit,
                "truncated": False,
            }

        columns = [column[0] for column in cursor.description]
        fetched_rows = cursor.fetchmany(applied_row_limit + 1)
        truncated = len(fetched_rows) > applied_row_limit
        rows = fetched_rows[:applied_row_limit]

        normalized_rows = [
            {
                column_name: normalize_for_json(value)
                for column_name, value in zip(columns, row, strict=True)
            }
            for row in rows
        ]
        normalized_columns = [
            {
                "name": column[0],
                "type_code": normalize_for_json(column[1]),
            }
            for column in cursor.description
        ]

        return {
            "sql": normalized_sql,
            "columns": normalized_columns,
            "rows": normalized_rows,
            "row_count": len(normalized_rows),
            "row_limit": applied_row_limit,
            "truncated": truncated,
        }


def _validate_read_only_sql(sql: str) -> None:
    try:
        import duckdb
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "DuckDB catalog SQL requires the optional `chartcoach[sql]` dependencies.",
            name=exc.name,
        ) from exc

    try:
        statements = duckdb.extract_statements(sql)
    except Exception as exc:
        raise ValueError(f"SQL could not be parsed: {exc}") from exc

    if len(statements) != 1:
        raise ValueError("SQL tool accepts exactly one read-only statement.")

    statement_type = str(getattr(statements[0], "type", ""))
    if statement_type != "StatementType.SELECT":
        raise ValueError(
            "SQL tool only accepts read-only SELECT-style statements such as SELECT, WITH, SHOW, and DESCRIBE."
        )


__all__ = ["SqlTools"]

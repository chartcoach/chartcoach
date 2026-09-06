from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from datetime import date, datetime, time
from decimal import Decimal
from os import PathLike, fspath
from typing import TYPE_CHECKING, Any, Literal, cast

if TYPE_CHECKING:
    from lancedb import Table

    from .catalog.collection import Catalog

_SEARCH_HINTS = (
    "Open indexed tools with `Tools.open(source, profile=profile)`.",
    "Use `mode='fts'` for provider-free text retrieval.",
    "The CLI equivalent is `chartcoach catalog find --source SOURCE --profile PROFILE QUERY`.",
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
    """Catalog SQL and search operations shared by Python, CLI, and MCP."""

    def __init__(
        self,
        catalog: Catalog,
        *,
        table: Table | None = None,
        source: str | PathLike[str] | None = None,
        profile: str | None = None,
    ) -> None:
        self._catalog = catalog
        self._table = table
        self._source = fspath(source) if source is not None else None
        self._profile = profile

    @classmethod
    def open(
        cls,
        source: str | PathLike[str] | None = None,
        *,
        profile: str | None = None,
        storage_options: Mapping[str, object] | None = None,
    ) -> Tools:
        """Open one catalog and its optional release-backed search table.

        Use this constructor when the same source and profile must identify
        the catalog, search table, and provenance returned by `search()`.

        Args:
            source: Authored catalog, bundle, `catalog.json`, or `release.json`
                path or URI. The official selected catalog is used when
                omitted. Use an exact `release.json` or release directory when
                the catalog and index must remain fixed across calls.
            profile: Named embedding profile to open for `search()`. SQL is
                available when omitted.
            storage_options: Credentials and transport options passed to both
                catalog and index loading.

        Returns:
            Tools bound to the opened catalog and optional search table.
        """

        if profile is not None:
            from .catalog.runtime import open_catalog_index

            catalog, table = open_catalog_index(
                source,
                profile=profile,
                storage_options=storage_options,
            )
        else:
            from .catalog import open_catalog

            catalog = open_catalog(source, storage_options=storage_options)
            table = None
        return cls(
            catalog,
            table=table,
            source=source,
            profile=profile,
        )

    @property
    def catalog(self) -> Catalog:
        return self._catalog

    def sql(self, statement: str, *, limit: int = 100) -> dict[str, object]:
        """Run one read-only SQL query over catalog tables."""

        import duckdb

        if limit < 1:
            raise ToolError("SQL query limit must be at least 1.")
        _validate_select_query(statement)
        conn = self.catalog.duckdb(config={"enable_external_access": False})
        try:
            try:
                relation = conn.sql(statement).limit(limit + 1)
                description = relation.description
                query_rows = relation.fetchall()
            except duckdb.Error as exc:
                raise ToolError(
                    str(exc),
                    hints=[
                        "Query the catalog tables with one read-only SELECT statement.",
                    ],
                ) from exc
        finally:
            conn.close()

        columns = tuple(item[0] for item in description)
        if len(columns) != len(set(columns)):
            raise ToolError(
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
        return {
            "columns": [
                {"name": item[0], "type": str(item[1])} for item in description
            ],
            "rows": rows,
            "row_count": len(rows),
            "truncated": len(query_rows) > limit,
            "limit": limit,
            "content_digest": self.catalog.content_digest(),
            "release_digest": (
                self.catalog.release.digest
                if self.catalog.release is not None
                else None
            ),
        }

    def search(
        self,
        search_query: str,
        *,
        vector: Sequence[float] | None = None,
        limit: int = 10,
        where: str | None = None,
        mode: Literal["fts", "vector", "hybrid"] = "fts",
    ) -> dict[str, object]:
        """Search indexed documents and return one row per guideline.

        Rows are ordered by `rank`. The `score` is relevance for full-text and
        hybrid search, where larger values are stronger. It is distance for
        vector search, where smaller values are stronger.
        """

        table = self._require_table()
        rows = _search_guidelines(
            self.catalog,
            table,
            search_query,
            vector=vector,
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
            "source": self._source,
            "profile": self._profile,
            "release_digest": (
                self.catalog.release.digest
                if self.catalog.release is not None
                else None
            ),
        }

    def _require_table(self) -> Table:
        if self._table is None:
            raise ToolError(
                "LanceDB table is required.",
                hints=_SEARCH_HINTS,
            )
        return self._table


def _search_guidelines(
    catalog: Catalog,
    table: Table,
    search_query: str,
    *,
    vector: Sequence[float] | None,
    limit: int,
    where: str | None,
    mode: Literal["fts", "vector", "hybrid"],
) -> list[dict[str, object]]:
    if not search_query.strip():
        raise ToolError("Search query must be a non-empty string.")
    if limit < 1:
        raise ToolError("Search limit must be at least 1.")
    if mode in {"vector", "hybrid"} and vector is None:
        raise ToolError(f"{mode} search requires a caller-provided vector.")

    query: Any
    if mode == "fts":
        query = table.search(search_query, query_type="fts", fts_columns="text")
    elif mode == "vector":
        query = cast(
            Any,
            table.search(
                list(vector or ()),
                query_type="vector",
                vector_column_name="vector",
            ),
        ).distance_type("cosine")
    elif mode == "hybrid":
        query = (
            cast(
                Any,
                table.search(
                    query_type="hybrid",
                    fts_columns="text",
                    vector_column_name="vector",
                ),
            )
            .vector(list(vector or ()))
            .text(search_query)
            .distance_type("cosine")
        )
    else:
        raise ToolError(f"Unsupported search mode: {mode!r}.")
    if where:
        query = query.where(where)

    rows: list[dict[str, object]] = []
    seen: set[str] = set()
    for match in query.limit(limit).to_list():
        guideline_id = _match_string(match, "parent_id")
        if guideline_id in seen:
            continue
        seen.add(guideline_id)
        try:
            guideline = catalog.entry(guideline_id)
        except KeyError as exc:
            raise ToolError(
                f"Indexed guideline is absent from the catalog: {guideline_id}"
            ) from exc
        labels = guideline.get("labels")
        rows.append(
            {
                "rank": len(rows) + 1,
                "id": guideline_id,
                "title": guideline["title"],
                "description": guideline["description"],
                "labels": list(labels) if isinstance(labels, list | tuple) else [],
                "matched_document_id": _match_string(match, "id"),
                "matched_role": _match_string(match, "role"),
                "matched_text": _match_string(match, "text"),
                "score": _match_score(match),
            }
        )
    return rows


def _match_string(row: Mapping[str, object], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value:
        raise ToolError(f"Indexed document is missing string field {key!r}.")
    return value


def _match_score(row: Mapping[str, object]) -> float | None:
    for key in ("_relevance_score", "_score", "_distance"):
        value = row.get(key)
        if isinstance(value, int | float):
            return float(value)
    return None


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


def _json_value_error() -> ToolError:
    return ToolError(
        "SQL query returned a value that cannot be represented as JSON.",
        hints=["Cast binary and custom values to VARCHAR in the SELECT list."],
    )


def format_error(message: str, hints: Sequence[str]) -> str:
    """Render an error message and recovery hints for CLI and MCP transports."""

    if not hints:
        return message
    joined_hints = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nGuidance:\n{joined_hints}"


def search_error(message: str, *, hints: Sequence[str] = ()) -> str:
    """Return a search error message with recovery guidance."""

    return format_error(
        message,
        (*hints, *_SEARCH_HINTS),
    )


def _validate_select_query(statement: str) -> None:
    import duckdb

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
    "ToolError",
    "Tools",
    "format_error",
    "search_error",
]

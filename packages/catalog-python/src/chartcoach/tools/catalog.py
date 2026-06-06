from __future__ import annotations

from collections.abc import Mapping, Sequence
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, cast

import duckdb
import polars as pl

from ..catalog.collection import Catalog
from ..catalog.relations import (
    TABLE_SPECS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)

if TYPE_CHECKING:
    from ..search import CacheMode, LanceIndex

_SEARCH_HINTS = (
    "Build or provide a search index for the current catalog digest.",
    "Inspect catalog artifacts to locate the LanceDB index path.",
)


class CatalogToolError(ValueError):
    """Error that carries a message plus recovery hints."""

    def __init__(self, message: str, *, hints: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.message = message
        self.hints = tuple(hints)

    def __str__(self) -> str:
        return format_tool_error(self.message, self.hints)


class CatalogTools:
    """Catalog-backed read tools shared by the CLI and MCP server.

    This layer is transport-agnostic. The CLI formats its returned rows for
    shells, and the MCP server exposes the same methods as tools.
    """

    def __init__(
        self,
        catalog: Catalog,
        *,
        index_dir: str | PathLike[str] | None = None,
        cache_mode: "CacheMode" = "reuse_only",
    ) -> None:
        self._catalog = catalog
        self._index_dir = Path(index_dir) if index_dir is not None else None
        self._cache_mode = cache_mode
        self._index: LanceIndex | None = None

    @property
    def catalog(self) -> Catalog:
        """Return the source catalog."""

        return self._catalog

    def list_tables(
        self, *, include_row_counts: bool = False
    ) -> list[dict[str, object]]:
        """List queryable structured tables."""

        if include_row_counts:
            return catalog_table_rows(self.catalog)
        return [
            {"name": spec.name, "columns": len(spec.schema), "rows": None}
            for spec in TABLE_SPECS.values()
        ]

    def describe_tables(self, tables: Sequence[str] = ()) -> list[dict[str, object]]:
        """List columns for structured catalog tables."""

        try:
            return catalog_table_schema(tables)
        except KeyError as exc:
            raise self._unknown_table_error([str(exc).strip("'")]) from exc

    def count_values(
        self,
        table: str,
        column: str,
        *,
        explode: bool = False,
        contains: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, object]]:
        """Count distinct values in a structured catalog table column."""

        frame = self._require_table(table)
        self._require_column(table, frame, column)
        dtype = frame.schema[column]
        if _is_list_dtype(dtype) and not explode:
            raise CatalogToolError(
                f"Column {table}.{column} is list-valued.",
                hints=[
                    "Pass explode=True to count each list item separately.",
                ],
            )

        value_expr = pl.col(column).explode() if explode else pl.col(column)
        values = frame.select(value_expr.alias("value")).filter(
            pl.col("value").is_not_null()
        )
        values = values.with_columns(pl.col("value").cast(pl.String).alias("value"))
        if contains:
            needle = contains.lower()
            values = values.filter(
                pl.col("value").str.to_lowercase().str.contains(needle, literal=True)
            )

        return (
            values.group_by("value")
            .len("rows")
            .sort(["rows", "value"], descending=[True, False])
            .head(limit)
            .with_columns(
                pl.lit(table).alias("table"),
                pl.lit(column).alias("column"),
            )
            .select("table", "column", "value", "rows")
            .to_dicts()
        )

    def sql_query(self, query: str, *, limit: int = 100) -> dict[str, object]:
        """Run one read-only SQL query over the catalog tables."""

        if limit < 1:
            raise CatalogToolError("SQL query limit must be at least 1.")
        _validate_select_query(query)
        conn = self.catalog.duckdb(config={"enable_external_access": False})
        try:
            try:
                frame = conn.sql(query).limit(limit + 1).pl()
            except duckdb.Error as exc:
                raise CatalogToolError(
                    str(exc),
                    hints=[
                        "Inspect table names before running the query.",
                        "Inspect column schemas before selecting fields.",
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

    def list_guidelines(
        self,
        *,
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        contains: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, object]]:
        """List guideline ids and summaries with deterministic filters."""

        self._validate_labels(labels)
        self._validate_label_prefixes(label_prefixes)
        df = self.catalog.guidelines().select(
            "id",
            "title",
            "description",
            "labels",
        )
        for label_value in labels:
            df = df.filter(pl.col("labels").list.contains(label_value))
        for prefix in label_prefixes:
            df = df.filter(
                pl.col("labels")
                .list.eval(pl.element().str.starts_with(prefix))
                .list.any()
            )
        if contains:
            needle = contains.lower()
            df = df.filter(
                pl.any_horizontal(
                    pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                    pl.col("title")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                    pl.col("description")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                )
            )
        return df.head(limit).to_dicts()

    def get_guideline(self, guideline_id: str) -> dict[str, object]:
        """Return one complete guideline entry by id."""

        try:
            return self.catalog.entry(guideline_id).to_record()
        except KeyError as exc:
            raise self._unknown_id_error(guideline_id) from exc

    def retrieve_guidelines(
        self,
        *,
        ids: Sequence[str] = (),
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        contains: str | None = None,
        roles: Sequence[str] = (),
        limit: int = 12,
    ) -> list[dict[str, object]]:
        """Return guideline records with optional label and section filters."""

        resolved_roles = self.validate_guideline_filters(
            labels=labels,
            label_prefixes=label_prefixes,
            roles=roles,
        )
        frame = self._query_guidelines(
            ids=ids,
            labels=labels,
            label_prefixes=label_prefixes,
            contains=contains,
            limit=limit,
        )

        return [
            _guideline_record_from_row(
                row,
                roles=set(resolved_roles) if resolved_roles else None,
            )
            for row in frame.to_dicts()
        ]

    def index_status(self) -> dict[str, object]:
        """Report the LanceDB index path and readiness for this catalog."""

        index_dir = self._require_index_dir()
        from ..search import LanceIndex

        paths = LanceIndex.cache_paths(self.catalog, cache_dir=index_dir)
        row: dict[str, object] = {
            "catalog_digest": self.catalog.digest(),
            "documents_version": paths.documents_version,
            "index_root": str(paths.index_root),
            "table_path": str(paths.table_path),
            "table_name": paths.table_name,
            "ready": False,
            "documents": None,
            "error": None,
        }
        try:
            index = self.open_index()
        except Exception as exc:
            row["error"] = str(exc)
            return row
        row["ready"] = True
        row["documents"] = index.document_count()
        return row

    def build_index(
        self,
        *,
        cache_mode: "CacheMode" = "reuse_or_create",
    ) -> dict[str, object]:
        """Open or build the LanceDB index and return its runtime summary."""

        index = self.open_index(cache_mode=cache_mode)
        return _index_summary(self.catalog, index)

    def query_documents(
        self,
        query: str,
        *,
        limit: int = 10,
        where: str | None = None,
    ) -> dict[str, object]:
        """Run full-text search over indexed catalog documents."""

        index = self.open_index()
        rows = index.query_documents(query, limit=limit, where=where)
        return {
            "query": query,
            "rows": rows,
            "row_count": len(rows),
            "limit": limit,
            "where": where,
            "index_root": str(index.index_root),
            "table_name": index.table_name,
        }

    def search_guidelines(
        self,
        query_text: str,
        *,
        limit: int | None = None,
        candidate_limit: int | None = None,
        where: str | None = None,
    ) -> dict[str, object]:
        """Search indexed documents and return deduplicated guideline rows."""

        from ..search import search_guidelines

        kwargs: dict[str, int] = {}
        if limit is not None:
            kwargs["limit"] = limit
        if candidate_limit is not None:
            kwargs["candidate_limit"] = candidate_limit
        result = search_guidelines(
            self.open_index(),
            query_text,
            where=where,
            **kwargs,
        )
        return result.to_dict()

    def validate_guideline_filters(
        self,
        *,
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        roles: Sequence[str] = (),
    ) -> tuple[str, ...]:
        """Validate reusable guideline filters and return section roles."""

        self._validate_labels(labels)
        self._validate_label_prefixes(label_prefixes)
        parsed_roles = tuple(roles)
        self._validate_section_roles(parsed_roles)
        return parsed_roles

    def open_index(
        self,
        *,
        cache_mode: "CacheMode | None" = None,
    ) -> "LanceIndex":
        """Open the configured LanceDB index lazily."""

        mode = cache_mode or self._cache_mode
        if self._index is not None and mode == self._cache_mode:
            return self._index
        index_dir = self._require_index_dir()
        from ..search import LanceIndex

        try:
            index = LanceIndex.from_cache(
                self.catalog,
                cache_dir=index_dir,
                cache_mode=mode,
            )
        except Exception as exc:
            raise CatalogToolError(str(exc), hints=_SEARCH_HINTS) from exc
        self._index = index
        self._cache_mode = mode
        return index

    def _query_guidelines(
        self,
        *,
        ids: Sequence[str],
        labels: Sequence[str],
        label_prefixes: Sequence[str],
        contains: str | None,
        limit: int,
    ) -> pl.DataFrame:
        df = self.catalog.guidelines()
        if ids:
            available = set(df.get_column("id").to_list())
            missing = [
                guideline_id for guideline_id in ids if guideline_id not in available
            ]
            if missing:
                raise self._unknown_id_error(missing[0])
            order = pl.DataFrame(
                {"id": list(ids), "_catalog_order": list(range(len(ids)))}
            )
            df = order.join(df, on="id", how="inner").sort("_catalog_order")

        for label in labels:
            df = df.filter(pl.col("labels").list.contains(label))
        for prefix in label_prefixes:
            df = df.filter(
                pl.col("labels")
                .list.eval(pl.element().str.starts_with(prefix))
                .list.any()
            )
        if contains:
            needle = contains.lower()
            df = df.filter(
                pl.any_horizontal(
                    pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                    pl.col("title")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                    pl.col("description")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                    pl.col("body")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                )
            )

        references = self.catalog.to_frame().select("id", "references")
        return (
            df.head(limit)
            .join(references, on="id", how="left")
            .drop("_catalog_order", strict=False)
        )

    def _require_table(self, table: str) -> pl.DataFrame:
        if table not in catalog_table_names():
            raise self._unknown_table_error([table])
        return self.catalog.table(table)

    def _require_column(
        self,
        table: str,
        frame: pl.DataFrame,
        column: str,
    ) -> None:
        if column not in frame.columns:
            raise self._unknown_column_error(table, frame, column)

    def _distinct_strings(
        self,
        *,
        table: str,
        column: str,
        explode: bool = False,
    ) -> set[str]:
        frame = self._require_table(table)
        self._require_column(table, frame, column)
        value_expr = pl.col(column).explode() if explode else pl.col(column)
        values = (
            frame.select(value_expr.alias("value"))
            .filter(pl.col("value").is_not_null())
            .with_columns(pl.col("value").cast(pl.String).alias("value"))
            .get_column("value")
            .to_list()
        )
        return {value for value in values if isinstance(value, str)}

    def _validate_labels(self, labels: Sequence[str]) -> None:
        if not labels:
            return
        available = self._distinct_strings(
            table="guideline_labels",
            column="label",
        )
        missing = sorted(set(labels) - available)
        if missing:
            raise CatalogToolError(
                f"Unknown label(s): {', '.join(missing)}",
                hints=[
                    "Inspect the guideline_labels table before filtering by label.",
                ],
            )

    def _validate_label_prefixes(self, prefixes: Sequence[str]) -> None:
        if not prefixes:
            return
        available = self._distinct_strings(
            table="guideline_labels",
            column="label",
        )
        missing = [
            prefix
            for prefix in sorted(set(prefixes))
            if not any(label.startswith(prefix) for label in available)
        ]
        if missing:
            raise CatalogToolError(
                f"No labels match prefix(es): {', '.join(missing)}",
                hints=[
                    "Inspect the guideline_labels table before filtering by label prefix.",
                ],
            )

    def _validate_section_roles(self, roles: Sequence[str]) -> None:
        if not roles:
            return
        available = self._distinct_strings(table="sections", column="role")
        missing = sorted(set(roles) - available)
        if missing:
            raise CatalogToolError(
                f"Unknown section role(s): {', '.join(missing)}",
                hints=[
                    "Inspect the sections table before filtering by role.",
                ],
            )

    def _unknown_table_error(self, tables: Sequence[str]) -> CatalogToolError:
        available = ", ".join(catalog_table_names())
        return CatalogToolError(
            f"Unknown table(s): {', '.join(tables)}",
            hints=[
                f"Available tables: {available}",
                "Use one of the available table names.",
            ],
        )

    def _unknown_column_error(
        self,
        table: str,
        frame: pl.DataFrame,
        column: str,
    ) -> CatalogToolError:
        columns = ", ".join(frame.columns)
        return CatalogToolError(
            f"Unknown column for table {table}: {column}",
            hints=[
                f"Available columns on {table}: {columns}",
                f"Use one of the available columns on {table}.",
            ],
        )

    def _unknown_id_error(self, guideline_id: str) -> CatalogToolError:
        return CatalogToolError(
            f"Unknown guideline id: {guideline_id}",
            hints=[
                "List guideline summaries before reading a specific id.",
                "Search by text or semantic similarity when the id is unknown.",
            ],
        )

    def _require_index_dir(self) -> Path:
        if self._index_dir is None:
            raise CatalogToolError(
                "Search index directory is required.",
                hints=_SEARCH_HINTS,
            )
        return self._index_dir


def _guideline_record_from_row(
    row: Mapping[str, object],
    *,
    roles: set[str] | None,
) -> dict[str, object]:
    """Return the transport-neutral record shape for one guideline."""

    raw_sections = cast(Sequence[Mapping[str, object]], row.get("sections") or ())
    sections = [
        {
            "role": str(section["role"]),
            "title": str(section["title"]),
            "content": str(section["content"]),
        }
        for section in raw_sections
        if roles is None or section.get("role") in roles
    ]
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "labels": list(cast(Sequence[str], row.get("labels") or ())),
        "references": list(cast(Sequence[str], row.get("references") or ())),
        "sections": sections,
    }


def _index_summary(catalog: Catalog, index: "LanceIndex") -> dict[str, object]:
    return {
        "guidelines": len(catalog),
        "documents": index.document_count(),
        "index_root": str(index.index_root),
        "table_name": index.table_name,
    }


def format_tool_error(message: str, hints: Sequence[str]) -> str:
    """Render an error message and recovery hints for CLI and MCP transports."""

    if not hints:
        return message
    joined_hints = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nGuidance:\n{joined_hints}"


def search_error_message(message: str) -> str:
    """Return a semantic-search error message with recovery guidance."""

    return format_tool_error(
        message,
        _SEARCH_HINTS,
    )


def _is_list_dtype(dtype: object) -> bool:
    return isinstance(dtype, pl.DataType) and dtype.base_type() == pl.List


def _validate_select_query(query: str) -> None:
    try:
        statements = duckdb.extract_statements(query)
    except duckdb.ParserException as exc:
        raise CatalogToolError(
            str(exc),
            hints=["Pass one SELECT query against the catalog tables."],
        ) from exc
    if len(statements) != 1:
        raise CatalogToolError(
            "SQL queries must contain exactly one statement.",
            hints=["Pass one SELECT query. Multiple statements are rejected."],
        )
    statement = statements[0]
    if str(statement.type) != "StatementType.SELECT":
        raise CatalogToolError(
            "Only SELECT queries are allowed.",
            hints=[
                "Create a durable DuckDB file through the catalog export tooling when mutation is needed.",
                "Inspect table schemas before writing the query.",
            ],
        )


__all__ = [
    "CatalogToolError",
    "CatalogTools",
    "format_tool_error",
    "search_error_message",
]

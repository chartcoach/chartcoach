from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast

import duckdb
import polars as pl

from ..catalog.collection import Catalog
from ..catalog.relations import (
    TABLE_SPECS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
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
    shells, and the MCP server exposes the same methods as tools for agents.
    """

    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog

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
                    f"CLI: chartcoach tables values {table} {column} --source PATH --explode --format jsonl",
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
                        "Run chartcoach tables list --source PATH to inspect table names.",
                        "Run chartcoach tables schema --source PATH --format jsonl to inspect columns.",
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
                    "Inspect the guideline_labels table through DuckDB or Polars.",
                    "CLI: chartcoach tables values guideline_labels label --source PATH --format jsonl",
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
                    "Inspect the guideline_labels table through DuckDB or Polars.",
                    "CLI: chartcoach tables values guideline_labels label --source PATH --format jsonl",
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
                    "Inspect the sections table through DuckDB or Polars.",
                    "CLI: chartcoach tables values sections role --source PATH --format jsonl",
                ],
            )

    def _unknown_table_error(self, tables: Sequence[str]) -> CatalogToolError:
        available = ", ".join(catalog_table_names())
        return CatalogToolError(
            f"Unknown table(s): {', '.join(tables)}",
            hints=[
                f"Available tables: {available}",
                "Run chartcoach tables list before schema.",
                "CLI: chartcoach tables list --source PATH --format jsonl",
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
                f"Run schema with table={table!r} before querying the catalog.",
                f"CLI: chartcoach tables schema --source PATH --table {table} --format jsonl",
            ],
        )

    def _unknown_id_error(self, guideline_id: str) -> CatalogToolError:
        return CatalogToolError(
            f"Unknown guideline id: {guideline_id}",
            hints=[
                "Discover ids with list_guidelines.",
                "CLI: chartcoach guidelines list --source PATH --format jsonl | head",
                "Search by text with search_guidelines or semantic search.",
            ],
        )


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


def format_tool_error(message: str, hints: Sequence[str]) -> str:
    """Render an error message and recovery hints for CLI and MCP transports."""

    if not hints:
        return message
    joined_hints = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nTry:\n{joined_hints}"


def search_error_message(message: str) -> str:
    """Return a semantic-search error message with index recovery commands."""

    return format_tool_error(
        message,
        [
            "If the search index is missing, run: chartcoach index build --source PATH --index-dir INDEX_DIR.",
            "Use chartcoach artifacts --source PATH --index-dir INDEX_DIR to locate the native Chroma path.",
        ],
    )


def _is_list_dtype(dtype: object) -> bool:
    return str(dtype).startswith("List")


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
                "Use chartcoach catalog duckdb --source PATH --out PATH for durable DuckDB files.",
                "Use chartcoach tables schema --source PATH --format jsonl to inspect columns.",
            ],
        )


__all__ = [
    "CatalogToolError",
    "CatalogTools",
    "format_tool_error",
    "search_error_message",
]

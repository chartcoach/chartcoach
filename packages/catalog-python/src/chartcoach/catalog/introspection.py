from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

import polars as pl

from .errors import CatalogLookupError
from .relations import (
    TABLE_SPECS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)

if TYPE_CHECKING:
    from .collection import Catalog

VALUE_ALIASES: Mapping[str, tuple[str, str, bool]] = {
    "labels": ("guideline_labels", "label", False),
    "roles": ("sections", "role", False),
    "label": ("guideline_labels", "label", False),
    "label.family": ("guideline_labels", "family", False),
    "label.category": ("guideline_labels", "category", False),
    "label.modifier": ("guideline_labels", "modifier", False),
}


def list_tables(
    catalog: "Catalog", *, include_row_counts: bool = False
) -> list[dict[str, object]]:
    if include_row_counts:
        return catalog_table_rows(catalog)
    return [
        {"name": spec.name, "columns": len(spec.schema), "rows": None}
        for spec in TABLE_SPECS.values()
    ]


def describe_tables(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    try:
        return catalog_table_schema(tables)
    except KeyError as exc:
        raise unknown_table_error([str(exc).strip("'")]) from exc


def parse_value_field(field: str) -> tuple[str, str, bool]:
    if field in VALUE_ALIASES:
        return VALUE_ALIASES[field]
    if "." not in field:
        raise CatalogLookupError(
            f"Unknown catalog value field: {field}",
            hints=[
                "FIELD names the value dimension to count, not the observed value to find.",
                "Use aliases such as labels, roles, label.family, label.category, or label.modifier.",
                "Filter values with `--contains TEXT`, for example `chartcoach catalog values labels --contains TEXT`.",
                "Use `chartcoach catalog labels --family FAMILY` to inspect one label family.",
                "Use raw table fields as TABLE.COLUMN after inspecting `chartcoach catalog schema`.",
            ],
        )
    table, column = field.split(".", 1)
    if not table or not column:
        raise CatalogLookupError("Value fields must be aliases or TABLE.COLUMN.")
    return table, column, False


def count_values(
    catalog: "Catalog",
    table: str,
    column: str,
    *,
    explode: bool = False,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    frame = require_table(catalog, table)
    require_column(table, frame, column)
    dtype = frame.schema[column]
    value_expr = (
        pl.col(column).explode() if explode or _is_list_dtype(dtype) else pl.col(column)
    )
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
        .with_columns(pl.lit(table).alias("table"), pl.lit(column).alias("column"))
        .select("table", "column", "value", "rows")
        .to_dicts()
    )


def require_table(catalog: "Catalog", table: str) -> pl.DataFrame:
    if table not in catalog_table_names():
        raise unknown_table_error([table])
    return catalog.table(table)


def require_column(table: str, frame: pl.DataFrame, column: str) -> None:
    if column not in frame.columns:
        columns = ", ".join(frame.columns)
        hints = [
            f"Available columns on {table}: {columns}",
            "Run `chartcoach catalog schema` to inspect fields.",
        ]
        if table == "labels" and column == "label":
            hints.append(
                "Use `chartcoach catalog values labels` or `chartcoach catalog values guideline_labels.label` for full label strings."
            )
            hints.append(
                "Use `chartcoach catalog values label.family` for label family names."
            )
        raise CatalogLookupError(
            f"Unknown column for table {table}: {column}",
            hints=hints,
        )


def unknown_table_error(tables: Sequence[str]) -> CatalogLookupError:
    available = ", ".join(catalog_table_names())
    return CatalogLookupError(
        f"Unknown table(s): {', '.join(tables)}",
        hints=[
            f"Available tables: {available}",
            "Run `chartcoach catalog schema --tables` to inspect tables.",
        ],
    )


def _is_list_dtype(dtype: object) -> bool:
    return isinstance(dtype, pl.DataType) and dtype.base_type() == pl.List

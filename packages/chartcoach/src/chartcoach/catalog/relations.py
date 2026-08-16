from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import TYPE_CHECKING

import polars as pl

from .schemas import (
    GUIDELINE_LABELS_SCHEMA,
    GUIDELINE_REFERENCES_SCHEMA,
    GUIDELINE_SOURCES_SCHEMA,
    GUIDELINES_SCHEMA,
    REFERENCES_SCHEMA,
    SECTIONS_SCHEMA,
)

if TYPE_CHECKING:
    from .collection import Catalog

TABLE_SCHEMAS: dict[str, Mapping[str, object]] = {
    "guidelines": GUIDELINES_SCHEMA,
    "sections": SECTIONS_SCHEMA,
    "guideline_labels": GUIDELINE_LABELS_SCHEMA,
    "references": REFERENCES_SCHEMA,
    "guideline_references": GUIDELINE_REFERENCES_SCHEMA,
    "guideline_sources": GUIDELINE_SOURCES_SCHEMA,
}


def catalog_table_names() -> tuple[str, ...]:
    """Return queryable catalog table names."""

    return tuple(TABLE_SCHEMAS)


def catalog_table(catalog: Catalog, name: str) -> pl.DataFrame:
    """Return one catalog table by name."""

    if name not in TABLE_SCHEMAS:
        raise KeyError(name)
    return getattr(catalog, name)()


def catalog_table_rows(catalog: Catalog) -> list[dict[str, object]]:
    """Return table names and row counts."""

    return [
        {"name": name, "rows": catalog_table(catalog, name).height}
        for name in TABLE_SCHEMAS
    ]


def catalog_table_schema(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    """Return column schemas."""

    selected = set(tables)
    unknown = sorted(selected - set(TABLE_SCHEMAS))
    if unknown:
        raise KeyError(", ".join(unknown))

    rows: list[dict[str, object]] = []
    for name, schema in TABLE_SCHEMAS.items():
        if selected and name not in selected:
            continue
        for column, dtype in schema.items():
            rows.append({"table": name, "column": column, "type": str(dtype)})
    return rows


def iter_catalog_tables(catalog: Catalog) -> Iterable[tuple[str, pl.DataFrame]]:
    """Yield each catalog table for exports."""

    for name in TABLE_SCHEMAS:
        yield name, catalog_table(catalog, name)


__all__ = [
    "TABLE_SCHEMAS",
    "catalog_table",
    "catalog_table_names",
    "catalog_table_rows",
    "catalog_table_schema",
    "iter_catalog_tables",
]

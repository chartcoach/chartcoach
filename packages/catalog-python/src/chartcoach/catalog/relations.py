from __future__ import annotations

import dataclasses as dc
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import TYPE_CHECKING

import polars as pl

from .tables import (
    FORMATTED_REFERENCES_SCHEMA,
    GUIDELINES_SCHEMA,
    GUIDELINE_LABELS_SCHEMA,
    GUIDELINE_REFERENCES_SCHEMA,
    GUIDELINE_SOURCES_SCHEMA,
    LABELS_SCHEMA,
    REFERENCES_SCHEMA,
    SECTIONS_SCHEMA,
)

if TYPE_CHECKING:
    from .collection import Catalog

GUIDELINES_RELATION = "guidelines"
SECTIONS_RELATION = "sections"
LABELS_RELATION = "labels"
GUIDELINE_LABELS_RELATION = "guideline_labels"
REFERENCES_RELATION = "references"
FORMATTED_REFERENCES_RELATION = "formatted_references"
GUIDELINE_REFERENCES_RELATION = "guideline_references"
GUIDELINE_SOURCES_RELATION = "guideline_sources"

TableLoader = Callable[["Catalog"], pl.DataFrame]
RowCounter = Callable[["Catalog"], int | None]


@dc.dataclass(frozen=True, slots=True)
class CatalogTableSpec:
    name: str
    schema: Mapping[str, object]
    load: TableLoader
    row_count: RowCounter


TABLE_SPECS: dict[str, CatalogTableSpec] = {
    GUIDELINES_RELATION: CatalogTableSpec(
        name=GUIDELINES_RELATION,
        schema=GUIDELINES_SCHEMA,
        load=lambda catalog: catalog.guidelines(),
        row_count=lambda catalog: len(catalog),
    ),
    SECTIONS_RELATION: CatalogTableSpec(
        name=SECTIONS_RELATION,
        schema=SECTIONS_SCHEMA,
        load=lambda catalog: catalog.sections(),
        row_count=lambda catalog: catalog.sections().height,
    ),
    LABELS_RELATION: CatalogTableSpec(
        name=LABELS_RELATION,
        schema=LABELS_SCHEMA,
        load=lambda catalog: catalog.labels(),
        row_count=lambda catalog: catalog.labels().height,
    ),
    GUIDELINE_LABELS_RELATION: CatalogTableSpec(
        name=GUIDELINE_LABELS_RELATION,
        schema=GUIDELINE_LABELS_SCHEMA,
        load=lambda catalog: catalog.guideline_labels(),
        row_count=lambda catalog: catalog.guideline_labels().height,
    ),
    REFERENCES_RELATION: CatalogTableSpec(
        name=REFERENCES_RELATION,
        schema=REFERENCES_SCHEMA,
        load=lambda catalog: catalog.references(),
        row_count=lambda catalog: catalog.references().height,
    ),
    FORMATTED_REFERENCES_RELATION: CatalogTableSpec(
        name=FORMATTED_REFERENCES_RELATION,
        schema=FORMATTED_REFERENCES_SCHEMA,
        load=lambda catalog: catalog.formatted_references(),
        row_count=lambda catalog: catalog.references().height,
    ),
    GUIDELINE_REFERENCES_RELATION: CatalogTableSpec(
        name=GUIDELINE_REFERENCES_RELATION,
        schema=GUIDELINE_REFERENCES_SCHEMA,
        load=lambda catalog: catalog.guideline_references(),
        row_count=lambda catalog: catalog.guideline_references().height,
    ),
    GUIDELINE_SOURCES_RELATION: CatalogTableSpec(
        name=GUIDELINE_SOURCES_RELATION,
        schema=GUIDELINE_SOURCES_SCHEMA,
        load=lambda catalog: catalog.guideline_sources(),
        row_count=lambda catalog: catalog.guideline_sources().height,
    ),
}


def catalog_table_names() -> tuple[str, ...]:
    """Return queryable catalog table names."""

    return tuple(TABLE_SPECS)


def catalog_table(catalog: Catalog, name: str) -> pl.DataFrame:
    """Return one catalog table by name."""

    return _require_table(name).load(catalog)


def catalog_table_rows(catalog: Catalog) -> list[dict[str, object]]:
    """Return table names and row counts."""

    return [
        {"name": spec.name, "rows": spec.row_count(catalog)}
        for spec in TABLE_SPECS.values()
    ]


def catalog_table_schema(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    """Return column schemas."""

    selected = set(tables)
    unknown = sorted(selected - set(TABLE_SPECS))
    if unknown:
        raise KeyError(", ".join(unknown))

    rows: list[dict[str, object]] = []
    for spec in TABLE_SPECS.values():
        if selected and spec.name not in selected:
            continue
        for column, dtype in spec.schema.items():
            rows.append({"table": spec.name, "column": column, "type": str(dtype)})
    return rows


def iter_catalog_tables(catalog: Catalog) -> Iterable[tuple[str, pl.DataFrame]]:
    """Yield each catalog table for exports."""

    for name in TABLE_SPECS:
        yield name, catalog_table(catalog, name)


def _require_table(name: str) -> CatalogTableSpec:
    try:
        return TABLE_SPECS[name]
    except KeyError as exc:
        raise KeyError(name) from exc


__all__ = [
    "CatalogTableSpec",
    "FORMATTED_REFERENCES_RELATION",
    "GUIDELINES_RELATION",
    "GUIDELINE_LABELS_RELATION",
    "GUIDELINE_REFERENCES_RELATION",
    "GUIDELINE_SOURCES_RELATION",
    "LABELS_RELATION",
    "REFERENCES_RELATION",
    "SECTIONS_RELATION",
    "TABLE_SPECS",
    "catalog_table",
    "catalog_table_names",
    "catalog_table_rows",
    "catalog_table_schema",
    "iter_catalog_tables",
]

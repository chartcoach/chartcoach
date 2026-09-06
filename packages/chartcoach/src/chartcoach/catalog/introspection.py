from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from .errors import CatalogLookupError
from .relations import (
    TABLE_SCHEMAS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)

if TYPE_CHECKING:
    from .collection import Catalog


def list_tables(
    catalog: "Catalog", *, include_row_counts: bool = False
) -> list[dict[str, object]]:
    if include_row_counts:
        return catalog_table_rows(catalog)
    return [
        {"name": name, "columns": len(schema), "rows": None}
        for name, schema in TABLE_SCHEMAS.items()
    ]


def describe_tables(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    try:
        return catalog_table_schema(tables)
    except KeyError as exc:
        raise unknown_table_error([str(exc).strip("'")]) from exc


def unknown_table_error(tables: Sequence[str]) -> CatalogLookupError:
    available = ", ".join(catalog_table_names())
    return CatalogLookupError(
        f"Unknown table(s): {', '.join(tables)}",
        hints=[
            f"Available tables: {available}",
            "Run `chartcoach catalog schema --tables` to inspect tables.",
        ],
    )

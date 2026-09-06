from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from .errors import CatalogLookupError, require_string_sequence
from .relations import (
    TABLE_SCHEMAS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)

if TYPE_CHECKING:
    from .collection import Catalog


def list_tables(
    catalog: Catalog, *, include_row_counts: bool = False
) -> list[dict[str, object]]:
    """Return query-table names and optional row counts.

    The default rows contain `name`, `columns`, and a null `rows` value.
    `include_row_counts=True` returns `name` and the current `rows` count.
    """

    if include_row_counts:
        return catalog_table_rows(catalog)
    return [
        {"name": name, "columns": len(schema), "rows": None}
        for name, schema in TABLE_SCHEMAS.items()
    ]


def describe_tables(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    """Return the static column contract for selected query tables."""

    require_string_sequence("tables", tables)
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
            "Call `chartcoach.agent.describe_tables()` to inspect tables in Python.",
            "Run `chartcoach catalog schema --tables` to inspect tables.",
        ],
    )

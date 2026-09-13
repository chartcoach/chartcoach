from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl

from .query import distinct_strings, unknown_label_family_error

if TYPE_CHECKING:
    from .model import Catalog


def validation_rows(catalog: Catalog) -> list[dict[str, object]]:
    manifest = catalog.manifest
    return [
        {"name": "manifest_section_roles", "rows": len(manifest.section_roles)},
        {"name": "manifest_label_families", "rows": len(manifest.label_families)},
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.table("sections").height},
        {"name": "references", "rows": catalog.table("references").height},
    ]


def list_labels(
    catalog: Catalog,
    *,
    family: str | None = None,
    prefix: str | None = None,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    """Return label counts after optional family, prefix, and text filters."""

    available_families = distinct_strings(
        catalog, table="guideline_labels", column="family"
    )
    if family is not None and family not in available_families:
        raise unknown_label_family_error(catalog, family)

    frame = catalog.table("guideline_labels")
    if family is not None:
        frame = frame.filter(pl.col("family") == family)
    if prefix is not None:
        frame = frame.filter(pl.col("label").str.starts_with(prefix))
    if contains is not None:
        needle = contains.lower()
        frame = frame.filter(
            pl.col("label").str.to_lowercase().str.contains(needle, literal=True)
        )
    return (
        frame.group_by("label", "family", "category", "modifier")
        .len("entries")
        .sort(["entries", "label"], descending=[True, False])
        .head(limit)
        .to_dicts()
    )


def list_roles(catalog: Catalog) -> list[dict[str, object]]:
    """Return each manifest section role with its guideline count and purpose."""

    count_rows = (
        catalog.table("sections")
        .group_by("role")
        .len("entries")
        .sort("role")
        .to_dicts()
    )
    counts = {str(row["role"]): row["entries"] for row in count_rows}
    return [
        {
            "role": role,
            "entries": counts.get(role, 0),
            "use": _first_sentence(definition.description),
        }
        for role, definition in catalog.manifest.section_roles.items()
    ]


def _first_sentence(text: str) -> str:
    stripped = " ".join(text.split())
    if "." not in stripped:
        return stripped
    return stripped.split(".", 1)[0] + "."


__all__ = [
    "list_labels",
    "list_roles",
    "validation_rows",
]

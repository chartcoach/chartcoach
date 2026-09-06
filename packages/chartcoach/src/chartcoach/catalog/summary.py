from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, cast

import polars as pl

from .query import distinct_strings, unknown_label_family_error

if TYPE_CHECKING:
    from .collection import Catalog


def catalog_overview(
    catalog: Catalog,
    *,
    source: str,
    release_digest: str | None = None,
) -> dict[str, object]:
    """Return catalog identity, primary table counts, roles, and label families.

    `release_digest` defaults to the digest carried by a release-backed
    catalog. The three table counts summarize authored guideline content. Use
    `list_tables(catalog, include_row_counts=True)` for all query tables.
    """

    manifest = catalog.manifest
    resolved_release_digest = release_digest
    if resolved_release_digest is None and catalog.release is not None:
        resolved_release_digest = catalog.release.digest
    return {
        "source": source,
        "release_digest": resolved_release_digest,
        "content_digest": catalog.content_digest(),
        "tables": overview_table_count_rows(catalog),
        "section_roles": list(manifest.section_roles),
        "label_families": list(manifest.label_families),
    }


def overview_table_count_rows(catalog: Catalog) -> list[dict[str, object]]:
    return [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "guideline_labels", "rows": catalog.guideline_labels().height},
    ]


def overview_table_rows(overview: Mapping[str, object]) -> list[dict[str, object]]:
    table_counts = {
        str(row["name"]): row["rows"]
        for row in cast(Sequence[Mapping[str, object]], overview["tables"])
    }
    return [
        {"name": "source", "value": overview["source"]},
        {"name": "release_digest", "value": overview["release_digest"]},
        {"name": "content_digest", "value": overview["content_digest"]},
        *[
            {"name": f"table.{name}", "value": rows}
            for name, rows in table_counts.items()
        ],
        {"name": "section_roles", "value": overview["section_roles"]},
        {"name": "label_families", "value": overview["label_families"]},
    ]


def validation_rows(catalog: Catalog) -> list[dict[str, object]]:
    manifest = catalog.manifest
    return [
        {"name": "manifest_section_roles", "rows": len(manifest.section_roles)},
        {"name": "manifest_label_families", "rows": len(manifest.label_families)},
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "references", "rows": catalog.references().height},
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

    frame = catalog.guideline_labels()
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
        catalog.sections().group_by("role").len("entries").sort("role").to_dicts()
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
    "catalog_overview",
    "list_labels",
    "list_roles",
    "overview_table_count_rows",
    "overview_table_rows",
    "validation_rows",
]

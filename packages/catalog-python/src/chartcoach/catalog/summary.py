from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, cast

import polars as pl

from .query import distinct_strings, unknown_label_family_error

if TYPE_CHECKING:
    from .collection import Catalog


def catalog_overview(catalog: "Catalog", *, source: str | None) -> dict[str, object]:
    manifest = catalog.manifest
    section_roles = (
        list(manifest.section_roles)
        if manifest is not None
        else sorted(distinct_strings(catalog, table="sections", column="role"))
    )
    label_families = (
        list(manifest.label_families)
        if manifest is not None
        else sorted(
            distinct_strings(catalog, table="guideline_labels", column="family")
        )
    )
    return {
        "source": source,
        "catalog_digest": catalog.digest(),
        "tables": overview_table_count_rows(catalog),
        "section_roles": section_roles,
        "label_families": label_families,
    }


def overview_table_count_rows(catalog: "Catalog") -> list[dict[str, object]]:
    return [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "guideline_labels", "rows": catalog.guideline_labels().height},
    ]


def overview_table_rows(overview: Mapping[str, object]) -> list[dict[str, object]]:
    table_counts = {
        str(row["name"]): row["rows"]
        for row in cast(Sequence[Mapping[str, object]], overview["tables"])
    }
    return [
        {"name": "source", "value": overview.get("source") or "default"},
        {"name": "catalog_digest", "value": overview["catalog_digest"]},
        *[
            {"name": f"table.{name}", "value": rows}
            for name, rows in table_counts.items()
        ],
        {"name": "section_roles", "value": overview["section_roles"]},
        {"name": "label_families", "value": overview["label_families"]},
    ]


def validation_rows(catalog: "Catalog") -> list[dict[str, object]]:
    manifest = catalog.manifest
    rows: list[dict[str, object]] = [
        {"name": "guidelines", "rows": len(catalog)},
        {"name": "sections", "rows": catalog.sections().height},
        {"name": "labels", "rows": catalog.labels().height},
        {"name": "references", "rows": catalog.references().height},
    ]
    if manifest is not None:
        rows.insert(
            0, {"name": "manifest_section_roles", "rows": len(manifest.section_roles)}
        )
        rows.insert(
            1, {"name": "manifest_label_families", "rows": len(manifest.label_families)}
        )
    return rows


def list_labels(
    catalog: "Catalog",
    *,
    family: str | None = None,
    prefix: str | None = None,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
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


def list_roles(catalog: "Catalog") -> list[dict[str, object]]:
    count_rows = (
        catalog.sections().group_by("role").len("entries").sort("role").to_dicts()
    )
    counts = {str(row["role"]): row["entries"] for row in count_rows}
    manifest = catalog.manifest
    definitions = manifest.section_roles if manifest is not None else {}
    role_names = list(definitions) if definitions else sorted(counts)
    return [
        {
            "role": role,
            "entries": counts.get(role, 0),
            "use": _first_sentence(definitions[role].description)
            if role in definitions
            else "",
        }
        for role in role_names
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

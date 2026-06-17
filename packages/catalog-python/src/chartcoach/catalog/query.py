from __future__ import annotations

from collections.abc import Mapping, Sequence
from difflib import SequenceMatcher
from typing import TYPE_CHECKING, cast

import polars as pl

from .errors import CatalogLookupError
from .labels import parse_label

if TYPE_CHECKING:
    from .collection import Catalog


def query_entries(
    catalog: "Catalog",
    *,
    ids: Sequence[str] = (),
    labels: Sequence[str] = (),
    any_labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    contains: str | None = None,
    body_contains: str | None = None,
    section_contains: str | None = None,
    limit: int = 50,
    include_body: bool = True,
) -> pl.DataFrame:
    validate_filters(
        catalog, labels=labels, any_labels=any_labels, label_prefixes=label_prefixes
    )
    validate_ids(catalog, ids)
    df = catalog.guidelines()
    if ids:
        order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
        df = order.join(df, on="id", how="inner").sort("_catalog_order")
    for label in labels:
        df = df.filter(pl.col("labels").list.contains(label))
    if any_labels:
        df = df.filter(
            pl.any_horizontal(
                *(pl.col("labels").list.contains(label) for label in any_labels)
            )
        )
    for prefix in label_prefixes:
        df = df.filter(
            pl.col("labels").list.eval(pl.element().str.starts_with(prefix)).list.any()
        )
    if contains:
        needle = contains.lower()
        df = df.filter(
            pl.any_horizontal(
                pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("description")
                .str.to_lowercase()
                .str.contains(needle, literal=True),
            )
        )
    if body_contains:
        needle = body_contains.lower()
        df = df.filter(
            pl.col("body").str.to_lowercase().str.contains(needle, literal=True)
        )
    if section_contains:
        matching_ids = _section_matching_ids(catalog, section_contains)
        df = df.filter(pl.col("id").is_in(matching_ids))
    references = catalog.to_frame().select("id", "references")
    selected = (
        df.head(limit)
        .join(references, on="id", how="left")
        .drop("_catalog_order", strict=False)
    )
    if not include_body:
        selected = selected.drop("body", "sections", "references", strict=False)
    return selected


def text_matches_for_entry(
    row: Mapping[str, object],
    *,
    contains: str | None = None,
    body_contains: str | None = None,
    section_contains: str | None = None,
) -> list[dict[str, object]]:
    matches: list[dict[str, object]] = []
    if contains:
        for field in ("id", "title", "description"):
            snippet = _snippet(str(row.get(field) or ""), contains)
            if snippet is not None:
                matches.append(
                    {
                        "predicate": "contains",
                        "field": field,
                        "query": contains,
                        "snippet": snippet,
                    }
                )
    if body_contains:
        snippet = _snippet(str(row.get("body") or ""), body_contains)
        if snippet is not None:
            matches.append(
                {
                    "predicate": "body-contains",
                    "field": "body",
                    "query": body_contains,
                    "snippet": snippet,
                }
            )
    if section_contains:
        for section in cast(Sequence[Mapping[str, object]], row.get("sections") or ()):
            role = str(section.get("role") or "")
            title = str(section.get("title") or "")
            title_snippet = _snippet(title, section_contains)
            if title_snippet is not None:
                matches.append(
                    {
                        "predicate": "section-contains",
                        "field": "section.title",
                        "role": role,
                        "title": title,
                        "query": section_contains,
                        "snippet": title_snippet,
                    }
                )
            content_snippet = _snippet(
                str(section.get("content") or ""), section_contains
            )
            if content_snippet is not None:
                matches.append(
                    {
                        "predicate": "section-contains",
                        "field": "section.content",
                        "role": role,
                        "title": title,
                        "query": section_contains,
                        "snippet": content_snippet,
                    }
                )
    return matches


def _section_matching_ids(catalog: "Catalog", contains: str) -> list[str]:
    needle = contains.lower()
    return (
        catalog.sections()
        .filter(
            pl.any_horizontal(
                pl.col("title").str.to_lowercase().str.contains(needle, literal=True),
                pl.col("content").str.to_lowercase().str.contains(needle, literal=True),
            )
        )
        .get_column("guideline_id")
        .unique()
        .to_list()
    )


def _snippet(text: str, needle: str, *, radius: int = 48) -> str | None:
    normalized = " ".join(text.split())
    index = normalized.lower().find(needle.lower())
    if index < 0:
        return None
    start = max(0, index - radius)
    end = min(len(normalized), index + len(needle) + radius)
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(normalized) else ""
    return f"{prefix}{normalized[start:end]}{suffix}"


def validate_filters(
    catalog: "Catalog",
    *,
    labels: Sequence[str] = (),
    any_labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
) -> None:
    validate_labels(catalog, (*labels, *any_labels))
    validate_label_prefixes(catalog, label_prefixes)


def validate_ids(catalog: "Catalog", ids: Sequence[str]) -> None:
    if not ids:
        return
    available = set(catalog.guidelines().get_column("id").to_list())
    for guideline_id in ids:
        if guideline_id not in available:
            raise unknown_id_error(catalog, guideline_id)


def validate_labels(catalog: "Catalog", labels: Sequence[str]) -> None:
    if not labels:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = sorted(set(labels) - available)
    if missing:
        raise unknown_label_error(catalog, missing)


def validate_label_prefixes(catalog: "Catalog", prefixes: Sequence[str]) -> None:
    if not prefixes:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = [
        prefix
        for prefix in sorted(set(prefixes))
        if not any(label.startswith(prefix) for label in available)
    ]
    if missing:
        raise CatalogLookupError(
            f"No labels match prefix(es): {', '.join(missing)}",
            hints=[
                "Run `chartcoach catalog labels` to inspect valid labels.",
                "Run `chartcoach catalog labels --family FAMILY` after choosing a family.",
            ],
        )


def validate_section_roles(catalog: "Catalog", roles: Sequence[str]) -> None:
    if not roles:
        return
    available = (
        set(catalog.manifest.section_roles)
        if catalog.manifest is not None
        else distinct_strings(catalog, table="sections", column="role")
    )
    missing = sorted(set(roles) - available)
    if missing:
        raise CatalogLookupError(
            f"Unknown section role(s): {', '.join(missing)}",
            hints=[
                "Valid roles: " + ", ".join(sorted(available)),
                "Run `chartcoach catalog roles` to inspect section roles.",
            ],
        )


def distinct_strings(catalog: "Catalog", *, table: str, column: str) -> set[str]:
    frame = catalog.table(table)
    value_expr = pl.col(column)
    if frame.schema[column].base_type() == pl.List:
        value_expr = value_expr.explode()
    values = (
        frame.select(value_expr.alias("value"))
        .filter(pl.col("value").is_not_null())
        .with_columns(pl.col("value").cast(pl.String).alias("value"))
        .get_column("value")
        .to_list()
    )
    return {value for value in values if isinstance(value, str)}


def unknown_id_error(catalog: "Catalog", guideline_id: str) -> CatalogLookupError:
    suggestions = nearest_values(
        guideline_id,
        [str(value) for value in catalog.guidelines().get_column("id").to_list()],
    )
    hints = []
    if suggestions:
        hints.append("Nearest entry ids: " + ", ".join(suggestions))
    hints.extend(
        [
            "Copy ids exactly from `chartcoach catalog list` or `chartcoach catalog query`.",
            "Run `chartcoach catalog read ID` with exact ids.",
        ]
    )
    return CatalogLookupError(f"Unknown entry id: {guideline_id}", hints=hints)


def unknown_label_error(
    catalog: "Catalog", labels: Sequence[str]
) -> CatalogLookupError:
    available = sorted(
        distinct_strings(catalog, table="guideline_labels", column="label")
    )
    hints: list[str] = []
    for label in labels:
        suggestions = nearest_values(label, available)
        if suggestions:
            hints.append(f"Nearest labels for {label}: " + ", ".join(suggestions))
        try:
            family = parse_label(label, context=f"label {label!r}").family
        except (TypeError, ValueError):
            family = None
        if family:
            hints.append(
                f"Run `chartcoach catalog labels --family {family}` to inspect that family."
            )
    hints.append("Run `chartcoach catalog labels` to inspect valid labels.")
    return CatalogLookupError(f"Unknown label(s): {', '.join(labels)}", hints=hints)


def unknown_label_family_error(catalog: "Catalog", family: str) -> CatalogLookupError:
    available = sorted(
        distinct_strings(catalog, table="guideline_labels", column="family")
    )
    suggestions = nearest_values(family, available)
    hints = ["Available label families: " + ", ".join(available)]
    if suggestions:
        hints.append("Nearest label families: " + ", ".join(suggestions))
    return CatalogLookupError(f"Unknown label family: {family}", hints=hints)


def nearest_values(
    value: str, candidates: Sequence[str], *, limit: int = 3
) -> list[str]:
    scored = [
        (SequenceMatcher(a=value, b=candidate).ratio(), candidate)
        for candidate in candidates
    ]
    return [
        candidate
        for score, candidate in sorted(scored, key=lambda item: (-item[0], item[1]))
        if score > 0
    ][:limit]


__all__ = [
    "distinct_strings",
    "nearest_values",
    "query_entries",
    "text_matches_for_entry",
    "unknown_id_error",
    "unknown_label_error",
    "unknown_label_family_error",
    "validate_filters",
    "validate_ids",
    "validate_label_prefixes",
    "validate_labels",
    "validate_section_roles",
]

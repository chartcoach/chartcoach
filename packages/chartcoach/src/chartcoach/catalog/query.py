from __future__ import annotations

import re
from collections.abc import Sequence
from difflib import SequenceMatcher
from typing import TYPE_CHECKING

import polars as pl

from ._polars import explode_expr
from .errors import (
    CatalogLookupError,
    CatalogValidationError,
    require_string_sequence,
)
from .labels import parse_label

if TYPE_CHECKING:
    from .collection import Catalog


def query_entries(
    catalog: Catalog,
    *,
    ids: Sequence[str] = (),
    labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
    contains: str | None = None,
    limit: int = 50,
    include_body: bool = True,
) -> pl.DataFrame:
    """Return guideline rows selected by exact filters and a text substring.

    The result is a Polars DataFrame in catalog order, or in requested ID order
    when `ids` is supplied. `include_body=False` returns the compact `id`,
    `title`, `description`, and `labels` fields. An empty match returns an empty
    DataFrame with the same schema. Text matching is case-insensitive and
    treats whitespace, hyphens, and underscores as equivalent separators.
    """

    if limit < 1:
        raise CatalogValidationError("Query limit must be at least 1.")
    validate_filters(catalog, labels=labels, label_prefixes=label_prefixes)
    validate_ids(catalog, ids)
    df = catalog.guidelines()
    if ids:
        order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
        df = order.join(df, on="id", how="inner").sort("_catalog_order")
    for label in labels:
        df = df.filter(pl.col("labels").list.contains(label))
    for prefix in label_prefixes:
        df = df.filter(
            pl.col("labels").list.eval(pl.element().str.starts_with(prefix)).list.any()
        )
    if contains:
        needle = _normalize_search_text(contains)
        if not needle:
            raise CatalogValidationError(
                "contains must not consist only of whitespace, hyphens, or underscores."
            )
        df = df.filter(
            pl.any_horizontal(
                *(
                    _normalized_search_column(column).str.contains(
                        needle,
                        literal=True,
                    )
                    for column in ("id", "title", "description")
                ),
            )
        )
    references = catalog.to_frame().select("id", "references")
    selected = (
        df.head(limit)
        .join(references, on="id", how="left")
        .drop("_catalog_order", strict=False)
    )
    if not include_body:
        selected = selected.drop("body", "sections", "references", strict=False)
    return selected


def validate_filters(
    catalog: Catalog,
    *,
    labels: Sequence[str] = (),
    label_prefixes: Sequence[str] = (),
) -> None:
    validate_labels(catalog, labels)
    validate_label_prefixes(catalog, label_prefixes)


def validate_ids(catalog: Catalog, ids: Sequence[str]) -> None:
    require_string_sequence("ids", ids)
    if not ids:
        return
    available = set(catalog.guidelines().get_column("id").to_list())
    for guideline_id in ids:
        if guideline_id not in available:
            raise unknown_id_error(catalog, guideline_id)


def validate_labels(catalog: Catalog, labels: Sequence[str]) -> None:
    require_string_sequence("labels", labels)
    if not labels:
        return
    available = distinct_strings(catalog, table="guideline_labels", column="label")
    missing = sorted(set(labels) - available)
    if missing:
        raise unknown_label_error(catalog, missing)


def validate_label_prefixes(catalog: Catalog, prefixes: Sequence[str]) -> None:
    require_string_sequence("label_prefixes", prefixes)
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
                "Call `chartcoach.agent.list_labels(catalog)` to inspect labels in Python.",
                "Run `chartcoach catalog labels` to inspect valid labels.",
                "Run `chartcoach catalog labels --family FAMILY` after choosing a family.",
            ],
        )


def validate_section_roles(catalog: Catalog, roles: Sequence[str]) -> None:
    require_string_sequence("roles", roles)
    if not roles:
        return
    available = set(catalog.manifest.section_roles)
    missing = sorted(set(roles) - available)
    if missing:
        raise CatalogLookupError(
            f"Unknown section role(s): {', '.join(missing)}",
            hints=[
                "Valid roles: " + ", ".join(sorted(available)),
                "Call `chartcoach.agent.list_roles(catalog)` to inspect roles in Python.",
                "Run `chartcoach catalog roles` to inspect section roles.",
            ],
        )


def distinct_strings(catalog: Catalog, *, table: str, column: str) -> set[str]:
    frame = catalog.table(table)
    value_expr = pl.col(column)
    if frame.schema[column].base_type() == pl.List:
        value_expr = explode_expr(value_expr)
    values = (
        frame.select(value_expr.alias("value"))
        .filter(pl.col("value").is_not_null())
        .with_columns(pl.col("value").cast(pl.String).alias("value"))
        .get_column("value")
        .to_list()
    )
    return {value for value in values if isinstance(value, str)}


def unknown_id_error(catalog: Catalog, guideline_id: str) -> CatalogLookupError:
    suggestions = nearest_values(
        guideline_id,
        [str(value) for value in catalog.guidelines().get_column("id").to_list()],
    )
    hints = []
    if suggestions:
        hints.append("Nearest entry ids: " + ", ".join(suggestions))
    hints.extend(
        [
            "Call `chartcoach.agent.query_entries(catalog, contains=...)` to inspect IDs in Python.",
            "Copy ids exactly from `chartcoach catalog list`.",
            "Run `chartcoach catalog read ID` with exact ids.",
        ]
    )
    return CatalogLookupError(f"Unknown entry id: {guideline_id}", hints=hints)


def unknown_label_error(catalog: Catalog, labels: Sequence[str]) -> CatalogLookupError:
    available = sorted(
        distinct_strings(catalog, table="guideline_labels", column="label")
    )
    available_families = distinct_strings(
        catalog,
        table="guideline_labels",
        column="family",
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
        if family in available_families:
            hints.append(
                f"Call `chartcoach.agent.list_labels(catalog, family={family!r})` in Python."
            )
            hints.append(
                f"Run `chartcoach catalog labels --family {family}` to inspect that family."
            )
    hints.extend(
        [
            "Call `chartcoach.agent.list_labels(catalog)` to inspect labels in Python.",
            "Run `chartcoach catalog labels` to inspect valid labels.",
        ]
    )
    return CatalogLookupError(f"Unknown label(s): {', '.join(labels)}", hints=hints)


def unknown_label_family_error(catalog: Catalog, family: str) -> CatalogLookupError:
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


def _normalize_search_text(value: str) -> str:
    return re.sub(r"[-_\s]+", " ", value.lower()).strip()


def _normalized_search_column(column: str) -> pl.Expr:
    return (
        pl.col(column)
        .str.to_lowercase()
        .str.replace_all(r"[-_\s]+", " ")
        .str.strip_chars()
    )


__all__ = [
    "distinct_strings",
    "nearest_values",
    "query_entries",
    "unknown_id_error",
    "unknown_label_error",
    "unknown_label_family_error",
    "validate_filters",
    "validate_ids",
    "validate_label_prefixes",
    "validate_labels",
    "validate_section_roles",
]

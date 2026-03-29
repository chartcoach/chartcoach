from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any

import polars as pl

from ..evaluation import overall_score_expr
from .spec import (
    DEFAULT_SELECTION,
    DEFAULT_SELECTION_DIMENSION_FILTERS,
    DIMENSION_SPECS,
    SCORE_BREAKDOWN_SPECS,
    VARIANT_SPECS,
    display_label,
    label_for_dimension,
)


def discover_registry(candidates_df: pl.DataFrame) -> dict[str, Any]:
    return {
        "vis_ids": _non_null_values(candidates_df, "vis_id"),
        "objectives": _sort_with_preference(
            _non_null_values(candidates_df, "objective"),
            DIMENSION_SPECS["objective"].get("order", {}),
        ),
    }


def default_selection_from_registry(registry: Mapping[str, Any]) -> dict[str, Any]:
    objective = _choose_requested_value(
        None,
        tuple(registry["objectives"]),
        preferred=DEFAULT_SELECTION["objective"],
    )
    return {
        "objective": objective,
        "request_chart": DEFAULT_SELECTION["request_chart"],
        "overview_variant": DEFAULT_SELECTION["overview_variant"],
        "dimension_filters": {
            key: value for key, value in DEFAULT_SELECTION_DIMENSION_FILTERS.items()
        },
    }


def build_catalog(
    candidates_df: pl.DataFrame,
    vis_ids: Sequence[str],
    *,
    request_chart_by_vis_id: Mapping[str, str | None] | None = None,
) -> list[dict[str, Any]]:
    catalog: list[dict[str, Any]] = []
    for vis_id in vis_ids:
        case_df = candidates_df.filter(pl.col("vis_id") == vis_id)
        query = case_df.item(0, "query")
        request_chart = (
            request_chart_by_vis_id.get(vis_id)
            if request_chart_by_vis_id is not None
            else _first_non_null(case_df.get_column("request_chart").to_list())
        )
        catalog.append(
            {
                "vis_id": vis_id,
                "nl_query": query,
                "request_chart": request_chart,
            }
        )
    return catalog


def enrich_candidates_with_scores(
    candidates_df: pl.DataFrame,
    judgements_df: pl.DataFrame | None,
) -> pl.DataFrame:
    if judgements_df is None or judgements_df.is_empty():
        return candidates_df

    if missing := ({"visgen_id", "judgement"} - set(judgements_df.columns)):
        raise ValueError(
            "Judgements are missing required viewer columns: "
            + ", ".join(sorted(missing))
            + "."
        )

    score_df = judgements_df.select(
        "visgen_id",
        "judgement",
        overall_score=overall_score_expr(
            source_columns=judgements_df.columns,
            round_to=2,
        ),
    )
    return candidates_df.join(score_df, on="visgen_id", how="left")


def normalize_selection(
    case_df: pl.DataFrame,
    *,
    registry: Mapping[str, Any],
    request_chart: str | None,
    objective: str | None,
    overview_variant: str | None,
    dimension_filters: Mapping[str, Any] | None,
    request_chart_options: Sequence[str | None],
) -> dict[str, Any]:
    defaults = default_selection_from_registry(registry)

    objective_options = tuple(
        _sort_with_preference(
            _non_null_values(case_df, "objective"),
            DIMENSION_SPECS["objective"].get("order", {}),
        )
    )
    chosen_objective = _choose_requested_value(
        objective,
        objective_options,
        preferred=defaults["objective"],
    )
    objective_df = apply_dimension_filters(case_df, {"objective": chosen_objective})

    requested_filters = dict(dimension_filters or {})
    audience_options = tuple(_values(objective_df, "audience"))
    chosen_audience = _choose_requested_value(
        requested_filters.get("audience"),
        audience_options,
        preferred=defaults["dimension_filters"]["audience"],
    )
    scoped_df = apply_dimension_filters(objective_df, {"audience": chosen_audience})

    valid_variants = [
        spec for spec in VARIANT_SPECS if _variant_is_valid(scoped_df, spec)
    ]
    if not valid_variants:
        raise ValueError("Viewer has no valid overview variant for the active slice.")

    valid_variant_ids = tuple(spec["id"] for spec in valid_variants)
    chosen_variant_id = _choose_requested_value(
        overview_variant,
        valid_variant_ids,
        preferred=defaults["overview_variant"],
    )
    chosen_variant = next(
        spec for spec in valid_variants if spec["id"] == chosen_variant_id
    )

    normalized_request_chart = (
        request_chart if request_chart in request_chart_options else None
    )
    selection = {
        "vis_id": str(case_df.item(0, "vis_id")),
        "request_chart": normalized_request_chart,
        "objective": chosen_objective,
        "overview_variant": chosen_variant["id"],
        "dimension_filters": {
            "audience": chosen_audience,
        },
    }
    return {
        "selection": selection,
        "objective_df": objective_df,
        "scoped_df": scoped_df,
        "variant": chosen_variant,
        "valid_variants": valid_variants,
    }


def build_ui_schema(
    *,
    registry: Mapping[str, Any],
    selection: Mapping[str, Any],
    valid_variants: Sequence[Mapping[str, Any]],
    request_chart_options: Sequence[str | None],
    variant: Mapping[str, Any],
    audience_options: Sequence[Any],
) -> dict[str, Any]:
    toolbar_pills = [
        {
            "id": "objective",
            "label": display_label("objective", selection["objective"]),
        }
    ]
    if len(valid_variants) > 1:
        toolbar_pills.append(
            {
                "id": "compare",
                "label": str(variant["label"]),
            }
        )

    scope_filters = [
        _filter_schema(
            dimension="request_chart",
            options=request_chart_options,
            value=selection["request_chart"],
        ),
        _filter_schema(
            dimension="objective",
            options=tuple(registry["objectives"]),
            value=selection["objective"],
        ),
    ]
    if len(audience_options) > 1:
        scope_filters.append(
            _filter_schema(
                dimension="audience",
                options=tuple(audience_options),
                value=selection["dimension_filters"].get("audience"),
            )
        )

    matrix_axes = {
        "group_label": (
            label_for_dimension(variant["group_dimension"])
            if variant.get("group_dimension")
            else None
        ),
        "row_label": label_for_dimension(variant["row_dimension"]),
        "column_label": label_for_dimension(variant["column_dimension"]),
    }

    schema: dict[str, Any] = {
        "toolbar": {"pills": toolbar_pills},
        "scope_filters": scope_filters,
        "matrix_axes": matrix_axes,
    }
    if len(valid_variants) > 1:
        schema["variant_controls"] = {
            "label": "Compare",
            "value": selection["overview_variant"],
            "options": [
                {
                    "value": spec["id"],
                    "label": str(spec["label"]),
                }
                for spec in valid_variants
            ],
        }
    return schema


def build_overview_matrix(
    *,
    objective_df: pl.DataFrame,
    scoped_df: pl.DataFrame,
    variant: Mapping[str, Any],
    image_loader: Callable[[dict[str, Any]], str],
    image_metadata_loader: Callable[[dict[str, Any]], dict[str, Any]],
) -> dict[str, Any]:
    group_dimension = variant.get("group_dimension")
    row_dimension = str(variant["row_dimension"])
    column_dimension = str(variant["column_dimension"])
    group_fields = (
        [str(group_dimension), row_dimension, column_dimension]
        if group_dimension
        else [row_dimension, column_dimension]
    )

    duplicate_cells = (
        scoped_df.group_by(*group_fields)
        .agg(pl.len().alias("count"))
        .filter(pl.col("count") > 1)
    )
    if not duplicate_cells.is_empty():
        raise ValueError(
            "Expected at most one candidate per overview cell, got "
            + str(duplicate_cells.to_dicts())
        )

    if group_dimension:
        available = {
            (
                record[str(group_dimension)],
                record[row_dimension],
                record[column_dimension],
            ): record
            for record in scoped_df.to_dicts()
        }
        group_values = _non_null_values(scoped_df, str(group_dimension))
        row_values = _non_null_values(scoped_df, row_dimension)
        column_values = _non_null_values(scoped_df, column_dimension)

        groups = []
        for group_value in group_values:
            rows = []
            for row_value in row_values:
                cells = []
                for column_value in column_values:
                    record = available.get((group_value, row_value, column_value))
                    cells.append(
                        _matrix_cell_payload(
                            objective_df=objective_df,
                            record=record,
                            group_dimension=str(group_dimension),
                            group_value=group_value,
                            row_dimension=row_dimension,
                            row_value=row_value,
                            column_dimension=column_dimension,
                            column_value=column_value,
                            image_loader=image_loader,
                            image_metadata_loader=image_metadata_loader,
                        )
                    )
                rows.append(
                    {
                        "value": row_value,
                        "label": display_label(row_dimension, row_value),
                        "cells": cells,
                    }
                )
            groups.append(
                {
                    "value": group_value,
                    "label": display_label(str(group_dimension), group_value),
                    "columns": [
                        {
                            "value": column_value,
                            "label": display_label(column_dimension, column_value),
                        }
                        for column_value in column_values
                    ],
                    "rows": rows,
                }
            )
        return {
            "kind": "grouped",
            "groups": groups,
        }

    available = {
        (record[row_dimension], record[column_dimension]): record
        for record in scoped_df.to_dicts()
    }
    row_values = _non_null_values(scoped_df, row_dimension)
    column_values = _non_null_values(scoped_df, column_dimension)
    rows = []
    for row_value in row_values:
        cells = []
        for column_value in column_values:
            record = available.get((row_value, column_value))
            cells.append(
                _matrix_cell_payload(
                    objective_df=objective_df,
                    record=record,
                    group_dimension=None,
                    group_value=None,
                    row_dimension=row_dimension,
                    row_value=row_value,
                    column_dimension=column_dimension,
                    column_value=column_value,
                    image_loader=image_loader,
                    image_metadata_loader=image_metadata_loader,
                )
            )
        rows.append(
            {
                "value": row_value,
                "label": display_label(row_dimension, row_value),
                "cells": cells,
            }
        )
    return {
        "kind": "flat",
        "columns": [
            {
                "value": column_value,
                "label": display_label(column_dimension, column_value),
            }
            for column_value in column_values
        ],
        "rows": rows,
    }


def serialize_candidate_record(
    record: Mapping[str, Any],
    *,
    image_loader: Callable[[dict[str, Any]], str],
    image_metadata_loader: Callable[[dict[str, Any]], dict[str, Any]],
) -> dict[str, Any]:
    judgement = record.get("judgement")
    payload: dict[str, Any] = {
        "visgen_id": str(record["visgen_id"]),
        "overall_score": record.get("overall_score"),
        "guideline_count": len(list(dict.fromkeys(record.get("guideline_ids") or []))),
        "score_breakdown": [
            {
                "id": spec["id"],
                "label": spec["label"],
                "dimension": spec["dimension"],
                "score": _score_value(
                    record=record,
                    judgement=judgement,
                    score_id=spec["id"],
                ),
            }
            for spec in SCORE_BREAKDOWN_SPECS
        ],
    }
    try:
        payload["image_url"] = image_loader(dict(record))
        payload["image_meta"] = image_metadata_loader(dict(record))
        payload["error"] = None
    except Exception as exc:
        payload["image_url"] = None
        payload["image_meta"] = None
        payload["error"] = str(exc)
    return payload


def apply_dimension_filters(
    df: pl.DataFrame,
    filters: Mapping[str, Any],
) -> pl.DataFrame:
    filtered = df
    for dimension, value in filters.items():
        if value is None:
            filtered = filtered.filter(pl.col(dimension).is_null())
        else:
            filtered = filtered.filter(pl.col(dimension) == value)
    return filtered


def _filter_schema(
    *,
    dimension: str,
    options: Sequence[Any],
    value: Any,
) -> dict[str, Any]:
    return {
        "id": dimension,
        "label": label_for_dimension(dimension),
        "value": value,
        "options": [
            {
                "value": option,
                "label": display_label(dimension, option),
            }
            for option in options
        ],
    }


def _matrix_cell_payload(
    *,
    objective_df: pl.DataFrame,
    record: Mapping[str, Any] | None,
    group_dimension: str | None,
    group_value: Any,
    row_dimension: str,
    row_value: Any,
    column_dimension: str,
    column_value: Any,
    image_loader: Callable[[dict[str, Any]], str],
    image_metadata_loader: Callable[[dict[str, Any]], dict[str, Any]],
) -> dict[str, Any]:
    return {
        "cell_key": _cell_key(group_value, row_value, column_value),
        "group_value": group_value,
        "group_label": (
            display_label(group_dimension, group_value) if group_dimension else None
        ),
        "row_value": row_value,
        "row_label": display_label(row_dimension, row_value),
        "column_value": column_value,
        "column_label": display_label(column_dimension, column_value),
        "missing": record is None,
        "placeholder_reason": (
            None
            if record is not None
            else _missing_reason(
                objective_df=objective_df,
                group_dimension=group_dimension,
                group_value=group_value,
                row_dimension=row_dimension,
                row_value=row_value,
                column_dimension=column_dimension,
                column_value=column_value,
            )
        ),
        "candidate": (
            None
            if record is None
            else serialize_candidate_record(
                record,
                image_loader=image_loader,
                image_metadata_loader=image_metadata_loader,
            )
        ),
    }


def _missing_reason(
    *,
    objective_df: pl.DataFrame,
    group_dimension: str | None,
    group_value: Any,
    row_dimension: str,
    row_value: Any,
    column_dimension: str,
    column_value: Any,
) -> str:
    filters: dict[str, Any] = {
        row_dimension: row_value,
        column_dimension: column_value,
    }
    if group_dimension is not None:
        filters[group_dimension] = group_value
    has_other_audience = not apply_dimension_filters(
        objective_df,
        {key: value for key, value in filters.items() if key != "audience"},
    ).is_empty()
    if has_other_audience:
        return "not run for this audience"
    return "missing candidate"


def _variant_is_valid(df: pl.DataFrame, variant: Mapping[str, Any]) -> bool:
    group_dimension = variant.get("group_dimension")
    row_dimension = str(variant["row_dimension"])
    column_dimension = str(variant["column_dimension"])

    if len(_non_null_values(df, row_dimension)) <= 1:
        return False
    if len(_non_null_values(df, column_dimension)) <= 1:
        return False
    if (
        group_dimension is not None
        and len(_non_null_values(df, str(group_dimension))) <= 1
    ):
        return False

    group_fields = (
        [str(group_dimension), row_dimension, column_dimension]
        if group_dimension
        else [row_dimension, column_dimension]
    )
    duplicates = (
        df.group_by(*group_fields)
        .agg(pl.len().alias("count"))
        .filter(pl.col("count") > 1)
    )
    return duplicates.is_empty()


def _score_value(
    *,
    record: Mapping[str, Any],
    judgement: Any,
    score_id: str,
) -> float | None:
    if score_id == "overall":
        value = record.get("overall_score")
        return float(value) if value is not None else None

    if score_id in record:
        value = record.get(score_id)
        return float(value) if value is not None else None

    if isinstance(judgement, Mapping):
        score_entry = judgement.get(score_id)
        if isinstance(score_entry, Mapping):
            value = score_entry.get("score")
            return float(value) if value is not None else None

    return None


def _cell_key(group_value: Any, row_value: Any, column_value: Any) -> str:
    return f"{_schema_value_key(group_value)}::{_schema_value_key(row_value)}::{_schema_value_key(column_value)}"


def _schema_value_key(value: Any) -> str:
    return "__none__" if value is None else str(value)


def _values(df: pl.DataFrame, dimension: str) -> list[Any]:
    order = DIMENSION_SPECS.get(dimension, {}).get("order")
    values = (
        df.select(pl.col(dimension))
        .unique(maintain_order=True)
        .get_column(dimension)
        .to_list()
    )
    if not order:
        return values

    def key(value: Any) -> tuple[int, str]:
        return (int(order.get(value, 999)), str(value))

    non_null = [value for value in values if value is not None]
    non_null.sort(key=key)
    if any(value is None for value in values):
        return [None, *non_null]
    return non_null


def _non_null_values(df: pl.DataFrame, dimension: str) -> list[str]:
    return [value for value in _values(df, dimension) if value is not None]


def _sort_with_preference(
    values: Sequence[str],
    preferences: Mapping[str, int],
) -> list[str]:
    return sorted(values, key=lambda value: (preferences.get(value, 999), value))


def _choose_requested_value(
    requested: Any,
    options: Sequence[Any],
    *,
    preferred: Any = None,
) -> Any:
    if not options:
        raise ValueError("Viewer selection has no valid options.")
    if requested in options:
        return requested
    if preferred in options:
        return preferred
    return options[0]


def _first_non_null(values: Sequence[str | None]) -> str | None:
    for value in values:
        if value is not None:
            return value
    return None


def _non_null_sequence(values: Sequence[str | None]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value is not None))

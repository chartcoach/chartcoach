from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import quote

import polars as pl

from ..evaluation import overall_score_expr
from .spec import (
    SCORE_BREAKDOWN_SPECS,
    ViewerConfig,
    ViewerLayout,
    dimension_map,
    display_label,
    label_for_dimension,
    resolved_case_label_field,
    resolved_search_fields,
)

_MISSING = object()


def discover_registry(
    candidates_df: pl.DataFrame,
    *,
    config: ViewerConfig,
) -> dict[str, Any]:
    return {
        "vis_ids": _non_null_values(candidates_df, config.case_id_field, config=config),
        "dimension_values": {
            dimension.id: _values(candidates_df, dimension.id, config=config)
            for dimension in config.dimensions
            if dimension.id in candidates_df.columns
        },
    }


def default_selection_from_registry(
    registry: Mapping[str, Any],
    *,
    config: ViewerConfig,
) -> dict[str, Any]:
    filters = {
        dimension_id: _choose_requested_value(
            None,
            tuple(registry["dimension_values"].get(dimension_id, [None])),
            preferred=config.default_filters.get(dimension_id),
        )
        for dimension_id in config.filter_dimensions
    }
    layout = _normalize_layout(
        requested={},
        axis_dimensions=tuple(config.axis_dimensions),
        preferred=config.default_layout,
    )
    return {
        "filters": filters,
        "layout": layout,
    }


def build_catalog(
    candidates_df: pl.DataFrame,
    vis_ids: Sequence[str],
    *,
    config: ViewerConfig,
) -> list[dict[str, Any]]:
    catalog: list[dict[str, Any]] = []
    label_field = resolved_case_label_field(config)
    search_fields = resolved_search_fields(config)
    for vis_id in vis_ids:
        case_df = candidates_df.filter(pl.col(config.case_id_field) == vis_id)
        label = (
            _first_non_null(case_df.get_column(label_field).cast(pl.String).to_list())
            or vis_id
        )
        search_text = " ".join(
            _non_null_sequence(
                [
                    str(value)
                    for field in search_fields
                    for value in case_df.get_column(field).cast(pl.String).to_list()
                ]
            )
        )
        catalog.append(
            {
                "vis_id": vis_id,
                "label": label,
                "search_text": search_text,
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
    config: ViewerConfig,
    filters: Mapping[str, Any] | None,
    layout: Mapping[str, Any] | None,
) -> dict[str, Any]:
    defaults = default_selection_from_registry(registry, config=config)
    requested_filters = dict(filters or {})

    normalized_filters: dict[str, Any] = {}
    filter_controls: list[dict[str, Any]] = []
    for dimension_id in config.filter_dimensions:
        options = tuple(_values(case_df, dimension_id, config=config))
        chosen = _choose_requested_value(
            requested_filters.get(dimension_id, _MISSING),
            options,
            preferred=config.default_filters.get(
                dimension_id,
                defaults["filters"].get(dimension_id),
            ),
        )
        normalized_filters[dimension_id] = chosen
        if len(options) > 1:
            filter_controls.append(
                {
                    "id": dimension_id,
                    "label": label_for_dimension(config, dimension_id),
                    "value": chosen,
                    "options": [
                        {
                            "value": option,
                            "label": display_label(config, dimension_id, option),
                        }
                        for option in options
                    ],
                }
            )

    scoped_df = apply_dimension_filters(case_df, normalized_filters)
    axis_dimensions = tuple(
        dimension_id
        for dimension_id in config.axis_dimensions
        if dimension_id in case_df.columns
    )
    normalized_layout = _normalize_layout(
        requested=layout or {},
        axis_dimensions=axis_dimensions,
        preferred=config.default_layout,
    )

    layout_controls = _build_layout_controls(
        axis_dimensions=axis_dimensions,
        layout=normalized_layout,
        config=config,
    )

    selection = {
        "vis_id": str(case_df.item(0, config.case_id_field)),
        "filters": normalized_filters,
        "layout": normalized_layout,
    }
    return {
        "selection": selection,
        "scoped_df": scoped_df,
        "axis_dimensions": axis_dimensions,
        "layout_controls": layout_controls,
        "filter_controls": filter_controls,
    }


def build_ui_schema(
    *,
    selection: Mapping[str, Any],
    axis_dimensions: Sequence[str],
    filter_controls: Sequence[Mapping[str, Any]],
    layout_controls: Sequence[Mapping[str, Any]],
    config: ViewerConfig,
) -> dict[str, Any]:
    pills = []
    if filter_controls:
        pills.append({"id": "filters", "label": "Filters"})
    if layout_controls:
        pills.append({"id": "layout", "label": "Layout"})

    return {
        "toolbar": {"pills": pills},
        "filters": list(filter_controls),
        "layout_controls": list(layout_controls),
        "matrix_axes": {
            "group_label": label_for_dimension(
                config,
                selection["layout"]["group_dimension"],
            )
            if selection["layout"]["group_dimension"] is not None
            else None,
            "row_label": label_for_dimension(
                config,
                selection["layout"]["row_dimension"],
            ),
            "column_label": label_for_dimension(
                config,
                selection["layout"]["column_dimension"],
            ),
            "hidden_labels": [
                label_for_dimension(config, dimension_id)
                for dimension_id in axis_dimensions
                if dimension_id
                not in {
                    selection["layout"]["row_dimension"],
                    selection["layout"]["column_dimension"],
                    selection["layout"]["group_dimension"],
                }
            ],
        },
    }


def build_overview_matrix(
    *,
    scoped_df: pl.DataFrame,
    layout: Mapping[str, Any],
    config: ViewerConfig,
) -> dict[str, Any]:
    group_dimension = layout.get("group_dimension")
    row_dimension = str(layout["row_dimension"])
    column_dimension = str(layout["column_dimension"])
    group_fields = (
        [str(group_dimension), row_dimension, column_dimension]
        if group_dimension is not None
        else [row_dimension, column_dimension]
    )
    axis_dimensions = tuple(
        dimension_id
        for dimension_id in config.axis_dimensions
        if dimension_id in scoped_df.columns
    )
    hidden_axes = tuple(
        dimension_id
        for dimension_id in axis_dimensions
        if dimension_id not in {row_dimension, column_dimension, group_dimension}
    )
    records = scoped_df.to_dicts()

    if group_dimension is not None:
        available = _bucket_records(records, group_fields)
        group_values = _values(scoped_df, str(group_dimension), config=config)
        row_values = _values(scoped_df, row_dimension, config=config)
        column_values = _values(scoped_df, column_dimension, config=config)

        groups = []
        for group_value in group_values:
            rows = []
            for row_value in row_values:
                cells = []
                for column_value in column_values:
                    bucket = available.get((group_value, row_value, column_value), [])
                    cells.append(
                        _matrix_cell_payload(
                            records=bucket,
                            config=config,
                            group_dimension=str(group_dimension),
                            group_value=group_value,
                            hidden_axes=hidden_axes,
                            row_dimension=row_dimension,
                            row_value=row_value,
                            column_dimension=column_dimension,
                            column_value=column_value,
                        )
                    )
                rows.append(
                    {
                        "value": row_value,
                        "label": display_label(config, row_dimension, row_value),
                        **_axis_value_meta(
                            scoped_df,
                            dimension_id=row_dimension,
                            value=row_value,
                        ),
                        "cells": cells,
                    }
                )
            groups.append(
                {
                    "value": group_value,
                    "label": display_label(config, str(group_dimension), group_value),
                    **_axis_value_meta(
                        scoped_df,
                        dimension_id=str(group_dimension),
                        value=group_value,
                    ),
                    "columns": [
                        {
                            "value": column_value,
                            "label": display_label(
                                config,
                                column_dimension,
                                column_value,
                            ),
                            **_axis_value_meta(
                                scoped_df,
                                dimension_id=column_dimension,
                                value=column_value,
                            ),
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

    available = _bucket_records(records, group_fields)
    row_values = _values(scoped_df, row_dimension, config=config)
    column_values = _values(scoped_df, column_dimension, config=config)
    rows = []
    for row_value in row_values:
        cells = []
        for column_value in column_values:
            bucket = available.get((row_value, column_value), [])
            cells.append(
                _matrix_cell_payload(
                    records=bucket,
                    config=config,
                    group_dimension=None,
                    group_value=None,
                    hidden_axes=hidden_axes,
                    row_dimension=row_dimension,
                    row_value=row_value,
                    column_dimension=column_dimension,
                    column_value=column_value,
                )
            )
        rows.append(
            {
                "value": row_value,
                "label": display_label(config, row_dimension, row_value),
                **_axis_value_meta(
                    scoped_df,
                    dimension_id=row_dimension,
                    value=row_value,
                ),
                "cells": cells,
            }
        )
    return {
        "kind": "flat",
        "columns": [
            {
                "value": column_value,
                "label": display_label(config, column_dimension, column_value),
                **_axis_value_meta(
                    scoped_df,
                    dimension_id=column_dimension,
                    value=column_value,
                ),
            }
            for column_value in column_values
        ],
        "rows": rows,
    }


def serialize_candidate_record(
    record: Mapping[str, Any],
    *,
    config: ViewerConfig,
) -> dict[str, Any]:
    judgement = record.get("judgement")
    visgen_id = str(record["visgen_id"])
    return {
        "visgen_id": visgen_id,
        "dimension_values": {
            dimension.id: record.get(dimension.id)
            for dimension in config.dimensions
            if dimension.id in record
        },
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
        "image_url": _build_image_url(config.image_base_url, visgen_id),
        "image_meta": None,
        "error": record.get("error"),
    }


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


def _build_layout_controls(
    *,
    axis_dimensions: Sequence[str],
    layout: Mapping[str, Any],
    config: ViewerConfig,
) -> list[dict[str, Any]]:
    row_dimension = str(layout["row_dimension"])
    column_dimension = str(layout["column_dimension"])
    group_dimension = layout.get("group_dimension")

    return [
        _layout_control(
            control_id="row_dimension",
            label="Rows",
            options=[
                dimension_id
                for dimension_id in axis_dimensions
                if dimension_id not in {column_dimension, group_dimension}
            ],
            value=row_dimension,
            config=config,
        ),
        _layout_control(
            control_id="column_dimension",
            label="Columns",
            options=[
                dimension_id
                for dimension_id in axis_dimensions
                if dimension_id not in {row_dimension, group_dimension}
            ],
            value=column_dimension,
            config=config,
        ),
        _layout_control(
            control_id="group_dimension",
            label="Groups",
            options=[
                None,
                *[
                    dimension_id
                    for dimension_id in axis_dimensions
                    if dimension_id not in {row_dimension, column_dimension}
                ],
            ],
            value=group_dimension,
            config=config,
        ),
    ]


def _layout_control(
    *,
    control_id: str,
    label: str,
    options: Sequence[str | None],
    value: str | None,
    config: ViewerConfig,
) -> dict[str, Any]:
    return {
        "id": control_id,
        "label": label,
        "value": value,
        "options": [
            {
                "value": option,
                "label": (
                    "No grouping"
                    if option is None
                    else label_for_dimension(config, option)
                ),
            }
            for option in options
        ],
    }


def _matrix_cell_payload(
    *,
    records: Sequence[Mapping[str, Any]],
    config: ViewerConfig,
    group_dimension: str | None,
    group_value: Any,
    hidden_axes: Sequence[str],
    row_dimension: str,
    row_value: Any,
    column_dimension: str,
    column_value: Any,
) -> dict[str, Any]:
    variants = _serialize_cell_variants(
        records,
        hidden_axes=hidden_axes,
        config=config,
    )
    return {
        "cell_key": _cell_key(group_value, row_value, column_value),
        "group_value": group_value,
        "group_label": (
            display_label(config, group_dimension, group_value)
            if group_dimension is not None
            else None
        ),
        "row_value": row_value,
        "row_label": display_label(config, row_dimension, row_value),
        "column_value": column_value,
        "column_label": display_label(config, column_dimension, column_value),
        "hidden_axes": list(hidden_axes),
        "hidden_axis_labels": [
            label_for_dimension(config, dimension_id) for dimension_id in hidden_axes
        ],
        "variant_count": len(variants),
        "missing": len(records) == 0,
        "placeholder_reason": None if records else "missing candidate",
        "variants": variants,
    }


def _normalize_layout(
    *,
    requested: Mapping[str, Any],
    axis_dimensions: Sequence[str],
    preferred: ViewerLayout,
) -> dict[str, str | None]:
    if len(axis_dimensions) < 2:
        raise ValueError("Viewer requires at least two axis dimensions.")

    row_dimension = _choose_requested_value(
        requested.get("row_dimension", _MISSING),
        axis_dimensions,
        preferred=preferred.row_dimension,
    )
    column_candidates = tuple(
        dimension_id
        for dimension_id in axis_dimensions
        if dimension_id != row_dimension
    )
    column_dimension = _choose_requested_value(
        requested.get("column_dimension", _MISSING),
        column_candidates,
        preferred=preferred.column_dimension,
    )

    group_candidates = tuple(
        [None]
        + [
            dimension_id
            for dimension_id in axis_dimensions
            if dimension_id not in {row_dimension, column_dimension}
        ]
    )
    group_dimension = _choose_requested_value(
        requested.get("group_dimension", _MISSING),
        group_candidates,
        preferred=preferred.group_dimension,
    )

    return {
        "row_dimension": str(row_dimension),
        "column_dimension": str(column_dimension),
        "group_dimension": None if group_dimension is None else str(group_dimension),
    }


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
    return (
        f"{_schema_value_key(group_value)}::"
        f"{_schema_value_key(row_value)}::"
        f"{_schema_value_key(column_value)}"
    )


def _schema_value_key(value: Any) -> str:
    return "__none__" if value is None else str(value)


def _axis_value_meta(
    df: pl.DataFrame,
    *,
    dimension_id: str,
    value: Any,
) -> dict[str, Any]:
    if dimension_id != "grounding_mode":
        return {
            "meta_label": None,
            "meta_kind": None,
        }

    scoped = (
        df.filter(pl.col(dimension_id).is_null())
        if value is None
        else df.filter(pl.col(dimension_id) == value)
    )
    guideline_ids = {
        guideline_id
        for guideline_list in scoped.get_column("guideline_ids").to_list()
        for guideline_id in (guideline_list or [])
    }
    count = len(guideline_ids)
    if count <= 0:
        return {
            "meta_label": None,
            "meta_kind": None,
        }
    return {
        "meta_label": f"{count} guideline{'s' if count != 1 else ''}",
        "meta_kind": "guidelines",
    }


def _bucket_records(
    records: Sequence[Mapping[str, Any]],
    fields: Sequence[str],
) -> dict[tuple[Any, ...], list[Mapping[str, Any]]]:
    buckets: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for record in records:
        key = tuple(record.get(field) for field in fields)
        buckets.setdefault(key, []).append(record)
    return buckets


def _serialize_cell_variants(
    records: Sequence[Mapping[str, Any]],
    *,
    hidden_axes: Sequence[str],
    config: ViewerConfig,
) -> list[dict[str, Any]]:
    if not records:
        return []

    ordered = sorted(
        records,
        key=lambda record: _variant_sort_key(
            record,
            hidden_axes=hidden_axes,
            config=config,
        ),
    )
    base_labels = [
        _variant_label(record, hidden_axes=hidden_axes, config=config)
        for record in ordered
    ]
    counts = Counter(base_labels)
    seen: Counter[str | None] = Counter()
    variants: list[dict[str, Any]] = []

    for record, base_label in zip(ordered, base_labels, strict=False):
        seen[base_label] += 1
        label = base_label
        if counts[base_label] > 1:
            suffix = f"#{seen[base_label]}"
            label = f"{base_label} · {suffix}" if base_label else suffix
        variants.append(
            {
                "variant_key": str(record["visgen_id"]),
                "variant_label": label,
                "candidate": serialize_candidate_record(record, config=config),
            }
        )
    return variants


def _variant_sort_key(
    record: Mapping[str, Any],
    *,
    hidden_axes: Sequence[str],
    config: ViewerConfig,
) -> tuple[Any, ...]:
    score_value = record.get("overall_score")
    overall_sort = (
        1,
        0.0,
    )
    if score_value is not None:
        overall_sort = (0, -float(score_value))

    axis_sort = tuple(
        _dimension_sort_key(
            dimension_id,
            record.get(dimension_id),
            config=config,
        )
        for dimension_id in hidden_axes
    )
    return (
        overall_sort,
        axis_sort,
        str(record.get("visgen_id") or ""),
    )


def _dimension_sort_key(
    dimension_id: str,
    value: Any,
    *,
    config: ViewerConfig,
) -> tuple[int, int, str]:
    spec = dimension_map(config).get(dimension_id)
    if value is None:
        return (0, -1, "")
    if spec is None:
        return (1, 999, str(value))
    return (
        1,
        int(spec.order.get(value, 999)),
        display_label(config, dimension_id, value),
    )


def _variant_label(
    record: Mapping[str, Any],
    *,
    hidden_axes: Sequence[str],
    config: ViewerConfig,
) -> str | None:
    parts = []
    for dimension_id in hidden_axes:
        parts.append(
            f"{label_for_dimension(config, dimension_id)}: "
            f"{display_label(config, dimension_id, record.get(dimension_id))}"
        )
    return " · ".join(parts) if parts else None


def _values(
    df: pl.DataFrame,
    dimension: str,
    *,
    config: ViewerConfig,
) -> list[Any]:
    spec = dimension_map(config).get(dimension)
    order = spec.order if spec is not None else {}
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


def _non_null_values(
    df: pl.DataFrame,
    dimension: str,
    *,
    config: ViewerConfig,
) -> list[str]:
    return [
        value for value in _values(df, dimension, config=config) if value is not None
    ]


def _choose_requested_value(
    requested: Any,
    options: Sequence[Any],
    *,
    preferred: Any = None,
) -> Any:
    if not options:
        raise ValueError("Viewer selection has no valid options.")
    if requested is _MISSING:
        if preferred in options:
            return preferred
        return options[0]
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


def _build_image_url(image_base_url: str, visgen_id: str) -> str:
    return f"{image_base_url.rstrip('/')}/{quote(visgen_id)}.png"


__all__ = [
    "apply_dimension_filters",
    "build_catalog",
    "build_overview_matrix",
    "build_ui_schema",
    "default_selection_from_registry",
    "discover_registry",
    "enrich_candidates_with_scores",
    "normalize_selection",
]

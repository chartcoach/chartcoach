from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import quote

import polars as pl

from ..evaluation import overall_score_expr
from .spec import (
    SCORE_BREAKDOWN_SPECS,
    ViewerConfig,
    dimension_map,
    resolved_case_label_field,
    resolved_search_fields,
)
from .guidelines import guideline_detail


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
    layout = {
        "row_dimension": config.default_layout.row_dimension,
        "column_dimension": config.default_layout.column_dimension,
        "group_dimension": config.default_layout.group_dimension,
    }
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


def enrich_candidates_with_judge_runs(
    candidates_df: pl.DataFrame,
    judgement_runs_df: pl.DataFrame | None,
) -> pl.DataFrame:
    if judgement_runs_df is None or judgement_runs_df.is_empty():
        return candidates_df

    if missing := (
        {"visgen_id", "judge_run_id", "judge_run_index", "judgement", "overall_score"}
        - set(judgement_runs_df.columns)
    ):
        raise ValueError(
            "Judgement runs are missing required viewer columns: "
            + ", ".join(sorted(missing))
            + "."
        )

    runs_df = (
        judgement_runs_df.sort("visgen_id", "judge_run_index")
        .group_by("visgen_id", maintain_order=True)
        .agg(
            judge_runs=pl.struct(
                "judge_run_id",
                "judge_run_index",
                "judgement",
                "overall_score",
            )
        )
    )
    return candidates_df.join(runs_df, on="visgen_id", how="left")


def serialize_candidate_record(
    record: Mapping[str, Any],
    *,
    config: ViewerConfig,
) -> dict[str, Any]:
    judgement = record.get("judgement")
    visgen_id = str(record["visgen_id"])
    guideline_ids = list(dict.fromkeys(record.get("guideline_ids") or []))
    judge_runs = list(record.get("judge_runs") or [])
    return {
        "visgen_id": visgen_id,
        "dimension_values": {
            dimension.id: record.get(dimension.id)
            for dimension in config.dimensions
            if dimension.id in record
        },
        "overall_score": record.get("overall_score"),
        "guideline_count": len(guideline_ids),
        "guideline_details": [
            guideline_detail(guideline_id, config=config)
            for guideline_id in guideline_ids
        ],
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
                "reasoning": _score_reasoning(
                    record=record,
                    judgement=judgement,
                    score_id=spec["id"],
                ),
                "runs": _score_runs(score_id=spec["id"], judge_runs=judge_runs),
            }
            for spec in SCORE_BREAKDOWN_SPECS
        ],
        "image_url": _build_image_url(config.image_base_url, visgen_id),
        "image_meta": None,
        "error": record.get("error"),
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


def _score_reasoning(
    *,
    record: Mapping[str, Any],
    judgement: Any,
    score_id: str,
) -> str | None:
    if score_id == "overall":
        return None

    if isinstance(judgement, Mapping):
        score_entry = judgement.get(score_id)
        if isinstance(score_entry, Mapping):
            reasoning = score_entry.get("reasoning")
            if reasoning:
                return str(reasoning)

    return None


def _score_runs(
    *,
    score_id: str,
    judge_runs: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for run in judge_runs:
        run_id = str(run.get("judge_run_id") or "")
        run_index = run.get("judge_run_index")
        label = (
            f"Run {int(run_index) + 1}" if run_index is not None else f"Run {run_id}"
        )

        if score_id == "overall":
            value = run.get("overall_score")
            items.append(
                {
                    "run_id": run_id,
                    "label": label,
                    "score": float(value) if value is not None else None,
                    "reasoning": None,
                }
            )
            continue

        judgement = run.get("judgement")
        if not isinstance(judgement, Mapping):
            continue
        score_entry = judgement.get(score_id)
        if not isinstance(score_entry, Mapping):
            continue
        value = score_entry.get("score")
        reasoning = score_entry.get("reasoning")
        items.append(
            {
                "run_id": run_id,
                "label": label,
                "score": float(value) if value is not None else None,
                "reasoning": str(reasoning) if reasoning else None,
            }
        )

    return items


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
    "build_catalog",
    "default_selection_from_registry",
    "discover_registry",
    "enrich_candidates_with_judge_runs",
    "enrich_candidates_with_scores",
    "serialize_candidate_record",
]

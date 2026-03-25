from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any, Final

import polars as pl

GROUNDING_MODES: Final[tuple[str, ...]] = ("none", "flat", "structured")
MODEL_COLUMNS: Final[tuple[str, ...]] = (
    "claude-sonnet-4.6",
    "gemini-3.1-pro-preview",
    "gpt-5.4",
)
GRAMMAR_OPTIONS: Final[tuple[str, ...]] = ("altair", "matplotlib", "plotly")
AUDIENCE_OPTIONS_BY_OBJECTIVE: Final[dict[str, tuple[str | None, ...]]] = {
    "refine": (None,),
    "select": (None, "casual", "novice", "expert"),
}
SCORE_FIELDS: Final[tuple[str, ...]] = (
    "data_fidelity",
    "semantic_readability",
    "insight_discovery",
    "design_style",
    "visual_composition",
    "color_harmony",
)
_DIMENSION_ORDERS: Final[dict[str, dict[str | None, int]]] = {
    "objective": {
        "refine": 0,
        "select": 1,
    },
    "model": {model: index for index, model in enumerate(MODEL_COLUMNS)},
    "grammar": {grammar: index for index, grammar in enumerate(GRAMMAR_OPTIONS)},
    "grounding_mode": {mode: index for index, mode in enumerate(GROUNDING_MODES)},
    "audience": {
        None: 0,
        "casual": 1,
        "novice": 2,
        "expert": 3,
    },
}


def unique_dimension_values(df: pl.DataFrame, dimension: str) -> list[str | None]:
    values = (
        df.select(pl.col(dimension))
        .unique(maintain_order=True)
        .get_column(dimension)
        .to_list()
    )
    order = _DIMENSION_ORDERS.get(dimension)
    if order is None:
        return sorted(values, key=lambda value: "" if value is None else str(value))
    return sorted(
        values,
        key=lambda value: (
            0 if value in order else 1,
            order.get(value, len(order)),
            "" if value is None else str(value),
        ),
    )


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

    def score_expr(score_field: str) -> pl.Expr:
        if score_field in judgements_df.columns:
            return pl.col(score_field).cast(pl.Float64)
        return (
            pl.col("judgement")
            .struct.field(score_field)
            .struct.field("score")
            .cast(pl.Float64)
        )

    score_df = judgements_df.select(
        "visgen_id",
        "judgement",
        overall_score=pl.mean_horizontal(
            *(score_expr(score_field) for score_field in SCORE_FIELDS)
        ).round(2),
    )
    return candidates_df.join(score_df, on="visgen_id", how="left")


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


def normalize_selection(
    case_df: pl.DataFrame,
    *,
    objective: str | None,
    grammar: str | None,
    audience: str | None,
) -> dict[str, Any]:
    objectives = unique_dimension_values(case_df, "objective")
    chosen_objective = _choose_requested_value(objective, objectives)
    objective_df = apply_dimension_filters(case_df, {"objective": chosen_objective})

    grammar_options = list(GRAMMAR_OPTIONS)
    chosen_grammar = _choose_requested_value(grammar, grammar_options)
    objective_grammar_df = apply_dimension_filters(
        objective_df,
        {"grammar": chosen_grammar},
    )

    if chosen_objective is None:
        raise ValueError("Viewer selection has no valid objective.")
    audience_options = list(AUDIENCE_OPTIONS_BY_OBJECTIVE[chosen_objective])
    chosen_audience = _choose_requested_value(audience, audience_options)
    selection_df = apply_dimension_filters(
        objective_grammar_df,
        {"audience": chosen_audience},
    )

    return {
        "selection": {
            "objective": chosen_objective,
            "grammar": chosen_grammar,
            "audience": chosen_audience,
        },
        "options": {
            "objectives": objectives,
            "grammars": grammar_options,
            "audiences": audience_options,
            "audience_enabled": chosen_objective == "select",
        },
        "objective_df": objective_df,
        "objective_grammar_df": objective_grammar_df,
        "selection_df": selection_df,
    }


def build_grounding_model_matrix(
    *,
    objective_grammar_df: pl.DataFrame,
    selection_df: pl.DataFrame,
    audience: str | None,
) -> dict[str, Any]:
    duplicate_cells = (
        selection_df.group_by("grounding_mode", "model")
        .agg(pl.len().alias("count"))
        .filter(pl.col("count") > 1)
    )
    if not duplicate_cells.is_empty():
        raise ValueError(
            "Expected at most one candidate per grounding/model cell, got "
            + str(duplicate_cells.to_dicts())
        )

    available_pairs = {
        (record["grounding_mode"], record["model"]): record
        for record in selection_df.to_dicts()
    }
    objective_grammar_pairs = {
        (record["grounding_mode"], record["model"]): record
        for record in objective_grammar_df.to_dicts()
    }

    rows = []
    for grounding_mode in GROUNDING_MODES:
        row_cells = []
        for model in MODEL_COLUMNS:
            record = available_pairs.get((grounding_mode, model))
            if record is not None:
                row_cells.append(
                    {
                        "grounding_mode": grounding_mode,
                        "model": model,
                        "record": record,
                        "placeholder_reason": None,
                    }
                )
                continue

            row_cells.append(
                {
                    "grounding_mode": grounding_mode,
                    "model": model,
                    "record": None,
                    "placeholder_reason": placeholder_reason(
                        objective_grammar_pairs=objective_grammar_pairs,
                        grounding_mode=grounding_mode,
                        model=model,
                        audience=audience,
                    ),
                }
            )
        rows.append({"grounding_mode": grounding_mode, "cells": row_cells})

    return {
        "models": list(MODEL_COLUMNS),
        "rows": rows,
        "record_map": available_pairs,
    }


def build_catalog(
    candidates_df: pl.DataFrame,
    vis_ids: Sequence[str],
) -> list[dict[str, Any]]:
    catalog: list[dict[str, Any]] = []
    for page_index, vis_id in enumerate(vis_ids):
        case_df = candidates_df.filter(pl.col("vis_id") == vis_id)
        catalog.append(
            {
                "vis_id": vis_id,
                "page_index": page_index,
                "nl_query": case_df.item(0, "query"),
                "objectives": unique_dimension_values(case_df, "objective"),
                "grammars": unique_dimension_values(case_df, "grammar"),
            }
        )
    return catalog


def serialize_candidate_record(
    record: Mapping[str, Any],
    *,
    image_loader: Callable[[dict[str, Any], str], str],
    image_variant: str,
    include_detail: bool,
) -> dict[str, Any]:
    image_record = dict(record)
    payload = {
        "visgen_id": record["visgen_id"],
        "vis_id": record["vis_id"],
        "grounding_mode": record["grounding_mode"],
        "objective": record["objective"],
        "model": record["model"],
        "grammar": record["grammar"],
        "audience": record["audience"],
        "visualization_type": record["visualization_type"],
        "overall_score": record.get("overall_score"),
    }
    if include_detail:
        payload |= {
            "nl_query": record["query"],
            "query_interpretation": record["query_interpretation"],
            "design_rationale": record["design_rationale"],
            "grounding_trace": record["grounding_trace"],
            "guideline_ids": list(dict.fromkeys(record.get("guideline_ids") or [])),
            "code": record["code"],
            "judgement_dimensions": judgement_dimensions(record.get("judgement")),
        }
    try:
        payload["image_url"] = image_loader(image_record, image_variant)
        payload["error"] = None
    except Exception as exc:  # pragma: no cover - exercised by tests
        payload["image_url"] = None
        payload["error"] = str(exc)
    return payload


def judgement_dimensions(judgement: object) -> list[dict[str, Any]]:
    if not isinstance(judgement, Mapping):
        return []
    judgement_map = dict(judgement)
    rows: list[dict[str, Any]] = []
    for score_field in SCORE_FIELDS:
        entry = judgement_map.get(score_field)
        if not isinstance(entry, Mapping):
            continue
        rows.append(
            {
                "dimension": score_field,
                "score": entry.get("score"),
                "reasoning": entry.get("reasoning"),
            }
        )
    return rows


def placeholder_reason(
    *,
    objective_grammar_pairs: Mapping[tuple[str, str], dict[str, Any]],
    grounding_mode: str,
    model: str,
    audience: str | None,
) -> str:
    if (grounding_mode, model) not in objective_grammar_pairs:
        return "not generated for this grammar"
    if audience is not None:
        return "not run for this audience"
    return "missing candidate"


def resolve_focus_key(
    record_map: Mapping[tuple[str, str], dict[str, Any]],
    *,
    focused_grounding_mode: str | None,
    focused_model: str | None,
) -> tuple[str, str] | None:
    if (
        focused_grounding_mode in GROUNDING_MODES
        and focused_model in MODEL_COLUMNS
        and (focused_grounding_mode, focused_model) in record_map
    ):
        return (focused_grounding_mode, focused_model)

    if focused_grounding_mode in GROUNDING_MODES:
        for model in MODEL_COLUMNS:
            if (focused_grounding_mode, model) in record_map:
                return (focused_grounding_mode, model)

    for grounding_mode in GROUNDING_MODES:
        for model in MODEL_COLUMNS:
            if (grounding_mode, model) in record_map:
                return (grounding_mode, model)
    return None


def _choose_requested_value(
    requested: str | None,
    options: Sequence[str | None],
) -> str | None:
    if not options:
        raise ValueError("Viewer selection has no valid options.")
    if requested in options:
        return requested
    return options[0]

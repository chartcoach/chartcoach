from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any

import polars as pl

from ..evaluation import SCORE_FIELDS, overall_score_expr

_SOFT_DEFAULTS = {
    "objective": "select",
    "grammar": "matplotlib",
    "audience": None,
}
_SOFT_ORDERS = {
    "objective": {"select": 0, "refine": 1},
    "grounding_mode": {"none": 0, "structured": 1},
}
_DIMENSION_LABELS = {
    "objective": "Objective",
    "grammar": "Grammar",
    "audience": "Audience",
    "grounding_mode": "Condition",
    "model": "Model",
}
_DISPLAY_ALIASES: dict[str, dict[str | None, str]] = {
    "grounding_mode": {
        "none": "Ungrounded",
        "structured": "Grounded",
    }
}
_COPY = {
    "title": "Compare design outcomes",
    "subtitle": (
        "Review how the same request changes across the available conditions "
        "and model outputs."
    ),
    "case_label": "Case",
    "search_placeholder": "Search by case ID or request",
    "request_label": "Request",
    "controls_label": "Controls",
    "controls_aside": "Adjust the current slice without losing the comparison.",
    "comparison_label": "Comparison",
    "comparison_aside": "Hover for a quick preview. Click a chart for deeper details.",
    "detail_label": "Selected chart",
    "detail_preview_label": "Chart preview",
    "detail_guidelines_label": "Guidelines used",
    "detail_story_label": "How it was grounded",
    "detail_interpretation_label": "Interpretation",
    "detail_rationale_label": "Why this design",
    "detail_review_label": "Reviewer notes",
    "detail_advanced_label": "Advanced details",
    "detail_trace_label": "Grounding trace",
    "detail_judge_label": "Detailed reviewer notes",
    "detail_code_label": "Chart code",
    "detail_metadata_label": "Dataset notes",
    "hover_label": "Quick preview",
    "hover_guidelines_label": "Guidelines used",
    "hover_story_label": "How it was grounded",
    "empty_guidelines": "No guidelines were retrieved for this chart.",
    "empty_grounding_story": "No grounding notes were recorded for this chart.",
    "empty_interpretation": "No interpretation was recorded for this chart.",
    "empty_rationale": "No rationale was recorded for this chart.",
    "empty_review": "No reviewer notes are available for this chart.",
    "empty_metadata": "No dataset notes were recorded for this chart.",
}


def discover_registry(candidates_df: pl.DataFrame) -> dict[str, Any]:
    objectives = _sort_with_preference(
        _non_null_values(candidates_df, "objective"),
        _SOFT_ORDERS["objective"],
    )
    grammars_by_objective = {
        objective: _non_null_values(
            candidates_df.filter(pl.col("objective") == objective),
            "grammar",
        )
        for objective in objectives
    }
    audiences_by_objective = {
        objective: _values(
            candidates_df.filter(pl.col("objective") == objective),
            "audience",
        )
        for objective in objectives
    }
    models = _non_null_values(candidates_df, "model")
    grounding_modes = _sort_with_preference(
        _non_null_values(candidates_df, "grounding_mode"),
        _SOFT_ORDERS["grounding_mode"],
    )
    vis_ids = _non_null_values(candidates_df, "vis_id")
    return {
        "vis_ids": vis_ids,
        "objectives": objectives,
        "grammars_by_objective": grammars_by_objective,
        "audiences_by_objective": audiences_by_objective,
        "models": models,
        "grounding_modes": grounding_modes,
    }


def default_selection_from_registry(
    registry: Mapping[str, Any],
) -> dict[str, str | None]:
    objective = _choose_requested_value(
        None,
        tuple(registry["objectives"]),
        preferred=_SOFT_DEFAULTS["objective"],
    )
    grammar = _choose_requested_value(
        None,
        tuple(registry["grammars_by_objective"][objective]),
        preferred=_SOFT_DEFAULTS["grammar"],
    )
    audience_options = tuple(registry["audiences_by_objective"][objective])
    preferred_audience = (
        None if audience_options == (None,) else _SOFT_DEFAULTS["audience"]
    )
    audience = _choose_requested_value(
        None,
        audience_options,
        preferred=preferred_audience,
    )
    return {
        "objective": objective,
        "grammar": grammar,
        "audience": audience,
    }


def build_ui_schema(
    *,
    registry: Mapping[str, Any],
    selection: Mapping[str, str | None],
    asset_version: str,
) -> dict[str, Any]:
    defaults = default_selection_from_registry(registry)
    filters = [
        _filter_schema(
            dimension="objective",
            options=tuple(registry["objectives"]),
            value=selection["objective"],
            disabled=False,
        ),
        _filter_schema(
            dimension="grammar",
            options=tuple(registry["grammars_by_objective"][selection["objective"]]),
            value=selection["grammar"],
            disabled=False,
        ),
    ]

    audience_options = tuple(registry["audiences_by_objective"][selection["objective"]])
    filters.append(
        _filter_schema(
            dimension="audience",
            options=audience_options,
            value=selection["audience"],
            disabled=len(audience_options) == 1 and audience_options[0] is None,
        )
    )

    return {
        "asset_version": asset_version,
        "copy": dict(_COPY),
        "filters": filters,
        "matrix_axes": {
            "row_dimension": "grounding_mode",
            "row_label": label_for_dimension("grounding_mode"),
            "column_dimension": "model",
            "column_label": label_for_dimension("model"),
        },
        "display_labels": {
            dimension: {
                _schema_value_key(value): display_label(dimension, value)
                for value in values
            }
            for dimension, values in (
                ("objective", registry["objectives"]),
                ("grammar", registry["grammars_by_objective"][selection["objective"]]),
                ("audience", audience_options),
                ("grounding_mode", registry["grounding_modes"]),
                ("model", registry["models"]),
            )
        },
        "defaults": defaults,
        "advanced_sections": [
            "grounding_trace",
            "judge_feedback",
            "dataset_notes",
            "chart_code",
        ],
    }


def build_catalog(
    candidates_df: pl.DataFrame,
    vis_ids: Sequence[str],
) -> list[dict[str, Any]]:
    catalog: list[dict[str, Any]] = []
    for page_index, vis_id in enumerate(vis_ids):
        case_df = candidates_df.filter(pl.col("vis_id") == vis_id)
        query = case_df.item(0, "query")
        catalog.append(
            {
                "vis_id": vis_id,
                "page_index": page_index,
                "nl_query": query,
                "search_label": f"{vis_id} · {_truncate(query, 88)}",
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
    registry: Mapping[str, Any],
    objective: str | None,
    grammar: str | None,
    audience: str | None,
) -> dict[str, Any]:
    defaults = default_selection_from_registry(registry)
    objectives = tuple(registry["objectives"])
    chosen_objective = _choose_requested_value(
        objective,
        objectives,
        preferred=defaults["objective"],
    )

    objective_df = apply_dimension_filters(case_df, {"objective": chosen_objective})

    grammar_options = tuple(registry["grammars_by_objective"][chosen_objective])
    chosen_grammar = _choose_requested_value(
        grammar,
        grammar_options,
        preferred=defaults["grammar"]
        if chosen_objective == defaults["objective"]
        else None,
    )
    objective_grammar_df = apply_dimension_filters(
        objective_df,
        {"grammar": chosen_grammar},
    )

    audience_options = tuple(registry["audiences_by_objective"][chosen_objective])
    preferred_audience = (
        defaults["audience"] if chosen_objective == defaults["objective"] else None
    )
    if audience_options == (None,):
        preferred_audience = None
    chosen_audience = _choose_requested_value(
        audience,
        audience_options,
        preferred=preferred_audience,
    )
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
            "objectives": list(objectives),
            "grammars": list(grammar_options),
            "audiences": list(audience_options),
            "audience_enabled": not (
                len(audience_options) == 1 and audience_options[0] is None
            ),
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
    models = _non_null_values(objective_grammar_df, "model")
    grounding_modes = _sort_with_preference(
        _non_null_values(objective_grammar_df, "grounding_mode"),
        _SOFT_ORDERS["grounding_mode"],
    )

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
    for grounding_mode in grounding_modes:
        row_cells = []
        for model in models:
            record = available_pairs.get((grounding_mode, model))
            row_cells.append(
                {
                    "grounding_mode": grounding_mode,
                    "grounding_label": display_label("grounding_mode", grounding_mode),
                    "model": model,
                    "model_label": display_label("model", model),
                    "record": record,
                    "placeholder_reason": (
                        None
                        if record is not None
                        else placeholder_reason(
                            objective_grammar_pairs=objective_grammar_pairs,
                            grounding_mode=grounding_mode,
                            model=model,
                            audience=audience,
                        )
                    ),
                }
            )
        rows.append(
            {
                "grounding_mode": grounding_mode,
                "grounding_label": display_label("grounding_mode", grounding_mode),
                "cells": row_cells,
            }
        )

    return {
        "columns": [
            {
                "value": model,
                "label": display_label("model", model),
            }
            for model in models
        ],
        "rows": rows,
        "record_map": available_pairs,
    }


def serialize_candidate_record(
    record: Mapping[str, Any],
    *,
    image_loader: Callable[[dict[str, Any], str], str],
    image_variant: str,
    include_detail: bool,
) -> dict[str, Any]:
    image_record = dict(record)
    guideline_ids = list(dict.fromkeys(record.get("guideline_ids") or []))
    payload: dict[str, Any] = {
        "visgen_id": record["visgen_id"],
        "vis_id": record["vis_id"],
        "grounding_mode": record["grounding_mode"],
        "grounding_label": display_label("grounding_mode", record["grounding_mode"]),
        "objective": record["objective"],
        "objective_label": display_label("objective", record["objective"]),
        "model": record["model"],
        "model_label": display_label("model", record["model"]),
        "grammar": record["grammar"],
        "grammar_label": display_label("grammar", record["grammar"]),
        "audience": record["audience"],
        "audience_label": display_label("audience", record["audience"]),
        "data_profile": record.get("data_profile"),
        "visualization_type": record["visualization_type"],
        "overall_score": record.get("overall_score"),
        "guideline_ids": guideline_ids,
        "guideline_count": len(guideline_ids),
        "grounding_trace": record["grounding_trace"],
        "grounding_story": grounding_story(
            record.get("grounding_trace"),
            guideline_count=len(guideline_ids),
        ),
    }
    if include_detail:
        payload |= {
            "nl_query": record["query"],
            "query_interpretation": record["query_interpretation"],
            "design_rationale": record["design_rationale"],
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
                "dimension_label": _humanize(score_field, title_case=True),
                "score": entry.get("score"),
                "reasoning": entry.get("reasoning"),
            }
        )
    return rows


def grounding_story(
    trace: object,
    *,
    guideline_count: int,
) -> list[str]:
    trace_items = (
        [str(item) for item in trace if item]
        if isinstance(trace, Sequence) and not isinstance(trace, str)
        else []
    )
    if trace_items:
        return trace_items[:2]
    if guideline_count:
        return [f"Retrieved {guideline_count} guideline IDs for this chart."]
    return []


def display_label(dimension: str, value: str | None) -> str:
    alias = _DISPLAY_ALIASES.get(dimension, {}).get(value)
    if alias is not None:
        return alias
    if dimension == "model" and value is not None:
        return str(value)
    return _humanize(value, title_case=False)


def label_for_dimension(dimension: str) -> str:
    return _DIMENSION_LABELS.get(dimension, _humanize(dimension, title_case=True))


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
    if focused_grounding_mode is not None and focused_model is not None:
        key = (focused_grounding_mode, focused_model)
        if key in record_map:
            return key

    if focused_grounding_mode is not None:
        for mode, model in record_map:
            if mode == focused_grounding_mode:
                return (mode, model)

    return next(iter(record_map), None)


def _filter_schema(
    *,
    dimension: str,
    options: Sequence[str | None],
    value: str | None,
    disabled: bool,
) -> dict[str, Any]:
    return {
        "id": dimension,
        "label": label_for_dimension(dimension),
        "value": value,
        "disabled": disabled,
        "options": [
            {
                "value": option,
                "label": display_label(dimension, option),
            }
            for option in options
        ],
    }


def _schema_value_key(value: str | None) -> str:
    return "__none__" if value is None else str(value)


def _values(df: pl.DataFrame, dimension: str) -> list[str | None]:
    return (
        df.select(pl.col(dimension))
        .unique(maintain_order=True)
        .get_column(dimension)
        .to_list()
    )


def _non_null_values(df: pl.DataFrame, dimension: str) -> list[str]:
    return [value for value in _values(df, dimension) if value is not None]


def _choose_requested_value(
    requested: str | None,
    options: Sequence[str | None],
    *,
    preferred: str | None = None,
) -> str | None:
    if not options:
        raise ValueError("Viewer selection has no valid options.")
    if requested in options:
        return requested
    if preferred in options:
        return preferred
    return options[0]


def _humanize(value: str | None, *, title_case: bool = False) -> str:
    if value is None:
        return "none"
    normalized = str(value).replace("_", " ").replace("-", " ")
    return normalized.title() if title_case else normalized


def _sort_with_preference(
    values: Sequence[str],
    preference: Mapping[str, int],
) -> list[str]:
    return sorted(
        values,
        key=lambda value: (preference.get(value, len(preference)), value),
    )


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"

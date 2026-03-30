from __future__ import annotations

from collections.abc import Collection, Mapping
from typing import Any

import polars as pl

SCORE_FIELDS: tuple[str, ...] = (
    "data_fidelity",
    "semantic_readability",
    "insight_discovery",
    "design_style",
    "visual_composition",
    "color_harmony",
)


def score_expr(
    score_field: str,
    *,
    source_columns: Collection[str],
    judgement_column: str = "judgement",
) -> pl.Expr:
    if score_field in source_columns:
        return pl.col(score_field).cast(pl.Float64)
    return (
        pl.col(judgement_column)
        .struct.field(score_field)
        .struct.field("score")
        .cast(pl.Float64)
    )


def overall_score_expr(
    *,
    source_columns: Collection[str],
    judgement_column: str = "judgement",
    round_to: int | None = None,
) -> pl.Expr:
    expr = pl.mean_horizontal(
        *(
            score_expr(
                score_field,
                source_columns=source_columns,
                judgement_column=judgement_column,
            )
            for score_field in SCORE_FIELDS
        )
    )
    if round_to is not None:
        expr = expr.round(round_to)
    return expr


def score_value(
    judgement: Mapping[str, Any] | None,
    score_field: str,
) -> float | None:
    if judgement is None:
        return None

    score_entry = judgement.get(score_field)
    if not isinstance(score_entry, Mapping):
        return None

    score = score_entry.get("score")
    if score is None:
        return None
    return float(score)


def overall_score_value(
    judgement: Mapping[str, Any] | None,
) -> float | None:
    if judgement is None:
        return None

    scores = [
        score
        for score_field in SCORE_FIELDS
        if (score := score_value(judgement, score_field)) is not None
    ]
    if not scores:
        return None
    return sum(scores) / len(scores)


__all__ = [
    "SCORE_FIELDS",
    "overall_score_expr",
    "overall_score_value",
    "score_value",
    "score_expr",
]

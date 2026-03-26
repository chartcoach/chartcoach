from __future__ import annotations

from collections.abc import Collection

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


__all__ = [
    "SCORE_FIELDS",
    "overall_score_expr",
    "score_expr",
]

"""Shared names and thresholds used across the analysis package."""

from __future__ import annotations

from visground.evaluation import SCORE_FIELDS

PAIR_AUDIENCE_SENTINEL = "__none__"
GUIDELINE_MIN_SUPPORT = 5

PRIMARY_SCORE_FIELDS: tuple[tuple[str, str, str], ...] = (
    ("overall", "overall_score", "delta_overall"),
    *tuple(
        (score_field, score_field, f"delta_{score_field}")
        for score_field in SCORE_FIELDS
    ),
)

VARIANCE_DELTA_COLUMNS: tuple[tuple[str, str], ...] = (
    ("pairwise_type_disagreement", "delta_pairwise_type_disagreement"),
    ("n_unique_visualization_types", "delta_n_unique_visualization_types"),
    ("dominant_type_share", "delta_dominant_type_share"),
    ("overall_score_std", "delta_overall_score_std"),
)

__all__ = [
    "GUIDELINE_MIN_SUPPORT",
    "PAIR_AUDIENCE_SENTINEL",
    "PRIMARY_SCORE_FIELDS",
    "VARIANCE_DELTA_COLUMNS",
]

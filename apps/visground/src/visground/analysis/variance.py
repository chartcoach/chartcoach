"""Measure whether grounding makes model/grammar outputs converge on similar designs."""

from __future__ import annotations

import statistics
from collections import Counter
from collections.abc import Sequence
from typing import Any

import polars as pl

from .schema import PAIR_AUDIENCE_SENTINEL, VARIANCE_DELTA_COLUMNS
from .stats import iter_slices, summarize_delta_values


def build_condition_variance_df(analysis_cases_df: pl.DataFrame) -> pl.DataFrame:
    """Compute per-condition design spread before grounded and baseline rows are paired."""
    rows: list[dict[str, Any]] = []
    grouped = analysis_cases_df.group_by(
        "vis_id",
        "objective",
        "_pair_audience",
        "grounding_mode",
        maintain_order=True,
    ).agg(group=pl.struct(pl.all()))

    for row in grouped.iter_rows(named=True):
        records = list(row["group"])
        types = [str(record["visualization_type"]) for record in records]
        scores = [
            float(record["overall_score"])
            for record in records
            if record.get("overall_score") is not None
        ]
        rows.append(
            {
                "vis_id": row["vis_id"],
                "objective": row["objective"],
                "audience": (
                    None
                    if row["_pair_audience"] == PAIR_AUDIENCE_SENTINEL
                    else row["_pair_audience"]
                ),
                "_pair_audience": row["_pair_audience"],
                "grounding_mode": row["grounding_mode"],
                "n_outputs": len(records),
                "n_unique_visualization_types": (
                    len(set(types)) if len(types) >= 2 else None
                ),
                "pairwise_type_disagreement": pairwise_type_disagreement(types),
                "dominant_type_share": dominant_type_share(types),
                "overall_score_std": score_std(scores),
            }
        )

    return pl.from_dicts(rows)


def build_design_variance_deltas_df(
    condition_variance_df: pl.DataFrame,
) -> pl.DataFrame:
    """Pair condition-level variance rows to show how grounding changes design spread."""
    grounded_df = condition_variance_df.filter(pl.col("grounding_mode") != "none")
    baseline_df = condition_variance_df.filter(pl.col("grounding_mode") == "none")

    baseline_select = [
        "vis_id",
        "objective",
        "_pair_audience",
        pl.col("n_outputs").alias("baseline_n_outputs"),
        pl.col("n_unique_visualization_types").alias(
            "baseline_n_unique_visualization_types"
        ),
        pl.col("pairwise_type_disagreement").alias(
            "baseline_pairwise_type_disagreement"
        ),
        pl.col("dominant_type_share").alias("baseline_dominant_type_share"),
        pl.col("overall_score_std").alias("baseline_overall_score_std"),
    ]
    return grounded_df.join(
        baseline_df.select(baseline_select),
        on=["vis_id", "objective", "_pair_audience"],
        how="left",
    ).with_columns(
        (
            pl.col("pairwise_type_disagreement")
            - pl.col("baseline_pairwise_type_disagreement")
        ).alias("delta_pairwise_type_disagreement"),
        (
            pl.col("n_unique_visualization_types")
            - pl.col("baseline_n_unique_visualization_types")
        ).alias("delta_n_unique_visualization_types"),
        (pl.col("dominant_type_share") - pl.col("baseline_dominant_type_share")).alias(
            "delta_dominant_type_share"
        ),
        (pl.col("overall_score_std") - pl.col("baseline_overall_score_std")).alias(
            "delta_overall_score_std"
        ),
    )


def build_variance_summary_df(design_variance_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Summarize whether grounding reduces or increases design spread across slices."""
    rows: list[dict[str, Any]] = []
    for slice_name, slice_value, slice_df in iter_slices(
        design_variance_deltas_df,
        columns=("objective",),
    ):
        for metric, delta_column in VARIANCE_DELTA_COLUMNS:
            values = [
                float(value)
                for value in slice_df.get_column(delta_column).drop_nulls().to_list()
            ]
            rows.append(
                {
                    "slice_name": slice_name,
                    "slice_value": slice_value,
                    "metric": metric,
                    **summarize_delta_values(values),
                }
            )
    return pl.from_dicts(rows)


def pairwise_type_disagreement(types: Sequence[str]) -> float | None:
    """Measure how often two outputs for the same query disagree on chart type."""
    n_types = len(types)
    if n_types < 2:
        return None

    total_pairs = n_types * (n_types - 1) / 2
    agreeing_pairs = sum(count * (count - 1) / 2 for count in Counter(types).values())
    return float((total_pairs - agreeing_pairs) / total_pairs)


def dominant_type_share(types: Sequence[str]) -> float | None:
    """Measure how strongly one chart type dominates the outputs for a query slice."""
    if not types:
        return None
    counts = Counter(types)
    return float(max(counts.values()) / len(types))


def score_std(scores: Sequence[float]) -> float | None:
    """Measure whether the judged quality of a query slice is tightly clustered or scattered."""
    if len(scores) < 2:
        return None
    return float(statistics.stdev(scores))


__all__ = [
    "VARIANCE_DELTA_COLUMNS",
    "build_condition_variance_df",
    "build_design_variance_deltas_df",
    "build_variance_summary_df",
    "dominant_type_share",
    "pairwise_type_disagreement",
    "score_std",
]

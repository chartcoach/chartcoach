from __future__ import annotations

import math

import polars as pl

from .contracts import VisEvalCohortConfig


def _compute_chart_quotas(
    capacities: dict[str, int],
    *,
    remaining_slots: int,
) -> dict[str, int]:
    quotas = {chart: 0 for chart in capacities}
    remaining_capacities = dict(capacities)
    remaining = remaining_slots

    while remaining_capacities and remaining > 0:
        even_share = remaining / len(remaining_capacities)
        exhausted = {
            chart: capacity
            for chart, capacity in remaining_capacities.items()
            if capacity <= even_share
        }

        if exhausted:
            for chart, capacity in exhausted.items():
                quotas[chart] = capacity
                remaining -= capacity
                del remaining_capacities[chart]
            continue

        floor_share = math.floor(even_share)
        for chart in remaining_capacities:
            quotas[chart] = floor_share

        assigned = floor_share * len(remaining_capacities)
        remainder = remaining - assigned
        for chart in sorted(
            remaining_capacities,
            key=lambda key: (remaining_capacities[key], key),
        )[:remainder]:
            quotas[chart] += 1
        remaining = 0

    return quotas


def _select_chart_balanced_round(
    round_df: pl.DataFrame,
    *,
    remaining_slots: int,
) -> pl.DataFrame:
    if round_df.height <= remaining_slots:
        return round_df

    capacities = {
        row["selected_chart"]: row["len"]
        for row in round_df.group_by("selected_chart").len().to_dicts()
    }
    quota_df = pl.DataFrame(
        {
            "selected_chart": list(capacities.keys()),
            "chart_quota": list(
                _compute_chart_quotas(
                    capacities,
                    remaining_slots=remaining_slots,
                ).values()
            ),
        }
    )

    return (
        round_df.with_columns(
            pl.int_range(1, pl.len() + 1)
            .over("selected_chart")
            .alias("chart_pick_rank")
        )
        .join(quota_df, on="selected_chart", how="left")
        .filter(pl.col("chart_pick_rank") <= pl.col("chart_quota"))
        .drop("chart_pick_rank", "chart_quota")
    )


def _select_interesting_round(
    ranked_candidates_df: pl.DataFrame,
    *,
    config: VisEvalCohortConfig,
) -> pl.DataFrame:
    floor = config["interestingness_score_floor"]
    above_floor_df = ranked_candidates_df.filter(pl.col("selection_score") >= floor)
    selected_df = _select_chart_balanced_round(
        above_floor_df,
        remaining_slots=config["target_n"],
    ).head(config["target_n"])

    if selected_df.height >= config["target_n"] or not config["backfill_below_floor"]:
        return selected_df

    fallback_df = ranked_candidates_df.filter(pl.col("selection_score") < floor)
    remaining_slots = config["target_n"] - selected_df.height
    if remaining_slots <= 0 or fallback_df.is_empty():
        return selected_df

    return pl.concat(
        [selected_df, fallback_df.head(remaining_slots)],
        how="vertical_relaxed",
    )

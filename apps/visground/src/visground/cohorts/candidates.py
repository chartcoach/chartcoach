from __future__ import annotations

from typing import cast

import polars as pl

from ..datasets import VisEvalDataset
from .chart_fit import _chart_fit_score
from .contracts import VisEvalCohortConfig
from .profile import interestingness_score, profile_dataframe

_HARDNESS_SCORE_MAP = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3,
    "Extra Hard": 4,
}

_SELECTED_CANDIDATE_FIELDS = [
    "chart_count",
    "selection_score",
    "interestingness_score",
    "chart_fit_score",
    "hardness_score",
    "chart",
    "id",
]


def _build_profile_df(
    dataset: VisEvalDataset,
    base_df: pl.DataFrame,
) -> pl.DataFrame:
    profile_rows: list[dict[str, object]] = []

    for row in base_df.select("id", "chart").iter_rows(named=True):
        vis_id = cast(str, row["id"])
        chart = cast(str, row["chart"])
        relation_df = dataset.vis_relation(vis_id).pl()
        profile = profile_dataframe(relation_df)
        base_score = interestingness_score(profile)
        chart_fit_score = _chart_fit_score(relation_df, chart)

        profile_rows.append(
            {
                "id": vis_id,
                "interestingness_score": base_score,
                "chart_fit_score": chart_fit_score,
                "selection_score": base_score + chart_fit_score,
            }
        )

    return pl.from_dicts(profile_rows)


def _build_request_base_df(dataset: VisEvalDataset) -> pl.DataFrame:
    return (
        dataset.queries_enriched_df.select(
            "id",
            "chart",
            "hardness",
            "db_id",
            "nl_query",
            "enrichment",
        )
        .unnest("enrichment")
        .group_by("id", maintain_order=True)
        .agg(data=pl.struct("*"))
        .select("id", pl.col("data").list.first())
        .unnest("data")
    )


def _build_scored_candidates_df(
    base_df: pl.DataFrame,
    profile_df: pl.DataFrame,
    *,
    seed: int,
) -> pl.DataFrame:
    chart_count_df = base_df.group_by("chart").len().rename({"len": "chart_count"})
    return (
        base_df.with_columns(
            hardness_score=pl.col("hardness").replace(_HARDNESS_SCORE_MAP)
        )
        .join(profile_df, on="id", how="left")
        .with_columns(
            pl.col("interestingness_score").fill_null(-10.0),
            pl.col("chart_fit_score").fill_null(0.0),
            pl.col("selection_score").fill_null(-10.0),
        )
        .join(chart_count_df, on="chart", how="left")
        .sample(fraction=1.0, seed=seed)
    )


def _select_query_representatives_df(
    scored_candidates_df: pl.DataFrame,
) -> pl.DataFrame:
    return (
        scored_candidates_df.group_by(
            "nl_query_canonical",
            "db_id",
            "task",
            "scope",
            "time_mode",
        )
        .agg(
            pl.col("chart").unique().alias("valid_charts"),
            pl.col("hardness").first().alias("hardness"),
            pl.col("hardness_score").max().alias("hardness_score"),
            pl.col("nl_query").first().alias("representative_nl_query"),
            pl.struct(_SELECTED_CANDIDATE_FIELDS)
            .sort_by(
                [
                    "chart_count",
                    "selection_score",
                    "interestingness_score",
                    "hardness_score",
                ],
                descending=[False, True, True, True],
            )
            .first()
            .alias("selected_candidate"),
        )
        .with_columns(
            num_valid_charts=pl.col("valid_charts").list.len(),
            original_id=pl.col("selected_candidate").struct.field("id"),
            selected_chart=pl.col("selected_candidate").struct.field("chart"),
            selected_chart_count=pl.col("selected_candidate").struct.field(
                "chart_count"
            ),
            interestingness_score=pl.col("selected_candidate").struct.field(
                "interestingness_score"
            ),
            chart_fit_score=pl.col("selected_candidate").struct.field(
                "chart_fit_score"
            ),
            selection_score=pl.col("selected_candidate").struct.field(
                "selection_score"
            ),
        )
        .drop("selected_candidate")
    )


def _apply_balance_ranks_df(
    representative_candidates_df: pl.DataFrame,
    *,
    max_tasks_per_db: int,
) -> pl.DataFrame:
    ranked_candidates_df = (
        representative_candidates_df.sort(
            by=[
                "selection_score",
                "interestingness_score",
                "num_valid_charts",
                "hardness_score",
                "selected_chart_count",
            ],
            descending=[True, True, True, True, False],
        )
        .with_columns(
            pl.int_range(1, pl.len() + 1).over("db_id").alias("db_balance_rank")
        )
        .filter(pl.col("db_balance_rank") <= max_tasks_per_db)
        .with_columns(
            pl.int_range(1, pl.len() + 1)
            .over(["db_balance_rank", "task"])
            .alias("task_balance_rank")
        )
    )

    return ranked_candidates_df.sort(
        by=[
            "db_balance_rank",
            "task_balance_rank",
            "selection_score",
            "interestingness_score",
            "num_valid_charts",
            "hardness_score",
            "selected_chart_count",
        ],
        descending=[False, False, True, True, True, True, False],
    )


def _build_ranked_candidates_df(
    dataset: VisEvalDataset,
    base_df: pl.DataFrame,
    *,
    config: VisEvalCohortConfig,
) -> pl.DataFrame:
    profile_df = _build_profile_df(dataset, base_df)
    scored_candidates_df = _build_scored_candidates_df(
        base_df,
        profile_df,
        seed=config["seed"],
    )
    representative_candidates_df = _select_query_representatives_df(
        scored_candidates_df
    )
    return _apply_balance_ranks_df(
        representative_candidates_df,
        max_tasks_per_db=config["max_tasks_per_db"],
    )

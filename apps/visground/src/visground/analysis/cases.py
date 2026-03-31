"""Build the grounded-vs-none score tables for matched chart-generation cases."""

from __future__ import annotations

from typing import Any

import polars as pl

from visground.evaluation import SCORE_FIELDS, overall_score_expr, score_expr

from .stats import fit_formula_model, iter_slices, summarize_delta_values
from .schema import PAIR_AUDIENCE_SENTINEL, PRIMARY_SCORE_FIELDS


def build_analysis_cases_df(
    candidates_df: pl.DataFrame,
    judgements_df: pl.DataFrame,
) -> pl.DataFrame:
    """Join generated charts with judge output so every row has comparable score columns."""
    selected_judgement_columns = [
        column
        for column in ("visgen_id", "judgement", "overall_score")
        if column in judgements_df.columns
    ]
    joined_df = candidates_df.join(
        judgements_df.select(selected_judgement_columns),
        on="visgen_id",
        how="left",
    )

    source_columns = joined_df.columns
    if "overall_score" in source_columns:
        overall_expr = pl.col("overall_score").cast(pl.Float64)
    else:
        overall_expr = overall_score_expr(source_columns=source_columns)

    return joined_df.with_columns(
        *(
            score_expr(score_field, source_columns=source_columns).alias(score_field)
            for score_field in SCORE_FIELDS
        ),
        overall_expr.alias("overall_score"),
        pl.col("guideline_ids").list.len().fill_null(0).alias("guideline_count"),
        pl.col("judgement").is_not_null().alias("has_judgement"),
        pl.col("grounding_mode").ne("none").alias("is_grounded"),
        pl.coalesce(pl.col("audience"), pl.lit(PAIR_AUDIENCE_SENTINEL)).alias(
            "_pair_audience"
        ),
    )


def build_paired_case_deltas_df(analysis_cases_df: pl.DataFrame) -> pl.DataFrame:
    """Match each grounded row to the same ungrounded setup to isolate grounding deltas."""
    pair_keys = [
        "vis_id",
        "objective",
        "model",
        "grammar",
        "_pair_audience",
    ]
    grounded_df = analysis_cases_df.filter(pl.col("is_grounded"))
    baseline_df = analysis_cases_df.filter(pl.col("grounding_mode") == "none")

    baseline_duplicates = (
        baseline_df.group_by(*pair_keys)
        .agg(pl.len().alias("count"))
        .filter(pl.col("count") > 1)
    )
    if not baseline_duplicates.is_empty():
        raise ValueError(
            "Expected at most one ungrounded baseline per pair key, got "
            + str(baseline_duplicates.to_dicts())
        )

    baseline_select = [
        *pair_keys,
        pl.col("visgen_id").alias("baseline_visgen_id"),
        pl.col("grounding_id").alias("baseline_grounding_id"),
        pl.col("visualization_type").alias("baseline_visualization_type"),
        pl.col("has_judgement").alias("baseline_has_judgement"),
        *(
            pl.col(source_column).alias(f"baseline_{source_column}")
            for _, source_column, _ in PRIMARY_SCORE_FIELDS
        ),
    ]
    paired_df = grounded_df.join(
        baseline_df.select(baseline_select),
        on=pair_keys,
        how="left",
    )

    complete_expr = pl.col("has_judgement") & pl.col(
        "baseline_has_judgement"
    ).fill_null(False)
    delta_exprs = [
        pl.when(complete_expr)
        .then(pl.col(source_column) - pl.col(f"baseline_{source_column}"))
        .otherwise(pl.lit(None).cast(pl.Float64))
        .alias(delta_column)
        for _, source_column, delta_column in PRIMARY_SCORE_FIELDS
    ]

    return paired_df.with_columns(
        complete_expr.alias("complete_pair"),
        pl.when(pl.col("baseline_visualization_type").is_not_null())
        .then(pl.col("visualization_type") != pl.col("baseline_visualization_type"))
        .otherwise(pl.lit(None).cast(pl.Boolean))
        .alias("chart_type_changed"),
        *delta_exprs,
    ).with_columns(
        pl.when(pl.col("delta_overall").is_not_null())
        .then(pl.col("delta_overall") > 0)
        .otherwise(pl.lit(None).cast(pl.Boolean))
        .alias("grounded_win"),
        pl.when(pl.col("delta_overall").is_not_null())
        .then(pl.col("delta_overall") < 0)
        .otherwise(pl.lit(None).cast(pl.Boolean))
        .alias("grounded_loss"),
        pl.when(pl.col("delta_overall").is_not_null())
        .then(pl.col("delta_overall") == 0)
        .otherwise(pl.lit(None).cast(pl.Boolean))
        .alias("tie"),
    )


def build_score_summary_df(paired_case_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Summarize whether grounding tends to raise or lower judged scores in matched pairs."""
    complete_df = paired_case_deltas_df.filter(pl.col("complete_pair"))
    rows: list[dict[str, Any]] = []
    for slice_name, slice_value, slice_df in iter_slices(
        complete_df,
        columns=("objective", "model", "grammar"),
    ):
        for metric, _, delta_column in PRIMARY_SCORE_FIELDS:
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


def build_score_models_df(paired_case_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Estimate the average `delta_overall` while controlling for objective, model, and grammar."""
    complete_df = paired_case_deltas_df.filter(pl.col("complete_pair"))
    if complete_df.is_empty():
        return pl.DataFrame(
            schema=[
                ("metric", pl.String),
                ("term", pl.String),
                ("coef", pl.Float64),
                ("std_err", pl.Float64),
                ("ci_low", pl.Float64),
                ("ci_high", pl.Float64),
                ("p_value", pl.Float64),
                ("n_obs", pl.Int64),
                ("n_clusters", pl.Int64),
                ("covariance_type", pl.String),
            ]
        )

    df = complete_df.to_pandas()
    model = fit_formula_model(df, outcome="delta_overall", feature_terms=())
    if model is None:
        return pl.DataFrame()

    conf_df = model.conf_int()
    n_clusters = int(df["vis_id"].nunique())
    rows = []
    for term in model.params.index:
        rows.append(
            {
                "metric": "overall",
                "term": term,
                "coef": float(model.params[term]),
                "std_err": float(model.bse[term]),
                "ci_low": float(conf_df.loc[term].iloc[0]),
                "ci_high": float(conf_df.loc[term].iloc[1]),
                "p_value": float(model.pvalues[term]),
                "n_obs": int(model.nobs),
                "n_clusters": n_clusters,
                "covariance_type": str(model.cov_type),
            }
        )
    return pl.from_dicts(rows)


def build_chart_type_summary_df(paired_case_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Show which grounded chart types tend to help or hurt relative to baseline."""
    return (
        paired_case_deltas_df.filter(pl.col("complete_pair"))
        .group_by("visualization_type")
        .agg(
            support=pl.len(),
            mean_delta=pl.col("delta_overall").mean(),
            win_rate=pl.col("grounded_win").cast(pl.Float64).mean(),
            mean_grounded_score=pl.col("overall_score").mean(),
            mean_baseline_score=pl.col("baseline_overall_score").mean(),
        )
        .sort("mean_delta", descending=True)
    )


def build_model_grammar_summary_df(paired_case_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Show where grounding helps most once model and grammar are considered together."""
    return (
        paired_case_deltas_df.filter(pl.col("complete_pair"))
        .group_by("model", "grammar")
        .agg(
            support=pl.len(),
            mean_delta=pl.col("delta_overall").mean(),
            win_rate=pl.col("grounded_win").cast(pl.Float64).mean(),
        )
        .sort(["model", "mean_delta"], descending=[False, True])
    )


def build_chart_transition_summary_df(
    paired_case_deltas_df: pl.DataFrame,
) -> pl.DataFrame:
    """Show which baseline-to-grounded chart-type transitions help or hurt most."""
    return (
        paired_case_deltas_df.filter(pl.col("complete_pair"))
        .group_by("baseline_visualization_type", "visualization_type")
        .agg(
            support=pl.len(),
            mean_delta=pl.col("delta_overall").mean(),
            win_rate=pl.col("grounded_win").cast(pl.Float64).mean(),
        )
        .sort("mean_delta", descending=True)
    )


__all__ = [
    "PAIR_AUDIENCE_SENTINEL",
    "PRIMARY_SCORE_FIELDS",
    "build_analysis_cases_df",
    "build_chart_type_summary_df",
    "build_chart_transition_summary_df",
    "build_model_grammar_summary_df",
    "build_paired_case_deltas_df",
    "build_score_models_df",
    "build_score_summary_df",
]

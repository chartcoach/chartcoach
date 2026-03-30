"""Summarize which retrieved guidelines show up and how they track grounded-vs-none deltas."""

from __future__ import annotations

from typing import Any

import polars as pl
from statsmodels.stats.multitest import fdrcorrection

from .schema import GUIDELINE_MIN_SUPPORT
from .stats import fit_formula_model, guideline_list, iter_slices


def build_guideline_summary_df(paired_case_deltas_df: pl.DataFrame) -> pl.DataFrame:
    """Count which grounded guidelines appear often and whether their paired deltas skew positive."""
    complete_df = paired_case_deltas_df.filter(
        pl.col("complete_pair") & (pl.col("guideline_count") > 0)
    )
    if complete_df.is_empty():
        return pl.DataFrame(
            schema=[
                ("slice_name", pl.String),
                ("slice_value", pl.String),
                ("guideline_id", pl.String),
                ("support", pl.Int64),
                ("coverage", pl.Float64),
                ("mean_delta_overall", pl.Float64),
                ("median_delta_overall", pl.Float64),
                ("win_rate", pl.Float64),
            ]
        )

    rows: list[dict[str, Any]] = []
    for slice_name, slice_value, slice_df in iter_slices(
        complete_df,
        columns=("objective",),
    ):
        total_pairs = slice_df.height
        exploded = slice_df.explode("guideline_ids").rename(
            {"guideline_ids": "guideline_id"}
        )
        for item in (
            exploded.group_by("guideline_id", maintain_order=True)
            .agg(
                support=pl.len(),
                mean_delta_overall=pl.col("delta_overall").mean(),
                median_delta_overall=pl.col("delta_overall").median(),
                win_rate=pl.col("grounded_win").cast(pl.Float64).mean(),
            )
            .iter_rows(named=True)
        ):
            rows.append(
                {
                    "slice_name": slice_name,
                    "slice_value": slice_value,
                    "guideline_id": item["guideline_id"],
                    "support": item["support"],
                    "coverage": (
                        float(item["support"]) / float(total_pairs)
                        if total_pairs
                        else None
                    ),
                    "mean_delta_overall": item["mean_delta_overall"],
                    "median_delta_overall": item["median_delta_overall"],
                    "win_rate": item["win_rate"],
                }
            )
    return pl.from_dicts(rows)


def build_guideline_associations_df(
    paired_case_deltas_df: pl.DataFrame,
) -> pl.DataFrame:
    """Check whether a specific guideline lines up with bigger or smaller `delta_overall` values."""
    complete_df = paired_case_deltas_df.filter(pl.col("complete_pair"))
    exploded = complete_df.explode("guideline_ids").rename(
        {"guideline_ids": "guideline_id"}
    )
    if exploded.is_empty():
        return pl.DataFrame(
            schema=[
                ("guideline_id", pl.String),
                ("support", pl.Int64),
                ("coef", pl.Float64),
                ("std_err", pl.Float64),
                ("ci_low", pl.Float64),
                ("ci_high", pl.Float64),
                ("p_value", pl.Float64),
                ("p_value_adj", pl.Float64),
                ("mean_delta_when_used", pl.Float64),
                ("mean_delta_when_not_used", pl.Float64),
            ]
        )

    guideline_support_df = (
        exploded.group_by("guideline_id")
        .agg(support=pl.len())
        .filter(pl.col("support") >= GUIDELINE_MIN_SUPPORT)
        .sort("guideline_id")
    )
    if guideline_support_df.is_empty():
        return guideline_support_df.with_columns(
            pl.lit(None, dtype=pl.Float64).alias("coef"),
            pl.lit(None, dtype=pl.Float64).alias("std_err"),
            pl.lit(None, dtype=pl.Float64).alias("ci_low"),
            pl.lit(None, dtype=pl.Float64).alias("ci_high"),
            pl.lit(None, dtype=pl.Float64).alias("p_value"),
            pl.lit(None, dtype=pl.Float64).alias("p_value_adj"),
            pl.lit(None, dtype=pl.Float64).alias("mean_delta_when_used"),
            pl.lit(None, dtype=pl.Float64).alias("mean_delta_when_not_used"),
        )

    base_df = complete_df.to_pandas()
    rows: list[dict[str, Any]] = []
    for item in guideline_support_df.iter_rows(named=True):
        guideline_id = str(item["guideline_id"])
        df = base_df.copy()
        df["has_guideline"] = df["guideline_ids"].apply(
            lambda ids: guideline_id in guideline_list(ids)
        )
        model = fit_formula_model(
            df,
            outcome="delta_overall",
            feature_terms=("has_guideline",),
        )
        if model is None or "has_guideline[T.True]" not in model.params.index:
            continue

        ci = model.conf_int().loc["has_guideline[T.True]"]
        used = df[df["has_guideline"]]
        not_used = df[~df["has_guideline"]]
        rows.append(
            {
                "guideline_id": guideline_id,
                "support": int(item["support"]),
                "coef": float(model.params["has_guideline[T.True]"]),
                "std_err": float(model.bse["has_guideline[T.True]"]),
                "ci_low": float(ci.iloc[0]),
                "ci_high": float(ci.iloc[1]),
                "p_value": float(model.pvalues["has_guideline[T.True]"]),
                "mean_delta_when_used": float(used["delta_overall"].mean()),
                "mean_delta_when_not_used": float(not_used["delta_overall"].mean()),
            }
        )

    associations_df = pl.from_dicts(rows)
    if associations_df.is_empty():
        return associations_df

    _, adjusted = fdrcorrection(associations_df.get_column("p_value").to_list())
    return associations_df.with_columns(pl.Series("p_value_adj", adjusted))


__all__ = [
    "GUIDELINE_MIN_SUPPORT",
    "build_guideline_associations_df",
    "build_guideline_summary_df",
]

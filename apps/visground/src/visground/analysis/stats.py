"""Shared helpers for summarizing grounding deltas and fitting simple robustness models."""

from __future__ import annotations

import statistics
from collections.abc import Sequence
from typing import Any

import pandas as pd
import polars as pl
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import DescrStatsW


def iter_slices(
    df: pl.DataFrame,
    *,
    columns: Sequence[str],
) -> Sequence[tuple[str, str, pl.DataFrame]]:
    """Yield the full data and the key objective/model/grammar slices used in comparisons."""
    slices: list[tuple[str, str, pl.DataFrame]] = [("all", "all", df)]
    for column in columns:
        if column not in df.columns:
            continue
        values = (
            df.get_column(column).drop_nulls().unique(maintain_order=True).to_list()
        )
        for value in values:
            slices.append((column, str(value), df.filter(pl.col(column) == value)))
    return slices


def summarize_delta_values(values: Sequence[float]) -> dict[str, Any]:
    """Turn paired grounded-vs-none deltas into effect size, uncertainty, and win rates."""
    n_values = len(values)
    if n_values == 0:
        return {
            "n_pairs": 0,
            "mean_delta": None,
            "median_delta": None,
            "ci_low": None,
            "ci_high": None,
            "win_rate": None,
            "loss_rate": None,
            "tie_rate": None,
            "win_count": 0,
            "loss_count": 0,
            "tie_count": 0,
        }

    stats = DescrStatsW(values)
    if n_values > 1:
        ci_low, ci_high = stats.tconfint_mean()
    else:
        ci_low, ci_high = (None, None)

    win_count = sum(value > 0 for value in values)
    loss_count = sum(value < 0 for value in values)
    tie_count = sum(value == 0 for value in values)
    return {
        "n_pairs": n_values,
        "mean_delta": float(stats.mean),
        "median_delta": float(statistics.median(values)),
        "ci_low": float(ci_low) if ci_low is not None else None,
        "ci_high": float(ci_high) if ci_high is not None else None,
        "win_rate": win_count / n_values,
        "loss_rate": loss_count / n_values,
        "tie_rate": tie_count / n_values,
        "win_count": win_count,
        "loss_count": loss_count,
        "tie_count": tie_count,
    }


def fit_formula_model(
    df: pd.DataFrame,
    *,
    outcome: str,
    feature_terms: Sequence[str],
) -> Any | None:
    """Fit one small OLS model to check whether a grounding signal survives simple controls."""
    if df.empty or df[outcome].isna().all():
        return None

    terms = list(feature_terms)
    for column in ("objective", "model", "grammar"):
        if column in df.columns and df[column].nunique(dropna=False) > 1:
            terms.append(f"C({column})")

    rhs = " + ".join(["1", *terms]) if terms else "1"
    formula = f"{outcome} ~ {rhs}"
    fitted = smf.ols(formula, data=df)

    if "vis_id" in df.columns and df["vis_id"].nunique(dropna=False) > 1:
        try:
            return fitted.fit(cov_type="cluster", cov_kwds={"groups": df["vis_id"]})
        except Exception:
            pass

    return fitted.fit(cov_type="HC3")


def guideline_list(value: object) -> list[str]:
    """Normalize stored guideline ids so usage and association checks read the same values."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence):
        return [str(item) for item in value]
    return []


__all__ = [
    "fit_formula_model",
    "guideline_list",
    "iter_slices",
    "summarize_delta_values",
]

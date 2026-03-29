from __future__ import annotations

import math
from datetime import date, datetime
from typing import cast

import polars as pl

from .basics import _clamp, _float_stat
from .columns import _numeric_series


def _series_variability_score(series: pl.Series) -> float:
    if series.is_empty():
        return -1.0

    n_values = series.len()
    n_unique = series.n_unique()
    if n_unique <= 1:
        return -1.5
    if n_values <= 2:
        return -1.0

    min_value = cast(int | float | None, series.min())
    max_value = cast(int | float | None, series.max())
    if min_value is None or max_value is None:
        return -1.0

    value_range = float(max_value - min_value)
    if value_range <= 0:
        return -1.5

    mean = _float_stat(series.mean())
    median = _float_stat(series.median())
    std = _float_stat(series.std())
    reference = max(abs(mean), abs(median), 1.0)
    cv = std / reference

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = float(q3 - q1) if q1 is not None and q3 is not None else 0.0
    iqr_share = iqr / value_range if value_range > 0 else 0.0

    score = 0.0
    score += 0.8 * _clamp(cv / 0.5)
    score += 0.5 * _clamp(iqr_share / 0.45)
    if n_unique >= min(n_values, 6):
        score += 0.25

    if cv < 0.08:
        score -= 1.0
    elif cv < 0.15:
        score -= 0.4

    if n_values <= 4:
        score -= 0.4

    return score


def _correlation_score(df: pl.DataFrame, measure_cols: list[str]) -> float:
    if len(measure_cols) < 2:
        return 0.0

    variable_cols = [
        name for name in measure_cols if df.get_column(name).drop_nulls().n_unique() > 1
    ]
    if len(variable_cols) < 2:
        return 0.0

    valid_df = df.select(pl.col(variable_cols).cast(pl.Float64)).drop_nulls()
    if valid_df.height < 6:
        return 0.0

    corr_values = valid_df.corr().to_numpy()
    max_corr = 0.0
    for i, row in enumerate(corr_values):
        for j, value in enumerate(row):
            if i == j or value is None or math.isnan(value):
                continue
            max_corr = max(max_corr, abs(float(value)))
    return max_corr


def _shape_anomaly_scores(
    df: pl.DataFrame,
    measure_cols: list[str],
) -> tuple[list[float], list[float]]:
    outlier_rates: list[float] = []
    skew_scores: list[float] = []

    for name in measure_cols:
        series = _numeric_series(df, name)
        if series.len() < 6:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        if q1 is not None and q3 is not None:
            iqr = q3 - q1
            if iqr > 0:
                lo = q1 - 1.5 * iqr
                hi = q3 + 1.5 * iqr
                outlier_mask = ((series < lo) | (series > hi)).cast(pl.Float64)
                outlier_rates.append(float(outlier_mask.sum()) / series.len())

        skew = series.skew()
        if skew is not None and not math.isnan(skew):
            skew_scores.append(abs(float(skew)))

    return outlier_rates, skew_scores


def _temporal_structure_score(
    df: pl.DataFrame,
    temporal_cols: list[str],
    measure_cols: list[str],
) -> float:
    best_score = 0.0
    if not temporal_cols or not measure_cols:
        return best_score

    for temporal_name in temporal_cols:
        temporal_series = df.get_column(temporal_name).drop_nulls()
        if temporal_series.is_empty() or temporal_series.n_unique() < 4:
            continue

        min_value = temporal_series.min()
        max_value = temporal_series.max()
        if min_value is None or max_value is None:
            continue
        if not isinstance(min_value, (date, datetime)) or not isinstance(
            max_value,
            (date, datetime),
        ):
            continue

        span_days = float((max_value - min_value).total_seconds() / 86400.0)
        if span_days < 30:
            continue

        for measure_name in measure_cols:
            pair_df = (
                df.select(temporal_name, measure_name).drop_nulls().sort(temporal_name)
            )
            if pair_df.height < 4:
                continue

            values = pair_df.get_column(measure_name).cast(pl.Float64)
            diffs = values.diff().drop_nulls().abs()
            if diffs.is_empty():
                continue

            mean_abs = max(abs(_float_stat(values.mean())), 1.0)
            movement = _float_stat(diffs.mean()) / mean_abs
            variability = _float_stat(values.std()) / mean_abs
            score = 0.6 * _clamp(movement / 0.25) + 0.4 * _clamp(variability / 0.2)
            best_score = max(best_score, score)

    return best_score

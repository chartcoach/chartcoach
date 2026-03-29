from __future__ import annotations

import math

import polars as pl

from .basics import _clamp, _normalized_entropy


def _sign_change_rate(values: list[float]) -> float:
    if len(values) < 3:
        return 0.0

    diffs = [float(b) - float(a) for a, b in zip(values, values[1:])]
    signs = [1 if diff > 1e-9 else -1 if diff < -1e-9 else 0 for diff in diffs]
    non_zero_signs = [sign for sign in signs if sign != 0]
    if len(non_zero_signs) < 2:
        return 0.0

    changes = sum(1 for a, b in zip(non_zero_signs, non_zero_signs[1:]) if a != b)
    return changes / (len(non_zero_signs) - 1)


def _line_chart_fit_score(df: pl.DataFrame) -> float:
    if df.width < 2:
        return -2.0

    x_col, y_col = df.columns[0], df.columns[1]
    group_col = df.columns[2] if df.width >= 3 else None
    work_df = df.select(df.columns[:3]).drop_nulls()
    if work_df.is_empty():
        return -2.0

    if group_col is None:
        grouped_series = [work_df]
    else:
        group_values = work_df.get_column(group_col).drop_nulls().unique().to_list()
        grouped_series = [
            work_df.filter(pl.col(group_col) == value) for value in group_values
        ]

    series_scores: list[float] = []
    for series_df in grouped_series:
        if series_df.height < 3:
            continue

        reduced_df = (
            series_df.group_by(x_col)
            .agg(pl.col(y_col).cast(pl.Float64).mean().alias(y_col))
            .sort(x_col)
        )
        y_values = [
            float(value)
            for value in reduced_df.get_column(y_col).to_list()
            if value is not None
        ]
        if len(y_values) < 3:
            continue

        rounded_y_values = [round(value, 9) for value in y_values]
        unique_y = len(set(rounded_y_values))
        non_monotonicity = _sign_change_rate(y_values)
        mean_abs = max(sum(abs(value) for value in y_values) / len(y_values), 1.0)
        amplitude = max(max(y_values) - min(y_values), 0.0) / mean_abs
        dominant_value_share = max(
            rounded_y_values.count(value) for value in set(rounded_y_values)
        ) / len(rounded_y_values)

        score = 0.0
        score += 1.7 * _clamp(non_monotonicity / 0.6)
        score += 0.8 * _clamp(amplitude / 1.0)
        score += 0.35 * _clamp((len(y_values) - 3) / 5.0)

        if unique_y <= 1:
            score -= 2.5
        elif unique_y <= 2:
            score -= 1.1
        if non_monotonicity == 0.0 and len(y_values) >= 5:
            score -= 1.4
        if len(y_values) <= 20 and amplitude < 1.0:
            if unique_y <= 2:
                score -= 1.0
            if dominant_value_share >= 0.6:
                score -= 1.3 * _clamp((dominant_value_share - 0.6) / 0.3)

        series_scores.append(score)

    if not series_scores:
        return -1.5

    return sum(series_scores) / len(series_scores)


def _pie_chart_fit_score(df: pl.DataFrame) -> float:
    if df.width < 2:
        return -2.0

    value_col = df.columns[1]
    try:
        values = [
            abs(float(value))
            for value in df.get_column(value_col)
            .drop_nulls()
            .cast(pl.Float64)
            .to_list()
            if value is not None and abs(float(value)) > 0
        ]
    except (TypeError, ValueError, pl.exceptions.InvalidOperationError):
        return -2.0

    if len(values) < 3:
        return -2.0

    total = sum(values)
    if total <= 0:
        return -2.0

    probabilities = [value / total for value in values]
    category_count = len(values)
    normalized_entropy = _normalized_entropy(values)
    mean_probability = 1.0 / category_count
    share_std = math.sqrt(
        sum((probability - mean_probability) ** 2 for probability in probabilities)
        / category_count
    )
    share_cv = share_std / mean_probability if mean_probability > 0 else 0.0
    dominance = max(probabilities)

    score = 0.0
    if 3 <= category_count <= 6:
        score += 1.0
    elif category_count <= 8:
        score += 0.35
    elif category_count <= 10:
        score -= 0.6
    else:
        score -= 1.2

    score += 1.15 * _clamp(share_cv / 0.75)
    score += 0.95 * _clamp((0.92 - normalized_entropy) / 0.32)

    if normalized_entropy >= 0.97:
        score -= 0.9 * _clamp((normalized_entropy - 0.97) / 0.03)
    if dominance >= 0.82:
        score -= 0.8 * _clamp((dominance - 0.82) / 0.18)

    return score


def _chart_fit_score(df: pl.DataFrame, chart: str) -> float:
    if chart in {"Line", "Grouping Line"}:
        return _line_chart_fit_score(df)
    if chart == "Pie":
        return _pie_chart_fit_score(df)
    return 0.0

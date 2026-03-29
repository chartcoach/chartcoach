from __future__ import annotations

import math

import polars as pl

from .basics import _clamp, _normalized_entropy


def _groupability_score(cardinality: int) -> float:
    if 3 <= cardinality <= 12:
        return 1.0
    if cardinality == 2:
        return -0.4
    if 13 <= cardinality <= 24:
        return 0.25
    if cardinality <= 1 or cardinality > 48:
        return -0.75
    return 0.0


def _distribution_shape_score(weights: list[float]) -> float:
    positive_weights = [float(weight) for weight in weights if float(weight) > 0]
    if len(positive_weights) <= 1:
        return -1.0

    if len(positive_weights) == 2:
        return -0.75

    total = sum(positive_weights)
    probabilities = [weight / total for weight in positive_weights]
    mean_probability = 1.0 / len(probabilities)
    normalized_entropy = _normalized_entropy(positive_weights)
    dominance = max(probabilities)
    share_std = math.sqrt(
        sum((probability - mean_probability) ** 2 for probability in probabilities)
        / len(probabilities)
    )
    share_cv = share_std / mean_probability if mean_probability > 0 else 0.0

    score = 0.0
    score += 1.0 - _clamp(abs(normalized_entropy - 0.75) / 0.35)
    score += 0.35 * _clamp(share_cv / 0.75)

    if normalized_entropy >= 0.95:
        score -= 0.9 * _clamp((normalized_entropy - 0.95) / 0.05)
    if dominance >= 0.8:
        score -= 1.0 * _clamp((dominance - 0.8) / 0.2)
    if share_cv >= 1.25:
        score -= 0.6 * _clamp((share_cv - 1.25) / 0.75)

    return score


def _distribution_scores(
    df: pl.DataFrame,
    grouping_cols: list[str],
    measure_cols: list[str],
) -> tuple[list[float], list[float]]:
    groupability_scores: list[float] = []
    distribution_scores: list[float] = []

    for name in grouping_cols:
        series = df.get_column(name).drop_nulls()
        if series.is_empty():
            continue

        n_unique = series.n_unique()
        groupability_scores.append(_groupability_score(n_unique))

        count_values = [
            float(value)
            for value in (
                series.value_counts(sort=True)
                .get_column("count")
                .cast(pl.Float64)
                .to_list()
            )
        ]
        best_distribution_score = _distribution_shape_score(count_values)

        for measure_name in measure_cols:
            pair_df = df.select(name, measure_name).drop_nulls()
            if pair_df.height <= 1:
                continue

            weighted_df = pair_df.group_by(name).agg(
                weight=pl.col(measure_name).abs().sum().cast(pl.Float64)
            )
            weights = weighted_df.get_column("weight").to_list()
            best_distribution_score = max(
                best_distribution_score,
                _distribution_shape_score(weights),
            )

        distribution_scores.append(best_distribution_score)

    return groupability_scores, distribution_scores

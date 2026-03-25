from __future__ import annotations

import math
import re
from datetime import date, datetime
from typing import Literal, TypedDict, cast

import polars as pl

RowBand = Literal["tiny", "small", "medium", "large"]
MeasureBand = Literal["single", "multi"]
GroupCardinalityBand = Literal["binary", "few", "many"]


class DataProfileMetrics(TypedDict):
    row_count: int
    column_count: int
    has_temporal: bool
    measure_count: int
    grouping_count: int
    interestingness_score: float
    max_abs_correlation: float
    mean_abs_skew: float
    mean_outlier_rate: float
    temporal_structure_score: float
    missing_fraction: float


class GroundingProfile(TypedDict):
    row_band: RowBand
    measure: MeasureBand
    has_temporal: bool
    group_cardinality: GroupCardinalityBand | None
    correlated: bool
    skewed: bool
    outlier_rich: bool
    temporal_dynamic: bool
    retrieval_labels: list[str]


class DataProfile(TypedDict):
    metrics: DataProfileMetrics
    facets: GroundingProfile
    retrieval_labels: list[str]


_IDENTIFIER_NAME_RE = re.compile(r"(?:^|_)id$", re.IGNORECASE)


def _clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(value, hi))


def _normalize_name(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", name.lower()).strip("_")


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


def _normalized_entropy(weights: list[float]) -> float:
    if len(weights) <= 1:
        return 0.0
    total = sum(weights)
    if total <= 0:
        return 0.0

    entropy = -sum(
        probability * math.log(probability)
        for probability in (weight / total for weight in weights)
        if probability > 0
    )
    return entropy / math.log(len(weights))


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


def _numeric_series(df: pl.DataFrame, column: str) -> pl.Series:
    return df.get_column(column).drop_nulls().cast(pl.Float64)


def _float_stat(value: object | None) -> float:
    if value is None:
        return 0.0
    return float(cast(int | float, value))


def _is_row_key_like(series: pl.Series) -> bool:
    if series.is_empty() or not series.dtype.is_integer():
        return False
    if series.len() < 8:
        return False

    unique_ratio = series.n_unique() / series.len()
    if unique_ratio < 0.98:
        return False

    return bool(series.is_sorted() or series.is_sorted(descending=True))


def _is_identifier_like_numeric(name: str, series: pl.Series) -> bool:
    normalized_name = _normalize_name(name)
    return bool(_IDENTIFIER_NAME_RE.search(normalized_name) or _is_row_key_like(series))


def _classify_numeric_columns(
    df: pl.DataFrame,
    numeric_cols: list[str],
) -> tuple[list[str], list[str]]:
    measure_cols: list[str] = []
    identifier_cols: list[str] = []

    for name in numeric_cols:
        series = df.get_column(name).drop_nulls()
        if series.is_empty():
            continue
        if _is_identifier_like_numeric(name, series):
            identifier_cols.append(name)
            continue
        measure_cols.append(name)

    return measure_cols, identifier_cols


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


def _row_band(n_rows: int) -> RowBand:
    if n_rows <= 5:
        return "tiny"
    if n_rows <= 20:
        return "small"
    if n_rows <= 100:
        return "medium"
    return "large"


def _group_cardinality_band(max_unique: int | None) -> GroupCardinalityBand | None:
    if max_unique is None:
        return None
    if max_unique <= 2:
        return "binary"
    if max_unique <= 12:
        return "few"
    return "many"


def _measure_band(measure_count: int) -> MeasureBand:
    return "multi" if measure_count >= 2 else "single"


def profile_dataframe(
    df: pl.DataFrame,
    *,
    include_samples: bool = False,
) -> DataProfile:
    schema = df.schema
    bool_cols = [name for name, dtype in schema.items() if dtype == pl.Boolean]
    numeric_cols = [
        name
        for name, dtype in schema.items()
        if dtype.is_numeric() and dtype != pl.Boolean
    ]
    temporal_cols = [name for name, dtype in schema.items() if dtype.is_temporal()]
    categorical_cols = [
        name
        for name in df.columns
        if name not in numeric_cols
        and name not in temporal_cols
        and name not in bool_cols
    ]
    measure_cols, identifier_cols = _classify_numeric_columns(df, numeric_cols)
    grouping_cols = [*categorical_cols, *bool_cols]

    group_uniques = []
    for name in grouping_cols:
        series = df.get_column(name).drop_nulls()
        if series.is_empty():
            continue
        group_uniques.append(int(series.n_unique()))

    groupability_scores, distribution_scores = _distribution_scores(
        df,
        grouping_cols,
        measure_cols,
    )
    variability_scores = [
        _series_variability_score(_numeric_series(df, name)) for name in measure_cols
    ]
    correlation_score = _correlation_score(df, measure_cols)
    outlier_rates, skew_scores = _shape_anomaly_scores(df, measure_cols)
    temporal_structure_score = _temporal_structure_score(
        df, temporal_cols, measure_cols
    )
    missing_fraction = float(df.null_count().sum_horizontal().item()) / max(
        df.height * max(df.width, 1),
        1,
    )

    score = 0.0
    informative_col_count = df.width - len(identifier_cols)
    score += 0.45 * min(math.log1p(df.height), 4.0)
    score += 0.55 * min(max(informative_col_count - 1, 0), 4)
    score += 0.6 * max(
        int(bool(measure_cols))
        + int(bool(categorical_cols))
        + int(bool(temporal_cols))
        + int(bool(bool_cols))
        - 1,
        0,
    )
    if groupability_scores:
        score += 0.8 * (sum(groupability_scores) / len(groupability_scores))
    if distribution_scores:
        score += 1.25 * (sum(distribution_scores) / len(distribution_scores))
    if variability_scores:
        score += 0.95 * (sum(variability_scores) / len(variability_scores))
    score += 1.35 * correlation_score
    if outlier_rates:
        score += 0.45 * min((sum(outlier_rates) / len(outlier_rates)) / 0.05, 1.0)
    if skew_scores:
        score += 0.45 * min((sum(skew_scores) / len(skew_scores)) / 1.0, 1.0)
    score += 0.65 * temporal_structure_score

    retrieval_labels: list[str] = []
    if measure_cols:
        retrieval_labels.append("data:quantitative")
    if categorical_cols or bool_cols:
        retrieval_labels.append("data:categorical")
    if temporal_cols:
        retrieval_labels.append("data:temporal")
    if df.width >= 3:
        retrieval_labels.append("data:tabular")
    if not temporal_cols:
        retrieval_labels.append("time:non-temporal")
    elif temporal_structure_score >= 0.5:
        retrieval_labels.append("time:ordered-time")
    retrieval_labels.append(f"measure:{_measure_band(len(measure_cols))}")
    if (
        group_band := _group_cardinality_band(
            max(group_uniques) if group_uniques else None
        )
    ) is not None:
        retrieval_labels.append(f"group-cardinality:{group_band}")
    if (sum(skew_scores) / len(skew_scores) if skew_scores else 0.0) >= 1.0:
        retrieval_labels.append("shape:skewed")
    if ((sum(outlier_rates) / len(outlier_rates)) if outlier_rates else 0.0) >= 0.05:
        retrieval_labels.append("shape:outlier-rich")
    if temporal_structure_score >= 0.5:
        retrieval_labels.append("temporal-pattern:dynamic")

    facets: GroundingProfile = {
        "row_band": _row_band(df.height),
        "measure": _measure_band(len(measure_cols)),
        "has_temporal": bool(temporal_cols),
        "group_cardinality": _group_cardinality_band(
            max(group_uniques) if group_uniques else None
        ),
        "correlated": correlation_score >= 0.5,
        "skewed": (sum(skew_scores) / len(skew_scores) if skew_scores else 0.0) >= 1.0,
        "outlier_rich": (
            (sum(outlier_rates) / len(outlier_rates)) if outlier_rates else 0.0
        )
        >= 0.05,
        "temporal_dynamic": temporal_structure_score >= 0.5,
        "retrieval_labels": list(dict.fromkeys(retrieval_labels)),
    }

    return {
        "metrics": {
            "row_count": df.height,
            "column_count": df.width,
            "has_temporal": bool(temporal_cols),
            "measure_count": len(measure_cols),
            "grouping_count": len(grouping_cols),
            "interestingness_score": float(score),
            "max_abs_correlation": float(correlation_score),
            "mean_abs_skew": float(sum(skew_scores) / len(skew_scores))
            if skew_scores
            else 0.0,
            "mean_outlier_rate": float(sum(outlier_rates) / len(outlier_rates))
            if outlier_rates
            else 0.0,
            "temporal_structure_score": float(temporal_structure_score),
            "missing_fraction": float(missing_fraction),
        },
        "facets": facets,
        "retrieval_labels": facets["retrieval_labels"],
    }


def compact_profile(profile: DataProfile) -> GroundingProfile:
    compact = dict(profile["facets"])
    compact["retrieval_labels"] = list(profile["retrieval_labels"])
    return cast(GroundingProfile, compact)


def profile_to_tablespec(profile: DataProfile) -> dict[str, object]:
    return {
        "metrics": profile["metrics"],
        "facets": profile["facets"],
    }


def interestingness_score(profile: DataProfile) -> float:
    return profile["metrics"]["interestingness_score"]


__all__ = [
    "DataProfile",
    "DataProfileMetrics",
    "GroundingProfile",
    "compact_profile",
    "interestingness_score",
    "profile_dataframe",
    "profile_to_tablespec",
]

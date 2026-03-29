from __future__ import annotations

import math
from dataclasses import dataclass

import polars as pl

from .columns import _classify_numeric_columns, _numeric_series
from .contracts import (
    DataProfile,
    DataProfileFacets,
    GroupCardinalityBand,
    MeasureBand,
    RowBand,
)
from .distribution import _distribution_scores
from .quantitative import (
    _correlation_score,
    _series_variability_score,
    _shape_anomaly_scores,
    _temporal_structure_score,
)


@dataclass(frozen=True)
class _ProfileColumns:
    bool_cols: list[str]
    numeric_cols: list[str]
    temporal_cols: list[str]
    categorical_cols: list[str]
    measure_cols: list[str]
    identifier_cols: list[str]
    grouping_cols: list[str]


@dataclass(frozen=True)
class _ProfileSignals:
    group_uniques: list[int]
    groupability_scores: list[float]
    distribution_scores: list[float]
    variability_scores: list[float]
    correlation_score: float
    outlier_rates: list[float]
    skew_scores: list[float]
    temporal_structure_score: float
    missing_fraction: float


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


def _profile_columns(df: pl.DataFrame) -> _ProfileColumns:
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

    return _ProfileColumns(
        bool_cols=bool_cols,
        numeric_cols=numeric_cols,
        temporal_cols=temporal_cols,
        categorical_cols=categorical_cols,
        measure_cols=measure_cols,
        identifier_cols=identifier_cols,
        grouping_cols=grouping_cols,
    )


def _group_uniques(df: pl.DataFrame, grouping_cols: list[str]) -> list[int]:
    group_uniques = []
    for name in grouping_cols:
        series = df.get_column(name).drop_nulls()
        if series.is_empty():
            continue
        group_uniques.append(int(series.n_unique()))

    return group_uniques


def _profile_signals(df: pl.DataFrame, columns: _ProfileColumns) -> _ProfileSignals:
    group_uniques = _group_uniques(df, columns.grouping_cols)
    groupability_scores, distribution_scores = _distribution_scores(
        df,
        columns.grouping_cols,
        columns.measure_cols,
    )
    variability_scores = [
        _series_variability_score(_numeric_series(df, name))
        for name in columns.measure_cols
    ]
    correlation_score = _correlation_score(df, columns.measure_cols)
    outlier_rates, skew_scores = _shape_anomaly_scores(df, columns.measure_cols)
    temporal_structure_score = _temporal_structure_score(
        df, columns.temporal_cols, columns.measure_cols
    )
    missing_fraction = float(df.null_count().sum_horizontal().item()) / max(
        df.height * max(df.width, 1),
        1,
    )

    return _ProfileSignals(
        group_uniques=group_uniques,
        groupability_scores=groupability_scores,
        distribution_scores=distribution_scores,
        variability_scores=variability_scores,
        correlation_score=correlation_score,
        outlier_rates=outlier_rates,
        skew_scores=skew_scores,
        temporal_structure_score=temporal_structure_score,
        missing_fraction=missing_fraction,
    )


def _profile_score(
    df: pl.DataFrame,
    columns: _ProfileColumns,
    signals: _ProfileSignals,
) -> float:
    score = 0.0
    informative_col_count = df.width - len(columns.identifier_cols)
    score += 0.45 * min(math.log1p(df.height), 4.0)
    score += 0.55 * min(max(informative_col_count - 1, 0), 4)
    score += 0.6 * max(
        int(bool(columns.measure_cols))
        + int(bool(columns.categorical_cols))
        + int(bool(columns.temporal_cols))
        + int(bool(columns.bool_cols))
        - 1,
        0,
    )
    if signals.groupability_scores:
        score += 0.8 * (
            sum(signals.groupability_scores) / len(signals.groupability_scores)
        )
    if signals.distribution_scores:
        score += 1.25 * (
            sum(signals.distribution_scores) / len(signals.distribution_scores)
        )
    if signals.variability_scores:
        score += 0.95 * (
            sum(signals.variability_scores) / len(signals.variability_scores)
        )
    score += 1.35 * signals.correlation_score
    if signals.outlier_rates:
        score += 0.45 * min(
            (sum(signals.outlier_rates) / len(signals.outlier_rates)) / 0.05,
            1.0,
        )
    if signals.skew_scores:
        score += 0.45 * min(
            (sum(signals.skew_scores) / len(signals.skew_scores)) / 1.0,
            1.0,
        )
    score += 0.65 * signals.temporal_structure_score

    return score


def _profile_facets(
    df: pl.DataFrame,
    columns: _ProfileColumns,
    signals: _ProfileSignals,
) -> DataProfileFacets:
    return {
        "row_band": _row_band(df.height),
        "measure": _measure_band(len(columns.measure_cols)),
        "has_temporal": bool(columns.temporal_cols),
        "group_cardinality": _group_cardinality_band(
            max(signals.group_uniques) if signals.group_uniques else None
        ),
        "correlated": signals.correlation_score >= 0.5,
        "skewed": (
            (sum(signals.skew_scores) / len(signals.skew_scores))
            if signals.skew_scores
            else 0.0
        )
        >= 1.0,
        "outlier_rich": (
            (sum(signals.outlier_rates) / len(signals.outlier_rates))
            if signals.outlier_rates
            else 0.0
        )
        >= 0.05,
        "temporal_dynamic": signals.temporal_structure_score >= 0.5,
    }


def _build_profile(df: pl.DataFrame) -> DataProfile:
    columns = _profile_columns(df)
    signals = _profile_signals(df, columns)
    score = _profile_score(df, columns, signals)
    facets = _profile_facets(df, columns, signals)

    return {
        "metrics": {
            "row_count": df.height,
            "column_count": df.width,
            "has_temporal": bool(columns.temporal_cols),
            "measure_count": len(columns.measure_cols),
            "grouping_count": len(columns.grouping_cols),
            "interestingness_score": float(score),
            "max_abs_correlation": float(signals.correlation_score),
            "mean_abs_skew": float(sum(signals.skew_scores) / len(signals.skew_scores))
            if signals.skew_scores
            else 0.0,
            "mean_outlier_rate": float(
                sum(signals.outlier_rates) / len(signals.outlier_rates)
            )
            if signals.outlier_rates
            else 0.0,
            "temporal_structure_score": float(signals.temporal_structure_score),
            "missing_fraction": float(signals.missing_fraction),
        },
        "facets": facets,
    }

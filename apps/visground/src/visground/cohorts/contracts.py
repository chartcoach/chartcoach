from __future__ import annotations

from typing import Literal, TypedDict

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


class DataProfileFacets(TypedDict):
    row_band: RowBand
    measure: MeasureBand
    has_temporal: bool
    group_cardinality: GroupCardinalityBand | None
    correlated: bool
    skewed: bool
    outlier_rich: bool
    temporal_dynamic: bool


class DataProfile(TypedDict):
    metrics: DataProfileMetrics
    facets: DataProfileFacets


class VisEvalCohortConfig(TypedDict):
    target_n: int
    max_tasks_per_db: int
    seed: int
    interestingness_score_floor: float
    backfill_below_floor: bool


class VisEvalCohortConfigOverrides(TypedDict, total=False):
    target_n: int
    max_tasks_per_db: int
    seed: int
    interestingness_score_floor: float
    backfill_below_floor: bool


_REQUEST_COLUMNS = [
    "id",
    "db_id",
    "chart",
    "hardness",
    "nl_query",
    "nl_query_canonical",
    "task",
    "scope",
    "time_mode",
]

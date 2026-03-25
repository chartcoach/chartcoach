from __future__ import annotations

import math
import re
from datetime import date, datetime
from typing import TypedDict, cast

import polars as pl

from .datasets import VisEvalDataset

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
    "data_profile",
]


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


_DEFAULT_CONFIG = VisEvalCohortConfig(
    target_n=150,
    max_tasks_per_db=6,
    seed=42,
    interestingness_score_floor=1.0,
    backfill_below_floor=True,
)

_IDENTIFIER_NAME_RE = re.compile(r"(?:^|_)id$", re.IGNORECASE)


def _clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(value, hi))


def _normalize_name(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", name.lower()).strip("_")


def _resolve_config(
    config: VisEvalCohortConfig | VisEvalCohortConfigOverrides | None,
) -> VisEvalCohortConfig:
    if config is None:
        return VisEvalCohortConfig(**_DEFAULT_CONFIG)

    merged = {**_DEFAULT_CONFIG, **config}
    return VisEvalCohortConfig(
        target_n=int(merged["target_n"]),
        max_tasks_per_db=int(merged["max_tasks_per_db"]),
        seed=int(merged["seed"]),
        interestingness_score_floor=float(merged["interestingness_score_floor"]),
        backfill_below_floor=bool(merged["backfill_below_floor"]),
    )


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


def df_interestingness_score(df: pl.DataFrame) -> float:
    """Score how visually informative a relation is likely to be.

    Higher scores favor relations with enough rows to show pattern, multiple
    dimensions, diverse dtypes, groupable categories, and quantitative
    structure such as correlation, skew, or outliers.
    """

    n_rows, n_cols = df.shape
    if n_rows == 0 or n_cols == 0:
        return -10.0

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

    score = 0.0
    if n_rows < 4:
        score -= 4.0
    if n_rows <= 2:
        score -= 1.5
    if n_cols < 2:
        score -= 2.0
    if not measure_cols and not temporal_cols:
        score -= 2.0

    informative_col_count = n_cols - len(identifier_cols)
    score += 0.45 * min(math.log1p(n_rows), 4.0)
    score += 0.55 * min(max(informative_col_count - 1, 0), 4)
    if identifier_cols:
        score -= 0.35 * min(len(identifier_cols), 2)

    dtype_diversity = (
        int(bool(measure_cols))
        + int(bool(categorical_cols))
        + int(bool(temporal_cols))
        + int(bool(bool_cols))
    )
    score += 0.6 * max(dtype_diversity - 1, 0)

    groupability_scores, distribution_scores = _distribution_scores(
        df,
        grouping_cols,
        measure_cols,
    )
    if groupability_scores:
        score += 0.8 * (sum(groupability_scores) / len(groupability_scores))
    if distribution_scores:
        score += 1.25 * (sum(distribution_scores) / len(distribution_scores))

    measure_series = {name: _numeric_series(df, name) for name in measure_cols}
    variability_scores = [
        _series_variability_score(series) for series in measure_series.values()
    ]
    if variability_scores:
        score += 0.95 * (sum(variability_scores) / len(variability_scores))

        low_variability_count = sum(
            1
            for series in measure_series.values()
            if (series.n_unique() <= 2)
            or (
                (_float_stat(series.std()) / max(abs(_float_stat(series.mean())), 1.0))
                < 0.08
            )
        )
        if low_variability_count == len(measure_cols):
            score -= 1.5

    score += 1.35 * _correlation_score(df, measure_cols)

    outlier_rates, skew_scores = _shape_anomaly_scores(df, measure_cols)
    if outlier_rates:
        score += 0.45 * min((sum(outlier_rates) / len(outlier_rates)) / 0.05, 1.0)
    if skew_scores:
        score += 0.45 * min((sum(skew_scores) / len(skew_scores)) / 1.0, 1.0)

    score += 0.65 * _temporal_structure_score(df, temporal_cols, measure_cols)

    return float(score)


class VisEvalCohortBuilder:
    """Build evaluation cohorts from the enriched VisEval corpus."""

    def __init__(self, dataset: VisEvalDataset) -> None:
        self.dataset = dataset

    def build_request_base_df(self) -> pl.DataFrame:
        """Return one row per visualization id with enriched task metadata."""

        return (
            self.dataset.queries_enriched_df.select(
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

    @staticmethod
    def _compute_chart_quotas(
        capacities: dict[str, int],
        *,
        remaining_slots: int,
    ) -> dict[str, int]:
        quotas = {chart: 0 for chart in capacities}
        remaining_capacities = dict(capacities)
        remaining = remaining_slots

        while remaining_capacities and remaining > 0:
            even_share = remaining / len(remaining_capacities)
            exhausted = {
                chart: capacity
                for chart, capacity in remaining_capacities.items()
                if capacity <= even_share
            }

            if exhausted:
                for chart, capacity in exhausted.items():
                    quotas[chart] = capacity
                    remaining -= capacity
                    del remaining_capacities[chart]
                continue

            floor_share = math.floor(even_share)
            for chart in remaining_capacities:
                quotas[chart] = floor_share

            assigned = floor_share * len(remaining_capacities)
            remainder = remaining - assigned
            for chart in sorted(
                remaining_capacities,
                key=lambda key: (remaining_capacities[key], key),
            )[:remainder]:
                quotas[chart] += 1
            remaining = 0

        return quotas

    def _select_chart_balanced_round(
        self,
        round_df: pl.DataFrame,
        *,
        remaining_slots: int,
    ) -> pl.DataFrame:
        if round_df.height <= remaining_slots:
            return round_df

        capacities = {
            row["selected_chart"]: row["len"]
            for row in round_df.group_by("selected_chart").len().to_dicts()
        }
        quota_df = pl.DataFrame(
            {
                "selected_chart": list(capacities.keys()),
                "chart_quota": list(
                    self._compute_chart_quotas(
                        capacities,
                        remaining_slots=remaining_slots,
                    ).values()
                ),
            }
        )

        return (
            round_df.with_columns(
                pl.int_range(1, pl.len() + 1)
                .over("selected_chart")
                .alias("chart_pick_rank")
            )
            .join(quota_df, on="selected_chart", how="left")
            .filter(pl.col("chart_pick_rank") <= pl.col("chart_quota"))
            .drop("chart_pick_rank", "chart_quota")
        )

    def _select_interesting_round(
        self,
        ranked_candidates_df: pl.DataFrame,
        *,
        config: VisEvalCohortConfig,
    ) -> pl.DataFrame:
        floor = config["interestingness_score_floor"]
        above_floor_df = ranked_candidates_df.filter(
            pl.col("interestingness_score") >= floor
        )
        selected_df = self._select_chart_balanced_round(
            above_floor_df,
            remaining_slots=config["target_n"],
        ).head(config["target_n"])

        if (
            selected_df.height >= config["target_n"]
            or not config["backfill_below_floor"]
        ):
            return selected_df

        fallback_df = ranked_candidates_df.filter(
            pl.col("interestingness_score") < floor
        )
        remaining_slots = config["target_n"] - selected_df.height
        if remaining_slots <= 0 or fallback_df.is_empty():
            return selected_df

        return pl.concat(
            [selected_df, fallback_df.head(remaining_slots)],
            how="vertical_relaxed",
        )

    def _build_sampled_aux_df(
        self,
        base_df: pl.DataFrame,
        *,
        config: VisEvalCohortConfig,
    ) -> pl.DataFrame:
        profile_df = self.dataset.profiles_df(
            base_df.get_column("id").unique().to_list()
        )
        chart_count_df = base_df.group_by("chart").len().rename({"len": "chart_count"})

        ranked_candidates_df = (
            base_df.with_columns(
                hardness_score=pl.col("hardness").replace(
                    {
                        "Easy": 1,
                        "Medium": 2,
                        "Hard": 3,
                        "Extra Hard": 4,
                    }
                )
            )
            .join(profile_df, on="id", how="left")
            .with_columns(pl.col("interestingness_score").fill_null(-10.0))
            .join(chart_count_df, on="chart", how="left")
            .sample(fraction=1.0, seed=config["seed"])
            .group_by(
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
                pl.struct(
                    [
                        "chart_count",
                        "interestingness_score",
                        "data_profile",
                        "hardness_score",
                        "chart",
                        "id",
                    ]
                )
                .sort_by(
                    ["chart_count", "interestingness_score", "hardness_score"],
                    descending=[False, True, True],
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
                data_profile=pl.col("selected_candidate").struct.field("data_profile"),
            )
            .drop("selected_candidate")
            .sort(
                by=[
                    "interestingness_score",
                    "num_valid_charts",
                    "hardness_score",
                    "selected_chart_count",
                ],
                descending=[True, True, True, False],
            )
            .with_columns(
                pl.int_range(1, pl.len() + 1).over("db_id").alias("db_balance_rank")
            )
            .filter(pl.col("db_balance_rank") <= config["max_tasks_per_db"])
            .with_columns(
                pl.int_range(1, pl.len() + 1)
                .over(["db_balance_rank", "task"])
                .alias("task_balance_rank")
            )
        )

        ranked_candidates_df = ranked_candidates_df.sort(
            by=[
                "db_balance_rank",
                "task_balance_rank",
                "interestingness_score",
                "num_valid_charts",
                "hardness_score",
                "selected_chart_count",
            ],
            descending=[False, False, True, True, True, False],
        )

        return self._select_interesting_round(
            ranked_candidates_df,
            config=config,
        ).head(config["target_n"])

    def build_request_df(
        self,
        *,
        config: VisEvalCohortConfig | VisEvalCohortConfigOverrides | None = None,
        base_df: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """Return the sampled request dataframe used by experiments."""

        resolved_config = _resolve_config(config)
        resolved_base_df = self.build_request_base_df() if base_df is None else base_df
        sampled_aux_df = self._build_sampled_aux_df(
            resolved_base_df,
            config=resolved_config,
        )
        return (
            sampled_aux_df.select(pl.col("original_id").alias("id"), "data_profile")
            .join(resolved_base_df, how="left", on="id")
            .select(_REQUEST_COLUMNS)
        )

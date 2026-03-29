from __future__ import annotations

import polars as pl

from ..datasets import VisEvalDataset
from .candidates import _build_ranked_candidates_df, _build_request_base_df
from .config import (
    _resolve_config,
)
from .contracts import (
    _REQUEST_COLUMNS,
    VisEvalCohortConfig,
    VisEvalCohortConfigOverrides,
)
from .selection import _select_interesting_round


class VisEvalCohortBuilder:
    """Build evaluation cohorts from the enriched VisEval corpus."""

    def __init__(self, dataset: VisEvalDataset) -> None:
        self.dataset = dataset

    def build_request_base_df(self) -> pl.DataFrame:
        """Return one row per visualization id with enriched task metadata."""

        return _build_request_base_df(self.dataset)

    def _build_sampled_aux_df(
        self,
        base_df: pl.DataFrame,
        *,
        config: VisEvalCohortConfig,
    ) -> pl.DataFrame:
        ranked_candidates_df = _build_ranked_candidates_df(
            self.dataset,
            base_df,
            config=config,
        )

        return _select_interesting_round(
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
            sampled_aux_df.select(pl.col("original_id").alias("id"))
            .join(resolved_base_df, how="left", on="id")
            .select(_REQUEST_COLUMNS)
        )

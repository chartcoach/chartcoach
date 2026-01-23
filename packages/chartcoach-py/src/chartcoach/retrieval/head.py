from __future__ import annotations

import dspy
import polars as pl

from .types import RetrievalRequest, RetrievalResponse


class HeadRetrievalStrategy(dspy.Module):
    """Dummy retrieval strategy.

    Hardcoded to return `catalog_df.head(request.k)` and ignore `request.query`.
    """

    strategy_id = "head@v0"

    def forward(
        self, request: RetrievalRequest, *, catalog_df: pl.DataFrame
    ) -> RetrievalResponse:
        if request.k <= 0:
            raise ValueError("k must be positive.")
        return RetrievalResponse(
            strategy_id=self.strategy_id,
            result_df=catalog_df.head(request.k),
        )

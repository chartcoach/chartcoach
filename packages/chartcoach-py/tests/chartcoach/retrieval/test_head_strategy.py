from __future__ import annotations

import polars as pl
import pytest

import dspy

from chartcoach.retrieval import HeadRetrievalStrategy, ImageItem, RetrievalRequest, TableItem, TextItem


def test_head_retrieval_strategy_returns_head_k() -> None:
    catalog_df = pl.DataFrame({"id": ["a", "b", "c"], "x": [1, 2, 3]})
    request = RetrievalRequest(
        context=[
            TextItem(role="query", text="Retrieve visualization guidelines relevant to this chart and intent."),
            TextItem(role="intent", text="I want to show change over time and highlight key comparisons."),
            ImageItem(role="chart", uri="file://chart.png", mime="image/png"),
            TableItem(role="dataset", df=pl.DataFrame({"a": [1, 2]})),
        ],
        meta={"scenario_id": "example", "title": "Example scenario"},
        k=2,
    )
    out = HeadRetrievalStrategy()(request=request, catalog_df=catalog_df)
    assert out.result_df.to_dicts() == [{"id": "a", "x": 1}, {"id": "b", "x": 2}]


def test_head_retrieval_strategy_rejects_non_positive_k() -> None:
    catalog_df = pl.DataFrame({"id": ["a"]})
    with pytest.raises(ValueError):
        HeadRetrievalStrategy()(
            request=RetrievalRequest(context=[TextItem(role="query", text="x")], k=0),
            catalog_df=catalog_df,
        )


def test_head_retrieval_strategy_is_a_dspy_module() -> None:
    assert isinstance(HeadRetrievalStrategy(), dspy.Module)

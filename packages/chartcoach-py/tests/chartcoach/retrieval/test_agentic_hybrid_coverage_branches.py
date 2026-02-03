from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

import dspy

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.index import VectorIndex
from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
    AgenticHybridStrategy,
    AgenticHybridTools,
)
from chartcoach.retrieval.strategy.pipelines.focus import FocusConfig
from chartcoach.retrieval.strategy.pipelines.guideline_status import StatusScorerConfig
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
)


class _FakeLanceIndex:
    backend = "lance"

    def __init__(self) -> None:
        self._dense_default = pl.DataFrame()
        self._fts_by_query: dict[str, pl.DataFrame] = {}
        self._hybrid_by_query: dict[str, pl.DataFrame] = {}

    def set_dense_default(self, df: pl.DataFrame) -> None:
        self._dense_default = df

    def set_fts(self, query: str, df: pl.DataFrame) -> None:
        self._fts_by_query[query] = df

    def set_hybrid(self, query: str, df: pl.DataFrame) -> None:
        self._hybrid_by_query[query] = df

    @staticmethod
    def _role_filter(df: pl.DataFrame, roles) -> pl.DataFrame:  # noqa: ANN001
        if roles:
            role_set = set(roles)
            if len(role_set) > 1 and "advice" not in role_set:
                return pl.DataFrame({"id": [], "role": [], "score": []})
        return df

    @staticmethod
    def _ids_filter(df: pl.DataFrame, ids) -> pl.DataFrame:  # noqa: ANN001
        if ids:
            return df.filter(pl.col("id").is_in(sorted(ids)))
        return df

    def search(self, _query: np.ndarray, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        df = self._role_filter(self._dense_default, roles)
        df = self._ids_filter(df, ids)
        return df.head(k)

    def search_fts(self, query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        df = self._fts_by_query.get(
            query, pl.DataFrame({"id": [], "role": [], "score": [], "text": []})
        )
        df = self._role_filter(df, roles)
        df = self._ids_filter(df, ids)
        return df.head(k)

    def search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,  # noqa: ARG002
        reranker=None,  # noqa: ANN001
        k: int = 10,
        roles=None,  # noqa: ANN001
        ids=None,  # noqa: ANN001
        fts_columns=None,  # noqa: ANN001, ARG002
    ):
        _ = reranker
        df = self._hybrid_by_query.get(
            query_text, pl.DataFrame({"id": [], "role": [], "score": []})
        )
        df = self._role_filter(df, roles)
        df = self._ids_filter(df, ids)
        return df.head(k)


def _make_vector_index(
    *, catalog: Catalog, fake: _FakeLanceIndex
) -> CatalogVectorIndex:
    embedded = pl.DataFrame(
        {
            "id": [e.id for e in catalog.entries],
            "role": ["advice"] * len(catalog.entries),
            "content": ["x"] * len(catalog.entries),
            "embedding": [[1.0, 0.0]] * len(catalog.entries),
        }
    )
    return CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=embedded,
        index=cast(VectorIndex, fake),
    )


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="T1",
                    description="D1",
                    labels=["x"],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="T2",
                    description="D2",
                    labels=["x"],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            ),
        ]
    )


def test_agentic_tools_role_fallback_branches(monkeypatch, catalog: Catalog) -> None:
    fake = _FakeLanceIndex()
    fake.set_dense_default(
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]})
    )
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    fake.set_hybrid(
        "S", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]})
    )

    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    tools = AgenticHybridTools(
        catalog=catalog,
        searcher=searcher,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )
    assert "g1" in tools.hybrid_search("S")
    assert "g1" in tools.dense_search("S")
    assert "g1" in tools.fts_search("S")


def test_agentic_strategy_calls_chart_vision_and_status_filter(
    monkeypatch, catalog: Catalog
) -> None:
    import chartcoach.retrieval.strategy.pipelines.agentic_hybrid as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")
    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    fake = _FakeLanceIndex()
    fake.set_dense_default(
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        )
    )
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=2,
        final_cross_encoder_model=None,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="g1")

    strat._program = DummyProgram()

    # Force duplicate IDs out of aggregation so the status-filter candidate pool
    # hits the defensive dedupe branch inside the strategy.
    monkeypatch.setattr(
        GuidelineSearcher,
        "aggregate_guideline_hits",
        staticmethod(
            lambda _hits_df, *, k, **_kwargs: pl.DataFrame(
                {
                    "id": ["g2", "g2", "g1"][:k],
                    "score": [1.0, 0.9, 0.8][:k],
                    "best_role": ["advice"] * min(3, k),
                }
            )
        ),
    )

    # Include an unknown id so the final status-filter candidate pool hits the
    # `gid not in id_to_entry` branch.
    monkeypatch.setattr(
        mod, "extract_guideline_ids", lambda **_kwargs: ["g1", "bogus", "g2"]
    )

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", object(), StatusScorerConfig(candidate_multiplier=2)),
    )
    monkeypatch.setattr(
        mod,
        "filter_guidelines_by_status",
        lambda *, entries, output_k, **_kwargs: (
            entries[:output_k],
            {"guideline_status_used": True},
        ),
    )

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["guideline_status_used"] is True


def test_agentic_strategy_cross_encoder_exception_sets_error(
    monkeypatch, catalog: Catalog
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]})
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    orig_search_hybrid = GuidelineSearcher.search_hybrid

    def raising_search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        k: int,
        reranker=None,
        roles=None,
        ids=None,
        fts_columns=None,
    ):
        if isinstance(reranker, DummyCrossEncoder):
            raise RuntimeError("boom")
        return orig_search_hybrid(
            self,
            query_text=query_text,
            query_vector=query_vector,
            k=k,
            reranker=reranker,
            roles=roles,
            ids=ids,
            fts_columns=fts_columns,
        )

    monkeypatch.setattr(GuidelineSearcher, "search_hybrid", raising_search_hybrid)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model="dummy",
        focus=FocusConfig(mode="all", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="g1")

    strat._program = DummyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["cross_encoder_fallback_used"] is True
    assert out.meta["cross_encoder_error"]
    assert "boom" in out.meta["cross_encoder_error"]


def test_agentic_strategy_evidence_collection_error_is_swallowed(
    monkeypatch, catalog: Catalog
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]})
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    orig_search_hybrid = GuidelineSearcher.search_hybrid

    def raising_search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        k: int,
        reranker=None,
        roles=None,
        ids=None,
        fts_columns=None,
    ):
        if ids is not None:
            raise RuntimeError("boom")
        return orig_search_hybrid(
            self,
            query_text=query_text,
            query_vector=query_vector,
            k=k,
            reranker=reranker,
            roles=roles,
            ids=ids,
            fts_columns=fts_columns,
        )

    monkeypatch.setattr(GuidelineSearcher, "search_hybrid", raising_search_hybrid)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model=None,
        focus=FocusConfig(mode="all", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="g1")

    strat._program = DummyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["hits"][0]["id"] == "g1"

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model="dummy",
        focus=FocusConfig(mode="all"),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="g1")

    strat._program = DummyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["cross_encoder_fallback_used"] is True
    assert out.meta["cross_encoder_error"]

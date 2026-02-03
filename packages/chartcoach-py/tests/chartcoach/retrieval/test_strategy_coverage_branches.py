from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

import dspy

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.index import VectorIndex
from chartcoach.retrieval.strategy.pipelines.bm25 import Bm25PrfStrategy
from chartcoach.retrieval.strategy.pipelines.dense import DenseMmrStrategy
from chartcoach.retrieval.strategy.pipelines.focus import FocusConfig
from chartcoach.retrieval.strategy.pipelines.hybrid import HybridRrfStrategy
from chartcoach.retrieval.strategy.pipelines.hyde import HydeConfig, HydeHybridStrategy
from chartcoach.retrieval.strategy.pipelines.query_fusion import (
    QueryFusionConfig,
    QueryFusionHybridStrategy,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.pipelines.guideline_status import StatusScorerConfig
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
            # Simulate "too strict" role filters: require advice to return anything
            # when multiple roles are requested.
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
                    title="Use accessible colors",
                    description="Ensure color choices are accessible.",
                    labels=["topic:color"],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            ),
        ]
    )


def test_bm25_dense_and_hybrid_cover_vision_role_fallback_and_status(
    monkeypatch, catalog: Catalog
) -> None:
    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_dense_default(
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        )
    )
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0], "text": ["x"]}),
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

    # Patch vision hook to avoid VLM calls while covering the strategy branch.
    import chartcoach.retrieval.strategy.pipelines.bm25 as bm25_mod
    import chartcoach.retrieval.strategy.pipelines.dense as dense_mod
    import chartcoach.retrieval.strategy.pipelines.hybrid as hybrid_mod

    monkeypatch.setattr(bm25_mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(dense_mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(hybrid_mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        bm25_mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )
    monkeypatch.setattr(
        dense_mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )
    monkeypatch.setattr(
        hybrid_mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    # Patch status scorer to avoid LM calls while covering the strategy branches.
    def fake_status_scorer():  # noqa: ANN001
        class DummyStatus:
            def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
                _ = (chart_key, situation)
                return [{"id": e.id, "status": "violated"} for e in entries]

        return ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2))

    for m in (bm25_mod, dense_mod, hybrid_mod):
        monkeypatch.setattr(m, "shared_status_scorer", fake_status_scorer)
        monkeypatch.setattr(
            m,
            "filter_guidelines_by_status",
            lambda *, entries, output_k, **_kwargs: (
                entries[:output_k],
                {"guideline_status_used": True},
            ),
        )

    # Avoid PRF expansion so the test data stays small.
    monkeypatch.setattr(
        bm25_mod, "_expand_query_from_hits", lambda *, query_text, **_kwargs: query_text
    )

    req = RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)

    out = Bm25PrfStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )(request=req)
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["guideline_status_used"] is True

    out = DenseMmrStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )(request=req)
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["guideline_status_used"] is True

    out = HybridRrfStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )(request=req)
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["guideline_status_used"] is True


def test_query_fusion_and_hyde_cover_role_fallback_cross_encoder_exception_and_status(
    monkeypatch, catalog: Catalog
) -> None:
    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_dense_default(
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]})
    )
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    # Per-query hybrid results (only returned after role fallback includes advice).
    fake.set_hybrid(
        "q1",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    fake.set_hybrid(
        "q2",
        pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]}),
    )
    # Hyde rerank query is the pseudo-document.
    fake.set_hybrid(
        "pseudo",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [3.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    # Patch vision hook + status scorer for both strategies.
    import chartcoach.retrieval.strategy.pipelines.query_fusion as qf_mod
    import chartcoach.retrieval.strategy.pipelines.hyde as hyde_mod

    monkeypatch.setattr(qf_mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(hyde_mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        qf_mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )
    monkeypatch.setattr(
        hyde_mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    def fake_status_scorer():  # noqa: ANN001
        class DummyStatus:
            def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
                _ = (chart_key, situation)
                return [{"id": e.id, "status": "violated"} for e in entries]

        return ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2))

    for m in (qf_mod, hyde_mod):
        monkeypatch.setattr(m, "shared_status_scorer", fake_status_scorer)
        monkeypatch.setattr(
            m,
            "filter_guidelines_by_status",
            lambda *, entries, output_k, **_kwargs: (
                entries[:output_k],
                {"guideline_status_used": True},
            ),
        )

    # Raise on cross-encoder rerank calls to exercise the exception branches.
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

    qf = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )

    class DummyQFProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(queries=["q1", "q2"], focused_situation="S")

    qf._program = DummyQFProgram()
    out = qf(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["cross_encoder_fallback_used"] is True
    assert out.meta["guideline_status_used"] is True

    hyde = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model="dummy"),
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )

    class DummyHydeProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="pseudo")

    hyde._program = DummyHydeProgram()
    out = hyde(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["cross_encoder_fallback_used"] is True
    assert out.meta["guideline_status_used"] is True

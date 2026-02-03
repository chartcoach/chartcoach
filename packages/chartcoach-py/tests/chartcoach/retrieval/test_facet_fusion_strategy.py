from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

import dspy

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.index import VectorIndex
from chartcoach.retrieval.strategy.pipelines.facet_fusion import (
    FacetFusionConfig,
    FacetFusionHybridStrategy,
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
        self._hybrid_by_query: dict[str, pl.DataFrame] = {}

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
        _ = (roles, ids)
        return pl.DataFrame({"id": [], "role": [], "score": []}).head(k)

    def search_fts(self, query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (query, roles, ids)
        return pl.DataFrame({"id": [], "role": [], "score": [], "text": []}).head(k)

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


def _make_searcher(*, catalog: Catalog, fake: _FakeLanceIndex) -> GuidelineSearcher:
    embedded = pl.DataFrame(
        {
            "id": [e.id for e in catalog.entries],
            "role": ["advice"] * len(catalog.entries),
            "content": ["x"] * len(catalog.entries),
            "embedding": [[1.0, 0.0]] * len(catalog.entries),
        }
    )
    vector_index = CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=embedded,
        index=cast(VectorIndex, fake),
    )
    return GuidelineSearcher(catalog=catalog, vector_index=vector_index)


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


@pytest.fixture(autouse=True)
def _patch_embed_query(monkeypatch) -> None:
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )


def _patch_strategy_deps(monkeypatch) -> None:
    import chartcoach.retrieval.strategy.pipelines.facet_fusion as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")
    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
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


def test_facet_fusion_hybrid_role_fallback_and_cross_encoder_rerank(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    fake.set_hybrid(
        "q2", pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]})
    )
    fake.set_hybrid(
        "q1\nq2",
        pl.DataFrame(
            {"id": ["g2", "g1"], "role": ["advice", "advice"], "score": [3.0, 2.0]}
        ),
    )

    searcher = _make_searcher(catalog=catalog, fake=fake)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="",
                canonical_query="q1",
                facet_queries=[" q1 ", "q2"],
                chart_terms="line chart",
                task_terms=[],
                risk_terms=[],
            )

    strat._program = DummyPlan()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["guideline_status_used"] is True


def test_facet_fusion_hybrid_runs_fill_fallback_when_underfilled(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=1, cross_encoder_model=None),
        default_k=2,
        focus=FocusConfig(mode="all"),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S",
                canonical_query="q1",
                facet_queries=[],
                chart_terms=[],
                task_terms=[],
                risk_terms=[],
            )

    strat._program = DummyPlan()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["fill_fallback_used"] is True


def test_facet_fusion_hybrid_records_lm_error_when_plan_fails(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=1, cross_encoder_model=None),
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class AlwaysFails(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            raise RuntimeError("boom")

    strat._program = AlwaysFails()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["lm_fallback_used"] is True
    assert out.meta["lm_error"]


def test_facet_fusion_hybrid_cross_encoder_empty_sets_fallback(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    fake.set_hybrid(
        "q2", pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]})
    )
    # Cross-encoder rerank step sees the joined query text; make it empty so `proposed` is empty.
    fake.set_hybrid("q1\nq2", pl.DataFrame({"id": [], "role": [], "score": []}))
    searcher = _make_searcher(catalog=catalog, fake=fake)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S", canonical_query="q1", facet_queries=["q2"]
            )

    strat._program = DummyPlan()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["cross_encoder_fallback_used"] is True


def test_facet_fusion_hybrid_cross_encoder_exception_sets_error(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)

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
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=1, cross_encoder_model="dummy"),
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S", canonical_query="q1", facet_queries=[]
            )

    strat._program = DummyPlan()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["cross_encoder_fallback_used"] is True
    assert out.meta["cross_encoder_error"]


def test_facet_fusion_hybrid_validates_k_is_positive(
    monkeypatch, catalog: Catalog
) -> None:
    fake = _FakeLanceIndex()
    searcher = _make_searcher(catalog=catalog, fake=fake)
    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=0,
        focus=FocusConfig(mode="all"),
    )
    with pytest.raises(ValueError, match="k must be positive"):
        strat(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))


def test_facet_fusion_hybrid_fills_from_fused_when_cross_encoder_partial(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]})
    )
    fake.set_hybrid(
        "q2", pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]})
    )
    # Cross-encoder step only returns a subset (g1); strategy should fill g2 from fused.
    fake.set_hybrid(
        "q1\nq2", pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [3.0]})
    )

    searcher = _make_searcher(catalog=catalog, fake=fake)
    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=2,
        focus=FocusConfig(mode="all"),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S", canonical_query="q1", facet_queries=["q2"]
            )

    strat._program = DummyPlan()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_facet_fusion_hybrid_includes_evidence_and_filters_bad_evidence(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import chartcoach.retrieval.strategy.pipelines.searcher as searcher_mod
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0], "text": ["x"]}),
    )
    fake.set_hybrid(
        "q1\nq2",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [3.0], "text": ["y"]}),
    )

    searcher = _make_searcher(catalog=catalog, fake=fake)

    original_agg = searcher_mod.GuidelineSearcher.aggregate_guideline_hits_with_evidence

    def patched_agg(hits_df: pl.DataFrame, *, k: int, **kwargs):  # noqa: ANN001
        if k == 40:
            return pl.DataFrame(
                {
                    "id": [None, "g1"],
                    "score": [0.1, 1.0],
                    "best_role": ["advice", "advice"],
                    "evidence": [
                        [],
                        [
                            {
                                "role": "advice",
                                "text": "axis title missing",
                                "score": 1.0,
                            }
                        ],
                    ],
                }
            )
        if k == 1:
            evidence = pl.Series(
                "evidence",
                [
                    [
                        {"role": "advice", "text": "good", "score": 3.0},
                        "not-a-dict",
                        {"role": "reason", "text": "   ", "score": 0.1},
                    ]
                ],
                dtype=pl.Object,
            )
            return pl.DataFrame(
                {
                    "id": ["g1"],
                    "score": [3.0],
                    "best_role": ["advice"],
                    "evidence": evidence,
                }
            )
        return original_agg(hits_df, k=k, **kwargs)

    monkeypatch.setattr(
        searcher_mod.GuidelineSearcher,
        "aggregate_guideline_hits_with_evidence",
        staticmethod(patched_agg),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S",
                canonical_query="q1",
                facet_queries=["q2"],
                chart_terms=[],
                task_terms=[],
                risk_terms=[],
            )

    strat._program = DummyPlan()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["hits"][0]["evidence"]


def test_facet_fusion_hybrid_role_fallback_loop_records_evidence(
    monkeypatch, catalog: Catalog
) -> None:
    _patch_strategy_deps(monkeypatch)

    import chartcoach.retrieval.strategy.pipelines.searcher as searcher_mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "q1",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0], "text": ["x"]}),
    )

    searcher = _make_searcher(catalog=catalog, fake=fake)

    original_agg = searcher_mod.GuidelineSearcher.aggregate_guideline_hits_with_evidence

    def patched_agg(hits_df: pl.DataFrame, *, k: int, **kwargs):  # noqa: ANN001
        if k == 40 and hits_df.is_empty():
            return pl.DataFrame(
                {
                    "id": [None],
                    "score": [0.1],
                    "best_role": ["advice"],
                    "evidence": [[]],
                }
            )
        if k == 40:
            return pl.DataFrame(
                {
                    "id": [None, "g1"],
                    "score": [0.1, 1.0],
                    "best_role": ["advice", "advice"],
                    "evidence": [
                        [],
                        [{"role": "advice", "text": "ok", "score": 1.0}],
                    ],
                }
            )
        return original_agg(hits_df, k=k, **kwargs)

    monkeypatch.setattr(
        searcher_mod.GuidelineSearcher,
        "aggregate_guideline_hits_with_evidence",
        staticmethod(patched_agg),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = FacetFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=FacetFusionConfig(n_queries=1, cross_encoder_model=None),
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )

    class DummyPlan(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                focused_situation="S",
                canonical_query="q1",
                facet_queries=[],
                chart_terms=[],
                task_terms=[],
                risk_terms=[],
            )

    strat._program = DummyPlan()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["hits"][0]["evidence"]

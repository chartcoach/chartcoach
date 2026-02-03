from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.embedding import GuidelineFieldTextSource
from chartcoach.index.sparse import CatalogSparseIndex, SparseEmbeddingConfig
from chartcoach.retrieval.strategy.pipelines.dense_sparse_rrf import (
    DenseSparseRrfStrategy,
)
from chartcoach.retrieval.strategy.pipelines.focus import FocusConfig
from chartcoach.retrieval.strategy.pipelines.hybrid_set_select import (
    HybridRrfFacilitySetSelectStrategy,
    HybridRrfLabelSetSelectStrategy,
    SetSelectConfig,
    _HybridSetSelectBase,
)
from chartcoach.retrieval.strategy.pipelines.ranking import (
    facility_location_select,
    label_round_robin_select,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.pipelines.sparse_splade import SparseSpladeStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
)
from chartcoach.index import VectorIndex


class _FakeSparseEmbedder:
    def embed(self, texts):  # noqa: ANN001
        out = []
        for text in texts:
            lowered = str(text).lower()
            if "color" in lowered:
                out.append(([1], [1.0]))
            elif "axis" in lowered:
                out.append(([2], [1.0]))
            else:
                out.append(([0], [1.0]))
        return out


class _FakeLanceIndex:
    backend = "lance"

    def __init__(self) -> None:
        self._dense: pl.DataFrame = pl.DataFrame()
        self._hybrid: pl.DataFrame = pl.DataFrame()

    def set_dense(self, df: pl.DataFrame) -> None:
        self._dense = df

    def set_hybrid(self, df: pl.DataFrame) -> None:
        self._hybrid = df

    def search(self, _query: np.ndarray, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        df = self._dense
        if roles:
            role_set = set(roles)
            if role_set and "advice" not in role_set:
                df = pl.DataFrame({"id": [], "role": [], "score": [], "text": []})
        if ids:
            df = df.filter(pl.col("id").is_in(sorted(ids)))
        return df.head(k)

    def search_fts(self, _query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return pl.DataFrame({"id": [], "role": [], "score": [], "text": []}).head(k)

    def search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,  # noqa: ARG002
        query_vector: np.ndarray,  # noqa: ARG002
        reranker=None,  # noqa: ANN001, ARG002
        k: int = 10,
        roles=None,  # noqa: ANN001
        ids=None,  # noqa: ANN001
        fts_columns=None,  # noqa: ANN001, ARG002
    ):
        df = self._hybrid
        if roles:
            role_set = set(roles)
            if role_set and "advice" not in role_set:
                df = pl.DataFrame({"id": [], "role": [], "score": [], "text": []})
        if ids:
            df = df.filter(pl.col("id").is_in(sorted(ids)))
        return df.head(k)


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="",
                    labels=["goal:accessibility", "topic:color"],
                    body="## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axis titles",
                    description="",
                    labels=["goal:clarity", "topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g3",
                    title="Add annotations",
                    description="",
                    labels=["goal:clarity", "topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd context annotations.\n",
                ),
                references=[],
            ),
        ]
    )


def _make_searcher(*, catalog: Catalog, fake: _FakeLanceIndex) -> GuidelineSearcher:
    embedded = pl.DataFrame(
        {
            "id": ["g1", "g2", "g3"],
            "role": ["advice", "advice", "advice"],
            "content": ["c1", "c2", "c3"],
            "embedding": [[1.0, 0.0], [0.0, 1.0], [1.0, 0.0]],
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


def _make_sparse_index(*, catalog: Catalog) -> CatalogSparseIndex:
    return CatalogSparseIndex.from_catalog(
        catalog,
        sources=[GuidelineFieldTextSource("title")],
        config=SparseEmbeddingConfig(),
        embedder=_FakeSparseEmbedder(),
    )


def test_label_round_robin_select_and_facility_location_select() -> None:
    with pytest.raises(ValueError, match="k must be positive"):
        label_round_robin_select(
            candidate_ids=["a"], relevance={}, labels_by_id={}, k=0
        )
    with pytest.raises(ValueError, match="non-negative"):
        label_round_robin_select(
            candidate_ids=["a"],
            relevance={},
            labels_by_id={},
            k=1,
            redundancy_gamma=-0.1,
        )
    assert (
        label_round_robin_select(candidate_ids=[], relevance={}, labels_by_id={}, k=1)
        == []
    )
    assert (
        label_round_robin_select(candidate_ids=[""], relevance={}, labels_by_id={}, k=1)
        == []
    )

    selected = label_round_robin_select(
        candidate_ids=["g1", "g2", "g3"],
        relevance={"g1": 3.0, "g2": 2.0, "g3": 1.0},
        labels_by_id={
            "g1": ["goal:a", "topic:x"],
            "g2": ["goal:b", "topic:y"],
            "g3": ["goal:b", "topic:y"],
        },
        k=2,
        group_prefixes=("goal", "topic"),
        redundancy_gamma=0.0,
    )
    assert selected == ["g1", "g2"]

    # Coverage pass selects one per group, then fill executes with redundancy penalty.
    selected = label_round_robin_select(
        candidate_ids=["g1", "g2", "g3"],
        relevance={"g1": 3.0, "g2": 2.0, "g3": 1.0},
        labels_by_id={
            "g1": ["goal:a", "topic:x"],
            "g2": ["goal:b", "topic:y"],
            "g3": ["goal:b", "topic:y"],
        },
        k=3,
        group_prefixes=("goal", "topic"),
        redundancy_gamma=0.5,
    )
    assert selected == ["g1", "g2", "g3"]

    # No grouping prefixes -> behave like relevance ordering.
    selected = label_round_robin_select(
        candidate_ids=["g1", "g2"],
        relevance={"g1": 1.0, "g2": 2.0},
        labels_by_id={"g1": ["topic:x"], "g2": ["topic:y"]},
        k=2,
        group_prefixes=(),
        redundancy_gamma=0.0,
    )
    assert selected == ["g2", "g1"]

    with pytest.raises(ValueError, match="k must be positive"):
        facility_location_select(candidate_ids=["a"], relevance={}, embeddings={}, k=0)
    with pytest.raises(ValueError, match="non-negative"):
        facility_location_select(
            candidate_ids=["a"], relevance={}, embeddings={}, k=1, alpha=-1.0
        )
    assert (
        facility_location_select(candidate_ids=[], relevance={}, embeddings={}, k=1)
        == []
    )

    # No embeddings -> relevance-only ordering.
    selected = facility_location_select(
        candidate_ids=["g1", "g2"],
        relevance={"g1": 1.0, "g2": 2.0},
        embeddings={},
        k=2,
    )
    assert selected == ["g2", "g1"]

    # With embeddings, prefer diverse coverage (g1 and g2 rather than g1 and g3).
    selected = facility_location_select(
        candidate_ids=["g1", "g3", "g2"],
        relevance={"g1": 3.0, "g3": 2.5, "g2": 2.0},
        embeddings={
            "g1": np.array([1.0, 0.0]),
            "g2": np.array([0.0, 1.0]),
            "g3": np.array([1.0, 0.0]),
        },
        k=2,
    )
    assert selected == ["g1", "g2"]


def test_sparse_splade_strategy_returns_hits_and_respects_focus(
    catalog: Catalog, monkeypatch
) -> None:
    sparse_index = _make_sparse_index(catalog=catalog)
    strat = SparseSpladeStrategy(
        catalog=catalog,
        sparse_index=sparse_index,
        default_k=1,
    )
    out = strat(
        request=RetrievalRequest(
            context=[TextItem(role="situation", text="color")], k=1
        )
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["hits"][0]["evidence"]

    import chartcoach.retrieval.strategy.pipelines.sparse_splade as sparse_mod

    class DummyStatusModule:  # noqa: D401
        pass

    def fake_shared_status_scorer():  # noqa: ANN001
        from chartcoach.retrieval.strategy.pipelines.guideline_status import (
            StatusScorerConfig,
        )

        return object(), DummyStatusModule(), StatusScorerConfig(candidate_multiplier=2)

    def fake_filter(**kwargs):  # noqa: ANN001
        entries = list(kwargs["entries"])
        return entries[: kwargs["output_k"]], {"guideline_status_used": True}

    monkeypatch.setattr(sparse_mod, "shared_status_scorer", fake_shared_status_scorer)
    monkeypatch.setattr(sparse_mod, "filter_guidelines_by_status", fake_filter)

    strat = SparseSpladeStrategy(
        catalog=catalog,
        sparse_index=sparse_index,
        default_k=1,
        focus=FocusConfig(mode="violations", use_status_filter=True),
    )
    out = strat(
        request=RetrievalRequest(
            context=[TextItem(role="situation", text="color")], k=1
        )
    )
    assert out.meta["guideline_status_used"] is True


def test_dense_sparse_rrf_strategy_filters_bad_evidence(
    monkeypatch, catalog: Catalog
) -> None:
    import chartcoach.retrieval.strategy.pipelines.searcher as searcher_mod

    fake = _FakeLanceIndex()
    fake.set_dense(
        pl.DataFrame(
            {"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["   "]}
        )
    )
    fake.set_hybrid(
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]})
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)
    sparse_index = _make_sparse_index(catalog=catalog)

    original_agg = searcher_mod.GuidelineSearcher.aggregate_guideline_hits_with_evidence
    calls = 0

    def patched_agg(hits_df: pl.DataFrame, *, k: int, **kwargs):  # noqa: ANN001
        nonlocal calls
        calls += 1
        if k == 12 and calls == 1:
            evidence = pl.Series(
                "evidence",
                [[{"role": "advice", "text": "   ", "score": 1.0}]],
                dtype=pl.Object,
            )
            return pl.DataFrame(
                {
                    "id": ["g1"],
                    "score": [1.0],
                    "best_role": ["advice"],
                    "evidence": evidence,
                }
            )
        if k == 12 and calls == 2:
            evidence = pl.Series(
                "evidence",
                [["not-a-dict", {"role": "advice", "text": "ok", "score": 0.9}]],
                dtype=pl.Object,
            )
            return pl.DataFrame(
                {
                    "id": ["g1"],
                    "score": [0.9],
                    "best_role": ["abstract"],
                    "evidence": evidence,
                }
            )
        return original_agg(hits_df, k=k, **kwargs)

    monkeypatch.setattr(
        searcher_mod.GuidelineSearcher,
        "aggregate_guideline_hits_with_evidence",
        staticmethod(patched_agg),
    )

    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    strat = DenseSparseRrfStrategy(
        catalog=catalog,
        searcher=searcher,
        sparse_index=sparse_index,
        default_k=1,
        candidate_multiplier=12,
    )
    out = strat(
        request=RetrievalRequest(
            context=[TextItem(role="situation", text="color")], k=1
        )
    )
    assert out.meta["hits"][0]["evidence"]


def test_dense_sparse_rrf_strategy_role_fallback_and_status_filter(
    monkeypatch, catalog: Catalog
) -> None:
    import chartcoach.retrieval.strategy.pipelines.dense_sparse_rrf as dense_sparse_mod

    fake = _FakeLanceIndex()
    fake.set_dense(
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]})
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)
    sparse_index = _make_sparse_index(catalog=catalog)

    class DummyStatusModule:  # noqa: D401
        pass

    def fake_shared_status_scorer():  # noqa: ANN001
        from chartcoach.retrieval.strategy.pipelines.guideline_status import (
            StatusScorerConfig,
        )

        return object(), DummyStatusModule(), StatusScorerConfig(candidate_multiplier=2)

    def fake_filter(**kwargs):  # noqa: ANN001
        entries = list(kwargs["entries"])
        return entries[: kwargs["output_k"]], {"guideline_status_used": True}

    monkeypatch.setattr(
        dense_sparse_mod, "shared_status_scorer", fake_shared_status_scorer
    )
    monkeypatch.setattr(dense_sparse_mod, "filter_guidelines_by_status", fake_filter)

    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    strat = DenseSparseRrfStrategy(
        catalog=catalog,
        searcher=searcher,
        sparse_index=sparse_index,
        default_k=1,
        focus=FocusConfig(
            mode="violations", allow_role_fallback=True, use_status_filter=True
        ),
        candidate_multiplier=2,
    )
    out = strat(
        request=RetrievalRequest(
            context=[TextItem(role="situation", text="color")], k=1
        )
    )
    assert out.meta["guideline_status_used"] is True
    assert out.meta["focus"]["roles"] is not None


def test_hybrid_setselect_strategies_cover_methods_and_focus(
    monkeypatch, catalog: Catalog
) -> None:
    import chartcoach.retrieval.strategy.pipelines.hybrid_set_select as setselect_mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [3.0, 2.0, 2.5],
                "text": ["c1", "c2", "c3"],
            }
        )
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )

    label = HybridRrfLabelSetSelectStrategy(catalog=catalog, searcher=searcher)
    out = label(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g3"]
    assert out.meta["set_select"]["method"] == "label_round_robin"

    facility = HybridRrfFacilitySetSelectStrategy(catalog=catalog, searcher=searcher)
    out = facility(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["set_select"]["method"] == "facility_location"
    assert facility._mean_embeddings([]) == {}

    class DummyStatusModule:  # noqa: D401
        pass

    def fake_shared_status_scorer():  # noqa: ANN001
        from chartcoach.retrieval.strategy.pipelines.guideline_status import (
            StatusScorerConfig,
        )

        return object(), DummyStatusModule(), StatusScorerConfig(candidate_multiplier=2)

    def fake_filter(**kwargs):  # noqa: ANN001
        entries = list(kwargs["entries"])
        return entries[: kwargs["output_k"]], {"guideline_status_used": True}

    monkeypatch.setattr(
        setselect_mod, "shared_status_scorer", fake_shared_status_scorer
    )
    monkeypatch.setattr(setselect_mod, "filter_guidelines_by_status", fake_filter)

    focus = FocusConfig(mode="violations", allow_role_fallback=True)
    bad = _HybridSetSelectBase(
        catalog=catalog,
        searcher=searcher,
        method="unknown",
        config=SetSelectConfig(),
        focus=focus,
    )
    with pytest.raises(ValueError, match="Unknown set selection method"):
        bad(
            request=RetrievalRequest(
                context=[TextItem(role="situation", text="S")], k=1
            )
        )

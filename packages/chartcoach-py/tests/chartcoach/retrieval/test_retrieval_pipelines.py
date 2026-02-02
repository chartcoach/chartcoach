from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

import dspy

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import AgenticHybridTools
from chartcoach.retrieval.strategy.pipelines.bm25 import (
    Bm25PrfStrategy,
    _expand_query_from_hits,
    _tokenize,
)
from chartcoach.retrieval.strategy.pipelines.dense import DenseMmrStrategy
from chartcoach.retrieval.strategy.pipelines.hybrid import HybridRrfStrategy
from chartcoach.retrieval.strategy.pipelines.hyde import HydeConfig, HydeHybridStrategy
from chartcoach.retrieval.strategy.pipelines.query_fusion import (
    QueryFusionConfig,
    QueryFusionHybridStrategy,
)
from chartcoach.retrieval.strategy.pipelines.ranking import (
    mmr_select,
    rrf_rank,
    rrf_scores,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
    describe_text_source,
)
from chartcoach.index import VectorIndex


class _FakeLanceIndex:
    backend = "lance"

    def __init__(self) -> None:
        self._dense: dict[str, pl.DataFrame] = {}
        self._fts: dict[str, pl.DataFrame] = {}
        self._hybrid: dict[str, pl.DataFrame] = {}
        self._hybrid_by_ids: dict[frozenset[str], pl.DataFrame] = {}

    def set_dense(self, key: str, df: pl.DataFrame) -> None:
        self._dense[key] = df

    def set_fts(self, key: str, df: pl.DataFrame) -> None:
        self._fts[key] = df

    def set_hybrid(self, key: str, df: pl.DataFrame) -> None:
        self._hybrid[key] = df

    def set_hybrid_for_ids(self, ids: set[str], df: pl.DataFrame) -> None:
        self._hybrid_by_ids[frozenset(ids)] = df

    def search(self, _query: np.ndarray, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return self._dense.get("default", pl.DataFrame()).head(k)

    def search_fts(self, query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return self._fts.get(query, pl.DataFrame()).head(k)

    def search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,  # noqa: ARG002
        reranker=None,  # noqa: ANN001
        k: int = 10,
        roles=None,  # noqa: ANN001
        ids=None,  # noqa: ANN001
        fts_columns=None,  # noqa: ANN001
    ):
        _ = (reranker, roles, fts_columns)
        if ids:
            by_ids = self._hybrid_by_ids.get(frozenset(ids))
            if by_ids is not None:
                return by_ids.head(k)
        return self._hybrid.get(query_text, pl.DataFrame()).head(k)


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
                    body="## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g3",
                    title="Add context annotations",
                    description="Add context to avoid misinterpretation.",
                    labels=["topic:annotation", "impact:credibility"],
                    body="## Advice <!-- role: advice -->\nAdd context notes.\n",
                ),
                references=[],
            ),
        ]
    )


def _make_vector_index(
    *, catalog: Catalog, fake_index: _FakeLanceIndex
) -> CatalogVectorIndex:
    # embedded_text_df is used for MMR; keep it tiny and deterministic.
    embedded = pl.DataFrame(
        {
            "id": ["g1", "g2", "g3"],
            "role": ["advice", "advice", "advice"],
            "content": ["color", "axis", "context"],
            "embedding": [[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
        }
    )
    return CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=embedded,
        index=cast(VectorIndex, fake_index),
    )


def test_rrf_scores_and_rank() -> None:
    scores = rrf_scores(rankings=[["a", "b"], ["b", "c"]], k=60)
    assert scores["b"] > scores["a"]
    assert rrf_rank(rankings=[["a", "b"], ["b", "c"]], k=60)[0] == "b"

    scores = rrf_scores(rankings=[["", "a"]], k=60)
    assert "" not in scores
    assert "a" in scores
    assert rrf_rank(rankings=[["", "a"], ["a", ""]], k=60) == ["a"]

    with pytest.raises(ValueError, match="k must be positive"):
        rrf_scores(rankings=[["a"]], k=0)


def test_mmr_select_prefers_diversity() -> None:
    emb = {
        "a": np.array([1.0, 0.0]),
        "b": np.array([1.0, 0.0]),
        "c": np.array([0.0, 1.0]),
    }
    rel = {"a": 0.9, "b": 0.89, "c": 0.1}
    selected = mmr_select(
        candidate_ids=["a", "b", "c"], relevance=rel, embeddings=emb, k=2
    )
    assert selected[0] == "a"
    assert selected[1] == "c"

    with pytest.raises(ValueError, match="k must be positive"):
        mmr_select(candidate_ids=["a"], relevance=rel, embeddings=emb, k=0)

    with pytest.raises(ValueError, match="lambda_mult"):
        mmr_select(
            candidate_ids=["a", "b"],
            relevance=rel,
            embeddings=emb,
            k=1,
            lambda_mult=1.5,
        )

    assert mmr_select(candidate_ids=[], relevance={}, embeddings={}, k=5) == []

    # Cover rel_denom<=0 and zero-vector normalization.
    selected = mmr_select(
        candidate_ids=["a", "b"],
        relevance={"a": 1.0, "b": 1.0},
        embeddings={"a": np.zeros(2), "b": np.array([1.0, 0.0])},
        k=2,
    )
    assert selected == ["a", "b"]

    # Cover NaN similarity causing the best_gid to remain unset for an iteration.
    selected = mmr_select(
        candidate_ids=["a", "b"],
        relevance={"a": 1.0, "b": 0.0},
        embeddings={"a": np.array([1.0, 0.0]), "b": np.array([np.nan, 0.0])},
        k=2,
        lambda_mult=0.5,
    )
    assert selected == ["a"]


def test_tokenize_and_prf_query_expansion() -> None:
    assert _tokenize("Use colors, for readers!") == ["use", "colors", "readers"]

    hits = pl.DataFrame(
        {
            "id": ["g1", "g2"],
            "role": ["advice", "advice"],
            "score": [1.0, 0.5],
            "text": ["colorblind safe palette", "axis labels and units"],
        }
    )
    expanded = _expand_query_from_hits(
        query_text="use colors", hits_df=hits, max_terms=2
    )
    assert expanded.startswith("use colors")
    assert "palette" in expanded or "colorblind" in expanded

    # Empty hits: no expansion.
    assert (
        _expand_query_from_hits(query_text="use colors", hits_df=hits.head(0))
        == "use colors"
    )

    # Missing `text` column: no expansion.
    assert (
        _expand_query_from_hits(
            query_text="use colors",
            hits_df=hits.select("id", "role", "score"),
        )
        == "use colors"
    )

    # No meaningful original terms: no expansion.
    assert (
        _expand_query_from_hits(
            query_text="the and", hits_df=hits.select("id", "role", "score", "text")
        )
        == "the and"
    )

    # If all PRF tokens are already in the original query, don't expand.
    assert (
        _expand_query_from_hits(
            query_text="color", hits_df=pl.DataFrame({"text": ["color color"]})
        )
        == "color"
    )


def test_bm25_strategy_expands_query_and_merges_hits(
    catalog: Catalog, monkeypatch
) -> None:
    import chartcoach.retrieval.strategy.pipelines.bm25 as bm25_mod

    fake = _FakeLanceIndex()
    fake.set_fts(
        "use colors",
        pl.DataFrame(
            {
                "id": ["g1"],
                "role": ["advice"],
                "score": [1.0],
                "text": ["colorblind safe palette"],
            }
        ),
    )

    monkeypatch.setattr(
        bm25_mod,
        "_expand_query_from_hits",
        lambda *, query_text, hits_df, **_kwargs: f"{query_text}\n\npalette",
    )

    fake.set_fts(
        "use colors\n\npalette",
        pl.DataFrame(
            {
                "id": ["g2"],
                "role": ["advice"],
                "score": [2.0],
                "text": ["axis labels"],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)
    strat = Bm25PrfStrategy(catalog=catalog, searcher=searcher, default_k=1)

    out = strat(
        request=RetrievalRequest(
            context=[TextItem(role="situation", text="use colors")], k=1
        )
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["query_expanded"] is True


def test_bm25_strategy_handles_no_hits(catalog: Catalog) -> None:
    fake = _FakeLanceIndex()
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)
    strat = Bm25PrfStrategy(catalog=catalog, searcher=searcher, default_k=1)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.catalog.entries == []
    assert out.meta["hits"] == []


def test_strategies_validate_k(catalog: Catalog) -> None:
    fake = _FakeLanceIndex()
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    with pytest.raises(ValueError, match="k must be positive"):
        Bm25PrfStrategy(catalog=catalog, searcher=searcher, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    with pytest.raises(ValueError, match="k must be positive"):
        DenseMmrStrategy(catalog=catalog, searcher=searcher, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    with pytest.raises(ValueError, match="k must be positive"):
        HybridRrfStrategy(catalog=catalog, searcher=searcher, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    from chartcoach.retrieval.strategy.pipelines.ann_dense import AnnDenseStrategy

    with pytest.raises(ValueError, match="k must be positive"):
        AnnDenseStrategy(catalog=catalog, searcher=searcher, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    from chartcoach.retrieval.strategy.pipelines.neighborhood_explorer import (
        NeighborhoodExplorerStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        NeighborhoodExplorerStrategy(catalog=catalog, searcher=searcher, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")

    with pytest.raises(ValueError, match="k must be positive"):
        HydeHybridStrategy(catalog=catalog, searcher=searcher, lm=lm, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )

    from chartcoach.retrieval.strategy.pipelines.label_gated_ann import (
        LabelGatedAnnStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        LabelGatedAnnStrategy(
            catalog=catalog, searcher=searcher, lm=lm, default_k=0
        )(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))

    from chartcoach.retrieval.strategy.pipelines.label_first_abstract import (
        LabelFirstAbstractStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        LabelFirstAbstractStrategy(
            catalog=catalog, abstract_searcher=searcher, lm=lm, default_k=0
        )(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))

    from chartcoach.retrieval.strategy.pipelines.decompose_parallel import (
        DecomposeParallelStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        DecomposeParallelStrategy(
            catalog=catalog, searcher=searcher, lm=lm, default_k=0
        )(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))

    from chartcoach.retrieval.strategy.pipelines.role_aware_sections import (
        RoleAwareSectionsStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        RoleAwareSectionsStrategy(
            catalog=catalog, searcher=searcher, lm=lm, default_k=0
        )(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))

    with pytest.raises(ValueError, match="k must be positive"):
        QueryFusionHybridStrategy(
            catalog=catalog, searcher=searcher, lm=lm, default_k=0
        )(request=RetrievalRequest(context=[TextItem(role="situation", text="S")]))

    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    with pytest.raises(ValueError, match="k must be positive"):
        AgenticHybridStrategy(catalog=catalog, searcher=searcher, lm=lm, default_k=0)(
            request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
        )


def test_searcher_requires_lance_backend(catalog: Catalog) -> None:
    class NotLance:
        backend = "memory"

        def search(self, *_args, **_kwargs):  # noqa: ANN001
            return pl.DataFrame()

    v = CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=pl.DataFrame(
            {"id": [], "role": [], "content": [], "embedding": []}
        ),
        index=NotLance(),
    )
    with pytest.raises(RuntimeError, match="requires the Lance backend"):
        GuidelineSearcher(catalog=catalog, vector_index=v)


def test_describe_text_source_includes_labels_source() -> None:
    from chartcoach.embedding import GuidelineLabelsTextSource

    meta = describe_text_source(GuidelineLabelsTextSource(role="labels"))
    assert meta["type"] == "guideline_labels"


def test_searcher_aggregate_guideline_hits() -> None:
    empty = GuidelineSearcher.aggregate_guideline_hits(pl.DataFrame(), k=5)
    assert empty.is_empty()

    with pytest.raises(ValueError, match="Missing required column"):
        GuidelineSearcher.aggregate_guideline_hits(
            pl.DataFrame({"id": ["g"], "role": ["x"]}), k=1
        )

    hits = pl.DataFrame(
        {
            "id": ["g1", "g1", "g2"],
            "role": ["a", "b", "a"],
            "score": [2.0, 1.0, 1.5],
        }
    )
    agg = GuidelineSearcher.aggregate_guideline_hits(hits, k=2)
    assert agg["id"].to_list() == ["g1", "g2"]


def test_dense_mmr_strategy_selects_diverse_guidelines(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    # Row-level hit scores: g1 strongest, g2 second but redundant (same embedding), g3 third.
    fake.set_dense(
        "default",
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [0.9, 0.85, 0.84],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    strat = DenseMmrStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=2,
        mmr_lambda=0.65,
    )
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")])
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g3"]
    assert out.meta["mmr_candidates"] >= 2


def test_dense_mmr_strategy_handles_empty_hits(catalog: Catalog, monkeypatch) -> None:
    fake = _FakeLanceIndex()
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)
    strat = DenseMmrStrategy(catalog=catalog, searcher=searcher, default_k=2)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.catalog.entries == []


def test_dense_mmr_strategy_fills_when_embeddings_missing(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_dense(
        "default",
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [0.9, 0.85, 0.84],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    # Remove g2 from embedded_text_df so MMR can only score g1/g3; strategy should
    # still include g2 via the fill step.
    vector_index.embedded_text_df = vector_index.embedded_text_df.filter(
        pl.col("id") != "g2"
    )
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)
    strat = DenseMmrStrategy(catalog=catalog, searcher=searcher, default_k=3)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=3)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g3", "g2"]


def test_dense_mmr_strategy_skips_zero_length_embedding_vectors(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_dense(
        "default",
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [0.9, 0.85, 0.84],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    vector_index.embedded_text_df = vector_index.embedded_text_df.with_columns(
        embedding=pl.when(pl.col("id") == "g2")
        .then(pl.lit([]))
        .otherwise(pl.col("embedding"))
    )
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)
    strat = DenseMmrStrategy(catalog=catalog, searcher=searcher, default_k=3)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=3)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g3", "g2"]


def test_hybrid_rrf_strategy_orders_by_score(catalog: Catalog, monkeypatch) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {
                "id": ["g2", "g1"],
                "role": ["advice", "advice"],
                "score": [2.0, 1.0],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    strat = HybridRrfStrategy(catalog=catalog, searcher=searcher, default_k=1)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["reranker"]["type"] == "rrf"


def test_query_fusion_strategy_fuses_queries_and_reranks_with_cross_encoder(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "color",
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    fake.set_hybrid(
        "annotation",
        pl.DataFrame(
            {"id": ["g2", "g1"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    # Final rerank (ids filter) prefers g2.
    fake.set_hybrid_for_ids(
        {"g1", "g2"},
        pl.DataFrame(
            {"id": ["g2", "g1"], "role": ["advice", "advice"], "score": [3.0, 2.0]}
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=1,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(queries=["color", "annotation"])

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["queries"][0] == "S"

    # Cover string-input parsing branch in `_clean_queries`.
    assert QueryFusionHybridStrategy._clean_queries(" color ", fallback="S") == [
        "S",
        "color",
    ]

    # Cover de-duplication branch in `_clean_queries`.
    assert QueryFusionHybridStrategy._clean_queries(
        ["color", "Color ", "annotation"], fallback="S"
    ) == ["S", "color", "annotation"]


def test_query_fusion_strategy_retries_lm_and_falls_back_when_rerank_empty(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "color",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=2, cross_encoder_model="dummy"),
        default_k=1,
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(queries=["color"])

    strat._program = FlakyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_query_fusion_strategy_fills_from_fused_when_cross_encoder_partial(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    # Cross-encoder rerank step only surfaces g1.
    fake.set_hybrid_for_ids(
        {"g1", "g2"},
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [3.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=1, cross_encoder_model="dummy"),
        default_k=2,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(queries=["S"])

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_query_fusion_strategy_runs_fill_fallback_when_underfilled(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [3.0, 2.0, 1.0],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=1, cross_encoder_model=None),
        default_k=5,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(queries=["S"])

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=5)
    )
    assert out.meta["fill_fallback_used"] is True


def test_query_fusion_strategy_fill_fallback_adds_new_ids(
    catalog: Catalog, monkeypatch
) -> None:
    import chartcoach.retrieval.strategy.pipelines.searcher as searcher_mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {
                "id": ["g1", "g2"],
                "role": ["advice", "advice"],
                "score": [2.0, 1.0],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    # Force fusion to under-produce by truncating per-query aggregation while
    # keeping the fill-fallback aggregation intact (k differs: 40 vs 50).
    original_agg = searcher_mod.GuidelineSearcher.aggregate_guideline_hits

    def patched_agg(hits_df: pl.DataFrame, *, k: int, **kwargs):  # noqa: ANN001
        if k == 40:
            return pl.DataFrame({"id": ["g1"], "score": [1.0], "best_role": ["advice"]})
        return original_agg(hits_df, k=k, **kwargs)

    monkeypatch.setattr(
        searcher_mod.GuidelineSearcher,
        "aggregate_guideline_hits",
        staticmethod(patched_agg),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = QueryFusionHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=QueryFusionConfig(n_queries=1, cross_encoder_model=None),
        default_k=2,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(queries=["S"])

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["fill_fallback_used"] is True


def test_hyde_strategy_fuses_fts_and_dense_and_reranks(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_fts(
        "S",
        pl.DataFrame(
            {"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["color"]}
        ),
    )
    fake.set_dense(
        "default",
        pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [0.9]}),
    )
    fake.set_hybrid_for_ids(
        {"g1", "g2"},
        pl.DataFrame(
            {"id": ["g2", "g1"], "role": ["advice", "advice"], "score": [3.0, 2.0]}
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model="dummy"),
        default_k=1,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="pseudo")

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["pseudo_document_chars"] > 0

    # Empty pseudo-document falls back to the situation text.
    class EmptyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="")

    strat._program = EmptyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["pseudo_document_chars"] >= len("S")


def test_hyde_strategy_retries_lm_and_falls_back_when_rerank_empty(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    fake.set_dense(
        "default",
        pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [0.9]}),
    )
    # No hybrid results for the situation => rerank returns empty.
    fake.set_hybrid("S", pl.DataFrame({"id": [], "role": [], "score": []}))

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model="dummy"),
        default_k=2,
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(pseudo_document="pseudo")

    strat._program = FlakyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_hyde_strategy_fills_when_cross_encoder_rerank_partial(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    fake.set_dense(
        "default",
        pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [0.9]}),
    )
    # Rerank step (ids filter) only returns g1, so the strategy must fill g2.
    fake.set_hybrid_for_ids(
        {"g1", "g2"},
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model="dummy"),
        default_k=2,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="pseudo")

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_hyde_strategy_runs_fill_fallback_when_underfilled(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    # Only 3 guidelines exist, but ask for k=5 to force fill_fallback_used.
    fake.set_fts(
        "S",
        pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice"] * 3,
                "score": [3.0, 2.0, 1.0],
                "text": ["x"] * 3,
            }
        ),
    )
    fake.set_dense(
        "default",
        pl.DataFrame(
            {"id": ["g1", "g2", "g3"], "role": ["advice"] * 3, "score": [0.9, 0.8, 0.7]}
        ),
    )
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {"id": ["g1", "g2", "g3"], "role": ["advice"] * 3, "score": [3.0, 2.0, 1.0]}
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model=None),
        default_k=5,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="pseudo")

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=5)
    )
    assert out.meta["fill_fallback_used"] is True


def test_hyde_strategy_fill_fallback_adds_new_ids(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    fake.set_dense(
        "default",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [0.9]}),
    )
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = HydeHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        config=HydeConfig(cross_encoder_model=None),
        default_k=2,
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(pseudo_document="pseudo")

    strat._program = DummyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["fill_fallback_used"] is True


def test_agentic_tools_and_strategy(catalog: Catalog, monkeypatch) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]}),
    )
    fake.set_dense(
        "default",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0]}),
    )
    fake.set_fts(
        "S",
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [1.0], "text": ["x"]}),
    )
    fake.set_hybrid_for_ids(
        {"g1"},
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    tools = AgenticHybridTools(catalog=catalog, searcher=searcher)
    assert "advice" in tools.list_roles()
    assert "id,role,score" in tools.hybrid_search("S")
    assert "id,role,score" in tools.dense_search("S")
    assert "id,role,score" in tools.fts_search("S")
    assert tools.hybrid_search("").startswith("id,role,score")
    assert tools.dense_search("").startswith("id,role,score")
    assert tools.fts_search("").startswith("id,role,score")
    assert tools.read_guidelines_by_id(["g1"])[0]["id"] == "g1"

    vector_index_no_role = _make_vector_index(catalog=catalog, fake_index=fake)
    vector_index_no_role.embedded_text_df = vector_index_no_role.embedded_text_df.drop(
        "role"
    )
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    tools_no_role = AgenticHybridTools(
        catalog=catalog,
        searcher=GuidelineSearcher(
            catalog=catalog, vector_index=vector_index_no_role
        ),
    )
    assert tools_no_role.list_roles() == []

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model="dummy",
    )
    assert strat.tools.searcher is searcher

    # Force a parse error on first try by raising AdapterParseError.
    from dspy.utils.exceptions import AdapterParseError
    from dspy.signatures.signature import Signature as DspySignature
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridSignature,
    )

    sig = cast(DspySignature, AgenticHybridSignature)

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise AdapterParseError("dummy", sig, "resp", message="boom")
            return dspy.Prediction(used_guideline_ids=["g1"], notes="g1")

    strat._program = FlakyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]

    class AlwaysBad(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            raise AdapterParseError("dummy", sig, "resp", message="boom")

    strat._program = AlwaysBad()
    with pytest.raises(ValueError, match="Failed to parse model output"):
        strat(
            request=RetrievalRequest(
                context=[TextItem(role="situation", text="S")], k=1
            )
        )


def test_agentic_strategy_falls_back_to_hybrid_when_no_ids(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {
                "id": ["g2", "g2", "g1"],
                "role": ["advice", "advice", "advice"],
                "score": [2.0, 1.5, 1.0],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model=None,
    )

    class NoIds(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=[], notes="no ids")

    strat._program = NoIds()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["fallback_used"] is True


def test_agentic_strategy_fills_to_k_with_hybrid_fallback(
    catalog: Catalog, monkeypatch
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        "S",
        pl.DataFrame(
            {
                "id": ["g1", "g2"],
                "role": ["advice", "advice"],
                "score": [2.0, 1.0],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=2,
        final_cross_encoder_model=None,
    )

    class OneId(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="no ids")

    strat._program = OneId()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["fallback_used"] is True


def test_agentic_strategy_cross_encoder_fallback_when_rerank_empty(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        final_cross_encoder_model="dummy",
    )

    class OneId(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1"], notes="no ids")

    strat._program = OneId()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["cross_encoder_fallback_used"] is True


def test_agentic_strategy_fills_when_cross_encoder_rerank_partial(
    catalog: Catalog, monkeypatch
) -> None:
    import lancedb.rerankers

    class DummyCrossEncoder:  # noqa: D401
        def __init__(self, model_name: str):  # noqa: ARG002
            pass

    monkeypatch.setattr(lancedb.rerankers, "CrossEncoderReranker", DummyCrossEncoder)

    fake = _FakeLanceIndex()
    # Rerank step (ids filter) only returns g1, so the strategy must fill g2
    # from its candidate set to reach k=2.
    fake.set_hybrid_for_ids(
        {"g1", "g2"},
        pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )

    vector_index = _make_vector_index(catalog=catalog, fake_index=fake)
    monkeypatch.setattr(
        CatalogVectorIndex,
        "embed_query",
        lambda _self, _t: np.array([1.0, 0.0]),
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    from chartcoach.retrieval.strategy.pipelines.agentic_hybrid import (
        AgenticHybridStrategy,
    )

    strat = AgenticHybridStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=2,
        final_cross_encoder_model="dummy",
    )

    class TwoIds(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(used_guideline_ids=["g1", "g2"], notes="no ids")

    strat._program = TwoIds()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["cross_encoder_fallback_used"] is True

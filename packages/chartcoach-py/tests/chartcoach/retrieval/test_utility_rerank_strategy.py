from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.index import VectorIndex
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.pipelines.utility_rerank_hybrid import (
    UtilityRerankHybridStrategy,
)
from chartcoach.retrieval.strategy.pipelines.utility_reranker import (
    UtilityRerankerConfig,
)
from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
)


class _FakeLanceIndex:
    backend = "lance"

    def __init__(self) -> None:
        self._hybrid: pl.DataFrame = pl.DataFrame()

    def set_hybrid(self, df: pl.DataFrame) -> None:
        self._hybrid = df

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
    ) -> pl.DataFrame:
        df = self._hybrid
        if roles:
            df = df.filter(pl.col("role").is_in(sorted(set(roles))))
        if ids:
            df = df.filter(pl.col("id").is_in(sorted(ids)))
        return df.head(k)

    def search(self, _query: np.ndarray, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return pl.DataFrame({"id": [], "role": [], "score": [], "text": []}).head(k)

    def search_fts(self, _query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return pl.DataFrame({"id": [], "role": [], "score": [], "text": []}).head(k)


def _make_searcher(*, catalog: Catalog, fake: _FakeLanceIndex) -> GuidelineSearcher:
    embedded = pl.DataFrame(
        {
            "id": ["g1", "g2"],
            "role": ["advice", "advice"],
            "content": ["c1", "c2"],
            "embedding": [[1.0, 0.0], [0.0, 1.0]],
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
                    title="Guideline one",
                    description="",
                    labels=["topic:x"],
                    body="## Advice <!-- role: advice -->\nA\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Guideline two",
                    description="",
                    labels=["topic:y"],
                    body="## Advice <!-- role: advice -->\nB\n",
                ),
                references=[],
            ),
        ]
    )


def test_utility_rerank_hybrid_orders_by_utility(monkeypatch, catalog: Catalog) -> None:
    import chartcoach.retrieval.strategy.pipelines.utility_rerank_hybrid as strat_mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        pl.DataFrame(
            {
                "id": ["g1", "g2"],
                "role": ["advice", "advice"],
                "score": [2.0, 1.0],
                "text": ["evidence a", "evidence b"],
            }
        )
    )
    searcher = _make_searcher(catalog=catalog, fake=fake)

    # Avoid real embedding calls.
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )

    class DummyModule:
        def score_guideline(self, *, request, situation_text, entry, evidence):  # noqa: ANN001
            return {
                "utility": 10.0 if entry.id == "g2" else 1.0,
                "applicability": "applicable",
            }

    def fake_shared_utility_reranker():  # noqa: ANN001
        return object(), DummyModule(), UtilityRerankerConfig(candidate_k=10)

    monkeypatch.setattr(
        strat_mod, "shared_utility_reranker", fake_shared_utility_reranker
    )

    strat = UtilityRerankHybridStrategy(catalog=catalog, searcher=searcher, default_k=2)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.guideline.id for e in out.catalog.entries] == ["g2", "g1"]
    assert out.meta["score_kind"] == "utility_rerank"
    assert out.meta["hits"][0]["utility"]["utility"] == 10.0

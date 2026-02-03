from __future__ import annotations

import numpy as np
import polars as pl

from chartcoach.retrieval.operators import (
    search_dense_with_focus,
    search_fts_with_focus,
    search_hybrid_with_focus,
)
from chartcoach.retrieval.strategy.pipelines.focus import (
    FocusConfig,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)


class _StubSearcher:
    def __init__(self) -> None:
        self.calls: list[tuple[str, set[str] | None]] = []

    def _df(self) -> pl.DataFrame:
        return pl.DataFrame(
            {
                "id": ["g1"],
                "role": ["advice"],
                "score": [1.0],
                "text": ["stub"],
            }
        )

    def search_dense(
        self,
        *,
        query_vector: np.ndarray,  # noqa: ARG002
        k: int,  # noqa: ARG002
        roles: set[str] | None = None,
        ids: set[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        self.calls.append(("dense", roles))
        if roles == primary_roles_for_focus("violations"):
            return pl.DataFrame()
        return self._df()

    def search_fts(
        self,
        *,
        query_text: str,  # noqa: ARG002
        k: int,  # noqa: ARG002
        roles: set[str] | None = None,
        ids: set[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        self.calls.append(("fts", roles))
        if roles == primary_roles_for_focus("violations"):
            return pl.DataFrame()
        return self._df()

    def search_hybrid(
        self,
        *,
        query_text: str,  # noqa: ARG002
        query_vector: np.ndarray,  # noqa: ARG002
        k: int,  # noqa: ARG002
        reranker: object | None = None,  # noqa: ARG002
        roles: set[str] | None = None,
        ids: set[str] | None = None,  # noqa: ARG002
        fts_columns: str | list[str] | None = None,  # noqa: ARG002
    ) -> pl.DataFrame:
        self.calls.append(("hybrid", roles))
        if roles == primary_roles_for_focus("violations"):
            return pl.DataFrame()
        return self._df()


def test_search_dense_with_focus_falls_back_on_empty() -> None:
    searcher = _StubSearcher()
    focus = FocusConfig(mode="violations", allow_role_fallback=True)
    hits, roles_used = search_dense_with_focus(
        searcher=searcher,
        query_vector=np.zeros(2),
        k=10,
        focus=focus,
        focus_mode=focus.mode,
    )

    assert not hits.is_empty()
    assert roles_used == fallback_roles_for_focus("violations")
    assert searcher.calls == [
        ("dense", primary_roles_for_focus("violations")),
        ("dense", fallback_roles_for_focus("violations")),
    ]


def test_search_fts_with_focus_falls_back_on_empty() -> None:
    searcher = _StubSearcher()
    focus = FocusConfig(mode="violations", allow_role_fallback=True)
    hits, roles_used = search_fts_with_focus(
        searcher=searcher,
        query_text="q",
        k=10,
        focus=focus,
        focus_mode=focus.mode,
    )

    assert not hits.is_empty()
    assert roles_used == fallback_roles_for_focus("violations")
    assert searcher.calls == [
        ("fts", primary_roles_for_focus("violations")),
        ("fts", fallback_roles_for_focus("violations")),
    ]


def test_search_hybrid_with_focus_falls_back_on_empty() -> None:
    searcher = _StubSearcher()
    focus = FocusConfig(mode="violations", allow_role_fallback=True)
    hits, roles_used = search_hybrid_with_focus(
        searcher=searcher,
        query_text="q",
        query_vector=np.zeros(2),
        k=10,
        reranker=None,
        focus=focus,
        focus_mode=focus.mode,
        fts_columns="text",
    )

    assert not hits.is_empty()
    assert roles_used == fallback_roles_for_focus("violations")
    assert searcher.calls == [
        ("hybrid", primary_roles_for_focus("violations")),
        ("hybrid", fallback_roles_for_focus("violations")),
    ]


def test_search_dense_with_focus_no_fallback_when_focus_all() -> None:
    searcher = _StubSearcher()
    focus = FocusConfig(mode="all", allow_role_fallback=True)
    hits, roles_used = search_dense_with_focus(
        searcher=searcher,
        query_vector=np.zeros(2),
        k=10,
        focus=focus,
        focus_mode=focus.mode,
    )

    assert roles_used is None
    assert searcher.calls == [("dense", None)]
    assert not hits.is_empty()

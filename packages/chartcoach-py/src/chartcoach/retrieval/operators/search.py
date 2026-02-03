from __future__ import annotations

from typing import Protocol

import numpy as np
import polars as pl

from chartcoach.retrieval.strategy.pipelines.focus import (
    FocusConfig,
    FocusMode,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)


class _DenseSearcher(Protocol):
    def search_dense(
        self,
        *,
        query_vector: np.ndarray,
        k: int,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame: ...


class _FtsSearcher(Protocol):
    def search_fts(
        self,
        *,
        query_text: str,
        k: int,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame: ...


class _HybridSearcher(Protocol):
    def search_hybrid(
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,
        k: int,
        reranker: object | None = None,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
        fts_columns: str | list[str] | None = None,
    ) -> pl.DataFrame: ...


def search_dense_with_roles_fallback(
    *,
    searcher: _DenseSearcher,
    query_vector: np.ndarray,
    k: int,
    roles: set[str] | None,
    fallback_roles: set[str] | None,
    allow_role_fallback: bool,
    ids: set[str] | None = None,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles_used = roles
    hits_df = searcher.search_dense(
        query_vector=query_vector, k=int(k), roles=roles_used, ids=ids
    )
    if (
        hits_df.is_empty()
        and allow_role_fallback
        and roles is not None
        and fallback_roles is not None
        and fallback_roles != roles
    ):
        roles_used = fallback_roles
        hits_df = searcher.search_dense(
            query_vector=query_vector, k=int(k), roles=roles_used, ids=ids
        )
    return hits_df, roles_used


def search_fts_with_roles_fallback(
    *,
    searcher: _FtsSearcher,
    query_text: str,
    k: int,
    roles: set[str] | None,
    fallback_roles: set[str] | None,
    allow_role_fallback: bool,
    ids: set[str] | None = None,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles_used = roles
    hits_df = searcher.search_fts(
        query_text=query_text, k=int(k), roles=roles_used, ids=ids
    )
    if (
        hits_df.is_empty()
        and allow_role_fallback
        and roles is not None
        and fallback_roles is not None
        and fallback_roles != roles
    ):
        roles_used = fallback_roles
        hits_df = searcher.search_fts(
            query_text=query_text, k=int(k), roles=roles_used, ids=ids
        )
    return hits_df, roles_used


def search_hybrid_with_roles_fallback(
    *,
    searcher: _HybridSearcher,
    query_text: str,
    query_vector: np.ndarray,
    k: int,
    reranker: object | None,
    roles: set[str] | None,
    fallback_roles: set[str] | None,
    allow_role_fallback: bool,
    ids: set[str] | None = None,
    fts_columns: str | list[str] | None = None,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles_used = roles
    hits_df = searcher.search_hybrid(
        query_text=query_text,
        query_vector=query_vector,
        reranker=reranker,
        k=int(k),
        roles=roles_used,
        ids=ids,
        fts_columns=fts_columns,
    )
    if (
        hits_df.is_empty()
        and allow_role_fallback
        and roles is not None
        and fallback_roles is not None
        and fallback_roles != roles
    ):
        roles_used = fallback_roles
        hits_df = searcher.search_hybrid(
            query_text=query_text,
            query_vector=query_vector,
            reranker=reranker,
            k=int(k),
            roles=roles_used,
            ids=ids,
            fts_columns=fts_columns,
        )
    return hits_df, roles_used


def search_dense_with_focus(
    *,
    searcher: _DenseSearcher,
    query_vector: np.ndarray,
    k: int,
    ids: set[str] | None = None,
    focus: FocusConfig,
    focus_mode: FocusMode,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles = primary_roles_for_focus(focus_mode)
    return search_dense_with_roles_fallback(
        searcher=searcher,
        query_vector=query_vector,
        k=k,
        roles=roles,
        fallback_roles=fallback_roles_for_focus(focus_mode),
        allow_role_fallback=focus.allow_role_fallback,
        ids=ids,
    )


def search_fts_with_focus(
    *,
    searcher: _FtsSearcher,
    query_text: str,
    k: int,
    ids: set[str] | None = None,
    focus: FocusConfig,
    focus_mode: FocusMode,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles = primary_roles_for_focus(focus_mode)
    return search_fts_with_roles_fallback(
        searcher=searcher,
        query_text=query_text,
        k=k,
        roles=roles,
        fallback_roles=fallback_roles_for_focus(focus_mode),
        allow_role_fallback=focus.allow_role_fallback,
        ids=ids,
    )


def search_hybrid_with_focus(
    *,
    searcher: _HybridSearcher,
    query_text: str,
    query_vector: np.ndarray,
    k: int,
    reranker: object | None,
    ids: set[str] | None = None,
    focus: FocusConfig,
    focus_mode: FocusMode,
    fts_columns: str | list[str] | None = None,
) -> tuple[pl.DataFrame, set[str] | None]:
    roles = primary_roles_for_focus(focus_mode)
    return search_hybrid_with_roles_fallback(
        searcher=searcher,
        query_text=query_text,
        query_vector=query_vector,
        k=k,
        reranker=reranker,
        roles=roles,
        fallback_roles=fallback_roles_for_focus(focus_mode),
        allow_role_fallback=focus.allow_role_fallback,
        ids=ids,
        fts_columns=fts_columns,
    )

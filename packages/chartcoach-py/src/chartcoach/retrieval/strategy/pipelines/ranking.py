from __future__ import annotations

from collections.abc import Mapping, Sequence

import numpy as np


def rrf_scores(*, rankings: Sequence[Sequence[str]], k: int = 60) -> dict[str, float]:
    """Compute Reciprocal Rank Fusion scores.

    References:
      - Cormack et al. (2009), "Reciprocal Rank Fusion Outperforms Condorcet and
        Individual Rank Learning Methods".
    """

    if k <= 0:
        raise ValueError("k must be positive.")

    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, gid in enumerate(ranking, start=1):
            if not gid:
                continue
            scores[gid] = scores.get(gid, 0.0) + 1.0 / (k + rank)
    return scores


def rrf_rank(*, rankings: Sequence[Sequence[str]], k: int = 60) -> list[str]:
    """Fuse ranked lists into a single ranking via RRF."""

    scores = rrf_scores(rankings=rankings, k=k)

    best_rank: dict[str, int] = {}
    for ranking in rankings:
        for rank, gid in enumerate(ranking, start=1):
            if not gid:
                continue
            current = best_rank.get(gid)
            if current is None or rank < current:
                best_rank[gid] = rank

    return sorted(
        scores,
        key=lambda gid: (
            -scores[gid],
            best_rank.get(gid, 2**31 - 1),
            gid,
        ),
    )


def _normalize(v: np.ndarray) -> np.ndarray:
    denom = float(np.linalg.norm(v))
    if denom <= 0:
        return v
    return v / denom


def mmr_select(
    *,
    candidate_ids: Sequence[str],
    relevance: Mapping[str, float],
    embeddings: Mapping[str, np.ndarray],
    k: int,
    lambda_mult: float = 0.5,
) -> list[str]:
    """Select a diverse top-k via Maximal Marginal Relevance (MMR)."""

    if k <= 0:
        raise ValueError("k must be positive.")
    if not (0.0 <= lambda_mult <= 1.0):
        raise ValueError("lambda_mult must be within [0, 1].")

    # Min-max normalize relevance to keep MMR stable across scoring scales.
    rel_values = [float(relevance.get(gid, 0.0)) for gid in candidate_ids]
    if not rel_values:
        return []
    rel_min = min(rel_values)
    rel_max = max(rel_values)
    rel_denom = rel_max - rel_min

    def rel(gid: str) -> float:
        value = float(relevance.get(gid, 0.0))
        if rel_denom <= 1e-9:
            return 0.0
        return (value - rel_min) / rel_denom

    normalized_embeddings: dict[str, np.ndarray] = {
        gid: _normalize(np.asarray(embeddings[gid], dtype=np.float32))
        for gid in candidate_ids
        if gid in embeddings
    }

    selected: list[str] = []
    remaining = [gid for gid in candidate_ids if gid in normalized_embeddings]

    while remaining and len(selected) < k:
        best_gid = None
        best_score = -1e9
        for gid in remaining:
            relevance_score = rel(gid)
            if not selected:
                mmr = relevance_score
            else:
                cand_vec = normalized_embeddings[gid]
                max_sim = max(
                    float(cand_vec @ normalized_embeddings[sid]) for sid in selected
                )
                mmr = lambda_mult * relevance_score - (1.0 - lambda_mult) * max_sim

            if mmr > best_score:
                best_score = mmr
                best_gid = gid

        if best_gid is None:
            break
        selected.append(best_gid)
        remaining = [gid for gid in remaining if gid != best_gid]

    return selected

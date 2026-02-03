from __future__ import annotations

from collections.abc import Mapping, Sequence

import numpy as np


def rrf_scores(
    *,
    rankings: Sequence[Sequence[str]],
    k: int = 60,
    weights: Sequence[float] | None = None,
) -> dict[str, float]:
    """Compute Reciprocal Rank Fusion scores.

    References:
      - Cormack et al. (2009), "Reciprocal Rank Fusion Outperforms Condorcet and
        Individual Rank Learning Methods".
    """

    if k <= 0:
        raise ValueError("k must be positive.")

    if weights is None:
        weights = [1.0 for _ in rankings]
    if len(weights) != len(rankings):
        raise ValueError("weights must match rankings length.")

    scores: dict[str, float] = {}
    for ranking, weight in zip(rankings, weights, strict=True):
        w = float(weight)
        if w <= 0:
            continue
        for rank, gid in enumerate(ranking, start=1):
            if not gid:
                continue
            scores[gid] = scores.get(gid, 0.0) + w / (k + rank)
    return scores


def rrf_rank(
    *,
    rankings: Sequence[Sequence[str]],
    k: int = 60,
    weights: Sequence[float] | None = None,
) -> list[str]:
    """Fuse ranked lists into a single ranking via RRF."""

    scores = rrf_scores(rankings=rankings, k=k, weights=weights)

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


def label_round_robin_select(
    *,
    candidate_ids: Sequence[str],
    relevance: Mapping[str, float],
    labels_by_id: Mapping[str, Sequence[str]],
    k: int,
    group_prefixes: Sequence[str] = ("goal", "topic"),
    redundancy_gamma: float = 0.0,
) -> list[str]:
    """Select top-k with label-group coverage via round-robin.

    This is a lightweight, explainable set selector baseline:
    - Partition candidates into label-derived groups (using the first matching value per prefix).
    - Round-robin across groups in descending group quality.
    - Fill remaining slots by relevance with an optional redundancy penalty based on label overlap.
    """

    if k <= 0:
        raise ValueError("k must be positive.")
    if redundancy_gamma < 0:
        raise ValueError("redundancy_gamma must be non-negative.")

    if not candidate_ids:
        return []

    prefixes = [p.strip().lower() for p in group_prefixes if str(p).strip()]

    def _group_key(gid: str) -> str:
        labels = labels_by_id.get(gid) or ()
        lowered = [str(label).strip() for label in labels if str(label).strip()]
        parts: list[str] = []
        for prefix in prefixes:
            match = next(
                (label for label in lowered if label.lower().startswith(f"{prefix}:")),
                None,
            )
            parts.append(match or f"{prefix}:<none>")
        if not parts:
            return "<all>"
        return "|".join(parts)

    groups: dict[str, list[str]] = {}
    for gid in candidate_ids:
        if not gid:
            continue
        groups.setdefault(_group_key(gid), []).append(gid)

    for key, gids in list(groups.items()):
        ordered = sorted(
            gids,
            key=lambda gid: (
                -float(relevance.get(gid, 0.0)),
                gid,
            ),
        )
        if ordered:
            groups[key] = ordered
        else:
            groups.pop(key, None)

    if not groups:
        return []

    group_order = sorted(
        groups,
        key=lambda key: (
            -float(relevance.get(groups[key][0], 0.0)),
            key,
        ),
    )

    selected: list[str] = []
    selected_set: set[str] = set()
    # Coverage pass: take at most one candidate per group.
    for key in group_order:
        items = groups[key]
        gid = next((cid for cid in items if cid and cid not in selected_set), None)
        if gid is None:
            continue
        selected.append(gid)
        selected_set.add(gid)
        if len(selected) >= k:
            return selected[:k]

    if len(selected) >= k:
        return selected[:k]

    remaining = [gid for gid in candidate_ids if gid and gid not in selected_set]
    if not remaining:
        return selected

    selected_label_sets = [
        set(
            str(label).strip()
            for label in (labels_by_id.get(gid) or ())
            if str(label).strip()
        )
        for gid in selected
    ]

    def _max_label_overlap(gid: str) -> float:
        if not selected_label_sets:
            return 0.0
        cand = set(
            str(label).strip()
            for label in (labels_by_id.get(gid) or ())
            if str(label).strip()
        )
        if not cand:
            return 0.0
        best = 0.0
        for other in selected_label_sets:
            denom = len(cand | other)
            if denom <= 0:
                continue
            best = max(best, len(cand & other) / denom)
        return best

    while remaining and len(selected) < k:
        best_gid: str | None = None
        best_score = -1e18
        for gid in remaining:
            base = float(relevance.get(gid, 0.0))
            penalty = (
                redundancy_gamma * _max_label_overlap(gid) if redundancy_gamma else 0.0
            )
            score = base - penalty
            if score > best_score or (
                abs(score - best_score) <= 1e-12 and gid < (best_gid or "~")
            ):
                best_score = score
                best_gid = gid
        if best_gid is None:
            break
        selected.append(best_gid)
        selected_set.add(best_gid)
        selected_label_sets.append(
            set(
                str(label).strip()
                for label in (labels_by_id.get(best_gid) or ())
                if str(label).strip()
            )
        )
        remaining = [gid for gid in remaining if gid != best_gid]

    return selected


def facility_location_select(
    *,
    candidate_ids: Sequence[str],
    relevance: Mapping[str, float],
    embeddings: Mapping[str, np.ndarray],
    k: int,
    alpha: float = 0.4,
    beta: float = 0.6,
    gamma: float = 0.0,
) -> list[str]:
    """Greedy facility-location style set selection.

    This selector prefers candidates that are both relevant and help "cover"
    the candidate neighborhood under cosine similarity.
    """

    if k <= 0:
        raise ValueError("k must be positive.")
    if alpha < 0 or beta < 0 or gamma < 0:
        raise ValueError("alpha/beta/gamma must be non-negative.")

    ids = [gid for gid in candidate_ids if gid]
    if not ids:
        return []

    n = len(ids)
    dim = None
    for gid in ids:
        if gid in embeddings:
            dim = int(np.asarray(embeddings[gid]).shape[0])
            break
    if dim is None:
        # No embeddings; fall back to relevance-only ordering.
        return sorted(ids, key=lambda gid: (-float(relevance.get(gid, 0.0)), gid))[:k]

    mat = np.zeros((n, dim), dtype=np.float32)
    for i, gid in enumerate(ids):
        vec = embeddings.get(gid)
        if vec is None:
            continue
        mat[i] = _normalize(np.asarray(vec, dtype=np.float32))

    sims = mat @ mat.T

    rel_values = np.array(
        [float(relevance.get(gid, 0.0)) for gid in ids], dtype=np.float32
    )
    rel_min = float(rel_values.min(initial=0.0))
    rel_max = float(rel_values.max(initial=0.0))
    denom = rel_max - rel_min
    rel_norm = (
        (rel_values - rel_min) / denom if denom > 1e-9 else np.zeros_like(rel_values)
    )

    selected_idx: list[int] = []
    remaining = list(range(n))
    best_sim = np.zeros(n, dtype=np.float32)
    best_sim_sum = 0.0

    while remaining and len(selected_idx) < min(int(k), n):
        best_j = None
        best_obj = -1e18
        for j in remaining:
            sim_j = sims[:, j]
            new_best = np.maximum(best_sim, sim_j)
            gain = float(new_best.sum() - best_sim_sum)
            redundancy = float(best_sim[j])
            obj = alpha * float(rel_norm[j]) + beta * gain - gamma * redundancy
            if obj > best_obj or (
                abs(obj - best_obj) <= 1e-12
                and best_j is not None
                and ids[j] < ids[best_j]
            ):
                best_obj = obj
                best_j = j

        if best_j is None:
            break

        selected_idx.append(best_j)
        remaining = [j for j in remaining if j != best_j]
        best_sim = np.maximum(best_sim, sims[:, best_j])
        best_sim_sum = float(best_sim.sum())

    return [ids[i] for i in selected_idx]

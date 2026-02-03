from __future__ import annotations

from typing import cast

import polars as pl


def merge_evidence(*sources: object, limit: int = 3) -> list[dict[str, object]]:
    """Merge evidence snippets (role/text/score dicts) from multiple sources.

    Strategies may retrieve the same guideline through multiple channels (dense,
    sparse, lexical, vision tokens, etc.). This helper provides a consistent way
    to surface a small set of the strongest evidence snippets per guideline.
    """

    merged: list[dict[str, object]] = []
    for source in sources:
        if not isinstance(source, list):
            continue
        for item in source:
            if not isinstance(item, dict):
                continue
            item_obj = cast("dict[str, object]", item)
            text = str(item_obj.get("text") or "").strip()
            if not text:
                continue
            merged.append(item_obj)

    merged.sort(key=lambda x: float(x.get("score") or 0.0), reverse=True)
    return merged[: max(0, int(limit))]


def extract_guideline_ranking(
    agg: pl.DataFrame,
) -> tuple[list[str], dict[str, list[dict[str, object]]], dict[str, str], dict[str, float]]:
    """Extract a ranking + per-guideline evidence/best_role maps from an agg DF."""

    ranking: list[str] = []
    evidence_by_id: dict[str, list[dict[str, object]]] = {}
    best_role_by_id: dict[str, str] = {}
    score_by_id: dict[str, float] = {}

    for row in agg.to_dicts():
        gid = row.get("id")
        if not isinstance(gid, str) or not gid:
            continue
        ranking.append(gid)

        score_by_id[gid] = float(row.get("score") or 0.0)
        best_role = row.get("best_role")
        if isinstance(best_role, str) and best_role:
            best_role_by_id.setdefault(gid, best_role)

        ev = row.get("evidence")
        if isinstance(ev, list) and ev:
            evidence_by_id.setdefault(gid, []).extend(
                [e for e in ev if isinstance(e, dict)]
            )

    return ranking, evidence_by_id, best_role_by_id, score_by_id

from __future__ import annotations

from typing import Sequence

import chartcoach as cc
import polars as pl

from .types import GroundingRecord


def rrf_fuse(
    ranked_lists: Sequence[Sequence[str]],
    *,
    k: int = 60,
) -> list[str]:
    scores: dict[str, float] = {}
    for ranked in ranked_lists:
        for rank, doc_id in enumerate(ranked, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)

    return [
        doc_id
        for doc_id, _ in sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    ]


def build_grounding_record(
    coach: cc.Coach,
    doc_ids: Sequence[str],
) -> GroundingRecord:
    materialized_doc_ids = list(doc_ids)
    if not materialized_doc_ids:
        return {
            "doc_ids": [],
            "guideline_ids": [],
            "guidance": [],
        }

    guidance = (
        pl.from_dict({"id": materialized_doc_ids})
        .join(coach.catalog.docs_df, how="left", on="id")
        .get_column("doc")
        .to_list()
    )

    return {
        "doc_ids": materialized_doc_ids,
        "guideline_ids": [doc_id.split("---")[0] for doc_id in materialized_doc_ids],
        "guidance": guidance,
    }

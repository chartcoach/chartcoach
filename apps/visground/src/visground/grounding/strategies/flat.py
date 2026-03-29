from __future__ import annotations

from dataclasses import dataclass
from typing import NotRequired, TypedDict

import chartcoach as cc

from ..types import GroundingRecord, GroundingRequest, GroundingStrategyMode
from ..utils import build_grounding_record, rrf_fuse


class FlatGroundingConfig(TypedDict):
    # Chroma fetch depth for each query rewrite before reciprocal-rank fusion.
    # This is not the final injected doc count, which can exceed `n_results`
    # after multiple rewrites are fused and deduplicated.
    n_results: int
    # Final cap on the returned `doc_ids` / `guidance` items after fusion and
    # materialization. Defaults to 4 when omitted.
    max_items: NotRequired[int]
    # Reciprocal-rank fusion damping constant. Larger values flatten the rank
    # contribution from each rewrite; smaller values reward top-ranked hits more.
    rrf_k: int


def _refine_query_texts(req: GroundingRequest) -> list[str]:
    return [
        req["query"],
        (
            f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
            f"{req['scope']} and {req['time_mode']} setting, need guidance to "
            "improve readability and prevent common mistakes."
        ),
        (
            f"{req['query']} Need guidance to improve readability and prevent "
            "common mistakes."
        ),
    ]


def _select_query_texts(req: GroundingRequest) -> list[str]:
    return [
        req["query"],
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, need guidance for choosing an "
            "appropriate chart design."
        ),
        (
            f"{req['query']} Need guidance for choosing an appropriate chart "
            "design and avoiding poor choices."
        ),
    ]


def _query_texts(req: GroundingRequest) -> list[str]:
    if req["objective"] == "refine":
        return _refine_query_texts(req)
    return _select_query_texts(req)


@dataclass(slots=True)
class FlatGroundingStrategy:
    coach: cc.Coach
    config: FlatGroundingConfig
    mode: GroundingStrategyMode = "flat"

    def retrieve(self, req: GroundingRequest) -> GroundingRecord:
        """Retrieve one grounding record using flat whole-document search."""

        matches = self.coach.index.collection.query(
            query_texts=_query_texts(req),
            where={"role": "document"},
            n_results=self.config["n_results"],
        )
        return build_grounding_record(
            self.coach,
            rrf_fuse(matches["ids"], k=self.config["rrf_k"])[
                : self.config.get("max_items", 4)
            ],
        )

    def retrieve_many(self, reqs: list[GroundingRequest]) -> list[GroundingRecord]:
        return [self.retrieve(req) for req in reqs]

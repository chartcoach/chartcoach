from __future__ import annotations

from dataclasses import dataclass

from ..types import GroundingRecord, GroundingRequest, GroundingStrategyMode


@dataclass(slots=True)
class NoneGroundingStrategy:
    mode: GroundingStrategyMode = "none"

    def retrieve(self, req: GroundingRequest) -> GroundingRecord:
        return {"doc_ids": [], "guideline_ids": [], "guidance": []}

from __future__ import annotations

from typing import Literal, NotRequired, Protocol, TypedDict

from ..data_profile import GroundingProfile

GroundingMode = Literal["none", "flat", "structured"]
AudienceModifierId = Literal[
    "novice",
    "casual",
    "expert",
]


class AudienceModifierSpec(TypedDict):
    description: str
    literacy_labels: list[str]
    audience_labels: list[str]
    needs_labels: list[str]


AUDIENCE_MODIFIER_SPECS: dict[AudienceModifierId, AudienceModifierSpec] = {
    "novice": {
        "description": (
            "Assume the intended audience is a casual public reader with limited "
            "visualization literacy. Prioritize low cognitive load, obvious "
            "takeaways, familiar encodings, direct labels, and minimal clutter."
        ),
        "literacy_labels": ["literacy:novice"],
        "audience_labels": ["audience:general-public"],
        "needs_labels": ["needs:low-domain-knowledge"],
    },
    "casual": {
        "description": (
            "Assume the intended audience is a general audience reading an "
            "explanatory chart. Prioritize balanced clarity and completeness, "
            "with clear labels and enough detail for a careful reader."
        ),
        "literacy_labels": ["literacy:general"],
        "audience_labels": ["audience:general-public"],
        "needs_labels": [],
    },
    "expert": {
        "description": (
            "Assume the intended audience is an expert analyst with high "
            "visualization literacy. Prioritize precision, information density, "
            "and efficient comparison over simplification."
        ),
        "literacy_labels": ["literacy:expert"],
        "audience_labels": ["audience:analyst", "audience:domain-expert"],
        "needs_labels": [],
    },
}

AUDIENCE_MODIFIER_IDS: tuple[AudienceModifierId, ...] = tuple(
    AUDIENCE_MODIFIER_SPECS.keys()
)


def get_audience_description(audience: AudienceModifierId) -> str:
    return AUDIENCE_MODIFIER_SPECS[audience]["description"]


class GroundingRequest(TypedDict):
    id: str
    query: str
    task: str
    scope: str
    time_mode: str
    chart: str | None
    objective: Literal["refine", "select"]
    audience: AudienceModifierId | None
    data_profile: NotRequired[GroundingProfile]


class GroundingRecord(TypedDict):
    doc_ids: list[str]
    guideline_ids: list[str]
    guidance: list[str]


GroundingStrategyMode = Literal["flat", "structured", "none"]


class GroundingStrategy(Protocol):
    mode: GroundingStrategyMode

    def retrieve(self, req: GroundingRequest) -> GroundingRecord: ...

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


FocusMode = Literal["all", "violations", "satisfied"]


class EvidenceSnippetTrace(BaseModel):
    model_config = ConfigDict(frozen=True)

    role: str | None = None
    text: str = Field(min_length=1)
    score: float | None = None


class HitTrace(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = Field(min_length=1)
    score: float | None = None
    best_role: str | None = None
    evidence: list[EvidenceSnippetTrace] = Field(default_factory=list)


class FocusTrace(BaseModel):
    model_config = ConfigDict(frozen=True)

    mode: FocusMode
    roles: list[str] | None = None


class StrategyTrace(BaseModel):
    """Typed schema for strategy telemetry embedded in `RetrievalResponse.meta`.

    The goal is to make it easy to consume strategy outputs (artifacts, analysis,
    UI) without heuristics over loosely-typed dicts while still allowing
    strategies to log additional fields.
    """

    model_config = ConfigDict(frozen=True, extra="allow")

    k: int = Field(ge=1)
    raw_k: int | None = Field(default=None, ge=1)
    score_kind: str | None = None
    focus: FocusTrace | None = None
    hits: list[HitTrace] = Field(default_factory=list)

    def extra_meta(self) -> dict[str, Any]:
        return dict(self.model_extra or {})

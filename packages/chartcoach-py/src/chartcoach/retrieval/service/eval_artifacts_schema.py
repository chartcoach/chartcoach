from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.strategy.base import StrategyInfo


ARTIFACT_SCHEMA_VERSION = 1


class _EvalArtifactsBaseModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class ScenarioChart(_EvalArtifactsBaseModel):
    uri: str = Field(min_length=1)
    mime: str | None = None


class ScenarioProvenance(_EvalArtifactsBaseModel):
    source: str | None = None


class ScenarioSpec(_EvalArtifactsBaseModel):
    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    lang: str = "en"
    chart: ScenarioChart | None = None
    query: str | None = None
    designer_intent: str | None = None
    audience: str | None = None
    medium: str | None = None
    constraints: str | None = None
    domain: str | None = None
    risk_tolerance: str | None = None
    time_budget: str | None = None
    counterfactual_group_id: str | None = None
    negative_guideline_ids: list[str] | None = None
    provenance: ScenarioProvenance | None = None


class ScenariosFile(_EvalArtifactsBaseModel):
    scenarios: list[ScenarioSpec]


class EvalEvidenceSnippet(_EvalArtifactsBaseModel):
    role: str | None = None
    text: str = Field(min_length=1)
    score: float | None = None


class EvalGuidelineResult(_EvalArtifactsBaseModel):
    rank: int = Field(ge=1)
    score: float = Field(gt=0)
    entry: CatalogEntry
    evidence: list[EvalEvidenceSnippet] | None = None


class EvalStrategyResult(_EvalArtifactsBaseModel):
    strategy_id: str = Field(min_length=1)
    strategy_name: str = Field(min_length=1)
    meta: dict[str, object] = Field(default_factory=dict)
    guidelines: list[EvalGuidelineResult] = Field(default_factory=list)


class EvalScenarioBundleArtifact(_EvalArtifactsBaseModel):
    schema_version: int = Field(default=ARTIFACT_SCHEMA_VERSION, frozen=True)
    generated_at: str = Field(min_length=1)
    digest: str = Field(min_length=1)
    scenario: ScenarioSpec
    strategies: list[EvalStrategyResult]
    meta: dict[str, object] = Field(default_factory=dict)


class EvalArtifactsIndexArtifact(_EvalArtifactsBaseModel):
    schema_version: int = Field(default=ARTIFACT_SCHEMA_VERSION, frozen=True)
    generated_at: str = Field(min_length=1)
    strategies: list[StrategyInfo]
    scenarios: list[ScenarioSpec]
    meta: dict[str, object] = Field(default_factory=dict)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

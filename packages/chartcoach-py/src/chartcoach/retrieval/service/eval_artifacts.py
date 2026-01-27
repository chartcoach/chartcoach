from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable, Sequence
from datetime import datetime, timezone
from os import PathLike
from pathlib import Path
from typing import Any

import obstore
import yaml
from obstore.store import ObjectStore
from pydantic import BaseModel, ConfigDict, Field

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.service.retrieval_service import RetrievalService
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.types import (
    ContextItem,
    ImageItem,
    RetrievalRequest,
    TextItem,
)


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
    provenance: ScenarioProvenance | None = None


class ScenariosFile(_EvalArtifactsBaseModel):
    scenarios: list[ScenarioSpec]


class EvalGuidelineResult(_EvalArtifactsBaseModel):
    rank: int = Field(ge=1)
    score: float = Field(gt=0)
    entry: CatalogEntry


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


class EvalArtifactsIndexArtifact(_EvalArtifactsBaseModel):
    schema_version: int = Field(default=ARTIFACT_SCHEMA_VERSION, frozen=True)
    generated_at: str = Field(min_length=1)
    strategies: list[StrategyInfo]
    scenarios: list[ScenarioSpec]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_scenarios(path: str | PathLike[str]) -> list[ScenarioSpec]:
    doc = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    parsed = ScenariosFile.model_validate(doc)
    return parsed.scenarios


def build_retrieval_request(
    scenario: ScenarioSpec, *, k: int | None
) -> RetrievalRequest:
    lang = scenario.lang or "en"
    context: list[ContextItem] = []

    if scenario.chart and scenario.chart.uri:
        context.append(
            ImageItem(role="chart", uri=scenario.chart.uri, mime=scenario.chart.mime)
        )

    situation = (scenario.designer_intent or "").strip()
    if not situation:
        raise ValueError(f"Scenario {scenario.id!r} is missing designer_intent.")

    context.append(TextItem(role="situation", text=situation, lang=lang))
    context.append(TextItem(role="chart_spec", text="{}", lang=lang))

    query = (scenario.query or "").strip()
    if query:
        context.append(TextItem(role="query", text=query, lang=lang))

    return RetrievalRequest(
        context=context,
        lang=lang,
        meta={"scenarioId": scenario.id},
        k=k,
    )


def compute_digest(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def build_bundle_digest(
    *,
    scenario: ScenarioSpec,
    catalog_uri: str,
    strategy_ids: list[str],
    k: int | None,
) -> str:
    return compute_digest(
        {
            "scenario": scenario.model_dump(mode="json"),
            "catalog_uri": catalog_uri,
            "strategy_ids": strategy_ids,
            "k": k,
        }
    )


def entry_score(index: int, total: int) -> float:
    denom = max(1, total)
    return max(0.01, 1.0 - (index / denom))


def build_strategy_result(
    *,
    strategy_info: StrategyInfo,
    response_catalog_entries: list[CatalogEntry],
    response_meta: dict[str, object],
) -> EvalStrategyResult:
    total = len(response_catalog_entries)
    guidelines = [
        EvalGuidelineResult(
            rank=index + 1,
            score=entry_score(index, total),
            entry=entry,
        )
        for index, entry in enumerate(response_catalog_entries)
    ]

    return EvalStrategyResult(
        strategy_id=strategy_info.id,
        strategy_name=strategy_info.name,
        meta=response_meta,
        guidelines=guidelines,
    )


def build_scenario_bundle(
    *,
    scenario: ScenarioSpec,
    catalog_uri: str,
    strategies: list[tuple[StrategyInfo, RetrievalStrategy]],
    k: int | None,
) -> EvalScenarioBundleArtifact:
    strategy_ids = [strategy_info.id for strategy_info, _strategy in strategies]
    digest = build_bundle_digest(
        scenario=scenario,
        catalog_uri=catalog_uri,
        strategy_ids=strategy_ids,
        k=k,
    )

    request = build_retrieval_request(scenario, k=k)
    results: list[EvalStrategyResult] = []
    for strategy_info, strategy in strategies:
        try:
            response = strategy(request=request)
        except Exception as e:  # noqa: BLE001
            results.append(
                EvalStrategyResult(
                    strategy_id=strategy_info.id,
                    strategy_name=strategy_info.name,
                    meta={"error": str(e)},
                    guidelines=[],
                )
            )
            continue

        results.append(
            build_strategy_result(
                strategy_info=strategy_info,
                response_catalog_entries=response.catalog.entries,
                response_meta=response.meta,
            )
        )

    return EvalScenarioBundleArtifact(
        generated_at=now_iso(),
        digest=digest,
        scenario=scenario,
        strategies=results,
    )


def read_json(store: ObjectStore, path: str) -> dict[str, Any] | None:
    try:
        result = obstore.get(store, path)
    except FileNotFoundError:
        return None

    raw = bytes(result.bytes()).decode("utf-8")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object at {path!r}.")
    return value


def write_json(store: ObjectStore, path: str, value: dict[str, Any]) -> None:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    obstore.put(store, path, data)


def list_paths(store: ObjectStore, *, prefix: str) -> list[str]:
    items = obstore.list(store, prefix=prefix).collect()
    return [item["path"] for item in items if isinstance(item.get("path"), str)]


def delete_paths(store: ObjectStore, paths: Iterable[str]) -> None:
    normalized = [p for p in paths if p]
    if not normalized:
        return
    obstore.delete(store, normalized)


class EvalArtifactsService:
    def __init__(self, *, store: ObjectStore, retrieval: RetrievalService) -> None:
        self._store = store
        self._retrieval = retrieval

    def purge(self, *, prefix: str = "") -> int:
        paths = list_paths(self._store, prefix=prefix)
        delete_paths(self._store, paths)
        return len(paths)

    def run(
        self,
        *,
        scenarios_path: Path,
        catalog_uri: str,
        strategy_ids: Sequence[str] | None,
        k: int | None,
    ) -> None:
        scenarios = load_scenarios(scenarios_path)

        strategies = self._retrieval.instantiate_strategies(
            catalog_uri=catalog_uri, strategy_ids=strategy_ids
        )
        # strategy ids are needed for stable digests even when some scenarios are skipped
        resolved_strategy_ids = [info.id for info, _strategy in strategies]

        for scenario in scenarios:
            digest = build_bundle_digest(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategy_ids=resolved_strategy_ids,
                k=k,
            )
            bundle_path = f"bundles/{scenario.id}.json"
            existing = read_json(self._store, bundle_path)
            if existing and existing.get("digest") == digest:
                continue

            bundle = build_scenario_bundle(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategies=strategies,
                k=k,
            )
            write_json(self._store, bundle_path, bundle.model_dump(mode="json"))

        index = EvalArtifactsIndexArtifact(
            generated_at=now_iso(),
            strategies=[info for info, _strategy in strategies],
            scenarios=scenarios,
        )
        write_json(self._store, "index.json", index.model_dump(mode="json"))

from __future__ import annotations

import hashlib
import json
import os
import signal
import threading
import time
from collections.abc import Iterable, Sequence
from contextlib import contextmanager
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
# Agentic retrieval strategies can take a few minutes depending on the LM,
# tool-call budget, and upstream provider latency. Keep a conservative default,
# but allow overrides via CHARTCOACH_STRATEGY_TIMEOUT_SECONDS.
DEFAULT_STRATEGY_TIMEOUT_SECONDS = 600.0


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
    meta: dict[str, object] = Field(default_factory=dict)


class EvalArtifactsIndexArtifact(_EvalArtifactsBaseModel):
    schema_version: int = Field(default=ARTIFACT_SCHEMA_VERSION, frozen=True)
    generated_at: str = Field(min_length=1)
    strategies: list[StrategyInfo]
    scenarios: list[ScenarioSpec]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _resolve_strategy_timeout_seconds() -> float | None:
    raw = (os.environ.get("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS") or "").strip()
    if not raw:
        return DEFAULT_STRATEGY_TIMEOUT_SECONDS
    try:
        value = float(raw)
    except ValueError:
        return DEFAULT_STRATEGY_TIMEOUT_SECONDS
    if value <= 0:
        return None
    return max(1.0, value)


class _StrategyTimeout(BaseException):
    pass


@contextmanager
def _timeout(seconds: float | None, *, message: str):
    if seconds is None or seconds <= 0:
        yield
        return

    if (
        not hasattr(signal, "SIGALRM")
        or not hasattr(signal, "setitimer")
        or threading.current_thread() is not threading.main_thread()
    ):
        yield
        return

    def _handler(_signum: int, _frame: object | None) -> None:
        raise _StrategyTimeout(message)

    old_handler = signal.getsignal(signal.SIGALRM)
    old_timer = signal.getitimer(signal.ITIMER_REAL)
    signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, old_timer[0], old_timer[1])
        signal.signal(signal.SIGALRM, old_handler)


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

    title = (scenario.title or "").strip()
    if title:
        context.append(TextItem(role="title", text=title, lang=lang))

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
    config: dict[str, object] | None = None,
) -> str:
    return compute_digest(
        {
            "scenario": scenario.model_dump(mode="json"),
            "catalog_uri": catalog_uri,
            "strategy_ids": strategy_ids,
            "k": k,
            "config": config or {},
        }
    )


def resolve_artifacts_config() -> dict[str, object]:
    """Resolve a non-secret configuration snapshot for digesting + debugging."""

    from dataclasses import asdict

    from chartcoach.retrieval.strategy.pipelines.guideline_status import (
        guideline_status_config_from_env,
    )
    from chartcoach.retrieval.strategy.pipelines.vision import chart_vision_config_from_env

    status_cfg = guideline_status_config_from_env()
    vision_cfg = chart_vision_config_from_env()

    return {
        "strategy_lm_model": os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL") or "gpt-5.1",
        "strategy_vlm_model": os.environ.get("CHARTCOACH_STRATEGY_VLM_MODEL") or "gpt-5.2",
        "guideline_status_lm_model": os.environ.get("CHARTCOACH_GUIDELINE_STATUS_LM_MODEL")
        or os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL")
        or "gpt-5.1",
        "guideline_status_timeout_seconds": os.environ.get(
            "CHARTCOACH_GUIDELINE_STATUS_TIMEOUT_SECONDS"
        )
        or os.environ.get("CHARTCOACH_LM_TIMEOUT_SECONDS")
        or "120",
        "guideline_status_num_retries": os.environ.get(
            "CHARTCOACH_GUIDELINE_STATUS_NUM_RETRIES"
        )
        or os.environ.get("CHARTCOACH_LM_NUM_RETRIES")
        or "6",
        "lm_timeout_seconds": os.environ.get("CHARTCOACH_LM_TIMEOUT_SECONDS") or "120",
        "lm_num_retries": os.environ.get("CHARTCOACH_LM_NUM_RETRIES") or "6",
        "vlm_timeout_seconds": os.environ.get("CHARTCOACH_VLM_TIMEOUT_SECONDS")
        or os.environ.get("CHARTCOACH_LM_TIMEOUT_SECONDS")
        or "120",
        "vlm_num_retries": os.environ.get("CHARTCOACH_VLM_NUM_RETRIES")
        or os.environ.get("CHARTCOACH_LM_NUM_RETRIES")
        or "6",
        "embedding_model": os.environ.get("CHARTCOACH_EMBEDDING_MODEL")
        or "BAAI/bge-small-en-v1.5",
        "embedding_projector": os.environ.get("CHARTCOACH_EMBEDDING_PROJECTOR")
        or "sentence_transformers",
        "strategy_timeout_seconds": _resolve_strategy_timeout_seconds(),
        "chart_vision": asdict(vision_cfg),
        "guideline_status": asdict(status_cfg),
        "query_fusion": {
            "n_queries": os.environ.get("CHARTCOACH_FUSION_N_QUERIES") or "4",
            "rrf_k": os.environ.get("CHARTCOACH_FUSION_RRF_K") or "60",
            "cross_encoder_model": os.environ.get("CHARTCOACH_FUSION_CROSS_ENCODER_MODEL")
            or "cross-encoder/ms-marco-TinyBERT-L-6",
            "cross_encoder_candidate_limit": os.environ.get("CHARTCOACH_FUSION_XENC_CANDIDATES")
            or "80",
        },
        "facet_fusion": {
            "n_queries": os.environ.get("CHARTCOACH_FACET_FUSION_N_QUERIES") or "5",
            "rrf_k": os.environ.get("CHARTCOACH_FACET_FUSION_RRF_K") or "60",
            "cross_encoder_model": os.environ.get(
                "CHARTCOACH_FACET_FUSION_CROSS_ENCODER_MODEL"
            )
            or "cross-encoder/ms-marco-TinyBERT-L-6",
            "cross_encoder_candidate_limit": os.environ.get(
                "CHARTCOACH_FACET_FUSION_XENC_CANDIDATES"
            )
            or "80",
        },
    }


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

    meta = dict(response_meta)
    # `score` is currently a rank-derived placeholder, not a calibrated confidence.
    meta.setdefault("score_kind", "rank_normalized")

    return EvalStrategyResult(
        strategy_id=strategy_info.id,
        strategy_name=strategy_info.name,
        meta=meta,
        guidelines=guidelines,
    )


def build_scenario_bundle(
    *,
    scenario: ScenarioSpec,
    catalog_uri: str,
    strategies: list[tuple[StrategyInfo, RetrievalStrategy]],
    k: int | None,
    config: dict[str, object] | None = None,
) -> EvalScenarioBundleArtifact:
    strategy_timeout_seconds = _resolve_strategy_timeout_seconds()
    strategy_ids = [strategy_info.id for strategy_info, _strategy in strategies]
    digest = build_bundle_digest(
        scenario=scenario,
        catalog_uri=catalog_uri,
        strategy_ids=strategy_ids,
        k=k,
        config=config,
    )

    request = build_retrieval_request(scenario, k=k)
    bundle_meta: dict[str, object] = {"config": config or {}}
    results: list[EvalStrategyResult] = []

    for strategy_info, strategy in strategies:
        usage_snapshots = {
            "lm_usage": _get_strategy_lm_history_snapshot(strategy, attr="_lm"),
            "vlm_usage": _get_strategy_lm_history_snapshot(strategy, attr="_vlm"),
            "status_lm_usage": _get_strategy_lm_history_snapshot(
                strategy, attr="_status_lm"
            ),
        }
        started = time.perf_counter()
        try:
            with _timeout(
                strategy_timeout_seconds,
                message=(
                    f"Timed out running strategy {strategy_info.id!r} for scenario"
                    f" {scenario.id!r} after {strategy_timeout_seconds:.0f}s."
                ),
            ):
                response = strategy(request=request)
        except _StrategyTimeout as e:
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            results.append(
                EvalStrategyResult(
                    strategy_id=strategy_info.id,
                    strategy_name=strategy_info.name,
                    meta={"error": str(e), "elapsed_ms": elapsed_ms},
                    guidelines=[],
                )
            )
            continue
        except Exception as e:  # noqa: BLE001
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            results.append(
                EvalStrategyResult(
                    strategy_id=strategy_info.id,
                    strategy_name=strategy_info.name,
                    meta={"error": str(e), "elapsed_ms": elapsed_ms},
                    guidelines=[],
                )
            )
            continue

        elapsed_ms = int((time.perf_counter() - started) * 1000)
        response_meta = dict(response.meta)
        response_meta.setdefault("elapsed_ms", elapsed_ms)

        for key, (lm, before_len) in usage_snapshots.items():
            if lm is None or before_len is None:
                continue
            response_meta.setdefault(
                key,
                _extract_lm_usage_delta(lm=lm, before_len=before_len),
            )
        results.append(
            build_strategy_result(
                strategy_info=strategy_info,
                response_catalog_entries=list(response.catalog.entries),
                response_meta=response_meta,
            )
        )

    return EvalScenarioBundleArtifact(
        generated_at=now_iso(),
        digest=digest,
        scenario=scenario,
        strategies=results,
        meta=bundle_meta,
    )


def _get_strategy_lm_history_snapshot(
    strategy: RetrievalStrategy, *, attr: str
) -> tuple[object | None, int | None]:
    lm = getattr(strategy, attr, None)
    history = getattr(lm, "history", None)
    if not isinstance(history, list):
        return None, None
    return lm, len(history)


def _extract_lm_usage_delta(*, lm: object, before_len: int) -> dict[str, object]:
    history = getattr(lm, "history", None)
    if not isinstance(history, list):
        return {}

    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0
    cost_usd = 0.0
    has_cost = False
    calls = 0

    for entry in history[before_len:]:
        if not isinstance(entry, dict):
            continue
        calls += 1

        usage = entry.get("usage")
        if isinstance(usage, dict):
            prompt_tokens += int(usage.get("prompt_tokens") or 0)
            completion_tokens += int(usage.get("completion_tokens") or 0)
            total_tokens += int(usage.get("total_tokens") or 0)

        cost = entry.get("cost")
        if isinstance(cost, (int, float)):
            cost_usd += float(cost)
            has_cost = True

    out: dict[str, object] = {
        "calls": calls,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
    }
    if has_cost:
        out["cost_usd"] = cost_usd
    return out


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

    @staticmethod
    def _bundle_has_errors(bundle: dict[str, Any]) -> bool:
        strategies = bundle.get("strategies")
        if not isinstance(strategies, list):
            return False
        for strategy in strategies:
            if not isinstance(strategy, dict):
                continue
            meta = strategy.get("meta")
            if isinstance(meta, dict) and meta.get("error"):
                return True
        return False

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
        config = resolve_artifacts_config()

        for scenario in scenarios:
            digest = build_bundle_digest(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategy_ids=resolved_strategy_ids,
                k=k,
                config=config,
            )
            bundle_path = f"bundles/{scenario.id}.json"
            existing = read_json(self._store, bundle_path)
            if (
                existing
                and existing.get("digest") == digest
                and not self._bundle_has_errors(existing)
            ):
                continue

            bundle = build_scenario_bundle(
                scenario=scenario,
                catalog_uri=catalog_uri,
                strategies=strategies,
                k=k,
                config=config,
            )
            write_json(self._store, bundle_path, bundle.model_dump(mode="json"))

        index = EvalArtifactsIndexArtifact(
            generated_at=now_iso(),
            strategies=[info for info, _strategy in strategies],
            scenarios=scenarios,
        )
        write_json(self._store, "index.json", index.model_dump(mode="json"))

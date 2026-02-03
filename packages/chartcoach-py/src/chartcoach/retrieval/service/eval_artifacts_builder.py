from __future__ import annotations

import signal
import threading
import time
from contextlib import contextmanager
from os import PathLike
from pathlib import Path
from typing import Callable, ContextManager

import yaml
from pydantic import ValidationError

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.trace import StrategyTrace
from chartcoach.retrieval.service.eval_artifacts_digests import build_bundle_digest
from chartcoach.retrieval.service.eval_artifacts_schema import (
    EvalArtifactsIndexArtifact,
    EvalEvidenceSnippet,
    EvalGuidelineResult,
    EvalScenarioBundleArtifact,
    EvalStrategyResult,
    ScenariosFile,
    ScenarioSpec,
    now_iso,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.types import (
    ContextItem,
    ImageItem,
    RetrievalRequest,
    TextItem,
)


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


def _default_timeout_cm(seconds: float | None, message: str) -> ContextManager[None]:
    return _timeout(seconds, message=message)


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

    context.append(TextItem(role="intent", text=situation, lang=lang))
    context.append(TextItem(role="chart_spec", text="{}", lang=lang))

    for role, value in (
        ("audience", scenario.audience),
        ("medium", scenario.medium),
        ("constraints", scenario.constraints),
        ("domain", scenario.domain),
        ("risk_tolerance", scenario.risk_tolerance),
        ("time_budget", scenario.time_budget),
    ):
        text = (value or "").strip()
        if text:
            context.append(TextItem(role=role, text=text, lang=lang))

    query = (scenario.query or "").strip()
    if query:
        context.append(TextItem(role="query", text=query, lang=lang))

    return RetrievalRequest(
        context=context,
        lang=lang,
        meta={"scenarioId": scenario.id},
        k=k,
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

    try:
        trace = StrategyTrace.model_validate(response_meta)
    except ValidationError as e:
        raise ValueError(
            f"Strategy meta for {strategy_info.id!r} did not match the trace schema."
        ) from e
    hit_evidence: dict[str, list[EvalEvidenceSnippet]] = {}
    for hit in trace.hits:
        if not hit.evidence:
            continue
        hit_evidence[hit.id] = [
            EvalEvidenceSnippet(
                role=snippet.role, text=snippet.text, score=snippet.score
            )
            for snippet in hit.evidence
        ]

    guidelines = [
        EvalGuidelineResult(
            rank=index + 1,
            score=entry_score(index, total),
            entry=entry,
            evidence=hit_evidence.get(entry.id) or None,
        )
        for index, entry in enumerate(response_catalog_entries)
    ]

    meta = dict(trace.model_dump(mode="json", exclude_none=True))
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
    strategy_timeout_seconds: float | None,
    config: dict[str, object] | None = None,
    _timeout_cm: Callable[
        [float | None, str], ContextManager[None]
    ] = _default_timeout_cm,
    _timeout_exc: type[BaseException] = _StrategyTimeout,
) -> EvalScenarioBundleArtifact:
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
    for key in ("repo_commit", "catalog_digest", "scenario_digest"):
        if config and key in config:
            bundle_meta.setdefault(key, config[key])
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
            timeout_desc = (
                "no-timeout"
                if strategy_timeout_seconds is None
                else f"{strategy_timeout_seconds:.0f}s"
            )
            message = (
                f"Timed out running strategy {strategy_info.id!r} for scenario"
                f" {scenario.id!r} after {timeout_desc}."
            )
            with _timeout_cm(strategy_timeout_seconds, message):
                response = strategy(request=request)
        except _timeout_exc as e:
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
    strategy: RetrievalStrategy, *, attr: str = "_lm"
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


def build_artifacts_index(
    *,
    scenarios: list[ScenarioSpec],
    strategies: list[tuple[StrategyInfo, RetrievalStrategy]],
    config: dict[str, object],
    runtime_env: dict[str, object] | None = None,
) -> EvalArtifactsIndexArtifact:
    return EvalArtifactsIndexArtifact(
        generated_at=now_iso(),
        strategies=[info for info, _strategy in strategies],
        scenarios=scenarios,
        meta={
            "config": config,
            "runtime_env": runtime_env or {},
            "repo_commit": config.get("repo_commit"),
            "catalog_digest": config.get("catalog_digest"),
            "scenario_digest": config.get("scenario_digest"),
        },
    )

from __future__ import annotations

import subprocess
from pathlib import Path

from chartcoach.retrieval.config import RetrievalRunConfig
from chartcoach.retrieval.service import eval_artifacts_builder as _builder
from chartcoach.retrieval.service.eval_artifacts_builder import (
    _StrategyTimeout,
    _timeout,
    _extract_lm_usage_delta,
    _get_strategy_lm_history_snapshot,
    build_retrieval_request,
    build_strategy_result,
    entry_score,
    load_scenarios,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.service.eval_artifacts_digests import (
    build_bundle_digest,
    compute_digest,
    resolve_catalog_digest,
    resolve_scenarios_digest,
)
from chartcoach.retrieval.service.eval_artifacts_schema import (
    ARTIFACT_SCHEMA_VERSION,
    EvalArtifactsIndexArtifact,
    EvalEvidenceSnippet,
    EvalGuidelineResult,
    EvalScenarioBundleArtifact,
    EvalStrategyResult,
    ScenarioChart,
    ScenarioProvenance,
    ScenarioSpec,
    ScenariosFile,
    now_iso,
)
from chartcoach.retrieval.service.eval_artifacts_service import EvalArtifactsService
from chartcoach.retrieval.service.eval_artifacts_store import (
    delete_paths,
    list_paths,
    read_json,
    write_json,
)


def _find_repo_root(start: Path) -> Path | None:
    """Walk up from `start` to find a git repo root (directory containing `.git`)."""

    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    return None


def _run_git(args: list[str], *, cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def resolve_repo_commit() -> str:
    """Best-effort git commit identifier for reproducibility metadata."""

    repo_root = _find_repo_root(Path.cwd()) or _find_repo_root(Path(__file__).resolve())
    if repo_root is None:
        return "unknown"

    commit = _run_git(["rev-parse", "HEAD"], cwd=repo_root)
    if not commit:
        return "unknown"

    dirty = False
    # Treat both staged and unstaged changes as "dirty".
    for cmd in (["diff", "--quiet"], ["diff", "--cached", "--quiet"]):
        try:
            proc = subprocess.run(
                ["git", *cmd],
                cwd=str(repo_root),
                check=False,
                capture_output=True,
            )
        except OSError:
            proc = None
        if proc is not None and proc.returncode != 0:
            dirty = True
            break

    short = commit[:12]
    return f"{short}-dirty" if dirty else short


def resolve_artifacts_config(*, run_config: RetrievalRunConfig) -> dict[str, object]:
    """Resolve a non-secret configuration snapshot for digesting + debugging."""

    return {
        "repo_commit": resolve_repo_commit(),
        **run_config.public_dict(),
    }


def build_scenario_bundle(
    *,
    scenario: ScenarioSpec,
    catalog_uri: str,
    strategies: list[tuple[StrategyInfo, RetrievalStrategy]],
    k: int | None,
    strategy_timeout_seconds: float | None,
    config: dict[str, object] | None = None,
) -> EvalScenarioBundleArtifact:
    def _timeout_cm(seconds: float | None, message: str):  # noqa: ANN001
        return _timeout(seconds, message=message)

    return _builder.build_scenario_bundle(
        scenario=scenario,
        catalog_uri=catalog_uri,
        strategies=strategies,
        k=k,
        strategy_timeout_seconds=strategy_timeout_seconds,
        config=config,
        _timeout_cm=_timeout_cm,
        _timeout_exc=_StrategyTimeout,
    )


__all__ = [
    "ARTIFACT_SCHEMA_VERSION",
    "EvalArtifactsIndexArtifact",
    "EvalArtifactsService",
    "EvalEvidenceSnippet",
    "EvalGuidelineResult",
    "EvalScenarioBundleArtifact",
    "EvalStrategyResult",
    "ScenarioChart",
    "ScenarioProvenance",
    "ScenarioSpec",
    "ScenariosFile",
    "build_bundle_digest",
    "build_retrieval_request",
    "build_scenario_bundle",
    "build_strategy_result",
    "compute_digest",
    "delete_paths",
    "entry_score",
    "list_paths",
    "load_scenarios",
    "now_iso",
    "read_json",
    "resolve_artifacts_config",
    "resolve_catalog_digest",
    "resolve_repo_commit",
    "resolve_scenarios_digest",
    "write_json",
    "_StrategyTimeout",
    "_extract_lm_usage_delta",
    "_find_repo_root",
    "_get_strategy_lm_history_snapshot",
    "_run_git",
    "_timeout",
]

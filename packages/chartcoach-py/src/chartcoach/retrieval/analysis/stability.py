from __future__ import annotations

import json
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import cast


@dataclass(frozen=True, slots=True)
class StabilityResult:
    """Aggregate stability metrics for one strategy across multiple runs."""

    strategy_id: str
    mean_jaccard: float
    scenarios: dict[str, float]


def _pairwise_jaccard(sets: Sequence[set[str]]) -> float:
    if len(sets) <= 1:
        return 1.0

    total = 0.0
    pairs = 0
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            denom = len(a | b)
            score = (len(a & b) / denom) if denom else 1.0
            total += score
            pairs += 1
    return total / max(1, pairs)


def _extract_guideline_id(entry: Mapping[str, object] | None) -> str | None:
    if not entry:
        return None
    guideline = entry.get("guideline")
    if isinstance(guideline, dict):
        gid = cast("dict[str, object]", guideline).get("id")
        return gid if isinstance(gid, str) and gid else None
    gid = entry.get("id")
    return gid if isinstance(gid, str) and gid else None


def load_run_bundle_sets(
    *, artifacts_root: Path, k: int | None = None
) -> dict[str, dict[str, list[str]]]:
    """Load per-scenario per-strategy top-k guideline ids from an artifacts directory."""

    bundles_dir = artifacts_root / "bundles"
    if not bundles_dir.exists():
        raise FileNotFoundError(f"Missing bundles/ under {artifacts_root}")

    out: dict[str, dict[str, list[str]]] = {}
    for bundle_path in sorted(bundles_dir.glob("*.json")):
        doc = json.loads(bundle_path.read_text(encoding="utf-8"))
        scenario = doc.get("scenario")
        if not isinstance(scenario, dict):
            continue
        scenario_id = scenario.get("id")
        if not isinstance(scenario_id, str) or not scenario_id:
            continue
        strategies = doc.get("strategies")
        if not isinstance(strategies, list):
            continue

        scenario_map: dict[str, list[str]] = {}
        for strategy in strategies:
            if not isinstance(strategy, dict):
                continue
            strategy_id = strategy.get("strategy_id")
            if not isinstance(strategy_id, str) or not strategy_id:
                continue
            results = strategy.get("guidelines")
            if not isinstance(results, list):
                continue
            ids: list[str] = []
            for row in results[: (int(k) if k is not None else None)]:
                if not isinstance(row, dict):
                    continue
                entry = row.get("entry")
                if not isinstance(entry, dict):
                    continue
                gid = _extract_guideline_id(entry)
                if gid:
                    ids.append(gid)
            scenario_map[strategy_id] = ids

        out[scenario_id] = scenario_map
    return out


def compute_stability(
    *,
    runs: Sequence[Path],
    k: int | None = None,
) -> list[StabilityResult]:
    """Compute mean pairwise Jaccard overlap across runs for each strategy."""

    if len(runs) < 2:
        raise ValueError("Need at least 2 runs to compute stability.")

    loaded = [load_run_bundle_sets(artifacts_root=r, k=k) for r in runs]

    # Collect all scenario ids present in all runs (intersection).
    scenario_ids: set[str] = set.intersection(*(set(run.keys()) for run in loaded))
    if not scenario_ids:
        return []

    # Collect strategy ids present in all runs for those scenarios.
    strategy_ids: set[str] = set()
    for sid in scenario_ids:
        per_run_ids = [set(run[sid].keys()) for run in loaded]
        strategy_ids |= set.intersection(*per_run_ids)

    results: list[StabilityResult] = []
    for strategy_id in sorted(strategy_ids):
        per_scenario: dict[str, float] = {}
        for sid in sorted(scenario_ids):
            sets = []
            for run in loaded:
                ids = run.get(sid, {}).get(strategy_id)
                if ids is None:
                    break
                sets.append(set(ids))
            if len(sets) != len(runs):
                continue
            per_scenario[sid] = _pairwise_jaccard(sets)

        mean = sum(per_scenario.values()) / max(1, len(per_scenario))
        results.append(
            StabilityResult(
                strategy_id=strategy_id, mean_jaccard=mean, scenarios=per_scenario
            )
        )
    return sorted(results, key=lambda r: (-r.mean_jaccard, r.strategy_id))


def format_stability_table(results: Iterable[StabilityResult]) -> str:
    rows = list(results)
    if not rows:
        return "No overlapping strategies/scenarios found across runs."

    lines = [
        "| strategy | mean_jaccard |",
        "|---|---:|",
    ]
    for row in rows:
        lines.append(f"| {row.strategy_id} | {row.mean_jaccard:.3f} |")
    return "\n".join(lines)

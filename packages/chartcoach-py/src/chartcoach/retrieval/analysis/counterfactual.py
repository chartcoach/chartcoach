from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

from chartcoach.retrieval.analysis.stability import load_run_bundle_sets


@dataclass(frozen=True, slots=True)
class CounterfactualSensitivityResult:
    """How much a strategy's top-k set changes across counterfactual variants."""

    strategy_id: str
    mean_jaccard: float
    groups: dict[str, float]


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


def load_counterfactual_groups(*, artifacts_root: Path) -> dict[str, list[str]]:
    """Return mapping counterfactual_group_id -> scenario ids from index.json."""

    index_path = artifacts_root / "index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing index.json under {artifacts_root}")

    doc = json.loads(index_path.read_text(encoding="utf-8"))
    scenarios = doc.get("scenarios")
    if not isinstance(scenarios, list):
        return {}

    groups: dict[str, list[str]] = defaultdict(list)
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            continue
        sid = scenario.get("id")
        gid = scenario.get("counterfactual_group_id")
        if not isinstance(sid, str) or not sid:
            continue
        if not isinstance(gid, str) or not gid:
            continue
        groups[gid].append(sid)

    return {gid: sorted(ids) for gid, ids in groups.items() if len(ids) >= 2}


def compute_counterfactual_sensitivity(
    *,
    artifacts_root: Path,
    k: int | None = None,
) -> list[CounterfactualSensitivityResult]:
    """Compute set overlap across counterfactual scenario groups for each strategy."""

    groups = load_counterfactual_groups(artifacts_root=artifacts_root)
    if not groups:
        return []

    results = load_run_bundle_sets(artifacts_root=artifacts_root, k=k)

    # Strategy ids present in all scenarios for a group can vary; take union then compute per-group.
    strategy_ids: set[str] = set()
    for scenarios in groups.values():
        for sid in scenarios:
            strategy_ids |= set((results.get(sid) or {}).keys())

    out: list[CounterfactualSensitivityResult] = []
    for strategy_id in sorted(strategy_ids):
        per_group: dict[str, float] = {}
        for group_id, scenario_ids in groups.items():
            sets: list[set[str]] = []
            for sid in scenario_ids:
                ids = results.get(sid, {}).get(strategy_id)
                if ids is None:
                    sets = []
                    break
                sets.append(set(ids))
            if not sets:
                continue
            per_group[group_id] = _pairwise_jaccard(sets)

        if not per_group:
            continue
        mean = sum(per_group.values()) / max(1, len(per_group))
        out.append(
            CounterfactualSensitivityResult(
                strategy_id=strategy_id,
                mean_jaccard=mean,
                groups=per_group,
            )
        )

    return sorted(out, key=lambda r: (r.mean_jaccard, r.strategy_id))


def format_counterfactual_table(
    results: Iterable[CounterfactualSensitivityResult],
) -> str:
    rows = list(results)
    if not rows:
        return "No counterfactual groups found."

    lines = [
        "| strategy | mean_overlap (Jaccard) |",
        "|---|---:|",
    ]
    for row in rows:
        lines.append(f"| {row.strategy_id} | {row.mean_jaccard:.3f} |")
    return "\n".join(lines)

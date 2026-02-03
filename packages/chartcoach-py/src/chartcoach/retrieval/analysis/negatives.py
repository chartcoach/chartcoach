from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from chartcoach.retrieval.analysis.stability import load_run_bundle_sets


@dataclass(frozen=True, slots=True)
class NegativeHitRateResult:
    """How often a strategy retrieves known negative/distractor guidelines."""

    strategy_id: str
    mean_negative_fraction: float
    any_negative_fraction: float
    scenarios: dict[str, float]


def load_negative_guideline_ids(*, artifacts_root: Path) -> dict[str, set[str]]:
    """Return mapping scenario_id -> negative guideline ids from index.json."""

    index_path = artifacts_root / "index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing index.json under {artifacts_root}")

    doc = json.loads(index_path.read_text(encoding="utf-8"))
    scenarios = doc.get("scenarios")
    if not isinstance(scenarios, list):
        return {}

    out: dict[str, set[str]] = {}
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            continue
        sid = scenario.get("id")
        if not isinstance(sid, str) or not sid:
            continue
        raw = scenario.get("negative_guideline_ids")
        if not isinstance(raw, list):
            continue
        neg: set[str] = set()
        for item in raw:
            if isinstance(item, str):
                gid = item.strip()
                if gid:
                    neg.add(gid)
        if neg:
            out[sid] = neg

    return out


def compute_negative_hit_rates(
    *,
    artifacts_root: Path,
    k: int | None = None,
) -> list[NegativeHitRateResult]:
    """Compute negative-hit rates per strategy for scenarios that define negatives."""

    negatives = load_negative_guideline_ids(artifacts_root=artifacts_root)
    if not negatives:
        return []

    results = load_run_bundle_sets(artifacts_root=artifacts_root, k=k)

    # Collect all strategies present anywhere in the run.
    strategy_ids: set[str] = set()
    for scenario_map in results.values():
        strategy_ids |= set(scenario_map.keys())

    out: list[NegativeHitRateResult] = []
    for strategy_id in sorted(strategy_ids):
        per_scenario: dict[str, float] = {}
        any_hits = 0
        counted = 0

        for scenario_id, neg_ids in negatives.items():
            ids = (results.get(scenario_id) or {}).get(strategy_id)
            if ids is None:
                continue
            denom = max(1, len(ids))
            frac = len(set(ids) & set(neg_ids)) / denom
            per_scenario[scenario_id] = frac
            counted += 1
            if frac > 0:
                any_hits += 1

        if not per_scenario:
            continue

        mean_frac = sum(per_scenario.values()) / max(1, len(per_scenario))
        out.append(
            NegativeHitRateResult(
                strategy_id=strategy_id,
                mean_negative_fraction=mean_frac,
                any_negative_fraction=any_hits / max(1, counted),
                scenarios=per_scenario,
            )
        )

    # Lower is better: fewer negative hits.
    return sorted(out, key=lambda r: (r.mean_negative_fraction, r.strategy_id))


def format_negative_hit_table(results: Iterable[NegativeHitRateResult]) -> str:
    rows = list(results)
    if not rows:
        return "No negative guidelines found in index.json."

    lines = [
        "| strategy | mean_negative_frac | any_negative_frac |",
        "|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row.strategy_id} | {row.mean_negative_fraction:.3f} | {row.any_negative_fraction:.3f} |"
        )
    return "\n".join(lines)

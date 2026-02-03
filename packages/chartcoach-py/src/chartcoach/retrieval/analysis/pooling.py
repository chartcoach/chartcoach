from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from chartcoach.retrieval.analysis.stability import load_run_bundle_sets


@dataclass(frozen=True, slots=True)
class PoolCoverageResult:
    scenario_id: str
    unique_guidelines: int
    strategies: int


def compute_pool_coverage(
    *,
    artifacts_root: Path,
    k: int | None = None,
) -> list[PoolCoverageResult]:
    """Compute union-of-top-k pool size per scenario for a single artifacts run."""

    per_scenario = load_run_bundle_sets(artifacts_root=artifacts_root, k=k)
    results: list[PoolCoverageResult] = []
    for scenario_id, strat_map in sorted(per_scenario.items()):
        pool: set[str] = set()
        for ids in strat_map.values():
            pool |= set(ids)
        results.append(
            PoolCoverageResult(
                scenario_id=scenario_id,
                unique_guidelines=len(pool),
                strategies=len(strat_map),
            )
        )
    return results


def format_pool_table(results: Iterable[PoolCoverageResult]) -> str:
    rows = list(results)
    if not rows:
        return "No bundles found."

    lines = [
        "| scenario | strategies | pool_size |",
        "|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row.scenario_id} | {row.strategies} | {row.unique_guidelines} |"
        )
    return "\n".join(lines)

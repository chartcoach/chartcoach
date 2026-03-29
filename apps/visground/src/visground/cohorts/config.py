from __future__ import annotations

from .contracts import VisEvalCohortConfig, VisEvalCohortConfigOverrides


_DEFAULT_CONFIG = VisEvalCohortConfig(
    target_n=150,
    max_tasks_per_db=6,
    seed=42,
    interestingness_score_floor=1.0,
    backfill_below_floor=True,
)


def _resolve_config(
    config: VisEvalCohortConfig | VisEvalCohortConfigOverrides | None,
) -> VisEvalCohortConfig:
    if config is None:
        return VisEvalCohortConfig(**_DEFAULT_CONFIG)

    merged = {**_DEFAULT_CONFIG, **config}
    return VisEvalCohortConfig(
        target_n=int(merged["target_n"]),
        max_tasks_per_db=int(merged["max_tasks_per_db"]),
        seed=int(merged["seed"]),
        interestingness_score_floor=float(merged["interestingness_score_floor"]),
        backfill_below_floor=bool(merged["backfill_below_floor"]),
    )

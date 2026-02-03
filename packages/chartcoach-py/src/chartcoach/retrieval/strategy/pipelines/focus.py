from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Literal


FocusMode = Literal["all", "violations", "satisfied"]

_FALLBACK_ALWAYS_ROLES: set[str] = {
    "advice",
    "title",
    "description",
    "labels",
    "__dangling__",
}


@dataclass(frozen=True, slots=True)
class FocusConfig:
    mode: FocusMode = "all"
    allow_role_fallback: bool = True
    use_status_filter: bool = False


def focus_config_from_env(*, default: FocusMode = "all") -> FocusConfig:
    raw = (os.environ.get("CHARTCOACH_STRATEGY_FOCUS") or "").strip().lower()
    mode: FocusMode
    if raw in {"all", "violations", "satisfied"}:
        mode = raw  # type: ignore[assignment]
    else:
        mode = default

    fallback_raw = (
        (os.environ.get("CHARTCOACH_STRATEGY_FOCUS_ROLE_FALLBACK") or "")
        .strip()
        .lower()
    )
    allow_role_fallback = True
    if fallback_raw in {"0", "false", "f", "no", "n", "off"}:
        allow_role_fallback = False

    status_raw = (
        (os.environ.get("CHARTCOACH_STRATEGY_STATUS_FILTER") or "").strip().lower()
    )
    use_status_filter = status_raw in {"1", "true", "t", "yes", "y", "on"}

    return FocusConfig(
        mode=mode,
        allow_role_fallback=allow_role_fallback,
        use_status_filter=use_status_filter,
    )


def primary_roles_for_focus(mode: FocusMode) -> set[str] | None:
    if mode == "all":
        return None
    if mode == "violations":
        return {"fix", "mistakes", "exceptions", "check"}
    if mode == "satisfied":
        return {"check", "reason", "context"}
    return None


def fallback_roles_for_focus(mode: FocusMode) -> set[str] | None:
    primary = primary_roles_for_focus(mode)
    if primary is None:
        return None
    # When role-filtered retrieval yields empty results, broaden the candidate
    # pool to include guideline-level fields and untagged sections.
    return set(primary) | set(_FALLBACK_ALWAYS_ROLES)

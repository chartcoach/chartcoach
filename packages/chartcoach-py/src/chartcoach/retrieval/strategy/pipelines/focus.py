from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Literal


FocusMode = Literal["all", "violations", "satisfied"]


@dataclass(frozen=True, slots=True)
class FocusConfig:
    mode: FocusMode = "all"
    allow_role_fallback: bool = True


def focus_config_from_env(*, default: FocusMode = "all") -> FocusConfig:
    raw = (os.environ.get("CHARTCOACH_STRATEGY_FOCUS") or "").strip().lower()
    mode: FocusMode
    if raw in {"all", "violations", "satisfied"}:
        mode = raw  # type: ignore[assignment]
    else:
        mode = default

    fallback_raw = (os.environ.get("CHARTCOACH_STRATEGY_FOCUS_ROLE_FALLBACK") or "").strip().lower()
    allow_role_fallback = True
    if fallback_raw in {"0", "false", "f", "no", "n", "off"}:
        allow_role_fallback = False

    return FocusConfig(mode=mode, allow_role_fallback=allow_role_fallback)


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
    return set(primary) | {"advice"}


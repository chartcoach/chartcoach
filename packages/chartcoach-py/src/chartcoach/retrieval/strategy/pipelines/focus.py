from __future__ import annotations

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

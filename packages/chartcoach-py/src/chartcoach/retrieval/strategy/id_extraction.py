from __future__ import annotations

from collections.abc import Iterable
from typing import cast


def normalize_guideline_id(raw: str) -> str:
    gid = raw.strip()
    gid = gid.strip("`").strip()
    gid = gid.strip().strip(".,;:()[]{}")
    return gid


def extract_guideline_ids(
    *,
    known_ids: set[str],
    raw_used: object,
    feedback: str = "",
) -> list[str]:
    """Extract and normalize guideline ids from model output.

    DSPy programs sometimes return ids as strings, lists, sets, or object payloads
    like `[{id: "..."}]`. In addition, some programs might omit a dedicated
    `used_guideline_ids` field and only include ids inside a free-form feedback
    string. This helper centralizes parsing + filtering to known ids.
    """

    candidates: list[object]
    if isinstance(raw_used, str):
        candidates = [raw_used]
    elif isinstance(raw_used, list | tuple):
        candidates = list(raw_used)
    elif isinstance(raw_used, dict):
        candidates = [raw_used]
    elif isinstance(raw_used, Iterable):
        candidates = list(raw_used)
    else:
        candidates = []

    seen: set[str] = set()
    cleaned: list[str] = []

    def maybe_add(value: str) -> None:
        gid = normalize_guideline_id(value)
        if not gid or gid in seen:
            return
        if gid not in known_ids:
            return
        cleaned.append(gid)
        seen.add(gid)

    for item in candidates:
        if isinstance(item, str):
            maybe_add(item)
            continue
        if isinstance(item, dict):
            item_dict = cast("dict[str, object]", item)
            for key in ("id", "guideline_id", "guidelineId"):
                value = item_dict.get(key)
                if isinstance(value, str):
                    maybe_add(value)
                    break

    if not cleaned and feedback:
        positions: list[tuple[int, str]] = []
        for gid in known_ids:
            pos = feedback.find(gid)
            if pos >= 0:
                positions.append((pos, gid))
        positions.sort(key=lambda item: item[0])
        for _pos, gid in positions:
            maybe_add(gid)

    if feedback and cleaned:
        original_order = {gid: idx for idx, gid in enumerate(cleaned)}
        id_positions = {gid: feedback.find(gid) for gid in cleaned}
        cleaned.sort(
            key=lambda gid: (
                id_positions[gid] if id_positions[gid] >= 0 else 2**31 - 1,
                original_order[gid],
            )
        )

    return cleaned

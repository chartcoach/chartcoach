import re
from typing import Any

from json_repair import repair_json

_FENCE_PATTERN = re.compile(r"```(?:[\w.+-]+)?\n(.*?)\n```", re.DOTALL)


def unfence(text: str) -> list[str]:
    """Return fenced blocks, or the raw text if none exist."""
    blocks = [match.strip() for match in _FENCE_PATTERN.findall(text)]
    return blocks or [text]


def extract_json(text: str) -> dict[str, Any]:
    """Extract one JSON object from raw or fenced text."""
    blocks = unfence(text)
    if len(blocks) != 1:
        raise ValueError(f"Expected exactly one JSON block, got {len(blocks)}.")

    data = repair_json(blocks[0], return_objects=True)
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object.")

    return data


__all__ = ["extract_json", "unfence"]

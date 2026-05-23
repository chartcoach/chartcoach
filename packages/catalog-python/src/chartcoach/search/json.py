from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any


def normalize_for_json(value: Any) -> Any:
    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, datetime | date | time):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): normalize_for_json(item) for key, item in value.items()}
    if isinstance(value, tuple | list | set):
        return [normalize_for_json(item) for item in value]
    if hasattr(value, "tolist") and callable(value.tolist):
        return normalize_for_json(value.tolist())
    if hasattr(value, "item") and callable(value.item):
        return normalize_for_json(value.item())
    return str(value)


__all__ = ["normalize_for_json"]

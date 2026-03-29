from __future__ import annotations

import math
from typing import cast


def _clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(value, hi))


def _normalized_entropy(weights: list[float]) -> float:
    if len(weights) <= 1:
        return 0.0

    total = sum(weights)
    if total <= 0:
        return 0.0

    entropy = -sum(
        probability * math.log(probability)
        for probability in (weight / total for weight in weights)
        if probability > 0
    )
    return entropy / math.log(len(weights))


def _float_stat(value: object | None) -> float:
    if value is None:
        return 0.0
    return float(cast(int | float, value))

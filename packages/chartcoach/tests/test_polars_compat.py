from __future__ import annotations

from typing import cast

import polars as pl
import pytest
from chartcoach.catalog._polars import explode_expr, explode_frame


class LegacyFrame:
    def __init__(self) -> None:
        self.columns: list[str] = []

    def explode(self, column: str) -> LegacyFrame:
        self.columns.append(column)
        return self


class LegacyExpr:
    def __init__(self) -> None:
        self.calls = 0

    def explode(self) -> LegacyExpr:
        self.calls += 1
        return self


def test_explode_frame_accepts_the_legacy_polars_signature() -> None:
    legacy = LegacyFrame()

    result = explode_frame(cast(pl.DataFrame, legacy), "items")

    assert result is legacy
    assert legacy.columns == ["items"]


def test_explode_expr_accepts_the_legacy_polars_signature() -> None:
    legacy = LegacyExpr()

    result = explode_expr(cast(pl.Expr, legacy))

    assert result is legacy
    assert legacy.calls == 1


def test_explode_frame_preserves_unrelated_type_errors() -> None:
    class BrokenFrame:
        def explode(self, column: str, **_options: object) -> BrokenFrame:
            raise TypeError(f"invalid column: {column}")

    with pytest.raises(TypeError, match="invalid column"):
        explode_frame(cast(pl.DataFrame, BrokenFrame()), "items")

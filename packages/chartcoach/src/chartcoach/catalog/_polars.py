from __future__ import annotations

import polars as pl


def explode_frame(frame: pl.DataFrame, column: str) -> pl.DataFrame:
    """Explode a list column while preserving empty rows across Polars versions."""

    try:
        return frame.explode(column, empty_as_null=True)
    except TypeError as exc:
        if "empty_as_null" not in str(exc):
            raise
        return frame.explode(column)


def explode_expr(expression: pl.Expr) -> pl.Expr:
    """Explode a list expression while preserving empty rows across Polars versions."""

    try:
        return expression.explode(empty_as_null=True)
    except TypeError as exc:
        if "empty_as_null" not in str(exc):
            raise
        return expression.explode()


__all__ = ["explode_expr", "explode_frame"]

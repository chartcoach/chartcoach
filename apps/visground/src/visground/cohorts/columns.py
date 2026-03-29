from __future__ import annotations

import re

import polars as pl

_IDENTIFIER_NAME_RE = re.compile(r"(?:^|_)id$", re.IGNORECASE)


def _normalize_name(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", name.lower()).strip("_")


def _numeric_series(df: pl.DataFrame, column: str) -> pl.Series:
    return df.get_column(column).drop_nulls().cast(pl.Float64)


def _is_row_key_like(series: pl.Series) -> bool:
    if series.is_empty() or not series.dtype.is_integer():
        return False
    if series.len() < 8:
        return False

    unique_ratio = series.n_unique() / series.len()
    if unique_ratio < 0.98:
        return False

    return bool(series.is_sorted() or series.is_sorted(descending=True))


def _is_identifier_like_numeric(name: str, series: pl.Series) -> bool:
    normalized_name = _normalize_name(name)
    return bool(_IDENTIFIER_NAME_RE.search(normalized_name) or _is_row_key_like(series))


def _classify_numeric_columns(
    df: pl.DataFrame,
    numeric_cols: list[str],
) -> tuple[list[str], list[str]]:
    measure_cols: list[str] = []
    identifier_cols: list[str] = []

    for name in numeric_cols:
        series = df.get_column(name).drop_nulls()
        if series.is_empty():
            continue
        if _is_identifier_like_numeric(name, series):
            identifier_cols.append(name)
            continue
        measure_cols.append(name)

    return measure_cols, identifier_cols

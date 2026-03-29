from __future__ import annotations

import polars as pl

from .contracts import DataProfile, DataProfileFacets, DataProfileMetrics
from .profile_parts import _build_profile


def profile_dataframe(df: pl.DataFrame) -> DataProfile:
    return _build_profile(df)


def interestingness_score(profile: DataProfile) -> float:
    return profile["metrics"]["interestingness_score"]


__all__ = [
    "DataProfile",
    "DataProfileFacets",
    "DataProfileMetrics",
    "interestingness_score",
    "profile_dataframe",
]

from __future__ import annotations

from os import PathLike
from pathlib import Path

from platformdirs import user_cache_path

from .constants import DEFAULT_DUCKDB_FILENAME

APP_NAME = "chartcoach"


def default_cache_dir(*parts: str | PathLike[str]) -> Path:
    """Return the platform-native cache directory for ChartCoach artifacts."""

    return user_cache_path(APP_NAME, appauthor=False).joinpath(*parts)


def default_artifact_dir() -> Path:
    """Return the default directory for generated catalog artifacts."""

    return default_cache_dir("artifacts")


def default_duckdb_path() -> Path:
    """Return the default generated DuckDB catalog path."""

    return default_artifact_dir() / DEFAULT_DUCKDB_FILENAME


def default_index_dir() -> Path:
    """Return the default directory for generated Chroma search indexes."""

    return default_cache_dir("index")


__all__ = [
    "APP_NAME",
    "default_artifact_dir",
    "default_cache_dir",
    "default_duckdb_path",
    "default_index_dir",
]

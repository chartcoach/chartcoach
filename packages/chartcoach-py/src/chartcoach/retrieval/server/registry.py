from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import dspy
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy import RetrievalStrategy


def _catalog_from_path(path: str) -> Catalog:
    if path.endswith(".parquet"):
        return Catalog.from_df(pl.read_parquet(path))
    return Catalog.from_disk(Path(path))


def _openai_env() -> tuple[str, str]:
    api_base = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_base or not api_key:
        raise RuntimeError("Set OPENAI_BASE_URL and OPENAI_API_KEY.")
    return api_base, api_key


def create_guideline_browser_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    api_base, api_key = _openai_env()
    guideline_browser_lm = dspy.LM(model="gpt-5.2", api_base=api_base, api_key=api_key)
    return GuidelineBrowserStrategy(catalog=catalog, lm=guideline_browser_lm)


def create_default_strategies(*, catalog: Catalog) -> list[RetrievalStrategy]:
    return [create_guideline_browser_strategy(catalog=catalog)]


def create_app_from_env() -> Any:
    from chartcoach.retrieval.server.app import create_app

    catalog_path = os.environ.get("CHARTCOACH_CATALOG_PATH")
    if not catalog_path:
        raise RuntimeError(
            "Set CHARTCOACH_CATALOG_PATH to a catalog folder or .parquet file."
        )

    _openai_env()
    catalog = _catalog_from_path(catalog_path)
    strategies = create_default_strategies(catalog=catalog)
    return create_app(strategies=strategies)

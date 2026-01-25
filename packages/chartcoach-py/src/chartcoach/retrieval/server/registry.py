from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import dspy
import polars as pl

from chartcoach.catalog import Catalog


def _catalog_from_path(path: str) -> Catalog:
    if path.endswith(".parquet"):
        return Catalog.from_df(pl.read_parquet(path))
    return Catalog.from_disk(Path(path))


def create_default_strategies(*, catalog: Catalog, lm: dspy.LM) -> list[Any]:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    return [GuidelineBrowserStrategy(catalog=catalog, lm=lm)]


def create_app_from_env() -> Any:
    from chartcoach.retrieval.server.app import create_app

    catalog_path = os.environ.get("CHARTCOACH_CATALOG_PATH")
    if not catalog_path:
        raise RuntimeError(
            "Set CHARTCOACH_CATALOG_PATH to a catalog folder or .parquet file."
        )

    api_base = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_base or not api_key:
        raise RuntimeError("Set OPENAI_BASE_URL and OPENAI_API_KEY.")

    lm = dspy.LM(model="gpt-5.2", api_base=api_base, api_key=api_key)
    catalog = _catalog_from_path(catalog_path)
    strategies = create_default_strategies(catalog=catalog, lm=lm)
    return create_app(strategies=strategies)

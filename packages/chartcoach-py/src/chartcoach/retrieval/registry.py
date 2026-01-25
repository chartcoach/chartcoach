from __future__ import annotations

import os
from os import PathLike
from pathlib import Path

import dspy
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy import RetrievalStrategy


def catalog_from_path(path: str | PathLike[str]) -> Catalog:
    p = Path(path)
    if p.suffix == ".parquet":
        return Catalog.from_df(pl.read_parquet(p))
    return Catalog.from_disk(p)


def openai_env() -> tuple[str, str]:
    api_base = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_base or not api_key:
        raise RuntimeError("Set OPENAI_BASE_URL and OPENAI_API_KEY.")
    return api_base, api_key


def create_guideline_browser_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    api_base, api_key = openai_env()
    lm = dspy.LM(model="gpt-5.2", api_base=api_base, api_key=api_key)
    return GuidelineBrowserStrategy(catalog=catalog, lm=lm)


def create_default_strategies(*, catalog: Catalog) -> list[RetrievalStrategy]:
    return [create_guideline_browser_strategy(catalog=catalog)]

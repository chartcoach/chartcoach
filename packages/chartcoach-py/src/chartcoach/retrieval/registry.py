from __future__ import annotations

from os import PathLike
from pathlib import Path

import dspy
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.env import get_openai_env
from chartcoach.retrieval.strategy import RetrievalStrategy


def catalog_from_path(path: str | PathLike[str]) -> Catalog:
    p = Path(path)
    if p.suffix == ".parquet":
        return Catalog.from_df(pl.read_parquet(p))
    return Catalog.from_disk(p)


def create_guideline_browser_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    openai = get_openai_env()
    lm = dspy.LM(model="gpt-5.2", api_base=openai.api_base, api_key=openai.api_key)
    return GuidelineBrowserStrategy(catalog=catalog, lm=lm)


def create_default_strategies(*, catalog: Catalog) -> list[RetrievalStrategy]:
    return [create_guideline_browser_strategy(catalog=catalog)]

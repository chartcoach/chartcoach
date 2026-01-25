from __future__ import annotations

from os import PathLike
from pathlib import Path
from io import BytesIO
from typing import Protocol
from urllib.request import urlopen
from urllib.parse import urlparse

import dspy
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.env import load_env
from chartcoach.retrieval.strategy import RetrievalStrategy


class StrategyFactory(Protocol):
    def __call__(self, *, catalog: Catalog) -> RetrievalStrategy: ...


StrategyRegistration = tuple[type[RetrievalStrategy], StrategyFactory]


def catalog_from_uri(uri: str | PathLike[str]) -> Catalog:
    if not isinstance(uri, str):
        return _catalog_from_path(Path(uri))

    if uri.startswith("file://"):
        return _catalog_from_path(Path(uri.removeprefix("file://")))

    parsed = urlparse(uri)
    if parsed.scheme in {"http", "https"}:
        if not parsed.path.endswith(".parquet"):
            raise ValueError("Remote catalog_uri must be a .parquet file.")
        return Catalog.from_df(_read_parquet_df_from_url(uri))

    if parsed.scheme == "s3":
        if not parsed.path.endswith(".parquet"):
            raise ValueError("Remote catalog_uri must be a .parquet file.")
        return Catalog.from_df(pl.read_parquet(uri))

    return _catalog_from_path(Path(uri))


def _catalog_from_path(path: Path) -> Catalog:
    if path.suffix == ".parquet":
        return Catalog.from_df(pl.read_parquet(path))
    return Catalog.from_disk(path)


def _read_parquet_df_from_url(url: str) -> pl.DataFrame:
    with urlopen(url) as resp:  # noqa: S310
        data = resp.read()
    return pl.read_parquet(BytesIO(data))


def create_guideline_browser_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    openai = load_env().openai.require()
    lm = dspy.LM(model="gpt-5.2", api_base=openai.api_base, api_key=openai.api_key)
    return GuidelineBrowserStrategy(catalog=catalog, lm=lm)


def create_default_strategy_registrations() -> list[StrategyRegistration]:
    from chartcoach.retrieval.guideline_browser import GuidelineBrowserStrategy

    return [(GuidelineBrowserStrategy, create_guideline_browser_strategy)]

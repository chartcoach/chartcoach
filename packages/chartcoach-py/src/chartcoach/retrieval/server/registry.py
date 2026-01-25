from __future__ import annotations

import os
from pathlib import Path
from typing import Any, cast

import dspy
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy import RetrievalStrategy


def _catalog_from_path(path: str) -> Catalog:
    if path.endswith(".parquet"):
        return Catalog.from_df(pl.read_parquet(path))
    return Catalog.from_disk(Path(path))


def _walk_subclasses(cls: type[RetrievalStrategy]) -> list[type[RetrievalStrategy]]:
    out: list[type[RetrievalStrategy]] = []
    queue: list[type[RetrievalStrategy]] = [cls]
    while queue:
        parent = queue.pop()
        for child in parent.__subclasses__():
            out.append(child)
            queue.append(child)
    return out


def list_strategy_classes() -> list[type[RetrievalStrategy]]:
    """
    Return all registered RetrievalStrategy subclasses.

    Strategy classes are discovered via subclass traversal; importing concrete strategy
    modules is required so they register themselves.
    """
    from chartcoach.retrieval import guideline_browser as _  # noqa: F401

    strategy_classes = _walk_subclasses(RetrievalStrategy)
    seen: set[str] = set()
    unique: list[type[RetrievalStrategy]] = []
    for cls in sorted(strategy_classes, key=lambda c: getattr(c, "id", c.__name__)):
        strategy_id = getattr(cls, "id", None)
        if not isinstance(strategy_id, str) or not strategy_id:
            continue
        if strategy_id in seen:
            continue
        seen.add(strategy_id)
        unique.append(cls)
    return unique


def create_default_strategies(
    *, catalog: Catalog, lm: dspy.LM
) -> list[RetrievalStrategy]:
    strategies: list[RetrievalStrategy] = []
    for cls in list_strategy_classes():
        strategies.append(cast(Any, cls)(catalog=catalog, lm=lm))
    return strategies


def create_app_from_env() -> Any:
    from chartcoach.retrieval.server.app import create_app

    catalog_path = os.environ.get("CHARTCOACH_CATALOG_PATH")
    if not catalog_path:
        raise RuntimeError(
            "Set CHARTCOACH_CATALOG_PATH to a catalog folder or .parquet file."
        )

    model = os.environ.get("CHARTCOACH_MODEL")
    api_base = os.environ.get("OPENAI_BASE_URL")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not model or not api_base or not api_key:
        raise RuntimeError("Set CHARTCOACH_MODEL, OPENAI_BASE_URL, and OPENAI_API_KEY.")

    lm = dspy.LM(model=model, api_base=api_base, api_key=api_key)
    catalog = _catalog_from_path(catalog_path)
    strategies = create_default_strategies(catalog=catalog, lm=lm)
    return create_app(strategies=strategies)

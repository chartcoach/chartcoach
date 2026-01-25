from __future__ import annotations

import pytest

from chartcoach.catalog.catalog import Catalog
from chartcoach.retrieval.strategy import RetrievalStrategy


def test_retrieval_strategy_stores_catalog() -> None:
    catalog = Catalog(entries=[])
    strategy = RetrievalStrategy(catalog, anything="ok")
    assert strategy.catalog is catalog


def test_retrieval_strategy_catalog_is_positional_only() -> None:
    catalog = Catalog(entries=[])
    with pytest.raises(TypeError):
        RetrievalStrategy(catalog=catalog)  # type: ignore[call-arg]


from __future__ import annotations

import pytest

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.types import RetrievalRequest


def test_retrieval_strategy_stores_catalog() -> None:
    catalog = Catalog(entries=[])
    strategy = RetrievalStrategy(catalog, anything="ok")
    assert strategy.catalog is catalog


def test_retrieval_strategy_catalog_is_positional_only() -> None:
    catalog = Catalog(entries=[])
    with pytest.raises(TypeError):
        RetrievalStrategy(catalog=catalog)  # type: ignore[call-arg]


def test_retrieval_strategy_forward_delegates_to_overridable_forward() -> None:
    strategy = RetrievalStrategy(Catalog(entries=[]))
    with pytest.raises(NotImplementedError):
        strategy(request=RetrievalRequest())

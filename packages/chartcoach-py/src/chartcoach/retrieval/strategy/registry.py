from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from chartcoach.catalog import Catalog
from chartcoach.env import load_env
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.optional import require_dspy

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


class StrategyFactory(Protocol):
    def __call__(self, *, catalog: Catalog) -> RetrievalStrategy: ...


StrategyRegistration = tuple[type[RetrievalStrategy], StrategyFactory]


def create_guideline_browser_strategy(*, catalog: Catalog) -> RetrievalStrategy:
    from chartcoach.retrieval.strategy.guideline_browser import GuidelineBrowserStrategy

    openai = load_env().openai.require()
    lm = dspy.LM(model="gpt-5.2", api_base=openai.api_base, api_key=openai.api_key)
    return GuidelineBrowserStrategy(catalog=catalog, lm=lm)


def create_default_strategy_registrations() -> list[StrategyRegistration]:
    from chartcoach.retrieval.strategy.guideline_browser import GuidelineBrowserStrategy

    return [(GuidelineBrowserStrategy, create_guideline_browser_strategy)]

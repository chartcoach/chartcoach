from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from pydantic import BaseModel, ConfigDict, Field

from chartcoach.retrieval.registry import StrategyRegistration, catalog_from_uri
from chartcoach.retrieval.strategy import StrategyInfo
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse

if TYPE_CHECKING:
    from fastapi import APIRouter


class StrategyRunRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    catalog_uri: str = Field(min_length=1)
    request: RetrievalRequest = Field(default_factory=RetrievalRequest)


def create_router(*, strategies: Sequence[StrategyRegistration]) -> "APIRouter":
    try:
        from fastapi import APIRouter as _APIRouter
        from fastapi import HTTPException
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    strategies_by_id = {
        strategy.id: (strategy, factory) for strategy, factory in strategies
    }
    router = _APIRouter(prefix="/v1")

    @router.get("/strategies", response_model=list[StrategyInfo])
    def get_strategies() -> list[StrategyInfo]:
        out = [strategy.info() for strategy, _factory in strategies_by_id.values()]
        return sorted(out, key=lambda s: s.id)

    @router.post("/strategies/{strategy_id}", response_model=RetrievalResponse)
    def run_strategy(strategy_id: str, body: StrategyRunRequest) -> RetrievalResponse:
        registration = strategies_by_id.get(strategy_id)
        if registration is None:
            raise HTTPException(status_code=404, detail="Unknown strategy id.")

        strategy_cls, factory = registration
        catalog = catalog_from_uri(body.catalog_uri)
        strategy = factory(catalog=catalog)
        return strategy(request=body.request)

    return router

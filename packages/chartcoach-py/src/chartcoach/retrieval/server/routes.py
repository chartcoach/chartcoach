from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from chartcoach.retrieval.strategy import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse

if TYPE_CHECKING:
    from fastapi import APIRouter


def create_router(*, strategies: Sequence[RetrievalStrategy]) -> "APIRouter":
    try:
        from fastapi import APIRouter as _APIRouter
        from fastapi import HTTPException
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    strategies_by_id = {s.id: s for s in strategies}
    router = _APIRouter(prefix="/v1")

    @router.get("/strategies", response_model=list[StrategyInfo])
    def get_strategies() -> list[StrategyInfo]:
        out = [s.info() for s in strategies_by_id.values()]
        return sorted(out, key=lambda s: s.id)

    @router.post("/strategies/{strategy_id}", response_model=RetrievalResponse)
    def run_strategy(strategy_id: str, req: RetrievalRequest) -> RetrievalResponse:
        strategy = strategies_by_id.get(strategy_id)
        if strategy is None:
            raise HTTPException(status_code=404, detail="Unknown strategy id.")
        return strategy(request=req)

    return router

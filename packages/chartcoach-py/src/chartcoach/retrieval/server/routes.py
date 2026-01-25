from __future__ import annotations

import inspect
from typing import TYPE_CHECKING, Sequence

from pydantic import BaseModel

from chartcoach.retrieval.strategy import RetrievalStrategy
from chartcoach.retrieval.types import RetrievalRequest, RetrievalResponse

if TYPE_CHECKING:
    from fastapi import APIRouter


class StrategyInfo(BaseModel):
    id: str
    name: str
    description: str


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
        out: list[StrategyInfo] = []
        for strategy in strategies_by_id.values():
            cls = strategy.__class__
            doc = inspect.getdoc(cls) or ""
            out.append(
                StrategyInfo(
                    id=strategy.id,
                    name=cls.__name__,
                    description=doc.splitlines()[0] if doc else "",
                )
            )
        return sorted(out, key=lambda s: s.id)

    @router.post("/strategies/{strategy_id}", response_model=RetrievalResponse)
    def run_strategy(strategy_id: str, req: RetrievalRequest) -> RetrievalResponse:
        strategy = strategies_by_id.get(strategy_id)
        if strategy is None:
            raise HTTPException(status_code=404, detail="Unknown strategy id.")
        return strategy(request=req)

    return router

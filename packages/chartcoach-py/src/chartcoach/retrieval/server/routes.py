from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

from chartcoach.retrieval.service.retrieval_service import (
    CatalogLoadError,
    RetrievalService,
    StrategyInitError,
    StrategyRunError,
    StrategyUpstreamError,
    UnknownStrategyError,
)
from chartcoach.retrieval.strategy.base import StrategyInfo
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

if TYPE_CHECKING:
    from fastapi import APIRouter


class StrategyRunRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    catalog_uri: str = Field(min_length=1)
    request: RetrievalRequest = Field(default_factory=RetrievalRequest)


def create_router(*, retrieval: RetrievalService) -> "APIRouter":
    try:
        from fastapi import APIRouter as _APIRouter
        from fastapi import HTTPException
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    router = _APIRouter(prefix="/v1")

    @router.get("/strategies", response_model=list[StrategyInfo])
    def get_strategies() -> list[StrategyInfo]:
        return retrieval.list_strategies()

    @router.post("/strategies/{strategy_id}", response_model=RetrievalResponse)
    def run_strategy(strategy_id: str, body: StrategyRunRequest) -> RetrievalResponse:
        try:
            return retrieval.run_strategy(
                strategy_id,
                catalog_uri=body.catalog_uri,
                request=body.request,
            )
        except UnknownStrategyError:
            raise HTTPException(status_code=404, detail="Unknown strategy id.")
        except CatalogLoadError as e:
            raise HTTPException(status_code=422, detail=str(e)) from e
        except StrategyInitError as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
        except StrategyRunError as e:
            raise HTTPException(status_code=422, detail=str(e)) from e
        except StrategyUpstreamError as e:
            raise HTTPException(status_code=502, detail=str(e)) from e

    return router

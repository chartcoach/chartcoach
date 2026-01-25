from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from chartcoach.retrieval.server.routes import create_router
from chartcoach.retrieval.registry import StrategyRegistration

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app(*, strategies: Sequence[StrategyRegistration]) -> "FastAPI":
    try:
        from fastapi import FastAPI as _FastAPI
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    app = _FastAPI(title="ChartCoach Retrieval Server", version="0.1.0")
    app.include_router(create_router(strategies=strategies))
    return app

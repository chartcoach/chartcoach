from __future__ import annotations

from typing import Any, Sequence

from chartcoach.retrieval.server.routes import create_router
from chartcoach.retrieval.strategy import RetrievalStrategy


def create_app(*, strategies: Sequence[RetrievalStrategy]) -> Any:
    try:
        from fastapi import FastAPI
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval-server]` to use the API server."
        ) from e

    app = FastAPI(title="ChartCoach Retrieval Server", version="0.1.0")
    app.include_router(create_router(strategies=strategies))
    return app

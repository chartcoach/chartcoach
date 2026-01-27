from __future__ import annotations

from typing import TYPE_CHECKING

from chartcoach.retrieval.service.retrieval_service import RetrievalService
from chartcoach.retrieval.strategy.registry import create_default_strategy_registrations

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app_from_env() -> "FastAPI":
    from chartcoach.retrieval.server.app import create_app

    registrations = create_default_strategy_registrations()
    retrieval = RetrievalService(registrations=registrations)
    return create_app(retrieval=retrieval)

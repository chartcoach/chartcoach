from __future__ import annotations

from typing import TYPE_CHECKING

from chartcoach.retrieval.registry import create_default_strategy_registrations

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app_from_env() -> "FastAPI":
    from chartcoach.retrieval.server.app import create_app

    strategies = create_default_strategy_registrations()
    return create_app(strategies=strategies)

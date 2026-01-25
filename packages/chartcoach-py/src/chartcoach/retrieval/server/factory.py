from __future__ import annotations

from typing import TYPE_CHECKING

from chartcoach.retrieval.env import get_retrieval_server_env
from chartcoach.retrieval.registry import catalog_from_path, create_default_strategies

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app_from_env() -> "FastAPI":
    from chartcoach.retrieval.server.app import create_app

    env = get_retrieval_server_env()
    catalog = catalog_from_path(env.catalog_path)
    strategies = create_default_strategies(catalog=catalog)
    return create_app(strategies=strategies)

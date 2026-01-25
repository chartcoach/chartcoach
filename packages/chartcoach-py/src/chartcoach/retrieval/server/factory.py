from __future__ import annotations

from typing import TYPE_CHECKING

from chartcoach.env import load_env
from chartcoach.retrieval.registry import catalog_from_path, create_default_strategies

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app_from_env() -> "FastAPI":
    from chartcoach.retrieval.server.app import create_app

    env = load_env()
    env.openai.require()
    catalog = catalog_from_path(env.retrieval_server.require_catalog_path())
    strategies = create_default_strategies(catalog=catalog)
    return create_app(strategies=strategies)

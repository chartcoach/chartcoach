from __future__ import annotations

import os
from typing import TYPE_CHECKING

from chartcoach.retrieval.registry import (
    catalog_from_path,
    create_default_strategies,
    openai_env,
)

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app_from_env() -> "FastAPI":
    from chartcoach.retrieval.server.app import create_app

    catalog_path = os.environ.get("CHARTCOACH_CATALOG_PATH")
    if not catalog_path:
        raise RuntimeError(
            "Set CHARTCOACH_CATALOG_PATH to a catalog folder or .parquet file."
        )

    openai_env()
    catalog = catalog_from_path(catalog_path)
    strategies = create_default_strategies(catalog=catalog)
    return create_app(strategies=strategies)

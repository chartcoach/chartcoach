from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class OpenAIEnv(BaseModel):
    model_config = ConfigDict(frozen=True)

    api_base: str
    api_key: str


class RetrievalServerEnv(BaseModel):
    model_config = ConfigDict(frozen=True)

    catalog_path: Path
    host: str
    port: int
    openai: OpenAIEnv


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}.")
    return value


def get_openai_env() -> OpenAIEnv:
    return OpenAIEnv(
        api_base=_require_env("OPENAI_BASE_URL"),
        api_key=_require_env("OPENAI_API_KEY"),
    )


def get_retrieval_server_env() -> RetrievalServerEnv:
    catalog_path = Path(_require_env("CHARTCOACH_CATALOG_PATH"))
    host = os.environ.get("CHARTCOACH_HOST", "127.0.0.1")
    port = int(os.environ.get("CHARTCOACH_PORT", "8000"))
    return RetrievalServerEnv(
        catalog_path=catalog_path,
        host=host,
        port=port,
        openai=get_openai_env(),
    )

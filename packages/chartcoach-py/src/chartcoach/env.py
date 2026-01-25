from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping

from pydantic import BaseModel, ConfigDict


class OpenAIEnv(BaseModel):
    """Optional OpenAI-compatible configuration (shared across features)."""

    model_config = ConfigDict(frozen=True)

    api_base: str | None = None
    api_key: str | None = None

    def require(self) -> OpenAIEnvRequired:
        if not self.api_base or not self.api_key:
            raise RuntimeError(
                "Missing required env vars: OPENAI_BASE_URL and OPENAI_API_KEY."
            )
        return OpenAIEnvRequired(api_base=self.api_base, api_key=self.api_key)


class OpenAIEnvRequired(BaseModel):
    model_config = ConfigDict(frozen=True)

    api_base: str
    api_key: str


class RetrievalServerEnv(BaseModel):
    """Optional server configuration (only needed when running the API server)."""

    model_config = ConfigDict(frozen=True)

    catalog_path: Path | None = None
    host: str = "127.0.0.1"
    port: int = 8000

    def require_catalog_path(self) -> Path:
        if self.catalog_path is None:
            raise RuntimeError("Missing required env var: CHARTCOACH_CATALOG_PATH.")
        return self.catalog_path


class ChartCoachEnv(BaseModel):
    """Unified env snapshot.

    Keep fields optional so different tools (retrieval, indexing, embedding) can
    require only what they need.
    """

    model_config = ConfigDict(frozen=True)

    openai: OpenAIEnv = OpenAIEnv()
    retrieval_server: RetrievalServerEnv = RetrievalServerEnv()


def load_env(environ: Mapping[str, str] | None = None) -> ChartCoachEnv:
    get = environ.get if environ is not None else os.environ.get

    openai = OpenAIEnv(
        api_base=get("OPENAI_BASE_URL"),
        api_key=get("OPENAI_API_KEY"),
    )

    catalog_path_raw = get("CHARTCOACH_CATALOG_PATH")
    retrieval_server = RetrievalServerEnv(
        catalog_path=Path(catalog_path_raw) if catalog_path_raw else None,
        host=get("CHARTCOACH_HOST") or "127.0.0.1",
        port=int(get("CHARTCOACH_PORT") or "8000"),
    )

    return ChartCoachEnv(openai=openai, retrieval_server=retrieval_server)

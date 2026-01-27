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


class S3Env(BaseModel):
    """Optional S3 configuration (used for artifact IO and ratings sync)."""

    model_config = ConfigDict(frozen=True)

    endpoint: str | None = None
    region: str | None = None
    access_key_id: str | None = None
    secret_access_key: str | None = None
    bucket: str | None = None
    prefix: str | None = None
    force_path_style: bool | None = None

    def require(self) -> S3EnvRequired:
        if not self.access_key_id or not self.secret_access_key or not self.bucket:
            raise RuntimeError(
                "Missing required env vars: S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, and S3_BUCKET."
            )
        return S3EnvRequired(
            endpoint=self.endpoint,
            region=self.region,
            access_key_id=self.access_key_id,
            secret_access_key=self.secret_access_key,
            bucket=self.bucket,
            prefix=self.prefix,
            force_path_style=self.force_path_style,
        )


class S3EnvRequired(BaseModel):
    model_config = ConfigDict(frozen=True)

    endpoint: str | None = None
    region: str | None = None
    access_key_id: str
    secret_access_key: str
    bucket: str
    prefix: str | None = None
    force_path_style: bool | None = None


class ChartCoachEnv(BaseModel):
    """Unified env snapshot.

    Keep fields optional so different tools (retrieval, indexing, embedding) can
    require only what they need.
    """

    model_config = ConfigDict(frozen=True)

    openai: OpenAIEnv = OpenAIEnv()
    retrieval_server: RetrievalServerEnv = RetrievalServerEnv()
    s3: S3Env = S3Env()


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

    force_path_style_raw = (get("S3_FORCE_PATH_STYLE") or "").strip().lower()
    force_path_style = (
        True
        if force_path_style_raw == "true"
        else False
        if force_path_style_raw == "false"
        else None
    )

    s3 = S3Env(
        endpoint=get("S3_ENDPOINT"),
        region=get("S3_REGION"),
        access_key_id=get("S3_ACCESS_KEY_ID"),
        secret_access_key=get("S3_SECRET_ACCESS_KEY"),
        bucket=get("S3_BUCKET"),
        prefix=get("S3_PREFIX"),
        force_path_style=force_path_style,
    )

    return ChartCoachEnv(openai=openai, retrieval_server=retrieval_server, s3=s3)

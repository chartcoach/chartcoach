from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlparse

from obstore.store import ObjectStore, from_url

from chartcoach.env import S3EnvRequired

if TYPE_CHECKING:
    from obstore.store import ClientConfig, S3Config


def normalize_prefix(prefix: str | None) -> str:
    if not prefix:
        return ""
    return prefix if prefix.endswith("/") else f"{prefix}/"


def default_artifacts_url(*, s3: S3EnvRequired, version: str = "v1") -> str:
    base = normalize_prefix(s3.prefix)
    return f"s3://{s3.bucket}/{base}eval-artifacts/{version}/"


def create_store(url: str, *, s3: S3EnvRequired | None = None) -> ObjectStore:
    parsed = urlparse(url)
    if parsed.scheme != "s3":
        return from_url(url)

    if s3 is None:
        raise ValueError("S3 configuration is required for s3:// stores.")

    config: S3Config = {
        "access_key_id": s3.access_key_id,
        "secret_access_key": s3.secret_access_key,
    }
    if s3.region:
        config["region"] = s3.region
    if s3.endpoint:
        config["endpoint"] = s3.endpoint
    if s3.force_path_style is not None:
        config["virtual_hosted_style_request"] = not s3.force_path_style

    client_options: ClientConfig | None = None
    if s3.endpoint and urlparse(s3.endpoint).scheme == "http":
        client_options = {"allow_http": True}

    return from_url(url, client_options=client_options, **config)

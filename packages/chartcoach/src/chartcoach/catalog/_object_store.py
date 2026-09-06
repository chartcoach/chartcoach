from __future__ import annotations

from collections.abc import Mapping
from urllib.parse import urlsplit, urlunsplit

CLOUD_SCHEMES = frozenset(
    {
        "abfs",
        "abfss",
        "adl",
        "az",
        "azure",
        "gcp",
        "gcs",
        "gs",
        "s3",
        "s3a",
    }
)
CATALOG_STORE_SCHEMES = CLOUD_SCHEMES | {"file"}


def copy_storage_options(
    storage_options: Mapping[str, object] | None,
) -> dict[str, object]:
    if storage_options is None:
        return {}
    if not isinstance(storage_options, Mapping) or not all(
        isinstance(key, str) for key in storage_options
    ):
        raise TypeError("storage_options must map strings to values.")
    return dict(storage_options)


def obstore_uri(uri: str) -> str:
    parsed = urlsplit(uri)
    scheme = {"gcp": "gs", "gcs": "gs"}.get(parsed.scheme.lower(), parsed.scheme)
    return urlunsplit(
        (scheme, parsed.netloc, parsed.path, parsed.query, parsed.fragment)
    )


__all__ = [
    "CATALOG_STORE_SCHEMES",
    "CLOUD_SCHEMES",
    "copy_storage_options",
    "obstore_uri",
]

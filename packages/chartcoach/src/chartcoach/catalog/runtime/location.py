from __future__ import annotations

import os
from dataclasses import dataclass
from os import PathLike
from pathlib import Path, PurePosixPath
from typing import Literal
from urllib.parse import unquote, urlsplit, urlunsplit
from urllib.request import url2pathname

from ...constants import CATALOG_ARTIFACT_BASE_URL, CATALOG_SELECTION_PATH
from .._object_store import CLOUD_SCHEMES
from ..errors import CatalogError

OFFICIAL_CATALOG_URL = (
    f"{CATALOG_ARTIFACT_BASE_URL.rstrip('/')}/{CATALOG_SELECTION_PATH}"
)


@dataclass(frozen=True, slots=True)
class LocalCatalogLocation:
    path: Path


@dataclass(frozen=True, slots=True)
class RemoteCatalogLocation:
    uri: str
    transport: Literal["http", "cloud"]


def normalize_location(
    location: str | PathLike[str] | None,
) -> LocalCatalogLocation | RemoteCatalogLocation:
    if location is None:
        return RemoteCatalogLocation(OFFICIAL_CATALOG_URL, "http")
    if not isinstance(location, str):
        value = os.fspath(location)
        if not isinstance(value, str):
            raise TypeError("Catalog location paths must contain text.")
        return LocalCatalogLocation(Path(value))

    scheme = path_scheme(location)
    if scheme is None:
        return LocalCatalogLocation(Path(location))
    scheme = scheme.lower()
    if scheme == "file":
        return LocalCatalogLocation(file_uri_path(location))
    if scheme in {"http", "https"}:
        return RemoteCatalogLocation(location, "http")
    if scheme in CLOUD_SCHEMES:
        return RemoteCatalogLocation(location, "cloud")
    raise CatalogError(f"Unsupported catalog location scheme: {scheme}.")


def path_scheme(value: str) -> str | None:
    index = value.find("://")
    return None if index < 0 else value[:index]


def file_uri_path(uri: str) -> Path:
    parsed = urlsplit(uri)
    if parsed.query or parsed.fragment or parsed.netloc not in {"", "localhost"}:
        raise CatalogError("file:// catalog locations must name a local path.")
    try:
        return Path(url2pathname(unquote(parsed.path)))
    except (UnicodeDecodeError, ValueError) as exc:
        raise CatalogError("file:// catalog location is invalid.") from exc


def uri_name(uri: str) -> str:
    return PurePosixPath(unquote(urlsplit(uri).path)).name


def uri_parent(uri: str) -> str:
    parsed = urlsplit(uri)
    parent = PurePosixPath(parsed.path).parent.as_posix()
    if not parent.startswith("/"):
        parent = f"/{parent}"
    if not parent.endswith("/"):
        parent += "/"
    return urlunsplit((parsed.scheme, parsed.netloc, parent, "", ""))


def join_uri_path(base: str, *parts: str) -> str:
    parsed = urlsplit(base)
    path = PurePosixPath(parsed.path, *parts).as_posix()
    if not path.startswith("/"):
        path = f"/{path}"
    return urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


__all__ = [
    "LocalCatalogLocation",
    "RemoteCatalogLocation",
    "join_uri_path",
    "normalize_location",
    "uri_name",
    "uri_parent",
]

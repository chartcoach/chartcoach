from __future__ import annotations

import os
from dataclasses import dataclass
from os import PathLike
from pathlib import Path, PurePosixPath
from typing import Literal
from urllib.parse import unquote, urlsplit, urlunsplit
from urllib.request import url2pathname

from ...constants import CATALOG_ARTIFACT_BASE_URL, CATALOG_ENTRY_PATH
from .._object_store import CLOUD_SCHEMES
from ..errors import CatalogError

OFFICIAL_CATALOG_URL = f"{CATALOG_ARTIFACT_BASE_URL.rstrip('/')}/{CATALOG_ENTRY_PATH}"


@dataclass(frozen=True, slots=True)
class LocalSource:
    path: Path


@dataclass(frozen=True, slots=True)
class RemoteSource:
    uri: str
    transport: Literal["http", "cloud"]


def normalize_source(
    source: str | PathLike[str] | None,
) -> LocalSource | RemoteSource:
    if source is None:
        return RemoteSource(OFFICIAL_CATALOG_URL, "http")
    if not isinstance(source, str):
        value = os.fspath(source)
        if not isinstance(value, str):
            raise TypeError("Catalog source paths must contain text.")
        return LocalSource(Path(value))

    scheme = path_scheme(source)
    if scheme is None:
        return LocalSource(Path(source))
    scheme = scheme.lower()
    if scheme == "file":
        return LocalSource(file_uri_path(source))
    if scheme in {"http", "https"}:
        return RemoteSource(source, "http")
    if scheme in CLOUD_SCHEMES:
        return RemoteSource(source, "cloud")
    raise CatalogError(f"Unsupported catalog source scheme: {scheme}.")


def path_scheme(value: str) -> str | None:
    index = value.find("://")
    return None if index < 0 else value[:index]


def file_uri_path(uri: str) -> Path:
    parsed = urlsplit(uri)
    if parsed.query or parsed.fragment or parsed.netloc not in {"", "localhost"}:
        raise CatalogError("file:// catalog sources must name a local path.")
    try:
        return Path(url2pathname(unquote(parsed.path)))
    except (UnicodeDecodeError, ValueError) as exc:
        raise CatalogError("file:// catalog source is invalid.") from exc


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
    "LocalSource",
    "RemoteSource",
    "join_uri_path",
    "normalize_source",
    "uri_name",
    "uri_parent",
]

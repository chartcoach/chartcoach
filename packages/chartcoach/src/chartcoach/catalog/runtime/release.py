from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Literal
from urllib.parse import urlsplit, urlunsplit

from ..errors import CatalogError, CatalogIntegrityError
from ..releases import CatalogRelease
from ..releases.hashing import release_digest
from ..releases.services import MAX_RELEASE_ARTIFACT_BYTES
from .cache import cache_remote_artifact, verify_local_artifact
from .location import (
    LocalCatalogLocation,
    RemoteCatalogLocation,
    join_uri_path,
    uri_name,
    uri_parent,
)
from .transport import read_local_bytes, read_remote_bytes

_DESCRIPTOR_NAMES = frozenset({"catalog.json", "release.json"})
_MAX_JSON_BYTES = 1024 * 1024
_MAX_CORE_ARTIFACT_BYTES = 64 * 1024**2


@dataclass(frozen=True, slots=True)
class ReleaseLocation:
    release: CatalogRelease
    artifact_base: Path | str
    descriptor: Path | str
    transport: Literal["local", "http", "cloud"]
    storage_options: Mapping[str, object]

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "storage_options", MappingProxyType(dict(self.storage_options))
        )

    @property
    def resolved_location(self) -> str:
        """Return an exact release locator with credentials removed."""

        return sanitize_location(self.descriptor)

    def artifact_path(self, path: str) -> Path:
        artifact = self.release.artifact(path)
        if self.transport == "local":
            base = self.artifact_base
            if not isinstance(base, Path):
                raise TypeError("Local release base must be a path.")
            local_path = base.joinpath(*PurePosixPath(path).parts)
            verify_local_artifact(base, local_path, path, artifact)
            return local_path

        base = self.artifact_base
        if not isinstance(base, str):
            raise TypeError("Remote release base must be a URI.")
        uri = join_uri_path(base, path)
        return cache_remote_artifact(
            uri,
            transport=self.transport,
            storage_options=self.storage_options,
            path=path,
            artifact=artifact,
        )


def release_location(
    location: LocalCatalogLocation | RemoteCatalogLocation,
    storage_options: Mapping[str, object],
) -> ReleaseLocation:
    if isinstance(location, LocalCatalogLocation):
        path = location.path.absolute()
        descriptor = path / "release.json" if path.is_dir() else path
        if descriptor.name not in _DESCRIPTOR_NAMES:
            raise CatalogError(
                "Catalog file locations must be named catalog.json or release.json."
            )
        if not descriptor.is_file():
            raise CatalogError(f"Catalog location does not exist: {descriptor}")
        release = parse_release(read_local_bytes(descriptor, _MAX_JSON_BYTES))
        _validate_descriptor_digest(descriptor, release)
        base = (
            descriptor.parent / "catalog" / "releases" / release.digest
            if descriptor.name == "catalog.json"
            else descriptor.parent
        )
        exact_descriptor = (
            base / "release.json" if descriptor.name == "catalog.json" else descriptor
        )
        return ReleaseLocation(
            release,
            base,
            exact_descriptor,
            "local",
            storage_options,
        )

    name = uri_name(location.uri)
    if name not in _DESCRIPTOR_NAMES:
        raise CatalogError(
            "Remote catalog locations must name catalog.json or release.json."
        )
    release = parse_release(
        read_remote_bytes(
            location.uri,
            transport=location.transport,
            storage_options=storage_options,
            limit=_MAX_JSON_BYTES,
            no_cache=name == "catalog.json",
        )
    )
    _validate_descriptor_digest(location.uri, release)
    base = (
        join_uri_path(uri_parent(location.uri), "catalog", "releases", release.digest)
        if name == "catalog.json"
        else uri_parent(location.uri)
    )
    exact_descriptor = (
        join_uri_path(base, "release.json") if name == "catalog.json" else location.uri
    )
    return ReleaseLocation(
        release,
        base,
        exact_descriptor,
        location.transport,
        storage_options,
    )


def sanitize_location(location: Path | str) -> str:
    """Return a path or URI locator without userinfo, query, or fragment data."""

    if isinstance(location, Path):
        return str(location.absolute())
    parsed = urlsplit(location)
    hostname = parsed.hostname or ""
    if ":" in hostname and not hostname.startswith("["):
        hostname = f"[{hostname}]"
    try:
        port = parsed.port
    except ValueError:
        port = None
    netloc = f"{hostname}:{port}" if port is not None else hostname
    return urlunsplit((parsed.scheme, netloc, parsed.path, "", ""))


def parse_release(data: bytes) -> CatalogRelease:
    try:
        value = json.loads(data.decode("utf-8"))
        release = CatalogRelease.from_mapping(value)
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise CatalogError(f"Catalog release descriptor is invalid: {exc}") from exc
    if release.digest != release_digest(release.artifacts):
        raise CatalogIntegrityError(
            "Catalog release digest does not match its artifact set."
        )
    for path, artifact in release.artifacts.items():
        if artifact.bytes > MAX_RELEASE_ARTIFACT_BYTES:
            raise CatalogError(f"Catalog artifact exceeds the 1 GiB limit: {path}")
        if (
            path in {"MANIFEST.md", "entries.parquet"}
            and artifact.bytes > _MAX_CORE_ARTIFACT_BYTES
        ):
            raise CatalogError(f"Catalog artifact exceeds the 64 MiB limit: {path}")
    return release


def _validate_descriptor_digest(
    descriptor: Path | str, release: CatalogRelease
) -> None:
    if isinstance(descriptor, Path):
        if descriptor.name != "release.json":
            return
        parent = descriptor.parent.name
    else:
        path = PurePosixPath(urlsplit(descriptor).path)
        if path.name != "release.json":
            return
        parent = path.parent.name
    if (
        parent != release.digest
        and len(parent) == 64
        and all(character in "0123456789abcdef" for character in parent)
    ):
        raise CatalogIntegrityError(
            "Catalog release digest does not match its digest-addressed location.",
            details={"expected_digest": parent, "release_digest": release.digest},
        )


__all__ = [
    "ReleaseLocation",
    "release_location",
    "sanitize_location",
]

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Literal

from ..errors import CatalogError
from ..releases import CatalogRelease
from ..releases.hashing import release_digest
from ..releases.services import MAX_RELEASE_ARTIFACT_BYTES
from .cache import cache_remote_artifact, verify_local_artifact
from .source import LocalSource, RemoteSource, join_uri_path, uri_name, uri_parent
from .transport import read_local_bytes, read_remote_bytes

_DESCRIPTOR_NAMES = frozenset({"catalog.json", "release.json"})
_MAX_JSON_BYTES = 1024 * 1024
_MAX_CORE_ARTIFACT_BYTES = 64 * 1024**2


@dataclass(frozen=True, slots=True)
class ReleaseLocation:
    release: CatalogRelease
    artifact_base: Path | str
    transport: Literal["local", "http", "cloud"]
    storage_options: Mapping[str, object]

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
    source: LocalSource | RemoteSource,
    storage_options: Mapping[str, object],
) -> ReleaseLocation:
    if isinstance(source, LocalSource):
        path = source.path
        descriptor = path / "release.json" if path.is_dir() else path
        if descriptor.name not in _DESCRIPTOR_NAMES:
            raise CatalogError(
                "Catalog file sources must be named catalog.json or release.json."
            )
        if not descriptor.is_file():
            raise CatalogError(f"Catalog source does not exist: {descriptor}")
        release = parse_release(read_local_bytes(descriptor, _MAX_JSON_BYTES))
        base = (
            descriptor.parent / "catalog" / "releases" / release.digest
            if descriptor.name == "catalog.json"
            else descriptor.parent
        )
        return ReleaseLocation(release, base, "local", storage_options)

    name = uri_name(source.uri)
    if name not in _DESCRIPTOR_NAMES:
        raise CatalogError(
            "Remote catalog sources must name catalog.json or release.json."
        )
    release = parse_release(
        read_remote_bytes(
            source.uri,
            transport=source.transport,
            storage_options=storage_options,
            limit=_MAX_JSON_BYTES,
            no_cache=name == "catalog.json",
        )
    )
    base = (
        join_uri_path(uri_parent(source.uri), "catalog", "releases", release.digest)
        if name == "catalog.json"
        else uri_parent(source.uri)
    )
    return ReleaseLocation(release, base, source.transport, storage_options)


def profile_ids(release: CatalogRelease) -> tuple[str, ...]:
    prefix = "profiles/"
    suffix = "/index.tar.gz"
    return tuple(
        sorted(
            path.removeprefix(prefix).removesuffix(suffix)
            for path in release.artifacts
            if path.startswith(prefix) and path.endswith(suffix)
        )
    )


def parse_release(data: bytes) -> CatalogRelease:
    try:
        value = json.loads(data.decode("utf-8"))
        release = CatalogRelease.from_mapping(value)
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        raise CatalogError(f"Catalog release descriptor is invalid: {exc}") from exc
    if release.digest != release_digest(release.artifacts):
        raise CatalogError("Catalog release digest does not match its artifact set.")
    for path, artifact in release.artifacts.items():
        if artifact.bytes > MAX_RELEASE_ARTIFACT_BYTES:
            raise CatalogError(f"Catalog artifact exceeds the 1 GiB limit: {path}")
        if (
            path in {"MANIFEST.md", "entries.parquet"}
            and artifact.bytes > _MAX_CORE_ARTIFACT_BYTES
        ):
            raise CatalogError(f"Catalog artifact exceeds the 64 MiB limit: {path}")
    return release


__all__ = ["ReleaseLocation", "profile_ids", "release_location"]

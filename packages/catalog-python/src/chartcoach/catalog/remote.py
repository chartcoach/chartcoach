from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
from typing import TYPE_CHECKING, Iterable, Literal, Mapping, Self, cast
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from platformdirs import user_cache_path

from chartcoach.constants import (
    ARTIFACT_BASE_URL_ENV,
    CACHE_DIR_ENV,
    DEFAULT_CATALOG_ARTIFACT_BASE_URL,
    DEFAULT_CATALOG_DIGEST,
    DEFAULT_CATALOG_VERSION,
)

if TYPE_CHECKING:
    from .collection import Catalog

ArtifactKind = Literal["manifest", "entries", "lancedb-index"]
CATALOG_ARTIFACT_KINDS: tuple[ArtifactKind, ...] = ("manifest", "entries")


@dataclass(frozen=True, slots=True)
class ArtifactDescriptor:
    """One file listed by catalog release metadata."""

    kind: ArtifactKind
    path: str
    digest: str
    bytes: int
    format: str | None = None
    rows: int | None = None
    extra: Mapping[str, object] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, value: object) -> Self:
        """Parse one artifact descriptor from JSON data."""

        if not isinstance(value, Mapping):
            raise ValueError("Artifact descriptor must be an object.")
        raw = cast(Mapping[str, object], value)
        kind = raw.get("kind")
        if kind not in ("manifest", "entries", "lancedb-index"):
            raise ValueError(f"Unsupported catalog artifact kind: {kind!r}")
        artifact_kind = cast(ArtifactKind, kind)
        path = _string(raw, "path")
        _validate_relative_artifact_path(path)
        digest = _string(raw, "digest")
        size = _int(raw, "bytes")
        artifact_format = raw.get("format")
        rows = raw.get("rows")
        return cls(
            kind=artifact_kind,
            path=path,
            digest=digest,
            bytes=size,
            format=artifact_format if isinstance(artifact_format, str) else None,
            rows=rows if isinstance(rows, int) else None,
            extra={
                key: raw_value
                for key, raw_value in raw.items()
                if key not in {"kind", "path", "digest", "bytes", "format", "rows"}
            },
        )

    def to_record(self) -> dict[str, object]:
        """Return the JSON shape for this artifact descriptor."""

        record: dict[str, object] = {
            "kind": self.kind,
            "path": self.path,
            "digest": self.digest,
            "bytes": self.bytes,
        }
        if self.format is not None:
            record["format"] = self.format
        if self.rows is not None:
            record["rows"] = self.rows
        record.update(self.extra)
        return record


@dataclass(frozen=True, slots=True)
class CatalogReleaseMetadata:
    """Release metadata for one catalog bundle."""

    version: str
    digest: str
    artifacts: tuple[ArtifactDescriptor, ...]

    @classmethod
    def from_mapping(cls, value: object) -> Self:
        """Parse catalog release metadata from JSON data."""

        if not isinstance(value, Mapping):
            raise ValueError("Catalog release metadata must be an object.")
        raw = cast(Mapping[str, object], value)
        artifacts = raw.get("artifacts")
        if not isinstance(artifacts, list):
            raise ValueError("Catalog release metadata artifacts must be a list.")
        parsed = tuple(ArtifactDescriptor.from_mapping(item) for item in artifacts)
        _require_artifact_kind(parsed, "manifest")
        _require_artifact_kind(parsed, "entries")
        return cls(
            version=_string(raw, "version"),
            digest=_string(raw, "digest"),
            artifacts=parsed,
        )

    @classmethod
    def from_json(cls, text: str) -> Self:
        """Parse catalog release metadata from JSON text."""

        return cls.from_mapping(json.loads(text))

    def to_record(self) -> dict[str, object]:
        """Return the JSON shape for this release metadata."""

        return {
            "version": self.version,
            "digest": self.digest,
            "artifacts": [artifact.to_record() for artifact in self.artifacts],
        }

    def artifact(self, kind: ArtifactKind) -> ArtifactDescriptor:
        """Return the descriptor for one artifact kind."""

        for artifact in self.artifacts:
            if artifact.kind == kind:
                return artifact
        raise KeyError(kind)


def default_metadata_url() -> str:
    """Return the package-pinned catalog metadata URL."""

    base_url = os.getenv(ARTIFACT_BASE_URL_ENV, DEFAULT_CATALOG_ARTIFACT_BASE_URL)
    return metadata_url(base_url)


def metadata_url(locator: str) -> str:
    """Return the metadata URL for an artifact base URL or metadata URL."""

    if locator.endswith("metadata.json"):
        return locator
    return urljoin(locator.rstrip("/") + "/", "metadata.json")


def cache_root() -> Path:
    """Return the local cache root for downloaded catalog artifacts."""

    if raw := os.getenv(CACHE_DIR_ENV):
        return Path(raw).expanduser()
    return user_cache_path("chartcoach")


def default_catalog_bundle() -> Path:
    """Return the cached package-pinned catalog bundle, downloading it when needed."""

    target = _cache_path(DEFAULT_CATALOG_VERSION, DEFAULT_CATALOG_DIGEST)
    if _cached_bundle_is_valid(target, expected_digest=DEFAULT_CATALOG_DIGEST):
        return target
    return download_catalog_bundle(
        default_metadata_url(),
        expected_version=DEFAULT_CATALOG_VERSION,
        expected_digest=DEFAULT_CATALOG_DIGEST,
    )


def download_catalog_bundle(
    metadata_url: str,
    *,
    expected_version: str | None = None,
    expected_digest: str | None = None,
) -> Path:
    """Download one catalog bundle into the local cache and return its path."""

    metadata, resolved_metadata_url = _read_remote_metadata(metadata_url)
    if expected_version is not None and metadata.version != expected_version:
        raise ValueError(
            f"Catalog metadata version {metadata.version!r} does not match {expected_version!r}."
        )
    if expected_digest is not None and metadata.digest != expected_digest:
        raise ValueError(
            f"Catalog metadata digest {metadata.digest!r} does not match {expected_digest!r}."
        )

    target = _cache_path(metadata.version, metadata.digest)
    if _cached_bundle_is_valid(target, expected_digest=metadata.digest):
        return target

    tmp = target.with_name(target.name + ".tmp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True, exist_ok=True)

    (tmp / "metadata.json").write_text(_metadata_json(metadata))
    for artifact in _catalog_artifacts(metadata):
        artifact_url = urljoin(resolved_metadata_url, artifact.path)
        output = tmp / artifact.path
        output.parent.mkdir(parents=True, exist_ok=True)
        _download_file(artifact_url, output)
        _validate_file(output, artifact)

    if target.exists():
        shutil.rmtree(target)
    tmp.rename(target)
    return target


def write_release_metadata(
    catalog: Catalog,
    bundle_path: Path,
    *,
    version: str = DEFAULT_CATALOG_VERSION,
) -> CatalogReleaseMetadata:
    """Write `metadata.json` for a bundle and return the parsed metadata."""

    manifest_path = bundle_path / "MANIFEST.md"
    entries_path = bundle_path / "entries.parquet"
    metadata = CatalogReleaseMetadata(
        version=version,
        digest=catalog.digest(),
        artifacts=(
            ArtifactDescriptor(
                kind="manifest",
                path="MANIFEST.md",
                digest=_sha256(manifest_path),
                bytes=manifest_path.stat().st_size,
                format="markdown",
            ),
            ArtifactDescriptor(
                kind="entries",
                path="entries.parquet",
                digest=_sha256(entries_path),
                bytes=entries_path.stat().st_size,
                format="parquet",
                rows=len(catalog),
            ),
        ),
    )
    (bundle_path / "metadata.json").write_text(_metadata_json(metadata))
    return metadata


def read_release_metadata(path: Path) -> CatalogReleaseMetadata:
    """Read `metadata.json` from a catalog bundle path."""

    return CatalogReleaseMetadata.from_json((path / "metadata.json").read_text())


def _cache_path(version: str, digest: str) -> Path:
    return cache_root() / "catalog" / version / digest


def _cached_bundle_is_valid(path: Path, *, expected_digest: str) -> bool:
    metadata_path = path / "metadata.json"
    if not metadata_path.exists():
        return False
    try:
        metadata = CatalogReleaseMetadata.from_json(metadata_path.read_text())
        if metadata.digest != expected_digest:
            return False
        for artifact in _catalog_artifacts(metadata):
            artifact_path = path / artifact.path
            if not artifact_path.exists():
                return False
            _validate_file(artifact_path, artifact)
    except (OSError, ValueError, json.JSONDecodeError):
        return False
    return True


def _read_url_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "chartcoach"})
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def _read_remote_metadata(url: str, *, depth: int = 0) -> tuple[CatalogReleaseMetadata, str]:
    if depth > 5:
        raise ValueError("Catalog metadata pointer chain is too deep.")
    raw = json.loads(_read_url_text(url))
    if not isinstance(raw, Mapping):
        raise ValueError("Catalog release metadata must be an object.")
    target = raw.get("target") if raw.get("kind") == "chartcoach-release-pointer" else None
    if target is not None:
        if not isinstance(target, str) or not target:
            raise ValueError("Catalog release pointer target must be a string.")
        target_url = _resolve_pointer_url(url, target)
        return _read_remote_metadata(target_url, depth=depth + 1)
    return CatalogReleaseMetadata.from_mapping(raw), url


def _download_file(url: str, path: Path) -> None:
    request = Request(url, headers={"User-Agent": "chartcoach"})
    with urlopen(request) as response, path.open("wb") as output:
        shutil.copyfileobj(response, output)


def _validate_file(path: Path, artifact: ArtifactDescriptor) -> None:
    if path.stat().st_size != artifact.bytes:
        raise ValueError(f"Catalog artifact size mismatch: {artifact.path}")
    if _sha256(path) != artifact.digest:
        raise ValueError(f"Catalog artifact digest mismatch: {artifact.path}")


def _sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _metadata_json(metadata: CatalogReleaseMetadata) -> str:
    return json.dumps(metadata.to_record(), indent=2, ensure_ascii=False) + "\n"


def _require_artifact_kind(
    artifacts: Iterable[ArtifactDescriptor],
    kind: ArtifactKind,
) -> None:
    if not any(artifact.kind == kind for artifact in artifacts):
        raise ValueError(f"Catalog release metadata is missing a {kind!r} artifact.")


def _catalog_artifacts(metadata: CatalogReleaseMetadata) -> tuple[ArtifactDescriptor, ...]:
    return tuple(
        artifact for artifact in metadata.artifacts if artifact.kind in CATALOG_ARTIFACT_KINDS
    )


def _resolve_pointer_url(url: str, target: str) -> str:
    parsed = urlparse(target)
    if parsed.scheme:
        if parsed.scheme not in {"http", "https"}:
            raise ValueError(f"Unsupported catalog release pointer URL: {target!r}")
        return target
    if target.startswith("/"):
        _validate_relative_artifact_path(target.lstrip("/"))
        return urljoin(url, target)
    _validate_relative_artifact_path(target)
    return urljoin(url, target)


def _validate_relative_artifact_path(path: str) -> None:
    parsed = PurePosixPath(path)
    if parsed.is_absolute() or ".." in parsed.parts:
        raise ValueError(f"Catalog artifact path must be relative: {path!r}")


def _string(value: Mapping[str, object], key: str) -> str:
    raw = value.get(key)
    if not isinstance(raw, str) or not raw:
        raise ValueError(f"Catalog release metadata {key!r} must be a string.")
    return raw


def _int(value: Mapping[str, object], key: str) -> int:
    raw = value.get(key)
    if not isinstance(raw, int) or raw < 0:
        raise ValueError(f"Catalog release metadata {key!r} must be a non-negative integer.")
    return raw

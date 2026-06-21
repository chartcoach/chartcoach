from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tarfile
from typing import TYPE_CHECKING, Callable, Iterable, Literal, Mapping, Self, cast
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from platformdirs import user_cache_path

from ..constants import (
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
DownloadKind = Literal["catalog", "index"]
DownloadReporter = Callable[[DownloadKind, str, Path], None]


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


@dataclass(frozen=True, slots=True)
class CatalogArtifactRelease:
    """One catalog release listed by the root artifact index."""

    name: str
    version: str
    digest: str
    root: str
    metadata: str
    artifacts: tuple[ArtifactDescriptor, ...]

    @classmethod
    def from_mapping(cls, value: object) -> Self:
        """Parse one catalog release entry from index JSON data."""

        if not isinstance(value, Mapping):
            raise ValueError("Catalog artifact index release must be an object.")
        raw = cast(Mapping[str, object], value)
        artifacts = raw.get("artifacts")
        if not isinstance(artifacts, list):
            raise ValueError("Catalog artifact index release artifacts must be a list.")
        return cls(
            name=_string(raw, "name"),
            version=_string(raw, "version"),
            digest=_string(raw, "digest"),
            root=_relative_index_path(raw, "root"),
            metadata=_relative_index_path(raw, "metadata"),
            artifacts=tuple(
                ArtifactDescriptor.from_mapping(item) for item in artifacts
            ),
        )

    def to_record(self) -> dict[str, object]:
        """Return the JSON shape for this artifact index release."""

        return {
            "name": self.name,
            "version": self.version,
            "digest": self.digest,
            "root": self.root,
            "metadata": self.metadata,
            "artifacts": [artifact.to_record() for artifact in self.artifacts],
        }


@dataclass(frozen=True, slots=True)
class CatalogArtifactIndex:
    """Root artifact index for chartcoach catalog releases."""

    kind: str
    version: int
    catalogs: tuple[CatalogArtifactRelease, ...]

    @classmethod
    def from_mapping(cls, value: object) -> Self:
        """Parse the root artifact index from JSON data."""

        if not isinstance(value, Mapping):
            raise ValueError("Catalog artifact index must be an object.")
        raw = cast(Mapping[str, object], value)
        catalogs = raw.get("catalogs")
        if not isinstance(catalogs, list):
            raise ValueError("Catalog artifact index catalogs must be a list.")
        kind = _string(raw, "kind")
        if kind != "chartcoach-artifact-index":
            raise ValueError(f"Unsupported catalog artifact index kind: {kind!r}")
        version = _int(raw, "version")
        return cls(
            kind=kind,
            version=version,
            catalogs=tuple(
                CatalogArtifactRelease.from_mapping(item) for item in catalogs
            ),
        )

    @classmethod
    def from_json(cls, text: str) -> Self:
        """Parse the root artifact index from JSON text."""

        return cls.from_mapping(json.loads(text))

    def to_record(self) -> dict[str, object]:
        """Return the JSON shape for this artifact index."""

        return {
            "kind": self.kind,
            "version": self.version,
            "catalogs": [catalog.to_record() for catalog in self.catalogs],
        }

    def catalog(
        self,
        *,
        name: str = "chartcoach/catalog",
        version: str | None = None,
        digest: str | None = None,
    ) -> CatalogArtifactRelease:
        """Return one catalog release entry."""

        matches = [
            catalog
            for catalog in self.catalogs
            if catalog.name == name
            and (version is None or catalog.version == version)
            and (digest is None or catalog.digest == digest)
        ]
        if not matches:
            raise KeyError(name, version, digest)
        return sorted(matches, key=lambda catalog: _version_sort_key(catalog.version))[
            -1
        ]


def default_artifact_index_url() -> str:
    """Return the root artifact index URL."""

    base_url = os.getenv(ARTIFACT_BASE_URL_ENV, DEFAULT_CATALOG_ARTIFACT_BASE_URL)
    return urljoin(base_url.rstrip("/") + "/", "index.json")


def read_artifact_index(index_url: str | None = None) -> CatalogArtifactIndex:
    """Read the root artifact index from `index_url`."""

    return CatalogArtifactIndex.from_json(
        _read_url_text(index_url or default_artifact_index_url())
    )


def release_metadata_url_from_index(
    release: CatalogArtifactRelease,
    *,
    base_url: str | None = None,
) -> str:
    """Return the metadata URL for one root artifact index release."""

    resolved_base_url = base_url or os.getenv(
        ARTIFACT_BASE_URL_ENV, DEFAULT_CATALOG_ARTIFACT_BASE_URL
    )
    return urljoin(resolved_base_url.rstrip("/") + "/", release.metadata)


def default_release_metadata_url() -> str:
    """Return the package-pinned catalog metadata URL."""

    base_url = os.getenv(ARTIFACT_BASE_URL_ENV, DEFAULT_CATALOG_ARTIFACT_BASE_URL)
    return release_metadata_url(
        urljoin(
            base_url.rstrip("/") + "/",
            f"catalog/releases/{DEFAULT_CATALOG_VERSION}/{DEFAULT_CATALOG_DIGEST}/",
        )
    )


def release_metadata_url(locator: str) -> str:
    """Return the metadata URL for a release root URL or metadata URL."""

    if locator.endswith("metadata.json"):
        return locator
    return urljoin(locator.rstrip("/") + "/", "metadata.json")


def cache_root() -> Path:
    """Return the local cache root for downloaded catalog artifacts."""

    if raw := os.getenv(CACHE_DIR_ENV):
        return Path(raw).expanduser()
    return user_cache_path("chartcoach", appauthor=False)


def artifact_cache_root() -> Path:
    """Return the local cache root for chartcoach-owned artifacts."""

    return cache_root() / "artifacts"


def default_catalog_bundle(
    *,
    reporter: DownloadReporter | None = None,
) -> Path:
    """Return the cached package-pinned catalog bundle, downloading it when needed."""

    target = _cache_path(DEFAULT_CATALOG_VERSION, DEFAULT_CATALOG_DIGEST)
    if _cached_bundle_is_valid(target, expected_digest=DEFAULT_CATALOG_DIGEST):
        return target
    return download_catalog_bundle(
        default_release_metadata_url(),
        expected_version=DEFAULT_CATALOG_VERSION,
        expected_digest=DEFAULT_CATALOG_DIGEST,
        reporter=reporter,
    )


def default_index_path(
    *,
    table_name: str,
    reporter: DownloadReporter | None = None,
) -> Path:
    """Return the cached package-pinned LanceDB index for `table_name`."""

    if cached := _cached_default_index_path(table_name=table_name):
        return cached
    return download_index_artifact(
        default_release_metadata_url(),
        table_name=table_name,
        expected_version=DEFAULT_CATALOG_VERSION,
        expected_digest=DEFAULT_CATALOG_DIGEST,
        reporter=reporter,
    )


def download_catalog_bundle(
    metadata_url: str,
    *,
    expected_version: str | None = None,
    expected_digest: str | None = None,
    reporter: DownloadReporter | None = None,
) -> Path:
    """Download one catalog bundle into the local cache and return its path."""

    metadata, resolved_metadata_url = _read_release_metadata(metadata_url)
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
    if reporter is not None:
        reporter("catalog", resolved_metadata_url, target)

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

    _replace_catalog_artifacts(tmp, target, metadata)
    return target


def download_index_artifact(
    metadata_url: str,
    *,
    table_name: str,
    expected_version: str | None = None,
    expected_digest: str | None = None,
    reporter: DownloadReporter | None = None,
) -> Path:
    """Download one LanceDB archive artifact into the local cache and return it."""

    metadata, resolved_metadata_url = _read_release_metadata(metadata_url)
    if expected_version is not None and metadata.version != expected_version:
        raise ValueError(
            f"Catalog metadata version {metadata.version!r} does not match {expected_version!r}."
        )
    if expected_digest is not None and metadata.digest != expected_digest:
        raise ValueError(
            f"Catalog metadata digest {metadata.digest!r} does not match {expected_digest!r}."
        )

    artifact = _index_archive_artifact(metadata, table_name=table_name)
    release_path = _cache_path(metadata.version, metadata.digest)
    target = _index_cache_path(metadata.version, metadata.digest, artifact)
    release_path.mkdir(parents=True, exist_ok=True)
    (release_path / "metadata.json").write_text(_metadata_json(metadata))
    if _cached_index_is_valid(target, artifact):
        return target
    if reporter is not None:
        reporter("index", urljoin(resolved_metadata_url, artifact.path), target)

    tmp = target.with_name(target.name + ".tmp")
    archive_path = release_path / artifact.path
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True, exist_ok=True)
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    _download_file(urljoin(resolved_metadata_url, artifact.path), archive_path)
    _validate_file(archive_path, artifact)
    _extract_tar_archive(archive_path, tmp)

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
    return artifact_cache_root() / "catalog" / "releases" / version / digest


def _cached_default_index_path(*, table_name: str) -> Path | None:
    release_path = _cache_path(DEFAULT_CATALOG_VERSION, DEFAULT_CATALOG_DIGEST)
    metadata_path = release_path / "metadata.json"
    if not metadata_path.exists():
        return None
    try:
        metadata = CatalogReleaseMetadata.from_json(metadata_path.read_text())
        if (
            metadata.version != DEFAULT_CATALOG_VERSION
            or metadata.digest != DEFAULT_CATALOG_DIGEST
        ):
            return None
        artifact = _index_archive_artifact(metadata, table_name=table_name)
        target = _index_cache_path(metadata.version, metadata.digest, artifact)
        if _cached_index_is_valid(target, artifact):
            return target
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    return None


def _index_cache_path(
    version: str,
    digest: str,
    artifact: ArtifactDescriptor,
) -> Path:
    artifact_path = PurePosixPath(artifact.path)
    if artifact_path.name.endswith(".tar.gz"):
        return _cache_path(version, digest) / Path(*artifact_path.parent.parts) / "db"
    return _cache_path(version, digest) / Path(*artifact_path.parts)


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


def _replace_catalog_artifacts(
    tmp: Path,
    target: Path,
    metadata: CatalogReleaseMetadata,
) -> None:
    if target.exists() and not target.is_dir():
        target.unlink()
    target.mkdir(parents=True, exist_ok=True)
    for relative_path in (
        "metadata.json",
        *(artifact.path for artifact in _catalog_artifacts(metadata)),
    ):
        source = tmp / relative_path
        destination = target / relative_path
        if destination.exists() and destination.is_dir():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.replace(destination)
    shutil.rmtree(tmp)


def _cached_index_is_valid(path: Path, artifact: ArtifactDescriptor) -> bool:
    table_name = artifact.extra.get("table")
    if not path.is_dir() or not isinstance(table_name, str):
        return False
    if not (path / f"{table_name}.lance").is_dir():
        return False
    if archive_path := _index_archive_cache_path(path, artifact):
        if not archive_path.is_file():
            return False
        try:
            _validate_file(archive_path, artifact)
        except (OSError, ValueError):
            return False
    legacy_marker = path / "artifact.json"
    if legacy_marker.is_file():
        legacy_marker.unlink(missing_ok=True)
    return True


def _index_archive_cache_path(
    path: Path,
    artifact: ArtifactDescriptor,
) -> Path | None:
    artifact_path = PurePosixPath(artifact.path)
    if not artifact_path.name.endswith(".tar.gz"):
        return None
    return path.parent / artifact_path.name


def _read_url_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "chartcoach"})
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def _read_release_metadata(url: str) -> tuple[CatalogReleaseMetadata, str]:
    raw = json.loads(_read_url_text(url))
    if not isinstance(raw, Mapping):
        raise ValueError("Catalog release metadata must be an object.")
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


def _catalog_artifacts(
    metadata: CatalogReleaseMetadata,
) -> tuple[ArtifactDescriptor, ...]:
    return tuple(
        artifact
        for artifact in metadata.artifacts
        if artifact.kind in CATALOG_ARTIFACT_KINDS
    )


def _index_archive_artifact(
    metadata: CatalogReleaseMetadata,
    *,
    table_name: str,
) -> ArtifactDescriptor:
    for artifact in metadata.artifacts:
        if (
            artifact.kind == "lancedb-index"
            and artifact.format == "tar+gzip"
            and artifact.extra.get("table") == table_name
        ):
            return artifact
    raise ValueError(
        f"Catalog release metadata is missing a {table_name!r} LanceDB archive."
    )


def _extract_tar_archive(archive_path: Path, target: Path) -> None:
    target_root = target.resolve(strict=False)
    with tarfile.open(archive_path, "r:gz") as archive:
        for member in archive.getmembers():
            output_path = _archive_output_path(member.name, target_root)
            if member.isdir():
                output_path.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                output_path.parent.mkdir(parents=True, exist_ok=True)
                source = archive.extractfile(member)
                if source is None:
                    raise ValueError(
                        f"Unreadable LanceDB archive member: {member.name!r}"
                    )
                with source, output_path.open("wb") as output:
                    shutil.copyfileobj(source, output)
            else:
                raise ValueError(f"Unsafe LanceDB archive member: {member.name!r}")


def _archive_output_path(member_name: str, target: Path) -> Path:
    path = PurePosixPath(member_name)
    if (
        "\\" in member_name
        or path.is_absolute()
        or ".." in path.parts
        or any(":" in part for part in path.parts)
    ):
        raise ValueError(f"Unsafe LanceDB archive member: {member_name!r}")
    output_path = target.joinpath(*path.parts).resolve(strict=False)
    if not output_path.is_relative_to(target):
        raise ValueError(f"Unsafe LanceDB archive member: {member_name!r}")
    return output_path


def _validate_relative_artifact_path(path: str) -> None:
    parsed = PurePosixPath(path)
    if parsed.is_absolute() or ".." in parsed.parts:
        raise ValueError(f"Catalog artifact path must be relative: {path!r}")


def _relative_index_path(value: Mapping[str, object], key: str) -> str:
    path = _string(value, key)
    _validate_relative_artifact_path(path)
    return path


def _version_sort_key(value: str) -> tuple[tuple[int, int | str], ...]:
    parts = value.replace("-", ".").split(".")
    return tuple((0, int(part)) if part.isdecimal() else (1, part) for part in parts)


def _string(value: Mapping[str, object], key: str) -> str:
    raw = value.get(key)
    if not isinstance(raw, str) or not raw:
        raise ValueError(f"Catalog release metadata {key!r} must be a string.")
    return raw


def _int(value: Mapping[str, object], key: str) -> int:
    raw = value.get(key)
    if not isinstance(raw, int) or raw < 0:
        raise ValueError(
            f"Catalog release metadata {key!r} must be a non-negative integer."
        )
    return raw

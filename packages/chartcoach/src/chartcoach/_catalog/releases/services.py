from __future__ import annotations

import json
import stat
from pathlib import Path, PurePosixPath

from .hashing import release_digest, sha256_file
from .models import CatalogRelease, ReleaseArtifact

_MAX_RELEASE_JSON_BYTES = 1024 * 1024
_MAX_RUNTIME_ARTIFACT_BYTES = 64 * 1024**2
MAX_RELEASE_ARTIFACT_BYTES = 1024**3


def validate_runtime_release(root: Path) -> CatalogRelease:
    """Validate and open the core files in a local release."""

    release_path = root / "release.json"
    _require_regular_file(root, release_path, label="Catalog release record")
    release = CatalogRelease.from_mapping(_read_release_json(release_path))
    if release.digest != release_digest(release.artifacts):
        raise ValueError("Catalog release digest does not match its artifacts.")

    for path, artifact in release.artifacts.items():
        _validate_artifact(root, path, artifact)

    return release


def _read_release_json(path: Path) -> object:
    if path.stat().st_size > _MAX_RELEASE_JSON_BYTES:
        raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
    with path.open("rb") as source:
        data = source.read(_MAX_RELEASE_JSON_BYTES + 1)
    if len(data) > _MAX_RELEASE_JSON_BYTES:
        raise ValueError("Catalog release JSON exceeds the 1 MiB limit.")
    return json.loads(data.decode("utf-8"))


def _validate_artifact(
    root: Path,
    artifact_path: str,
    artifact: ReleaseArtifact,
) -> None:
    validate_artifact_size(artifact_path, artifact)

    path = root.joinpath(*PurePosixPath(artifact_path).parts)
    _require_regular_file(root, path, label=f"Catalog artifact {artifact_path!r}")
    size = path.stat().st_size
    if size != artifact.bytes:
        raise ValueError(f"Catalog artifact byte count does not match: {artifact_path}")
    if sha256_file(path) != artifact.sha256:
        raise ValueError(f"Catalog artifact SHA-256 does not match: {artifact_path}")


def validate_artifact_size(artifact_path: str, artifact: ReleaseArtifact) -> None:
    """Reject artifact sizes beyond the local and published release limits."""

    if artifact.bytes > MAX_RELEASE_ARTIFACT_BYTES:
        raise ValueError(f"Catalog artifact exceeds the 1 GiB limit: {artifact_path}")
    if (
        artifact_path in {"MANIFEST.md", "entries.parquet"}
        and artifact.bytes > _MAX_RUNTIME_ARTIFACT_BYTES
    ):
        raise ValueError(f"Runtime artifact exceeds the 64 MiB limit: {artifact_path}")


def _require_regular_file(root: Path, path: Path, *, label: str) -> None:
    if component := _symlink_component(root, path):
        raise ValueError(f"{label} cannot contain a symlink: {component}")
    try:
        metadata = path.stat()
    except FileNotFoundError:
        raise ValueError(f"{label} is missing: {path}") from None
    if not stat.S_ISREG(metadata.st_mode):
        raise ValueError(f"{label} must be a regular file: {path}")


def _symlink_component(root: Path, path: Path) -> Path | None:
    root = root.absolute()
    try:
        relative = path.absolute().relative_to(root)
    except ValueError:
        return path
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return current
    return None


__all__ = ["validate_artifact_size", "validate_runtime_release"]

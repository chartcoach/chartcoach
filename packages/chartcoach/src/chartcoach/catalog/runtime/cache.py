from __future__ import annotations

import hashlib
import os
import shutil
from collections.abc import Mapping
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Literal
from uuid import uuid4

from platformdirs import user_cache_path

from ...constants import LANCE_DOCUMENT_TABLE
from ..errors import CatalogError
from ..releases import ReleaseArtifact
from ..releases.archive import extract_tar_archive
from ..releases.hashing import sha256_file
from .transport import remote_chunks

_CACHE_MARKER = ".complete"


def cache_remote_artifact(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    path: str,
    artifact: ReleaseArtifact,
) -> Path:
    target = _cache_root() / "artifacts" / artifact.sha256
    if _cached_artifact_is_valid(target, artifact):
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.parent / f".{artifact.sha256}.{uuid4().hex}.tmp"
    digest = hashlib.sha256()
    size = 0
    try:
        with staging.open("xb") as output:
            for chunk in remote_chunks(
                uri,
                transport=transport,
                storage_options=storage_options,
            ):
                view = memoryview(chunk)
                size += view.nbytes
                if size > artifact.bytes:
                    raise CatalogError(f"Catalog artifact byte count mismatch: {path}")
                digest.update(view)
                output.write(view)
        if size != artifact.bytes:
            raise CatalogError(f"Catalog artifact byte count mismatch: {path}")
        if digest.hexdigest() != artifact.sha256:
            raise CatalogError(f"Catalog artifact SHA-256 mismatch: {path}")
        os.replace(staging, target)
    finally:
        staging.unlink(missing_ok=True)
    return target


def verify_local_artifact(
    base: Path,
    path: Path,
    artifact_path: str,
    artifact: ReleaseArtifact,
) -> None:
    try:
        if _symlink_component(base, path) is not None or not path.is_file():
            raise CatalogError(f"Catalog artifact is missing: {artifact_path}")
        size = path.stat().st_size
    except OSError as exc:
        raise CatalogError(f"Could not read catalog artifact: {artifact_path}") from exc
    if size != artifact.bytes:
        raise CatalogError(f"Catalog artifact byte count mismatch: {artifact_path}")
    if sha256_file(path) != artifact.sha256:
        raise CatalogError(f"Catalog artifact SHA-256 mismatch: {artifact_path}")


def cached_index(archive: Path, digest: str, *, refresh: bool = False) -> Path:
    target = _cache_root() / "indexes" / digest
    if not refresh and _index_cache_is_complete(target, digest):
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(target, ignore_errors=True)
    with TemporaryDirectory(prefix=f".{digest}.", dir=target.parent) as temporary:
        staged = Path(temporary) / "index"
        extract_tar_archive(archive, staged)
        if not (staged / f"{LANCE_DOCUMENT_TABLE}.lance").is_dir():
            raise CatalogError(
                f"LanceDB archive does not contain table: {LANCE_DOCUMENT_TABLE}"
            )
        (staged / _CACHE_MARKER).write_text(digest, encoding="ascii")
        try:
            os.replace(staged, target)
        except FileExistsError:
            if not _index_cache_is_complete(target, digest):
                raise
    return target


def _cached_artifact_is_valid(path: Path, artifact: ReleaseArtifact) -> bool:
    try:
        return (
            path.is_file()
            and path.stat().st_size == artifact.bytes
            and sha256_file(path) == artifact.sha256
        )
    except OSError:
        return False


def _symlink_component(base: Path, path: Path) -> Path | None:
    base = base.absolute()
    try:
        relative = path.absolute().relative_to(base)
    except ValueError:
        return path
    current = base
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return current
    return None


def _index_cache_is_complete(target: Path, digest: str) -> bool:
    try:
        return (target / _CACHE_MARKER).read_text(encoding="ascii") == digest and (
            target / f"{LANCE_DOCUMENT_TABLE}.lance"
        ).is_dir()
    except (OSError, UnicodeDecodeError):
        return False


def _cache_root() -> Path:
    return user_cache_path("chartcoach", appauthor=False)


__all__ = ["cache_remote_artifact", "cached_index", "verify_local_artifact"]

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
from collections.abc import Mapping
from pathlib import Path
from typing import Literal
from uuid import uuid4

from platformdirs import user_cache_path

from ...constants import LANCE_DOCUMENT_TABLE
from ..errors import CatalogError, CatalogIntegrityError
from ..releases import ReleaseArtifact
from ..releases.archive import extract_tar_archive
from ..releases.hashing import sha256_file
from .transport import remote_chunks

_CACHE_MARKER = ".complete"
_INDEX_CACHE_NAMESPACE = "indexes-v2"
_CURRENT_GENERATION = "current.json"


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
                    raise CatalogIntegrityError(
                        f"Catalog artifact byte count mismatch: {path}"
                    )
                digest.update(view)
                output.write(view)
        if size != artifact.bytes:
            raise CatalogIntegrityError(f"Catalog artifact byte count mismatch: {path}")
        if digest.hexdigest() != artifact.sha256:
            raise CatalogIntegrityError(f"Catalog artifact SHA-256 mismatch: {path}")
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
            raise CatalogIntegrityError(f"Catalog artifact is missing: {artifact_path}")
        size = path.stat().st_size
    except OSError as exc:
        raise CatalogIntegrityError(
            f"Could not read catalog artifact: {artifact_path}"
        ) from exc
    if size != artifact.bytes:
        raise CatalogIntegrityError(
            f"Catalog artifact byte count mismatch: {artifact_path}"
        )
    if sha256_file(path) != artifact.sha256:
        raise CatalogIntegrityError(
            f"Catalog artifact SHA-256 mismatch: {artifact_path}"
        )


def cached_index(
    archive: Path,
    digest: str,
    *,
    refresh: bool = False,
    protected: bool = True,
) -> Path:
    if protected and not shared_index_cache_supported():
        raise CatalogError(
            "Protected shared index extraction is unavailable on this platform.",
            code="unavailable_capability",
            hints=["Pass a new caller-owned directory to catalog.index(...)."],
        )
    namespace = _INDEX_CACHE_NAMESPACE if protected else "indexes-internal-v2"
    root = _cache_root() / namespace / digest
    if not refresh:
        current = _current_generation(root, digest, protected=protected)
        if current is not None:
            return current

    generations = root / "generations"
    generations.mkdir(parents=True, exist_ok=True)
    generation = uuid4().hex
    staged = root / f".{generation}.tmp"
    published = generations / generation
    try:
        extract_tar_archive(archive, staged)
        if not (staged / f"{LANCE_DOCUMENT_TABLE}.lance").is_dir():
            raise CatalogIntegrityError(
                f"LanceDB archive does not contain table: {LANCE_DOCUMENT_TABLE}"
            )
        (staged / _CACHE_MARKER).write_text(digest, encoding="ascii")
        os.replace(staged, published)
        if protected:
            try:
                _seal_tree(published)
            except BaseException:
                _make_tree_writable(published)
                shutil.rmtree(published, ignore_errors=True)
                raise
        _publish_current(root, digest=digest, generation=generation)
    finally:
        if staged.exists():
            _make_tree_writable(staged)
            shutil.rmtree(staged, ignore_errors=True)
    return published


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


def shared_index_cache_supported() -> bool:
    """Return whether POSIX permission bits can protect shared extractions."""

    return os.name == "posix"


def _current_generation(root: Path, digest: str, *, protected: bool) -> Path | None:
    try:
        value = json.loads((root / _CURRENT_GENERATION).read_text(encoding="utf-8"))
        if not isinstance(value, dict) or set(value) != {"digest", "generation"}:
            return None
        generation = value["generation"]
        if value["digest"] != digest or not isinstance(generation, str):
            return None
        if len(generation) != 32 or any(
            character not in "0123456789abcdef" for character in generation
        ):
            return None
        target = root / "generations" / generation
        return (
            target
            if _generation_is_complete(target, digest, protected=protected)
            else None
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def _generation_is_complete(target: Path, digest: str, *, protected: bool) -> bool:
    try:
        if protected and (target.stat().st_mode & 0o222) != 0:
            return False
        if (target / _CACHE_MARKER).read_text(encoding="ascii") != digest:
            return False
        table = target / f"{LANCE_DOCUMENT_TABLE}.lance"
        return table.is_dir() and (not protected or (table.stat().st_mode & 0o222) == 0)
    except (OSError, UnicodeDecodeError):
        return False


def _publish_current(root: Path, *, digest: str, generation: str) -> None:
    temporary = root / f".{_CURRENT_GENERATION}.{uuid4().hex}.tmp"
    try:
        temporary.write_text(
            json.dumps({"digest": digest, "generation": generation}, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, root / _CURRENT_GENERATION)
    finally:
        temporary.unlink(missing_ok=True)


def _seal_tree(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        path.chmod(0o555 if path.is_dir() else 0o444)
    root.chmod(0o555)


def _make_tree_writable(root: Path) -> None:
    for path in [root, *root.rglob("*")]:
        try:
            mode = path.stat().st_mode
            path.chmod(mode | stat.S_IWUSR | (stat.S_IXUSR if path.is_dir() else 0))
        except OSError:
            continue


def _cache_root() -> Path:
    return user_cache_path("chartcoach", appauthor=False)


__all__ = [
    "cache_remote_artifact",
    "cached_index",
    "shared_index_cache_supported",
    "verify_local_artifact",
]

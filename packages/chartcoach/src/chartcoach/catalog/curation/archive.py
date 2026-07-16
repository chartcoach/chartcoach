from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Protocol

from obspec import Put

from ..releases.archive import _validated_tar_archive


class ArchiveStore(Put, Protocol):
    """Writes regular archive members to object storage."""


def extract_tar_archive(
    archive_path: Path,
    store: ArchiveStore,
    *,
    prefix: str,
) -> tuple[str, ...]:
    """Extract regular tar members through ``store`` below ``prefix``."""

    extracted_members: list[str] = []
    with _validated_tar_archive(archive_path) as (archive, members):
        for member, member_path in members:
            if member.isdir():
                continue
            source = archive.extractfile(member)
            if source is None:
                raise ValueError(f"Unreadable LanceDB archive member: {member.name!r}")
            target = _object_key(prefix, member_path.as_posix())
            with source:
                store.put(target, source)
            extracted_members.append(member_path.as_posix())
    return tuple(sorted(extracted_members))


def _object_key(*parts: str) -> str:
    return PurePosixPath(*parts).as_posix()


__all__ = ["ArchiveStore", "extract_tar_archive"]

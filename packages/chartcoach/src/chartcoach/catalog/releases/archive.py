from __future__ import annotations

import shutil
import tarfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path, PurePosixPath

from .models import safe_relative_path

_MAX_ARCHIVE_MEMBERS = 100_000
_MAX_ARCHIVE_MEMBER_BYTES = 2 * 1024**3
_MAX_ARCHIVE_TOTAL_BYTES = 8 * 1024**3


def extract_tar_archive(archive_path: Path, target: Path) -> None:
    """Extract a bounded regular-file tar archive into a new directory."""

    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir()
    try:
        with _validated_tar_archive(archive_path) as (archive, members):
            for member, member_path in members:
                output = target.joinpath(*member_path.parts)
                if member.isdir():
                    output.mkdir(parents=True, exist_ok=True)
                    continue
                output.parent.mkdir(parents=True, exist_ok=True)
                source = archive.extractfile(member)
                if source is None:
                    raise ValueError(f"Unreadable archive member: {member.name!r}")
                with source, output.open("wb") as destination:
                    shutil.copyfileobj(source, destination)
    except BaseException:
        shutil.rmtree(target, ignore_errors=True)
        raise


@contextmanager
def _validated_tar_archive(
    archive_path: Path,
) -> Iterator[
    tuple[tarfile.TarFile, tuple[tuple[tarfile.TarInfo, PurePosixPath], ...]]
]:
    with tarfile.open(archive_path, mode="r:gz") as archive:
        members: list[tuple[tarfile.TarInfo, PurePosixPath]] = []
        files: dict[str, str] = {}
        directories: dict[str, str] = {}
        total_bytes = 0
        for member in archive:
            if len(members) >= _MAX_ARCHIVE_MEMBERS:
                raise ValueError("LanceDB archive contains too many members.")
            path = PurePosixPath(
                safe_relative_path(member.name, label="Unsafe LanceDB archive member")
            )
            if not member.isdir() and not member.isfile():
                raise ValueError(f"Unsafe LanceDB archive member: {member.name!r}")
            if member.size < 0 or member.size > _MAX_ARCHIVE_MEMBER_BYTES:
                raise ValueError(
                    f"LanceDB archive member is too large: {member.name!r}"
                )
            total_bytes += member.size
            if total_bytes > _MAX_ARCHIVE_TOTAL_BYTES:
                raise ValueError("LanceDB archive expands beyond the 8 GiB limit.")
            _record_member(
                path,
                is_directory=member.isdir(),
                files=files,
                directories=directories,
            )
            members.append((member, path))
        yield archive, tuple(members)


def _record_member(
    path: PurePosixPath,
    *,
    is_directory: bool,
    files: dict[str, str],
    directories: dict[str, str],
) -> None:
    value = path.as_posix()
    folded = value.casefold()
    previous = files.get(folded) or directories.get(folded)
    if previous is not None:
        raise ValueError(f"LanceDB archive members collide: {previous!r}, {value!r}")
    for length in range(1, len(path.parts)):
        parent = PurePosixPath(*path.parts[:length]).as_posix()
        parent_folded = parent.casefold()
        if previous := files.get(parent_folded):
            raise ValueError(
                f"LanceDB archive members collide: {previous!r}, {value!r}"
            )
        directories.setdefault(parent_folded, parent)
    namespace = directories if is_directory else files
    namespace[folded] = value


__all__ = ["extract_tar_archive"]

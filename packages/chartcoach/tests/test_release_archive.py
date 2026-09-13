from __future__ import annotations

import tarfile
from io import BytesIO
from pathlib import Path

import pytest
from chartcoach._catalog.releases.archive import extract_tar_archive


def test_extracts_regular_files(tmp_path: Path) -> None:
    archive = _archive(tmp_path, {"documents.lance/data": b"content"})

    target = tmp_path / "index"
    extract_tar_archive(archive, target)

    assert (target / "documents.lance" / "data").read_bytes() == b"content"


def test_rejects_paths_outside_the_target_and_cleans_up(tmp_path: Path) -> None:
    archive = _archive(tmp_path, {"../outside": b"unsafe"})
    target = tmp_path / "index"

    with pytest.raises(ValueError, match="Unsafe LanceDB archive member"):
        extract_tar_archive(archive, target)

    assert not target.exists()
    assert not (tmp_path / "outside").exists()


def test_rejects_case_insensitive_namespace_collisions(tmp_path: Path) -> None:
    archive = _archive(tmp_path, {"Table": b"first", "table": b"second"})

    with pytest.raises(ValueError, match="archive members collide"):
        extract_tar_archive(archive, tmp_path / "index")


def test_does_not_follow_an_existing_target_symlink(tmp_path: Path) -> None:
    archive = _archive(tmp_path, {"data": b"new"})
    outside = tmp_path / "outside"
    outside.mkdir()
    target = tmp_path / "index"
    target.symlink_to(outside, target_is_directory=True)

    with pytest.raises(FileExistsError):
        extract_tar_archive(archive, target)

    assert list(outside.iterdir()) == []


def _archive(tmp_path: Path, members: dict[str, bytes]) -> Path:
    path = tmp_path / "index.tar.gz"
    with tarfile.open(path, "w:gz") as archive:
        for name, payload in members.items():
            member = tarfile.TarInfo(name)
            member.size = len(payload)
            archive.addfile(member, BytesIO(payload))
    return path

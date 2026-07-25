from __future__ import annotations

from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
import tarfile

from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest, sha256_file


_RELEASE_FIXTURE = Path(__file__).parents[3] / "fixtures" / "catalog-release"


def test_base_catalog_import_does_not_load_optional_capabilities() -> None:
    script = f"""
import importlib.abc
import sys

class BlockOptional(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {{"lancedb", "mcp", "obstore", "obspec", "pyarrow", "umap"}}:
            raise ModuleNotFoundError(f"blocked optional module: {{fullname}}", name=fullname)
        return None

sys.meta_path.insert(0, BlockOptional())
import chartcoach
catalog = chartcoach.open_catalog({str(_RELEASE_FIXTURE)!r})
assert catalog.release is not None
assert len(catalog) > 0
assert not any(name.split(".", 1)[0] in {{"lancedb", "mcp", "obstore", "obspec", "pyarrow", "umap"}} for name in sys.modules)
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_cloud_source_reports_the_cloud_extra_when_obstore_is_absent() -> None:
    script = """
import importlib.abc

class BlockObstore(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "obstore" or fullname.startswith("obstore."):
            raise ModuleNotFoundError("blocked obstore", name=fullname)
        return None

import sys
sys.meta_path.insert(0, BlockObstore())
from chartcoach import open_catalog
try:
    open_catalog("s3://bucket/catalog.json")
except ModuleNotFoundError as exc:
    assert "chartcoach[cloud]" in str(exc)
else:
    raise AssertionError("cloud source unexpectedly opened")
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_release_profile_reports_the_index_extra_when_lancedb_is_absent(
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    root.mkdir()
    for path in ("MANIFEST.md", "entries.parquet"):
        (root / path).write_bytes((_RELEASE_FIXTURE / path).read_bytes())
    archive = root / "profiles" / "test" / "index.tar.gz"
    archive.parent.mkdir(parents=True)
    with tarfile.open(archive, "w:gz") as output:
        member = tarfile.TarInfo("documents.lance/placeholder")
        payload = b"placeholder"
        member.size = len(payload)
        output.addfile(member, BytesIO(payload))
    artifacts = {
        path: ReleaseArtifact(
            sha256=sha256_file(root / path),
            bytes=(root / path).stat().st_size,
        )
        for path in (
            "MANIFEST.md",
            "entries.parquet",
            "profiles/test/index.tar.gz",
        )
    }
    release = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    (root / "release.json").write_text(json.dumps(release.to_record()))
    script = f"""
import importlib.abc

class BlockLanceDB(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "lancedb" or fullname.startswith("lancedb."):
            raise ModuleNotFoundError("blocked lancedb", name=fullname)
        return None

import sys
sys.meta_path.insert(0, BlockLanceDB())
from chartcoach import open_index
try:
    open_index({str(root)!r}, profile="test")
except ModuleNotFoundError as exc:
    assert "chartcoach[index]" in str(exc)
else:
    raise AssertionError("release profile unexpectedly opened")
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr

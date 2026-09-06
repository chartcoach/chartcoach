from __future__ import annotations

import json
import os
import subprocess
import sys
import tarfile
from io import BytesIO
from pathlib import Path

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import open_catalog
from chartcoach.catalog.manifest import manifest_digest
from chartcoach.catalog.model import Catalog
from chartcoach.catalog.profiles import EmbeddingBinding, ProfileMetadata
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest, sha256_file

_RELEASE_FIXTURE = Path(__file__).parents[3] / "fixtures" / "catalog-release"


def test_base_catalog_contract_works_without_optional_dependencies() -> None:
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
assert catalog.query(contains="labels", limit=2).height > 0
assert catalog.read(ids=["direct-labels"], source_detail="minimal")
assert catalog.cite(ids=["direct-labels"])
assert catalog.sql("select count(*) as rows from guidelines")["rows"]
assert catalog.describe()["release_digest"] == catalog.release.digest
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_cloud_location_reports_the_cloud_extra_when_obstore_is_absent() -> None:
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
    raise AssertionError("cloud location unexpectedly opened")
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


@pytest.mark.curation
@pytest.mark.search
def test_profile_description_works_without_index_or_projection_dependencies(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.catalog.curation import EmbeddingProfile, build_release

    profile = "test-metadata"
    release = tmp_path / "release"
    build_release(
        sample_catalog,
        release,
        profiles={
            profile: EmbeddingProfile(deterministic_embedding("metadata-profile"))
        },
    )
    script = f"""
import importlib.abc
import sys

class BlockIndexDependencies(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {{"lancedb", "pyarrow", "umap"}}:
            raise ModuleNotFoundError(f"blocked optional module: {{fullname}}", name=fullname)
        return None

sys.meta_path.insert(0, BlockIndexDependencies())
from chartcoach import open_catalog
catalog = open_catalog({str(release)!r})
description = catalog.describe(profile={profile!r})
assert description["profile"]["dimensions"] == 4
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


@pytest.mark.curation
@pytest.mark.search
def test_projection_free_profile_builds_without_umap(tmp_path: Path) -> None:
    release = tmp_path / "release"
    script = f"""
import importlib.abc
import sys

class BlockUmap(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "umap" or fullname.startswith("umap."):
            raise ModuleNotFoundError("blocked umap", name=fullname)
        return None

sys.meta_path.insert(0, BlockUmap())
from lancedb_embedding_fixture import registered_embedding
from chartcoach import open_catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release
build_release(
    open_catalog({str(_RELEASE_FIXTURE)!r}),
    {str(release)!r},
    profiles={{"test-no-projection": EmbeddingProfile(registered_embedding())}},
)
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        env={
            **os.environ,
            "PYTHONPATH": str(Path(__file__).parent),
        },
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_mcp_command_reports_the_extra_when_mcp_is_absent() -> None:
    script = """
import importlib.abc

class BlockMCP(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "mcp" or fullname.startswith("mcp."):
            raise ModuleNotFoundError("blocked mcp", name=fullname)
        return None

import sys
sys.meta_path.insert(0, BlockMCP())
from chartcoach.cli.main import main
from click.testing import CliRunner

result = CliRunner().invoke(main, ["mcp"])
assert result.exit_code == 1
assert "chartcoach[mcp]" in result.output
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_index_profile_reports_the_index_extra_when_lancedb_is_absent(
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
    catalog = open_catalog(_RELEASE_FIXTURE)
    metadata_path = archive.parent / "profile.json"
    metadata_path.write_bytes(
        ProfileMetadata(
            entries_digest=catalog.entries_digest(),
            manifest_digest=manifest_digest(catalog.manifest.markdown),
            embedding_functions=(EmbeddingBinding(name="test-missing", model={}),),
            dimensions=4,
            distance_metric="cosine",
            python_requirements={},
            lancedb_version="0.38.0",
            projection=None,
        ).to_bytes()
    )
    artifacts = {
        path: ReleaseArtifact(
            sha256=sha256_file(root / path),
            bytes=(root / path).stat().st_size,
        )
        for path in (
            "MANIFEST.md",
            "entries.parquet",
            "profiles/test/profile.json",
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
from chartcoach import CatalogError, open_catalog
try:
    open_catalog({str(root)!r}).index("test")
except CatalogError as exc:
    assert exc.code == "unavailable_capability"
    assert "chartcoach[index]" in str(exc)
else:
    raise AssertionError("index profile unexpectedly opened")
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr

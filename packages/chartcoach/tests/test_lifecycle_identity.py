from __future__ import annotations

import json
import subprocess
from pathlib import Path

import chartcoach
import polars as pl
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogManifest
from chartcoach.catalog.curation import (
    EmbeddingProfile,
    build_release,
    publish_release,
    select_release,
)
from chartcoach.catalog.manifest import manifest_digest
from chartcoach.catalog.releases import CatalogRelease

pytestmark = pytest.mark.curation


def test_entry_manifest_and_profile_changes_have_independent_digests(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    baseline = build_release(sample_catalog, tmp_path / "baseline")

    entries_catalog = Catalog(
        sample_catalog.to_frame().with_columns(
            pl.when(pl.col("id") == "direct-labels")
            .then(pl.lit("Changed guidance"))
            .otherwise(pl.col("description"))
            .alias("description")
        ),
        manifest=sample_catalog.manifest,
    )
    entries = build_release(entries_catalog, tmp_path / "entries")

    manifest_catalog = Catalog(
        sample_catalog.to_frame(),
        manifest=CatalogManifest.from_text(
            sample_catalog.manifest.markdown.replace(
                "Actionable guidance for applying the guideline.",
                "Guidance that states the recommended action.",
            )
        ),
    )
    manifest = build_release(manifest_catalog, tmp_path / "manifest")

    profiled = build_release(
        sample_catalog,
        tmp_path / "profile",
        profiles={
            "test-identity": EmbeddingProfile(
                deterministic_embedding("lifecycle-profile")
            )
        },
    )

    assert entries_catalog.entries_digest() != sample_catalog.entries_digest()
    assert manifest_catalog.entries_digest() == sample_catalog.entries_digest()
    assert manifest_digest(manifest_catalog.manifest.markdown) != manifest_digest(
        sample_catalog.manifest.markdown
    )
    assert entries.digest != baseline.digest
    assert manifest.digest != baseline.digest
    assert profiled.digest != baseline.digest
    assert baseline.artifact("MANIFEST.md") == entries.artifact("MANIFEST.md")
    assert baseline.artifact("entries.parquet") == manifest.artifact("entries.parquet")


def test_software_release_script_accepts_the_package_version() -> None:
    root = Path(__file__).parents[3]

    result = subprocess.run(
        [
            root / "scripts" / "release.sh",
            "check-version",
            f"v{chartcoach.__version__}",
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_software_version_is_not_part_of_catalog_release_identity(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    baseline = build_release(sample_catalog, tmp_path / "baseline")
    monkeypatch.setattr(chartcoach, "__version__", "999.0.0")

    rebuilt = build_release(sample_catalog, tmp_path / "rebuilt")

    assert rebuilt == baseline


def test_selection_changes_only_the_mutable_catalog_pointer(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    baseline_root = tmp_path / "baseline"
    baseline = build_release(sample_catalog, baseline_root)
    changed_catalog = Catalog(
        sample_catalog.to_frame().with_columns(
            pl.when(pl.col("id") == "direct-labels")
            .then(pl.lit("Changed guidance"))
            .otherwise(pl.col("description"))
            .alias("description")
        ),
        manifest=sample_catalog.manifest,
    )
    changed_root = tmp_path / "changed"
    changed = build_release(changed_catalog, changed_root)
    destination_root = tmp_path / "published"
    destination = destination_root.as_uri()
    publish_release(baseline_root, destination)
    publish_release(changed_root, destination)
    release_paths = {
        release.digest: destination_root
        / "catalog"
        / "releases"
        / release.digest
        / "release.json"
        for release in (baseline, changed)
    }
    immutable_descriptors = {
        digest: path.read_bytes() for digest, path in release_paths.items()
    }

    select_release(baseline.digest, destination)
    select_release(changed.digest, destination)

    selection = CatalogRelease.from_mapping(
        json.loads((destination_root / "catalog.json").read_text())
    )
    assert selection == changed
    assert {
        digest: path.read_bytes() for digest, path in release_paths.items()
    } == immutable_descriptors

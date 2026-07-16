from __future__ import annotations

import json
from pathlib import Path

from click.testing import CliRunner
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation.release_builder import build_catalog_release
from chartcoach.catalog.paths import paths
from chartcoach.catalog.releases import CatalogRelease
from chartcoach.cli.main import main


pytestmark = pytest.mark.curation


def test_release_publish_and_select_create_local_store(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    release = build_catalog_release(sample_catalog, root=release_root)
    store = tmp_path / "store"

    published = runner.invoke(
        main,
        [
            "catalog",
            "release",
            "publish",
            str(release_root),
            "--store",
            store.as_uri(),
            "--format",
            "json",
        ],
    )
    selected = runner.invoke(
        main,
        [
            "catalog",
            "release",
            "select",
            release.digest,
            "--store",
            store.as_uri(),
            "--format",
            "json",
        ],
    )

    assert published.exit_code == 0, published.output
    assert selected.exit_code == 0, selected.output
    selected_release = CatalogRelease.from_mapping(
        json.loads((store / paths.selected()).read_text())
    )
    assert selected_release == release

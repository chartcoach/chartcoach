from __future__ import annotations

import json
from pathlib import Path

import pytest
from chartcoach import Catalog
from chartcoach._catalog.paths import paths
from chartcoach._catalog.releases import CatalogRelease
from chartcoach.cli.main import main
from chartcoach.curation import build_release, publish_release, select_release
from click.testing import CliRunner

pytestmark = pytest.mark.curation


def test_release_publish_and_select_create_local_store(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    release = build_release(sample_catalog, release_root)
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


def test_release_validate_accepts_local_candidate_and_selected_catalog(
    runner: CliRunner, sample_catalog: Catalog, tmp_path: Path
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = (tmp_path / "store").as_uri()
    publish_release(root, store)
    select_release(release.digest, store)

    for arguments in (
        [str(root)],
        ["--store", store, "--digest", release.digest],
        ["--store", store, "--expect-digest", release.digest],
    ):
        result = runner.invoke(
            main, ["catalog", "release", "validate", *arguments, "--format", "json"]
        )
        assert result.exit_code == 0, result.output
        assert CatalogRelease.from_mapping(json.loads(result.stdout)) == release

    wrong = runner.invoke(
        main,
        [
            "catalog",
            "release",
            "validate",
            "--store",
            store,
            "--expect-digest",
            "0" * 64,
            "--format",
            "json",
        ],
    )
    assert wrong.exit_code == 1
    assert wrong.stdout == ""
    assert release.digest in wrong.stderr


@pytest.mark.parametrize(
    "arguments",
    [
        [],
        ["release", "--store", "file:///unused"],
        ["release", "--digest", "0" * 64],
        ["release", "--expect-digest", "0" * 64],
        [
            "--store",
            "file:///unused",
            "--digest",
            "0" * 64,
            "--expect-digest",
            "0" * 64,
        ],
        ["--store", "file:///unused", "--digest", "invalid"],
        ["--store", "file:///unused", "--expect-digest", "invalid"],
    ],
)
def test_release_validate_rejects_ambiguous_or_invalid_selection_arguments(
    runner: CliRunner, arguments: list[str]
) -> None:
    result = runner.invoke(main, ["catalog", "release", "validate", *arguments])

    assert result.exit_code == 2
    assert "Error:" in result.stderr


def test_release_select_dry_run_validates_fresh_candidate_bytes(
    runner: CliRunner, sample_catalog: Catalog, tmp_path: Path
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = tmp_path / "store"
    publish_release(root, store.as_uri())
    arguments = [
        "catalog",
        "release",
        "select",
        release.digest,
        "--store",
        store.as_uri(),
        "--dry-run",
        "--format",
        "json",
    ]

    preview = runner.invoke(main, arguments)

    assert preview.exit_code == 0, preview.output
    assert json.loads(preview.stdout) == [
        {"digest": release.digest, "path": "catalog.json"}
    ]
    assert not (store / "catalog.json").exists()
    (store / paths.release(release.digest).artifact("entries.parquet")).write_bytes(
        b"corrupt"
    )
    rejected = runner.invoke(main, arguments)
    assert rejected.exit_code == 1
    assert rejected.stdout == ""
    assert not (store / "catalog.json").exists()

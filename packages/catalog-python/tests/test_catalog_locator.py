from __future__ import annotations

from pathlib import Path
from typing import NoReturn

import pytest

from chartcoach import Catalog
from chartcoach.catalog.locator import locate_catalog, open_catalog


def test_locate_catalog_classifies_default() -> None:
    location = locate_catalog()

    assert location.kind == "default"
    assert location.source is None
    assert location.path is None
    assert location.metadata_url is None
    assert location.is_default


def test_locate_catalog_normalizes_http_metadata_url() -> None:
    location = locate_catalog("https://example.test/catalog/releases/v1/digest")

    assert location.kind == "metadata-url"
    assert location.source == "https://example.test/catalog/releases/v1/digest"
    assert location.metadata_url == (
        "https://example.test/catalog/releases/v1/digest/metadata.json"
    )
    assert location.path is None
    assert not location.is_default


def test_locate_catalog_keeps_existing_metadata_url() -> None:
    source = "https://example.test/catalog/releases/v1/digest/metadata.json"

    location = locate_catalog(source)

    assert location.kind == "metadata-url"
    assert location.metadata_url == source


def test_locate_catalog_classifies_bundle_folder_and_parquet(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    folder_path = tmp_path / "source"
    sample_catalog.write_folder(folder_path)
    parquet_path = tmp_path / "entries.parquet"
    sample_catalog.write_parquet(parquet_path)

    bundle = locate_catalog(bundle_path)
    folder = locate_catalog(folder_path)
    parquet = locate_catalog(parquet_path)
    missing = locate_catalog(tmp_path / "missing.parquet")

    assert bundle.kind == "bundle"
    assert bundle.path == bundle_path
    assert folder.kind == "folder"
    assert folder.path == folder_path
    assert parquet.kind == "parquet"
    assert parquet.path == parquet_path
    assert missing.kind == "parquet"
    assert missing.path == tmp_path / "missing.parquet"


def test_open_catalog_passes_reporter_to_default_bundle(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.catalog.locator as locator

    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    calls: dict[str, object] = {}

    def default_bundle(*, reporter: object) -> Path:
        calls["reporter"] = reporter
        return bundle_path

    def reporter(kind: str, source: str, target: Path) -> NoReturn:
        raise AssertionError("reporter should only be forwarded")

    monkeypatch.setattr(locator, "default_catalog_bundle", default_bundle)

    catalog = open_catalog(None, reporter=reporter)

    assert catalog.guidelines().height == sample_catalog.guidelines().height
    assert calls == {"reporter": reporter}


def test_open_catalog_passes_reporter_to_remote_download(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.catalog.locator as locator

    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    calls: dict[str, object] = {}

    def download_bundle(metadata_url: str, *, reporter: object) -> Path:
        calls["metadata_url"] = metadata_url
        calls["reporter"] = reporter
        return bundle_path

    def reporter(kind: str, source: str, target: Path) -> NoReturn:
        raise AssertionError("reporter should only be forwarded")

    monkeypatch.setattr(locator, "download_catalog_bundle", download_bundle)

    catalog = open_catalog(
        "https://example.test/catalog/releases/v1/digest",
        reporter=reporter,
    )

    assert catalog.guidelines().height == sample_catalog.guidelines().height
    assert calls == {
        "metadata_url": "https://example.test/catalog/releases/v1/digest/metadata.json",
        "reporter": reporter,
    }


def test_open_catalog_does_not_report_local_loads(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle")
    folder_path = tmp_path / "source"
    sample_catalog.write_folder(folder_path)
    parquet_path = tmp_path / "entries.parquet"
    sample_catalog.write_parquet(parquet_path)

    def reporter(kind: str, source: str, target: Path) -> NoReturn:
        raise AssertionError("local catalog loads should not receive reporter")

    assert open_catalog(bundle_path, reporter=reporter).require_manifest()
    assert open_catalog(folder_path, reporter=reporter).guidelines().height == 2
    assert open_catalog(parquet_path, reporter=reporter).guidelines().height == 2

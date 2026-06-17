from __future__ import annotations

import io
import json
import shutil
import tarfile
from pathlib import Path
from typing import cast

import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog import remote as catalog_remote
from chartcoach.catalog.remote import (
    ArtifactDescriptor,
    CatalogReleaseMetadata,
    read_release_metadata,
)

from catalog_testkit import sha256, write_catalog_entry, write_manifest


def test_release_metadata_preserves_index_artifact_body() -> None:
    metadata = CatalogReleaseMetadata.from_mapping(
        {
            "version": "0.0.0",
            "digest": "catalog-digest",
            "artifacts": [
                {
                    "kind": "manifest",
                    "path": "MANIFEST.md",
                    "digest": "manifest-digest",
                    "bytes": 1,
                },
                {
                    "kind": "entries",
                    "path": "entries.parquet",
                    "digest": "entries-digest",
                    "bytes": 2,
                },
                {
                    "kind": "lancedb-index",
                    "path": "indexes/lancedb/openrouter/openai-text-embedding-3-large/index.tar.gz",
                    "digest": "index-digest",
                    "bytes": 3,
                    "format": "tar+gzip",
                    "table": "catalog_documents",
                    "catalog": {
                        "version": "0.0.0",
                        "digest": "catalog-digest",
                    },
                    "embedding": {
                        "registry": "openai",
                        "provider": "openrouter",
                        "model": "openai/text-embedding-3-large",
                        "options": {
                            "name": "text-embedding-3-large",
                            "dim": 3072,
                        },
                    },
                },
                {
                    "kind": "lancedb-index",
                    "path": "indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
                    "digest": "tree-digest",
                    "bytes": 4,
                    "format": "lancedb",
                    "table": "catalog_documents",
                    "uri": "s3://chartcoach/catalog/releases/0.0.0/catalog-digest/indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
                    "catalog": {
                        "version": "0.0.0",
                        "digest": "catalog-digest",
                    },
                    "embedding": {
                        "registry": "openai",
                        "provider": "openrouter",
                        "model": "openai/text-embedding-3-large",
                        "options": {
                            "name": "text-embedding-3-large",
                            "dim": 3072,
                        },
                    },
                },
            ],
        }
    )

    index_artifact = metadata.artifact("lancedb-index")
    assert index_artifact.path.endswith("index.tar.gz")
    assert index_artifact.extra["table"] == "catalog_documents"
    direct_artifact = [
        artifact
        for artifact in metadata.artifacts
        if artifact.kind == "lancedb-index" and artifact.format == "lancedb"
    ][0]
    assert direct_artifact.extra["uri"] == (
        "s3://chartcoach/catalog/releases/0.0.0/catalog-digest/"
        "indexes/lancedb/openrouter/openai-text-embedding-3-large/db"
    )
    artifacts = cast(list[dict[str, object]], metadata.to_record()["artifacts"])
    assert artifacts[2]["embedding"] == {
        "registry": "openai",
        "provider": "openrouter",
        "model": "openai/text-embedding-3-large",
        "options": {
            "name": "text-embedding-3-large",
            "dim": 3072,
        },
    }


def test_download_catalog_bundle_uses_release_root_without_index_download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    source_catalog = Catalog.from_folder(tmp_path / "source")
    bundle_path = source_catalog.write_bundle(tmp_path / "bundle")
    metadata = read_release_metadata(bundle_path)
    metadata = CatalogReleaseMetadata(
        version=metadata.version,
        digest=metadata.digest,
        artifacts=(
            *metadata.artifacts,
            ArtifactDescriptor(
                kind="lancedb-index",
                path="indexes/lancedb/openrouter/openai-text-embedding-3-large/index.tar.gz",
                digest="index-digest",
                bytes=3,
                format="tar+gzip",
            ),
        ),
    )
    release_url = f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/metadata.json"
    downloads: list[str] = []

    def read_url_text(url: str) -> str:
        if url == release_url:
            return json.dumps(metadata.to_record())
        raise AssertionError(f"Unexpected metadata URL: {url}")

    def download_file(url: str, path: Path) -> None:
        downloads.append(url)
        if url.endswith("/MANIFEST.md"):
            shutil.copyfile(bundle_path / "MANIFEST.md", path)
            return
        if url.endswith("/entries.parquet"):
            shutil.copyfile(bundle_path / "entries.parquet", path)
            return
        raise AssertionError(f"Unexpected artifact URL: {url}")

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    cached = catalog_remote.download_catalog_bundle(release_url)

    assert (cached / "MANIFEST.md").exists()
    assert (cached / "entries.parquet").exists()
    assert not (cached / "indexes").exists()
    assert downloads == [
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/MANIFEST.md",
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/entries.parquet",
    ]


def test_download_index_artifact_extracts_and_caches_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    archive_source = tmp_path / "index.tar.gz"
    index_source = tmp_path / "index-source"
    table_dir = index_source / "catalog_documents.lance"
    table_dir.mkdir(parents=True)
    (table_dir / "data.txt").write_text("indexed rows")
    with tarfile.open(archive_source, "w:gz") as archive:
        archive.add(table_dir, arcname="catalog_documents.lance")

    metadata = CatalogReleaseMetadata.from_mapping(
        {
            "version": "0.0.0",
            "digest": "catalog-digest",
            "artifacts": [
                {
                    "kind": "manifest",
                    "path": "MANIFEST.md",
                    "digest": "manifest-digest",
                    "bytes": 1,
                },
                {
                    "kind": "entries",
                    "path": "entries.parquet",
                    "digest": "entries-digest",
                    "bytes": 2,
                },
                {
                    "kind": "lancedb-index",
                    "path": "indexes/lancedb/openrouter/model/index.tar.gz",
                    "digest": sha256(archive_source),
                    "bytes": archive_source.stat().st_size,
                    "format": "tar+gzip",
                    "table": "catalog_documents",
                },
            ],
        }
    )
    downloads: list[str] = []

    def read_url_text(url: str) -> str:
        assert url == "https://example.test/metadata.json"
        return json.dumps(metadata.to_record())

    def download_file(url: str, path: Path) -> None:
        downloads.append(url)
        shutil.copyfile(archive_source, path)

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    first = catalog_remote.download_index_artifact(
        "https://example.test/metadata.json",
        table_name="catalog_documents",
    )
    second = catalog_remote.download_index_artifact(
        "https://example.test/metadata.json",
        table_name="catalog_documents",
    )

    assert first == second
    assert (
        first / "catalog_documents.lance" / "data.txt"
    ).read_text() == "indexed rows"
    assert (first / "artifact.json").exists()
    assert first == (
        tmp_path
        / "cache"
        / "catalog"
        / "releases"
        / "0.0.0"
        / "catalog-digest"
        / "indexes"
        / "lancedb"
        / "openrouter"
        / "model"
        / "db"
    )
    assert (first.parents[4] / "metadata.json").exists()
    assert downloads == [
        "https://example.test/indexes/lancedb/openrouter/model/index.tar.gz"
    ]


def test_catalog_download_preserves_cached_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    source_catalog = Catalog.from_folder(tmp_path / "source")
    bundle_path = source_catalog.write_bundle(tmp_path / "bundle")
    base_metadata = read_release_metadata(bundle_path)

    archive_source = tmp_path / "index.tar.gz"
    index_source = tmp_path / "index-source"
    table_dir = index_source / "catalog_documents.lance"
    table_dir.mkdir(parents=True)
    (table_dir / "data.txt").write_text("indexed rows")
    with tarfile.open(archive_source, "w:gz") as archive:
        archive.add(table_dir, arcname="catalog_documents.lance")

    metadata = CatalogReleaseMetadata(
        version=base_metadata.version,
        digest=base_metadata.digest,
        artifacts=(
            *base_metadata.artifacts,
            ArtifactDescriptor(
                kind="lancedb-index",
                path="indexes/lancedb/openrouter/model/index.tar.gz",
                digest=sha256(archive_source),
                bytes=archive_source.stat().st_size,
                format="tar+gzip",
                extra={"table": "catalog_documents"},
            ),
        ),
    )
    release_url = f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/metadata.json"
    downloads: list[str] = []

    def read_url_text(url: str) -> str:
        assert url == release_url
        return json.dumps(metadata.to_record())

    def download_file(url: str, path: Path) -> None:
        downloads.append(url)
        if url.endswith("/index.tar.gz"):
            shutil.copyfile(archive_source, path)
            return
        if url.endswith("/MANIFEST.md"):
            shutil.copyfile(bundle_path / "MANIFEST.md", path)
            return
        if url.endswith("/entries.parquet"):
            shutil.copyfile(bundle_path / "entries.parquet", path)
            return
        raise AssertionError(f"Unexpected artifact URL: {url}")

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    index_path = catalog_remote.download_index_artifact(
        release_url,
        table_name="catalog_documents",
    )
    catalog_path = catalog_remote.download_catalog_bundle(release_url)

    assert catalog_path == index_path.parents[4]
    assert (catalog_path / "MANIFEST.md").exists()
    assert (catalog_path / "entries.parquet").exists()
    assert (
        index_path / "catalog_documents.lance" / "data.txt"
    ).read_text() == "indexed rows"
    assert downloads == [
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/indexes/lancedb/openrouter/model/index.tar.gz",
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/MANIFEST.md",
        f"https://example.test/catalog/releases/{metadata.version}/{metadata.digest}/entries.parquet",
    ]


@pytest.mark.parametrize(
    "member_name",
    [
        r"C:\Users\petergy\index\catalog_documents.lance\data.txt",
        r"\\server\share\catalog_documents.lance\data.txt",
        "C:/Users/petergy/index/catalog_documents.lance/data.txt",
    ],
)
def test_index_archive_rejects_windows_escape_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    member_name: str,
) -> None:
    archive_path = tmp_path / "index.tar.gz"
    content = b"indexed rows"
    with tarfile.open(archive_path, "w:gz") as archive:
        member = tarfile.TarInfo(member_name)
        member.size = len(content)
        archive.addfile(member, io.BytesIO(content))

    metadata = CatalogReleaseMetadata.from_mapping(
        {
            "version": "0.0.0",
            "digest": "catalog-digest",
            "artifacts": [
                {
                    "kind": "manifest",
                    "path": "MANIFEST.md",
                    "digest": "manifest-digest",
                    "bytes": 1,
                },
                {
                    "kind": "entries",
                    "path": "entries.parquet",
                    "digest": "entries-digest",
                    "bytes": 2,
                },
                {
                    "kind": "lancedb-index",
                    "path": "indexes/lancedb/openrouter/model/index.tar.gz",
                    "digest": sha256(archive_path),
                    "bytes": archive_path.stat().st_size,
                    "format": "tar+gzip",
                    "table": "catalog_documents",
                },
            ],
        }
    )

    def read_url_text(url: str) -> str:
        assert url == "https://example.test/metadata.json"
        return json.dumps(metadata.to_record())

    def download_file(_url: str, path: Path) -> None:
        shutil.copyfile(archive_path, path)

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)
    monkeypatch.setattr(catalog_remote, "_download_file", download_file)

    with pytest.raises(ValueError, match="Unsafe LanceDB archive member"):
        catalog_remote.download_index_artifact(
            "https://example.test/metadata.json",
            table_name="catalog_documents",
        )


def test_catalog_open_uses_cached_default_bundle(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    source_catalog = Catalog.from_folder(tmp_path / "source")
    bundle_path = source_catalog.write_bundle(tmp_path / "bundle")
    metadata = read_release_metadata(bundle_path)
    cache_root = tmp_path / "cache"
    cached_bundle = (
        cache_root / "catalog" / "releases" / metadata.version / metadata.digest
    )
    cached_bundle.parent.mkdir(parents=True)
    shutil.copytree(bundle_path, cached_bundle)
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_VERSION", metadata.version)
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_DIGEST", metadata.digest)

    catalog = Catalog.open()

    assert catalog.to_frame().to_dicts() == source_catalog.to_frame().to_dicts()

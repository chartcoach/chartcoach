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
    CatalogArtifactIndex,
    CatalogReleaseMetadata,
    read_release_metadata,
    release_metadata_url_from_index,
)

from catalog_testkit import sha256, write_catalog_entry, write_manifest


def test_cache_root_defaults_to_platformdirs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[dict[str, object]] = []

    def fake_user_cache_path(appname: str, **kwargs: object) -> Path:
        calls.append({"appname": appname, **kwargs})
        return tmp_path / "platform-cache" / appname

    monkeypatch.delenv("CHARTCOACH_CACHE_DIR", raising=False)
    monkeypatch.setattr(catalog_remote, "user_cache_path", fake_user_cache_path)

    assert catalog_remote.cache_root() == tmp_path / "platform-cache" / "chartcoach"
    assert calls == [{"appname": "chartcoach", "appauthor": False}]


def test_artifact_cache_root_lives_under_platform_cache_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(tmp_path / "cache"))

    assert catalog_remote.artifact_cache_root() == tmp_path / "cache" / "artifacts"


def test_release_metadata_preserves_index_artifact_body() -> None:
    metadata = CatalogReleaseMetadata.from_mapping(
        {
            "version": "0.1.4",
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
                        "version": "0.1.4",
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
                    "uri": "s3://chartcoach/catalog/releases/0.1.4/catalog-digest/indexes/lancedb/openrouter/openai-text-embedding-3-large/db",
                    "catalog": {
                        "version": "0.1.4",
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
        "s3://chartcoach/catalog/releases/0.1.4/catalog-digest/"
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


def test_artifact_index_resolves_latest_catalog_metadata_url() -> None:
    index = CatalogArtifactIndex.from_mapping(
        {
            "kind": "chartcoach-artifact-index",
            "version": 1,
            "catalogs": [
                {
                    "name": "chartcoach/catalog",
                    "version": "0.0.0",
                    "digest": "old-digest",
                    "root": "catalog/releases/0.0.0/old-digest/",
                    "metadata": "catalog/releases/0.0.0/old-digest/metadata.json",
                    "artifacts": [
                        {
                            "kind": "manifest",
                            "path": "catalog/releases/0.0.0/old-digest/MANIFEST.md",
                            "digest": "manifest-digest",
                            "bytes": 1,
                        }
                    ],
                },
                {
                    "name": "chartcoach/catalog",
                    "version": "0.1.4",
                    "digest": "new-digest",
                    "root": "catalog/releases/0.1.4/new-digest/",
                    "metadata": "catalog/releases/0.1.4/new-digest/metadata.json",
                    "artifacts": [
                        {
                            "kind": "entries",
                            "path": "catalog/releases/0.1.4/new-digest/entries.parquet",
                            "digest": "entries-digest",
                            "bytes": 2,
                        }
                    ],
                },
            ],
        }
    )

    release = index.catalog()

    assert release.version == "0.1.4"
    assert release.digest == "new-digest"
    assert (
        release_metadata_url_from_index(
            release,
            base_url="https://example.test",
        )
        == "https://example.test/catalog/releases/0.1.4/new-digest/metadata.json"
    )


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
            "version": "0.1.4",
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
    assert first == (
        tmp_path
        / "cache"
        / "artifacts"
        / "catalog"
        / "releases"
        / "0.1.4"
        / "catalog-digest"
        / "indexes"
        / "lancedb"
        / "openrouter"
        / "model"
        / "db"
    )
    assert (first.parent / "index.tar.gz").is_file()
    assert not (first / "artifact.json").exists()
    assert (first.parents[4] / "metadata.json").exists()
    assert downloads == [
        "https://example.test/indexes/lancedb/openrouter/model/index.tar.gz"
    ]


def test_default_index_path_uses_cached_index_without_remote_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cache_root = tmp_path / "cache"
    release_path = (
        cache_root / "artifacts" / "catalog" / "releases" / "0.1.4" / "catalog-digest"
    )
    index_path = release_path / "indexes" / "lancedb" / "openrouter" / "model" / "db"
    (index_path / "catalog_documents.lance").mkdir(parents=True)
    archive_path = (
        release_path / "indexes" / "lancedb" / "openrouter" / "model" / "index.tar.gz"
    )
    archive_path.write_bytes(b"cached archive")
    artifact = ArtifactDescriptor(
        kind="lancedb-index",
        path="indexes/lancedb/openrouter/model/index.tar.gz",
        digest=sha256(archive_path),
        bytes=archive_path.stat().st_size,
        format="tar+gzip",
        extra={"table": "catalog_documents"},
    )
    metadata = CatalogReleaseMetadata(
        version="0.1.4",
        digest="catalog-digest",
        artifacts=(
            ArtifactDescriptor(
                kind="manifest",
                path="MANIFEST.md",
                digest="manifest-digest",
                bytes=1,
            ),
            ArtifactDescriptor(
                kind="entries",
                path="entries.parquet",
                digest="entries-digest",
                bytes=2,
            ),
            artifact,
        ),
    )
    (index_path / "artifact.json").write_text(json.dumps(artifact.to_record()))
    (release_path / "metadata.json").write_text(json.dumps(metadata.to_record()))

    def read_url_text(_url: str) -> str:
        raise AssertionError("cached default index should not fetch remote metadata")

    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_VERSION", "0.1.4")
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_DIGEST", "catalog-digest")
    monkeypatch.setattr(catalog_remote, "_read_url_text", read_url_text)

    assert (
        catalog_remote.default_index_path(table_name="catalog_documents") == index_path
    )
    assert not (index_path / "artifact.json").exists()


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
    assert (
        catalog_path / "indexes" / "lancedb" / "openrouter" / "model" / "index.tar.gz"
    ).is_file()
    assert not (index_path / "artifact.json").exists()
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
            "version": "0.1.4",
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
        cache_root
        / "artifacts"
        / "catalog"
        / "releases"
        / metadata.version
        / metadata.digest
    )
    cached_bundle.parent.mkdir(parents=True)
    shutil.copytree(bundle_path, cached_bundle)
    monkeypatch.setenv("CHARTCOACH_CACHE_DIR", str(cache_root))
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_VERSION", metadata.version)
    monkeypatch.setattr(catalog_remote, "DEFAULT_CATALOG_DIGEST", metadata.digest)

    catalog = Catalog.open()

    assert catalog.to_frame().to_dicts() == source_catalog.to_frame().to_dicts()

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterator
from dataclasses import replace
from pathlib import Path
from typing import cast

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogError, CatalogRelease, ReleaseArtifact
from chartcoach._catalog.curation import published_validation
from chartcoach._catalog.curation.release_publisher import (
    _publish_release,
    _select_release,
)
from chartcoach._catalog.paths import paths
from chartcoach._catalog.releases.hashing import release_digest, sha256_file
from chartcoach.curation import (
    EmbeddingProfile,
    build_release,
    publish_release,
    select_release,
    validate_published_release,
)
from obspec import GetOptions, GetResult
from obstore.store import MemoryStore

pytestmark = pytest.mark.curation


@pytest.fixture
def published_store(
    sample_catalog: Catalog, tmp_path: Path
) -> tuple[MemoryStore, CatalogRelease]:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()
    _publish_release(store, root)
    _select_release(store, release.digest)
    return store, release


def test_published_validation_reads_selected_and_exact_bytes_fresh(
    published_store: tuple[MemoryStore, CatalogRelease], monkeypatch: pytest.MonkeyPatch
) -> None:
    store, release = published_store
    reads: list[str] = []

    class ReadOnlyStore:
        def get(self, path: str, *, options: GetOptions | None = None) -> GetResult:
            reads.append(path)
            return store.get(path, options=options)

    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: ReadOnlyStore()
    )
    assert validate_published_release("s3://example") == release
    assert reads[:2] == [paths.selected(), paths.release(release.digest).json()]
    assert Counter(reads[2:]) == Counter(
        paths.release(release.digest).artifact(path) for path in release.artifacts
    )
    reads.clear()
    assert validate_published_release("s3://example", digest=release.digest) == release
    assert paths.selected() not in reads

    key = paths.release(release.digest).artifact("entries.parquet")
    current = bytes(store.get(key).buffer())
    store.put(key, bytes([current[0] ^ 1]) + current[1:])
    with pytest.raises(ValueError, match="SHA-256"):
        validate_published_release("s3://example")


@pytest.mark.parametrize("missing", ["catalog.json", "descriptor", "artifact"])
def test_selected_validation_rejects_missing_objects(
    published_store: tuple[MemoryStore, CatalogRelease],
    missing: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    store, release = published_store
    key = {
        "catalog.json": paths.selected(),
        "descriptor": paths.release(release.digest).json(),
        "artifact": paths.release(release.digest).artifact("entries.parquet"),
    }[missing]
    store.delete(key)
    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: store
    )

    with pytest.raises(FileNotFoundError, match="Published catalog object is missing"):
        validate_published_release("s3://example")


def test_selected_validation_rejects_a_selector_descriptor_mismatch(
    published_store: tuple[MemoryStore, CatalogRelease], monkeypatch: pytest.MonkeyPatch
) -> None:
    store, release = published_store
    selection = replace(
        release,
        artifacts={
            **release.artifacts,
            "entries.parquet": replace(
                release.artifacts["entries.parquet"],
                bytes=release.artifacts["entries.parquet"].bytes + 1,
            ),
        },
    )
    store.put(paths.selected(), json.dumps(selection.to_record()).encode())
    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: store
    )

    with pytest.raises(ValueError, match="catalog.json does not match"):
        validate_published_release("s3://example")


def test_published_validation_preserves_file_destination_state(
    sample_catalog: Catalog, tmp_path: Path
) -> None:
    source = tmp_path / "release"
    release = build_release(sample_catalog, source)
    destination = tmp_path / "published"
    publish_release(source, destination.as_uri())
    select_release(release.digest, destination.as_uri())
    before = {
        path.relative_to(destination): path.read_bytes()
        for path in destination.rglob("*")
        if path.is_file()
    }

    assert validate_published_release(destination.as_uri()) == release

    assert {
        path.relative_to(destination): path.read_bytes()
        for path in destination.rglob("*")
        if path.is_file()
    } == before
    missing = tmp_path / "absent"
    with pytest.raises(CatalogError, match="could not be opened"):
        validate_published_release(missing.as_uri(), storage_options={"mkdir": True})
    assert not missing.exists()


@pytest.mark.parametrize("object_kind", ["descriptor", "artifact"])
def test_published_validation_stops_at_the_stream_byte_limit(
    published_store: tuple[MemoryStore, CatalogRelease],
    object_kind: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    store, release = published_store
    key = (
        paths.release(release.digest).json()
        if object_kind == "descriptor"
        else paths.release(release.digest).artifact("MANIFEST.md")
    )
    limit = (
        1024 * 1024
        if object_kind == "descriptor"
        else release.artifacts["MANIFEST.md"].bytes
    )

    def oversized_chunks() -> Iterator[bytes]:
        yield b"x" * (limit + 1)
        pytest.fail("Validation read beyond the byte limit")

    class StreamingStore:
        def get(self, path: str, *, options: GetOptions | None = None) -> GetResult:
            return (
                cast(GetResult, oversized_chunks())
                if path == key
                else store.get(path, options=options)
            )

    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: StreamingStore()
    )
    with pytest.raises(ValueError, match="1 MiB|byte count"):
        validate_published_release("s3://example", digest=release.digest)


@pytest.mark.parametrize(
    ("artifact_path", "size", "message"),
    [
        ("entries.parquet", 64 * 1024**2 + 1, "64 MiB"),
        ("extra.bin", 1024**3 + 1, "1 GiB"),
        ("profiles/test/profile.json", 65_537, "64 KiB"),
    ],
)
def test_published_validation_rejects_declared_limits_before_downloading_artifacts(
    published_store: tuple[MemoryStore, CatalogRelease],
    artifact_path: str,
    size: int,
    message: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    store, release = published_store
    artifacts = dict(release.artifacts)
    artifacts[artifact_path] = ReleaseArtifact(sha256="0" * 64, bytes=size)
    if artifact_path.startswith("profiles/"):
        artifacts["profiles/test/index.tar.gz"] = ReleaseArtifact(
            sha256="0" * 64, bytes=1
        )
    oversized = CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)
    descriptor = paths.release(oversized.digest).json()
    store.put(descriptor, json.dumps(oversized.to_record()).encode())
    reads: list[str] = []

    class ObservedStore:
        def get(self, path: str, *, options: GetOptions | None = None) -> GetResult:
            reads.append(path)
            return store.get(path, options=options)

    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: ObservedStore()
    )
    with pytest.raises(ValueError, match=message):
        validate_published_release("s3://example", digest=oversized.digest)
    assert reads == [descriptor]


def test_published_validation_redacts_storage_diagnostics(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    marker = "private-storage-credential"

    class FailingStore:
        def get(self, path: str, *, options: GetOptions | None = None) -> GetResult:
            raise RuntimeError(marker)

    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: FailingStore()
    )
    with pytest.raises(CatalogError) as exc_info:
        validate_published_release("s3://example")

    assert exc_info.value.code == "operation_failed"
    assert marker not in str(exc_info.value)
    assert "catalog.json" in str(exc_info.value)


def test_published_validation_rejects_stale_index_documents_with_valid_hashes(
    sample_catalog: Catalog, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import polars as pl

    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={
            "test": EmbeddingProfile(
                deterministic_embedding("published-validation-documents")
            )
        },
    )
    changed_frame = sample_catalog.to_frame().with_columns(
        pl.lit("Changed guidance.").alias("description")
    )
    changed = Catalog(changed_frame, manifest=sample_catalog.manifest)
    changed_frame.write_parquet(root / "entries.parquet")
    profile_path = root / "profiles/test/profile.json"
    profile = json.loads(profile_path.read_text())
    profile["entries_digest"] = changed.entries_digest()
    profile_path.write_text(json.dumps(profile))
    artifacts = dict(release.artifacts)
    for path in ("entries.parquet", "profiles/test/profile.json"):
        artifact = root / path
        artifacts[path] = ReleaseArtifact(
            sha256=sha256_file(artifact), bytes=artifact.stat().st_size
        )
    stale = CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)
    store = MemoryStore()
    for path in artifacts:
        store.put(
            paths.release(stale.digest).artifact(path), (root / path).read_bytes()
        )
    store.put(
        paths.release(stale.digest).json(), json.dumps(stale.to_record()).encode()
    )
    monkeypatch.setattr(
        published_validation, "from_url", lambda *_args, **_kwargs: store
    )

    with pytest.raises(ValueError, match="document rows do not match.*Regenerate"):
        validate_published_release("s3://example", digest=stale.digest)

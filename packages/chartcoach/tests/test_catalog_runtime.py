from __future__ import annotations

import inspect
import json
import shutil
from collections import Counter
from collections.abc import Iterator
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from typing import Any

import pytest
from chartcoach import CatalogError, open_catalog
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest, sha256_file
from chartcoach.catalog.runtime import transport as catalog_transport


def test_open_catalog_accepts_the_local_source_matrix(
    sample_catalog: Catalog,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    bundle = sample_catalog.write_bundle(tmp_path / "bundle")
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    store = tmp_path / "store"
    _publish_local(release_root, release, store)

    authored = open_catalog(sample_workspace_path)
    compiled = open_catalog(bundle)
    compiled_uri = open_catalog(bundle.as_uri())
    local_release = open_catalog(release_root)
    exact = open_catalog(release_root / "release.json")
    selected = open_catalog(store / "catalog.json")

    assert authored.release is None
    assert compiled.release is None
    assert compiled_uri.release is None
    assert local_release.release == release
    assert exact.release == release
    assert selected.release == release
    assert {
        len(authored),
        len(compiled),
        len(compiled_uri),
        len(local_release),
        len(exact),
        len(selected),
    } == {len(sample_catalog)}


def test_top_level_api_is_the_supported_catalog_contract() -> None:
    import chartcoach

    assert set(chartcoach.__all__) == {
        "Catalog",
        "CatalogError",
        "CatalogManifest",
        "CatalogRelease",
        "__version__",
        "open_catalog",
        "open_index",
    }
    assert str(inspect.signature(chartcoach.open_catalog)) == (
        "(source: 'str | PathLike[str] | None' = None, *, "
        "storage_options: 'Mapping[str, object] | None' = None) -> 'Catalog'"
    )
    assert str(inspect.signature(chartcoach.open_index)) == (
        "(source: 'str | PathLike[str] | None' = None, *, profile: 'str', "
        "storage_options: 'Mapping[str, object] | None' = None) -> 'Table'"
    )


def test_http_errors_redact_credentials(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(*_: object, **__: object) -> None:
        raise OSError("offline")

    monkeypatch.setattr(catalog_transport, "urlopen", fail)
    uri = "https://user:password@example.test/catalog.json?token=secret#fragment"

    with pytest.raises(CatalogError) as exc_info:
        list(
            catalog_transport.remote_chunks(
                uri,
                transport="http",
                storage_options={},
            )
        )

    message = str(exc_info.value)
    assert "https://example.test/catalog.json" in message
    assert "user:password" not in message
    assert "token=secret" not in message
    assert "#fragment" not in message


def test_digest_shaped_source_is_an_ordinary_local_path(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    digest = "a" * 64
    sample_catalog.write_bundle(tmp_path / digest)
    monkeypatch.chdir(tmp_path)

    catalog = open_catalog(digest)

    assert catalog.release is None
    assert len(catalog) == len(sample_catalog)


def test_local_directory_rejects_an_ambiguous_shape(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = sample_catalog.write_bundle(tmp_path / "catalog")
    (root / "entries").mkdir()

    with pytest.raises(CatalogError, match="ambiguous"):
        open_catalog(root)


@pytest.mark.parametrize(
    ("source", "message"),
    [
        ("ftp://example.test/catalog.json", "Unsupported catalog source scheme"),
        ("https://example.test/catalog", "must name catalog.json or release.json"),
    ],
)
def test_remote_source_rejects_unsupported_shapes(source: str, message: str) -> None:
    with pytest.raises(CatalogError, match=message):
        open_catalog(source)


def test_http_catalog_and_release_descriptors_share_verified_artifacts(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    store = tmp_path / "store"
    _publish_local(release_root, release, store)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root",
        lambda: tmp_path / "cache",
    )

    with _serve(store) as (base_url, requests):
        selected_url = f"{base_url}/catalog.json"
        exact_url = f"{base_url}/catalog/releases/{release.digest}/release.json"
        selected = open_catalog(
            selected_url,
            storage_options={"headers": {"X-ChartCoach-Test": "runtime"}},
        )
        exact = open_catalog(exact_url)

    assert selected.release == exact.release == release
    assert requests["/catalog.json"] == 1
    assert requests[f"/catalog/releases/{release.digest}/release.json"] == 1
    assert requests[f"/catalog/releases/{release.digest}/MANIFEST.md"] == 1
    assert requests[f"/catalog/releases/{release.digest}/entries.parquet"] == 1


def test_http_catalog_identifies_chartcoach_to_the_server(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    store = tmp_path / "store"
    _publish_local(release_root, release, store)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root",
        lambda: tmp_path / "cache",
    )

    with _serve(store, required_user_agent="chartcoach") as (base_url, _requests):
        catalog = open_catalog(f"{base_url}/catalog.json")

    assert catalog.release == release


def test_selected_descriptor_refreshes_while_artifact_cache_is_reused(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first_root, first = _write_release(sample_catalog, tmp_path / "first")
    second_root, second = _write_release(
        sample_catalog,
        tmp_path / "second",
        manifest_suffix="\n",
    )
    store = tmp_path / "store"
    _publish_local(first_root, first, store)
    _publish_local(second_root, second, store, select=False)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root",
        lambda: tmp_path / "cache",
    )

    with _serve(store) as (base_url, requests):
        source = f"{base_url}/catalog.json"
        first_catalog = open_catalog(source)
        (store / "catalog.json").write_text(
            json.dumps(second.to_record()),
            encoding="utf-8",
        )
        second_catalog = open_catalog(source)
        repeated = open_catalog(source)

    assert first_catalog.release == first
    assert second_catalog.release == repeated.release == second
    assert requests["/catalog.json"] == 3
    assert requests[f"/catalog/releases/{second.digest}/MANIFEST.md"] == 1
    assert requests[f"/catalog/releases/{second.digest}/entries.parquet"] == 0


def test_remote_artifact_integrity_is_checked_before_cache_commit(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    store = tmp_path / "store"
    _publish_local(release_root, release, store)
    entries = store / "catalog" / "releases" / release.digest / "entries.parquet"
    entries.write_bytes(b"corrupt")
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach.catalog.runtime.cache._cache_root", lambda: cache)

    with (
        _serve(store) as (base_url, _requests),
        pytest.raises(CatalogError, match="byte count|SHA-256"),
    ):
        open_catalog(f"{base_url}/catalog.json")

    assert not (
        cache / "artifacts" / release.artifact("entries.parquet").sha256
    ).exists()


def test_release_rejects_an_oversized_core_artifact(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    artifacts = dict(release.artifacts)
    entries = artifacts["entries.parquet"]
    artifacts["entries.parquet"] = ReleaseArtifact(
        sha256=entries.sha256,
        bytes=64 * 1024**2 + 1,
    )
    oversized = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    (release_root / "release.json").write_text(
        json.dumps(oversized.to_record()),
        encoding="utf-8",
    )

    with pytest.raises(CatalogError, match="64 MiB"):
        open_catalog(release_root)


def test_cloud_transport_receives_a_copy_of_storage_options(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    descriptor = json.dumps(release.to_record()).encode()
    objects = {
        "s3://bucket/catalog.json": descriptor,
        (f"s3://bucket/catalog/releases/{release.digest}/MANIFEST.md"): (
            release_root / "MANIFEST.md"
        ).read_bytes(),
        (f"s3://bucket/catalog/releases/{release.digest}/entries.parquet"): (
            release_root / "entries.parquet"
        ).read_bytes(),
    }
    seen: list[dict[str, object]] = []

    class Store:
        def __init__(self, parent: str) -> None:
            self.parent = parent.rstrip("/")

        def get(self, key: str) -> Iterator[bytes]:
            yield objects[f"{self.parent}/{key}"]

    def from_url(parent: str, **options: object) -> Store:
        seen.append(options)
        return Store(parent)

    monkeypatch.setattr("obstore.store.from_url", from_url)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root",
        lambda: tmp_path / "cache",
    )
    storage_options: dict[str, object] = {
        "region": "eu-central-1",
        "skip_signature": True,
    }

    catalog = open_catalog(
        "s3://bucket/catalog.json",
        storage_options=storage_options,
    )

    assert catalog.release == release
    assert storage_options == {
        "region": "eu-central-1",
        "skip_signature": True,
    }
    assert seen == [storage_options, storage_options, storage_options]
    assert all(options is not storage_options for options in seen)


def _write_release(
    catalog: Catalog,
    root: Path,
    *,
    manifest_suffix: str = "",
) -> tuple[Path, CatalogRelease]:
    catalog.write_bundle(root)
    if manifest_suffix:
        manifest = root / "MANIFEST.md"
        manifest.write_text(
            manifest.read_text(encoding="utf-8") + manifest_suffix,
            encoding="utf-8",
        )
    artifacts = {
        path: ReleaseArtifact(
            sha256=sha256_file(root / path),
            bytes=(root / path).stat().st_size,
        )
        for path in ("MANIFEST.md", "entries.parquet")
    }
    release = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    (root / "release.json").write_text(
        json.dumps(release.to_record()),
        encoding="utf-8",
    )
    return root, release


def _publish_local(
    release_root: Path,
    release: CatalogRelease,
    store: Path,
    *,
    select: bool = True,
) -> None:
    target = store / "catalog" / "releases" / release.digest
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(release_root, target)
    if select:
        (store / "catalog.json").write_text(
            json.dumps(release.to_record()),
            encoding="utf-8",
        )


@contextmanager
def _serve(
    root: Path,
    *,
    required_user_agent: str | None = None,
) -> Iterator[tuple[str, Counter[str]]]:
    requests: Counter[str] = Counter()

    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self) -> None:
            requests[self.path.split("?", 1)[0]] += 1
            if (
                required_user_agent is not None
                and self.headers.get("User-Agent") != required_user_agent
            ):
                self.send_error(403)
                return
            super().do_GET()

        def log_message(self, format: str, *args: Any) -> None:
            return

    server = ThreadingHTTPServer(
        ("127.0.0.1", 0),
        partial(Handler, directory=str(root)),
    )
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host = str(server.server_address[0])
        port = server.server_port
        yield f"http://{host}:{port}", requests
    finally:
        server.shutdown()
        thread.join()
        server.server_close()

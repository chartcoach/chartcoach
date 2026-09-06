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
from catalog_testkit import deterministic_embedding
from chartcoach import CatalogError, open_catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release, write_bundle
from chartcoach.catalog.model import Catalog
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest, sha256_file
from chartcoach.catalog.runtime import transport as catalog_transport
from chartcoach.catalog.runtime.release import ReleaseLocation


def test_open_catalog_accepts_the_local_location_matrix(
    sample_catalog: Catalog,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    bundle = write_bundle(sample_catalog, tmp_path / "bundle")
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    store = tmp_path / "store"
    _publish_local(release_root, release, store)

    authored = open_catalog(sample_workspace_path)
    compiled = open_catalog(bundle)
    compiled_uri = open_catalog(bundle.as_uri())
    local_release = open_catalog(release_root)
    exact = open_catalog(release_root / "release.json")
    selected = open_catalog(store / "catalog.json")
    deployed = open_catalog(store)

    assert authored.release is None
    assert compiled.release is None
    assert compiled_uri.release is None
    assert local_release.release == release
    assert exact.release == release
    assert selected.release == release
    assert deployed.release == release
    assert deployed.describe()["resolved_location"] == str(
        store / "catalog" / "releases" / release.digest / "release.json"
    )
    assert {
        len(authored),
        len(compiled),
        len(compiled_uri),
        len(local_release),
        len(exact),
        len(selected),
        len(deployed),
    } == {len(sample_catalog)}


def test_local_directory_rejects_selection_and_release_descriptors(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, release = _write_release(sample_catalog, tmp_path / "catalog")
    (root / "catalog.json").write_text(json.dumps(release.to_record()))

    with pytest.raises(CatalogError, match="both catalog.json and release.json"):
        open_catalog(root)


def test_runtime_rejects_profile_metadata_without_an_index_archive(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, release = _write_release(sample_catalog, tmp_path / "release")
    artifacts = {
        **release.artifacts,
        "profiles/minilm-normalized/profile.json": ReleaseArtifact(
            sha256="c" * 64,
            bytes=1,
        ),
    }
    changed = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    (root / "release.json").write_text(json.dumps(changed.to_record()))

    with pytest.raises(CatalogError, match="missing index.tar.gz") as exc_info:
        open_catalog(root)

    assert exc_info.value.code == "incompatible_profile"


def test_top_level_api_is_the_supported_catalog_contract() -> None:
    import chartcoach

    assert set(chartcoach.__all__) == {
        "Catalog",
        "CatalogError",
        "CatalogInfo",
        "CatalogManifest",
        "CatalogRelease",
        "CitationRecord",
        "CitationSource",
        "GuidelineEntryRecord",
        "SearchResult",
        "GuidelineMatch",
        "ProfileInfo",
        "SectionRecord",
        "SourceDetail",
        "SqlColumn",
        "SqlResult",
        "__version__",
        "open_catalog",
    }
    open_parameters = inspect.signature(chartcoach.open_catalog).parameters
    assert tuple(open_parameters) == ("location", "storage_options")
    assert open_parameters["location"].default is None
    assert open_parameters["storage_options"].kind is inspect.Parameter.KEYWORD_ONLY
    assert open_parameters["storage_options"].default is None

    catalog_parameters = inspect.signature(chartcoach.Catalog).parameters
    assert tuple(catalog_parameters) == ("frame", "manifest")
    assert catalog_parameters["frame"].default is inspect.Parameter.empty
    assert catalog_parameters["manifest"].kind is inspect.Parameter.KEYWORD_ONLY
    assert catalog_parameters["manifest"].default is inspect.Parameter.empty


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


def test_catalog_description_redacts_exact_release_credentials(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _write_release(sample_catalog, tmp_path / "release")
    location = ReleaseLocation(
        release=release,
        artifact_base=release_root,
        descriptor=(
            "https://user:password@example.test/catalog/releases/"
            f"{release.digest}/release.json?token=secret#fragment"
        ),
        transport="local",
        storage_options={},
    )
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.release_location", lambda *_: location
    )

    catalog = open_catalog("https://example.test/release.json")

    assert catalog.describe()["resolved_location"] == (
        f"https://example.test/catalog/releases/{release.digest}/release.json"
    )


def test_digest_shaped_location_is_an_ordinary_local_path(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    digest = "a" * 64
    write_bundle(sample_catalog, tmp_path / digest)
    monkeypatch.chdir(tmp_path)

    catalog = open_catalog(digest)

    assert catalog.release is None
    assert len(catalog) == len(sample_catalog)


def test_local_directory_rejects_an_ambiguous_shape(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = write_bundle(sample_catalog, tmp_path / "catalog")
    (root / "entries").mkdir()

    with pytest.raises(CatalogError, match="ambiguous"):
        open_catalog(root)


@pytest.mark.parametrize(
    ("location", "message"),
    [
        ("ftp://example.test/catalog.json", "Unsupported catalog location scheme"),
        ("https://example.test/catalog", "must name catalog.json or release.json"),
    ],
)
def test_remote_location_rejects_unsupported_shapes(
    location: str, message: str
) -> None:
    with pytest.raises(CatalogError, match=message):
        open_catalog(location)


def test_digest_addressed_release_rejects_another_self_consistent_digest(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root, _ = _write_release(sample_catalog, tmp_path / "release")
    wrong = tmp_path / ("0" * 64)
    release_root.rename(wrong)

    with pytest.raises(CatalogError, match="digest-addressed location") as exc_info:
        open_catalog(wrong / "release.json")

    assert exc_info.value.code == "integrity"


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

    with _serve(store, required_user_agent="chartcoach") as (base_url, requests):
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


@pytest.mark.curation
@pytest.mark.search
def test_opening_and_description_keep_profile_artifacts_lazy(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    profile = "test-lazy"
    release_root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        release_root,
        profiles={
            profile: EmbeddingProfile(
                deterministic_embedding("chartcoach-lazy-profile")
            )
        },
    )
    store = tmp_path / "store"
    _publish_local(release_root, release, store)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )

    with _serve(store, required_header=("X-Profile-Test", "bound")) as (
        base_url,
        requests,
    ):
        catalog = open_catalog(
            f"{base_url}/catalog.json",
            storage_options={"headers": {"X-Profile-Test": "bound"}},
        )
        assert catalog.describe()["profiles"] == [profile]
        selected_profile = catalog.describe(profile=profile)["profile"]
        assert selected_profile is not None
        assert set(selected_profile) == {
            "name",
            "profile_schema_version",
            "documents_version",
            "embedding_functions",
            "dimensions",
            "distance_metric",
            "python_requirements",
            "lancedb_version",
            "projection",
        }
        assert selected_profile["distance_metric"] == "cosine"

    base = f"/catalog/releases/{release.digest}/profiles/{profile}"
    assert requests[f"{base}/profile.json"] == 1
    assert requests[f"{base}/documents.parquet"] == 0
    assert requests[f"{base}/index.tar.gz"] == 0


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
        location = f"{base_url}/catalog.json"
        first_catalog = open_catalog(location)
        (store / "catalog.json").write_text(
            json.dumps(second.to_record()),
            encoding="utf-8",
        )
        second_catalog = open_catalog(location)
        repeated = open_catalog(location)

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


def test_cloud_transport_forwards_storage_options_to_catalog_resources(
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
    expected_options: dict[str, object] = {
        "region": "eu-central-1",
        "skip_signature": True,
    }

    class Store:
        def __init__(self, parent: str) -> None:
            self.parent = parent.rstrip("/")

        def get(self, key: str) -> Iterator[bytes]:
            yield objects[f"{self.parent}/{key}"]

    def from_url(parent: str, **options: object) -> Store:
        assert options == expected_options
        return Store(parent)

    monkeypatch.setattr("obstore.store.from_url", from_url)
    monkeypatch.setattr(
        "chartcoach.catalog.runtime.cache._cache_root",
        lambda: tmp_path / "cache",
    )
    storage_options = dict(expected_options)

    catalog = open_catalog(
        "s3://bucket/catalog.json",
        storage_options=storage_options,
    )

    assert catalog.release == release
    assert storage_options == expected_options


def _write_release(
    catalog: Catalog,
    root: Path,
    *,
    manifest_suffix: str = "",
) -> tuple[Path, CatalogRelease]:
    write_bundle(catalog, root)
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
    required_header: tuple[str, str] | None = None,
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
            if (
                required_header is not None
                and self.headers.get(required_header[0]) != required_header[1]
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

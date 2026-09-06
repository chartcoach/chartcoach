from __future__ import annotations

from pathlib import Path

import pytest

from chartcoach import (
    CatalogRelease,
    open_catalog,
    open_index,
    resolve_release,
)
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.releases import ReleaseArtifact


def test_open_catalog_loads_local_bundle_and_authored_folder(
    sample_catalog: Catalog,
    sample_workspace_path: Path,
    tmp_path: Path,
) -> None:
    bundle_path = sample_catalog.write_bundle(tmp_path / "bundle@draft")
    bundle = open_catalog(str(bundle_path))
    folder = open_catalog(sample_workspace_path)

    assert "Section Roles" in bundle.manifest.markdown
    assert folder.guidelines().height == sample_catalog.guidelines().height


def test_explicit_digest_shaped_paths_load_a_local_catalog(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    digest = "a" * 64
    sample_catalog.write_bundle(tmp_path / digest)
    monkeypatch.chdir(tmp_path)

    relative = open_catalog(f"./{digest}")
    path_object = open_catalog(Path(digest))

    assert relative.guidelines().height == sample_catalog.guidelines().height
    assert path_object.guidelines().height == sample_catalog.guidelines().height


@pytest.mark.curation
@pytest.mark.parametrize("reference", [None, "a" * 64])
def test_published_catalog_uses_the_entry_document_or_exact_digest(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    reference: str | None,
) -> None:
    from chartcoach.catalog.curation import cache
    import lancedb

    digest = "a" * 64
    bundle = sample_catalog.write_bundle(tmp_path / digest)
    release = CatalogRelease(
        digest=digest,
        artifacts={
            "MANIFEST.md": ReleaseArtifact("1" * 64, 1),
            "entries.parquet": ReleaseArtifact("2" * 64, 1),
        },
    )
    index = tmp_path / "cached-index"
    table = object()
    store = object()
    calls: list[tuple[str, str | None]] = []

    def read_release(source: object, reference: str | None) -> CatalogRelease:
        assert source is store
        calls.append(("resolve", reference))
        return release

    def download_catalog_bundle(
        reference: str | None,
    ) -> tuple[CatalogRelease, Path]:
        calls.append(("catalog", reference))
        return release, bundle

    def download_index_artifact(reference: str | None, *, profile: str) -> Path:
        calls.append((f"index:{profile}", reference))
        return index

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cache, "artifact_store", lambda: store)
    monkeypatch.setattr(cache, "read_release", read_release)
    monkeypatch.setattr(cache, "download_catalog_bundle", download_catalog_bundle)
    monkeypatch.setattr(cache, "download_index_artifact", download_index_artifact)

    class Connection:
        def open_table(self, name: str) -> object:
            assert name == "documents"
            return table

    monkeypatch.setattr(lancedb, "connect", lambda location: Connection())

    resolved = resolve_release(reference)
    catalog = open_catalog(reference)
    opened = open_index(reference, profile="minilm")

    assert resolved is release
    assert catalog.guidelines().height == sample_catalog.guidelines().height
    assert opened is table
    assert calls == [
        ("resolve", reference),
        ("catalog", reference),
        ("index:minilm", reference),
    ]


def test_open_index_requires_profile_for_a_remote_release() -> None:
    with pytest.raises(ValueError, match="Pass profile"):
        open_index("a" * 64)


def test_resolve_release_rejects_a_local_catalog_path(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Catalog release reference must be"):
        resolve_release(str(tmp_path / "catalog"))

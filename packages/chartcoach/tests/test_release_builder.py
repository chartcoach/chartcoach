from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogManifest, open_catalog
from chartcoach._catalog.curation.projection import project_vectors
from chartcoach._catalog.releases.hashing import release_digest
from chartcoach.curation import (
    EmbeddingProfile,
    IndexProfile,
    ProfileReuse,
    build_release,
    validate_release,
)

pytestmark = pytest.mark.curation
_PROFILE = "test-deterministic"
_EMBEDDING = "chartcoach-release-test"


def test_native_index_vectors_are_materialized_and_configured_for_release(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import lancedb
    from lancedb.embeddings import EmbeddingFunctionConfig
    from lancedb.index import BTree

    source = tmp_path / "native"
    embedding = deterministic_embedding("native-prebuilt-profile")
    connection = lancedb.connect(source)
    table = connection.create_table(
        "documents",
        data=sample_catalog.documents().to_arrow(),
        embedding_functions=[
            EmbeddingFunctionConfig(
                source_column="text", vector_column="vector", function=embedding
            ),
        ],
    )
    connection.create_table("unrelated", data=[{"secret": "caller data"}])
    vectors = table.to_arrow()["vector"].to_pylist()

    def forbid_provider(*args, **kwargs):
        raise AssertionError("Packaging constructed the embedding provider")

    monkeypatch.setattr(type(embedding), "create", forbid_provider)

    def configure(table):
        table.create_index("parent_id", config=BTree())

    output = tmp_path / "release"
    build_release(
        sample_catalog,
        output,
        profiles={
            "native": IndexProfile(table, configure=configure, export_documents=True)
        },
    )
    assert list(table.list_indices()) == []
    shutil.rmtree(source)
    assert validate_release(output)
    released = open_catalog(output).index("native")
    assert released.to_arrow()["vector"].to_pylist() == vectors
    assert (
        released.search("labels", query_type="fts", fts_columns="text")
        .where("parent_id = 'direct-labels'")
        .limit(1)
        .to_list()
    )
    assert {index.index_type for index in released.list_indices()} == {"FTS", "BTree"}
    documents = pq.read_table(output / "profiles/native/documents.parquet")
    assert (
        documents.select(sample_catalog.documents().columns).to_pylist()
        == sample_catalog.documents().to_dicts()
    )


def test_profile_reuse_accepts_manifest_prose_changes_with_identical_documents(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    first = build_release(
        sample_catalog,
        source,
        profiles={
            "model": EmbeddingProfile(deterministic_embedding("reuse-vocabulary"))
        },
    )
    manifest = CatalogManifest.from_text(
        sample_catalog.manifest.markdown.replace(
            "Actionable guidance", "Practical guidance"
        )
    )
    revised = Catalog(sample_catalog.to_frame(), manifest=manifest)
    assert revised.documents().equals(sample_catalog.documents())
    output = tmp_path / "revised"
    second = build_release(
        revised, output, profiles={"model": ProfileReuse(source, "model")}
    )
    assert first.artifact("profiles/model/index.tar.gz") == second.artifact(
        "profiles/model/index.tar.gz"
    )
    assert first.digest != second.digest
    assert validate_release(output) == second
    assert (
        open_catalog(output).describe(profile="model")["manifest_digest"]
        != open_catalog(source).describe()["manifest_digest"]
    )


def test_projection_options_are_checked_before_embedding_work(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    embedding = deterministic_embedding("projection-preflight")

    def forbid_provider(*args, **kwargs):
        raise AssertionError("Embedding started before options were checked")

    monkeypatch.setattr(type(embedding), "create", forbid_provider)
    with pytest.raises(ValueError, match="n_components"):
        build_release(
            sample_catalog,
            tmp_path / "release",
            profiles={
                "paid": EmbeddingProfile(embedding),
                "invalid": EmbeddingProfile(embedding, umap={"n_components": 3}),
            },
        )


def test_core_release_contains_the_catalog_bundle(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)

    assert set(release.artifacts) == {"MANIFEST.md", "entries.parquet"}
    assert release.digest == release_digest(release.artifacts)
    assert json.loads((root / "release.json").read_text()) == release.to_record()


@pytest.mark.parametrize("profile", ["provider/model", "Uppercase", "trailing-"])
def test_profile_ids_are_flat_lowercase_names(
    sample_catalog: Catalog,
    tmp_path: Path,
    profile: str,
) -> None:
    with pytest.raises(ValueError, match="lowercase portable single-component"):
        build_release(
            sample_catalog,
            tmp_path / "release",
            profiles={
                profile: EmbeddingProfile(
                    embedding=deterministic_embedding("invalid-profile-id")
                )
            },
        )


def test_profile_release_separates_index_documents_and_projection(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    profile = EmbeddingProfile(
        embedding=deterministic_embedding(_EMBEDDING),
        umap={"n_neighbors": 3, "metric": "cosine", "random_state": 7},
        export_documents=True,
    )
    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={_PROFILE: profile},
    )

    assert validate_release(root) == release
    profile_path = root / "profiles" / _PROFILE / "documents.parquet"
    documents = pq.read_table(profile_path)
    assert set(documents.column_names) == {
        "row_id",
        "id",
        "parent_id",
        "role",
        "labels",
        "content_hash",
        "text",
        "vector",
    }
    assert pa.types.is_fixed_size_list(documents.schema.field("vector").type)
    metadata = documents.schema.metadata or {}
    assert metadata[b"chartcoach_profile"] == _PROFILE.encode()
    assert b"chartcoach_projection" not in metadata

    projection = pq.read_table(root / "profiles" / _PROFILE / "projection.parquet")
    assert set(projection.column_names) == {
        "row_id",
        "id",
        "parent_id",
        "role",
        "projection_x",
        "projection_y",
        "neighbors",
    }
    projection_metadata = projection.schema.metadata or {}
    assert projection_metadata[b"chartcoach_profile"] == _PROFILE.encode()
    assert (
        json.loads(projection_metadata[b"chartcoach_projection"])["options"][
            "n_neighbors"
        ]
        == 3
    )
    profile_metadata = json.loads(
        (root / "profiles" / _PROFILE / "profile.json").read_text()
    )
    import lancedb

    assert profile_metadata["entries_digest"] == sample_catalog.entries_digest()
    assert profile_metadata["dimensions"] == 4
    assert profile_metadata["distance_metric"] == "cosine"
    assert profile_metadata["python_requirements"] == {}
    assert profile_metadata["lancedb_version"] == lancedb.__version__
    assert profile_metadata["projection"]["algorithm"] in {"linear", "umap"}


def test_profile_exports_are_opt_in(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("projection-free-profile")
            )
        },
    )

    metadata = json.loads((root / "profiles" / _PROFILE / "profile.json").read_text())
    assert set(release.artifacts) == {
        "MANIFEST.md",
        "entries.parquet",
        f"profiles/{_PROFILE}/profile.json",
        f"profiles/{_PROFILE}/index.tar.gz",
    }
    assert metadata["projection"] is None
    assert validate_release(root) == release


def test_projection_builds_independently_of_the_document_export(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("projection-only-export"),
                umap={"n_neighbors": 3},
            )
        },
    )

    assert f"profiles/{_PROFILE}/documents.parquet" not in release.artifacts
    assert f"profiles/{_PROFILE}/projection.parquet" in release.artifacts
    assert validate_release(root) == release


def test_document_export_builds_independently_of_projection(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("documents-only-export"),
                export_documents=True,
            )
        },
    )

    assert f"profiles/{_PROFILE}/documents.parquet" in release.artifacts
    assert f"profiles/{_PROFILE}/projection.parquet" not in release.artifacts
    assert validate_release(root) == release


def test_profile_reuse_builds_projection_from_the_index_archive(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    reusable_release = tmp_path / "reusable-release"
    build_release(
        sample_catalog,
        reusable_release,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("reusable-profile")
            )
        },
    )
    reusable_archive = reusable_release / "profiles" / _PROFILE / "index.tar.gz"
    reusable_bytes = reusable_archive.read_bytes()

    output = tmp_path / "reused"
    release = build_release(
        sample_catalog,
        output,
        profiles={
            "projected-reuse": ProfileReuse(
                release=reusable_release,
                profile=_PROFILE,
                umap={"n_neighbors": 3},
            )
        },
    )

    reused_root = output / "profiles" / "projected-reuse"
    assert (reused_root / "index.tar.gz").read_bytes() == reusable_bytes
    assert (reused_root / "projection.parquet").is_file()
    assert validate_release(output) == release


def test_profile_reuse_requires_the_same_indexed_documents(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    reusable_release = tmp_path / "reusable-release"
    build_release(
        sample_catalog,
        reusable_release,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("identity-bound-reuse")
            )
        },
    )
    changed_rows = sample_catalog.to_frame()
    changed_rows[0, "title"] = "Changed title"
    changed = Catalog(changed_rows, manifest=sample_catalog.manifest)
    expensive = deterministic_embedding("preflight-before-embedding")

    def forbid_embedding(*args, **kwargs):
        raise AssertionError("Embeddings started before reusable inputs were checked")

    monkeypatch.setattr(type(expensive), "compute_source_embeddings", forbid_embedding)

    with pytest.raises(ValueError, match="document rows"):
        build_release(
            changed,
            tmp_path / "reused",
            profiles={
                "expensive": EmbeddingProfile(expensive),
                "reused-profile": ProfileReuse(
                    release=reusable_release,
                    profile=_PROFILE,
                ),
            },
        )


def test_profile_reuse_exports_from_the_index_archive_in_a_fresh_process(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    reusable_release = tmp_path / "reusable-release"
    output = tmp_path / "reused"
    build_release(
        sample_catalog,
        reusable_release,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding("fresh-process-reuse")
            )
        },
    )
    script = f"""
from chartcoach import open_catalog
from chartcoach.curation import ProfileReuse, build_release

build_release(
    open_catalog({str(reusable_release)!r}),
    {str(output)!r},
    profiles={{
        "reexported": ProfileReuse(
            release={str(reusable_release)!r},
            profile={_PROFILE!r},
            export_documents=True,
        )
    }},
)
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        env={**os.environ, "PYTHONPATH": ""},
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert (output / "profiles" / "reexported" / "documents.parquet").is_file()


def test_projection_is_deterministic_for_small_catalogs() -> None:
    vectors = np.asarray(
        [[1.0, float(index), 0.5] for index in range(3)],
        dtype=np.float32,
    )

    first = project_vectors(vectors, umap={})
    second = project_vectors(vectors, umap={})

    assert first.coordinates.shape == (3, 2)
    assert np.array_equal(first.coordinates, second.coordinates)
    assert np.array_equal(first.neighbor_ids, second.neighbor_ids)
    assert np.isfinite(first.neighbor_distances).all()


@pytest.mark.parametrize(
    ("option", "value", "message"),
    [
        ("n_neighbors", True, "n_neighbors must be an integer"),
        ("n_neighbors", 2.5, "n_neighbors must be an integer"),
        ("random_state", True, "random_state must be an integer"),
        ("random_state", 2.5, "random_state must be an integer"),
        ("metric", 42, "metric must be a string"),
    ],
)
def test_projection_rejects_invalid_umap_option_types(
    option: str,
    value: object,
    message: str,
) -> None:
    vectors = np.asarray([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)

    with pytest.raises(TypeError, match=message):
        project_vectors(vectors, umap={option: value})


def test_profile_rejects_unknown_lancedb_model_settings_before_embedding(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from lancedb.embeddings import get_registry

    embedding = (
        get_registry()
        .get("sentence-transformers")
        .create(
            name="all-MiniLM-L6-v2",
            revision="unforwarded-revision",
            trust_remote_code=False,
        )
    )

    with pytest.raises(ValueError, match="unsupported setting.*revision"):
        build_release(
            sample_catalog,
            tmp_path / "release",
            profiles={_PROFILE: EmbeddingProfile(embedding)},
        )


def test_profile_requirements_must_match_the_producer_environment() -> None:
    with pytest.raises(ValueError, match=r"lancedb must be 0\.0\.0, found "):
        EmbeddingProfile(
            deterministic_embedding("profile-requirement-check"),
            python_requirements={"lancedb": "0.0.0"},
        )

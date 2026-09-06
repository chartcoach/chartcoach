from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation import (
    EmbeddingProfile,
    build_release,
    validate_release,
)
from chartcoach.catalog.curation.projection import project_vectors
from chartcoach.catalog.releases.archive import extract_tar_archive
from chartcoach.catalog.releases.hashing import release_digest
from chartcoach.constants import LANCE_DOCUMENT_TABLE

pytestmark = pytest.mark.curation
_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-release-test"


def test_core_release_contains_the_catalog_bundle(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)

    assert set(release.artifacts) == {"MANIFEST.md", "entries.parquet"}
    assert release.digest == release_digest(release.artifacts)
    assert json.loads((root / "release.json").read_text()) == release.to_record()


def test_profile_release_is_atlas_ready_and_opens_as_native_lancedb(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    profile = EmbeddingProfile(
        embedding=deterministic_embedding(_EMBEDDING),
        umap={"n_neighbors": 3, "metric": "cosine", "random_state": 7},
    )
    root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        root,
        profiles={_PROFILE: profile, "research/alternate": profile},
    )

    assert validate_release(root) == release
    profile_path = root / "profiles" / _PROFILE / "documents.parquet"
    documents = pq.read_table(profile_path)
    assert {
        "row_id",
        "id",
        "vector",
        "projection_x",
        "projection_y",
        "neighbors",
    }.issubset(documents.column_names)
    assert pa.types.is_fixed_size_list(documents.schema.field("vector").type)
    metadata = documents.schema.metadata or {}
    assert metadata[b"chartcoach_profile"] == _PROFILE.encode()
    assert json.loads(metadata[b"chartcoach_projection"])["n_neighbors"] == 3

    database = tmp_path / "index"
    extract_tar_archive(
        root / "profiles" / _PROFILE / "index.tar.gz",
        database,
    )
    import lancedb

    table = lancedb.connect(database).open_table(LANCE_DOCUMENT_TABLE)
    assert table.count_rows() == documents.num_rows
    assert table.search(documents["vector"][0].as_py()).limit(1).to_list()


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

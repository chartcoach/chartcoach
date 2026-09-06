from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from tempfile import TemporaryDirectory

import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach.catalog.curation import (
    EmbeddingProfile,
    build_release,
    validate_release,
)
from chartcoach.catalog.curation.artifacts import _write_lancedb_archive
from chartcoach.catalog.model import Catalog
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.archive import extract_tar_archive
from chartcoach.catalog.releases.hashing import release_digest, sha256_file
from chartcoach.catalog.releases.services import validate_runtime_release

pytestmark = pytest.mark.curation
_PROFILE = "test-deterministic"
_EMBEDDING = "chartcoach-validation-test"


def test_runtime_validation_rejects_corrupt_artifacts(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    build_release(sample_catalog, root)
    (root / "entries.parquet").write_bytes(b"corrupt")

    with pytest.raises(ValueError, match="byte count|SHA-256"):
        validate_runtime_release(root)


def test_curation_validation_requires_complete_profiles(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, release = _profile_release(sample_catalog, tmp_path)
    index_path = f"profiles/{_PROFILE}/index.tar.gz"
    artifacts = dict(release.artifacts)
    artifacts.pop(index_path)
    _write_release(root, artifacts)

    with pytest.raises(ValueError, match="missing index"):
        validate_release(root)


def test_profile_validation_requires_profile_metadata(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, release = _profile_release(sample_catalog, tmp_path)
    metadata_path = f"profiles/{_PROFILE}/profile.json"
    artifacts = dict(release.artifacts)
    artifacts.pop(metadata_path)
    (root / metadata_path).unlink()
    _write_release(root, artifacts)

    with pytest.raises(ValueError, match="missing profile.json"):
        validate_release(root)


def test_profile_metadata_requires_its_projection_artifact(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, release = _profile_release(sample_catalog, tmp_path)
    projection_path = f"profiles/{_PROFILE}/projection.parquet"
    artifacts = dict(release.artifacts)
    artifacts.pop(projection_path)
    (root / projection_path).unlink()
    _write_release(root, artifacts)

    with pytest.raises(ValueError, match="missing projection.parquet"):
        validate_release(root)


def test_projection_artifact_requires_profile_metadata(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    metadata_path = f"profiles/{_PROFILE}/profile.json"
    path = root / metadata_path
    metadata = json.loads(path.read_text())
    metadata["projection"] = None
    path.write_text(json.dumps(metadata))
    _refresh_artifact(root, metadata_path)

    with pytest.raises(ValueError, match="absent from profile.json"):
        validate_release(root)


@pytest.mark.parametrize(
    ("metadata", "message"),
    [
        (
            [
                {
                    "name": "sentence-transformers",
                    "model": {
                        "name": "all-MiniLM-L6-v2",
                        "trust_remote_code": True,
                    },
                    "source_column": "text",
                    "vector_column": "vector",
                }
            ],
            "remote model code",
        ),
        (
            [
                {
                    "name": "openai",
                    "model": {
                        "name": "text-embedding-3-small",
                        "api_key": "literal-secret",
                    },
                    "source_column": "text",
                    "vector_column": "vector",
                }
            ],
            "must use a registry variable",
        ),
    ],
)
def test_curation_validation_rejects_unsafe_embedding_metadata(
    sample_catalog: Catalog,
    tmp_path: Path,
    metadata: object,
    message: str,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    profile_path = f"profiles/{_PROFILE}/documents.parquet"
    path = root / profile_path
    table = pq.read_table(path)
    schema_metadata = dict(table.schema.metadata or {})
    schema_metadata[b"embedding_functions"] = json.dumps(metadata).encode()
    pq.write_table(table.replace_schema_metadata(schema_metadata), path)
    _refresh_artifact(root, profile_path)

    with pytest.raises(ValueError, match=message):
        validate_release(root)


def test_release_validation_detects_changed_document_text_with_recomputed_hashes(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    profile_path = f"profiles/{_PROFILE}/documents.parquet"
    path = root / profile_path
    table = pq.read_table(path)
    text = table["text"].to_pylist()
    text[0] = "Changed source text"
    table = table.set_column(
        table.column_names.index("text"),
        "text",
        pa.array(text, type=table.schema.field("text").type),
    )
    pq.write_table(table, path)
    _refresh_artifact(root, profile_path)

    with pytest.raises(ValueError, match="document rows"):
        validate_release(root)


def test_release_validation_detects_changed_vectors_with_recomputed_hashes(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    profile_path = f"profiles/{_PROFILE}/documents.parquet"
    path = root / profile_path
    table = pq.read_table(path)
    vectors = table["vector"].to_pylist()
    vectors[0][0] += 1.0
    table = table.set_column(
        table.column_names.index("vector"),
        "vector",
        pa.array(vectors, type=table.schema.field("vector").type),
    )
    pq.write_table(table, path)
    _refresh_artifact(root, profile_path)

    with pytest.raises(ValueError, match="vectors do not match"):
        validate_release(root)


def test_release_validation_detects_changed_projection_identity(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    projection_path = f"profiles/{_PROFILE}/projection.parquet"
    path = root / projection_path
    table = pq.read_table(path)
    ids = table["id"].to_pylist()
    ids[0] = "different"
    table = table.set_column(
        table.column_names.index("id"),
        "id",
        pa.array(ids, type=table.schema.field("id").type),
    )
    pq.write_table(table, path)
    _refresh_artifact(root, projection_path)

    with pytest.raises(ValueError, match="projection document identities"):
        validate_release(root)


@pytest.mark.parametrize(
    ("field", "message"),
    [
        ("entries_digest", "entries digest"),
        ("manifest_digest", "manifest digest"),
    ],
)
def test_release_validation_links_profile_metadata_to_catalog_identity(
    sample_catalog: Catalog,
    tmp_path: Path,
    field: str,
    message: str,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    metadata_path = f"profiles/{_PROFILE}/profile.json"
    path = root / metadata_path
    metadata = json.loads(path.read_text())
    metadata[field] = "0" * 64
    path.write_text(json.dumps(metadata))
    _refresh_artifact(root, metadata_path)

    with pytest.raises(ValueError, match=message):
        validate_release(root)


def test_release_validation_treats_the_producer_lancedb_version_as_provenance(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    metadata_path = f"profiles/{_PROFILE}/profile.json"
    path = root / metadata_path
    metadata = json.loads(path.read_text())
    metadata["lancedb_version"] = "0.37.1"
    path.write_text(json.dumps(metadata))
    _refresh_artifact(root, metadata_path)

    validate_release(root)


def test_release_validation_requires_a_trusted_registered_alias(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    metadata_path = f"profiles/{_PROFILE}/profile.json"
    path = root / metadata_path
    metadata = json.loads(path.read_text())
    metadata["embedding_functions"][0]["name"] = "unregistered-alias"
    path.write_text(json.dumps(metadata))
    _refresh_artifact(root, metadata_path)

    with pytest.raises(ValueError, match="alias is not registered"):
        validate_release(root)


def test_release_validation_detects_changed_lancedb_text_with_stable_ids(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)

    def change_text(table: pa.Table) -> pa.Table:
        values = table["text"].to_pylist()
        values[0] = "Changed LanceDB source text"
        return table.set_column(
            table.column_names.index("text"),
            "text",
            pa.array(values, type=table.schema.field("text").type),
        )

    _mutate_lancedb_table(root, change_text)

    with pytest.raises(ValueError, match="LanceDB document rows"):
        validate_release(root)


def test_release_validation_detects_changed_lancedb_binding(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)

    def change_binding(table: pa.Table) -> pa.Table:
        metadata = dict(table.schema.metadata or {})
        binding = json.loads(metadata[b"embedding_functions"])
        binding[0]["model"]["max_retries"] = 1
        metadata[b"embedding_functions"] = json.dumps(binding).encode()
        return table.replace_schema_metadata(metadata)

    _mutate_lancedb_table(root, change_binding)

    with pytest.raises(ValueError, match="embedding metadata"):
        validate_release(root)


def _profile_release(catalog: Catalog, tmp_path: Path) -> tuple[Path, CatalogRelease]:
    root = tmp_path / "release"
    release = build_release(
        catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
                export_documents=True,
            )
        },
    )
    return root, release


def _refresh_artifact(root: Path, artifact_path: str) -> None:
    release = CatalogRelease.from_mapping(
        json.loads((root / "release.json").read_text())
    )
    path = root / artifact_path
    artifacts = dict(release.artifacts)
    artifacts[artifact_path] = ReleaseArtifact(
        sha256=sha256_file(path),
        bytes=path.stat().st_size,
    )
    _write_release(root, artifacts)


def _mutate_lancedb_table(
    root: Path,
    transform: Callable[[pa.Table], pa.Table],
) -> None:
    artifact_path = f"profiles/{_PROFILE}/index.tar.gz"
    archive = root / artifact_path
    with TemporaryDirectory() as temporary:
        database = Path(temporary) / "index"
        extract_tar_archive(archive, database)
        import lancedb

        connection = lancedb.connect(database)
        table = connection.open_table("documents")
        changed = transform(table.to_arrow())
        del table
        connection.create_table("documents", data=changed, mode="overwrite")
        _write_lancedb_archive(database, archive)
    _refresh_artifact(root, artifact_path)


def _write_release(root: Path, artifacts: dict[str, ReleaseArtifact]) -> None:
    release = CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)
    (root / "release.json").write_text(json.dumps(release.to_record(), indent=2) + "\n")

from __future__ import annotations

import json
from pathlib import Path

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
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest, sha256_file
from chartcoach.catalog.releases.services import validate_runtime_release

pytestmark = pytest.mark.curation
_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-validation-test"
_CATALOG_RELEASE_FIXTURE = Path(__file__).parents[3] / "fixtures" / "catalog-release"


def test_runtime_validation_accepts_the_shared_release_fixture() -> None:
    release = validate_runtime_release(_CATALOG_RELEASE_FIXTURE)

    assert set(release.artifacts) == {"MANIFEST.md", "entries.parquet"}


def test_runtime_validation_loads_the_core_bundle(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)

    assert validate_runtime_release(root) == release


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
            "sensitive LanceDB field",
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


def test_curation_validation_aligns_profile_and_index_row_identities(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root, _ = _profile_release(sample_catalog, tmp_path)
    profile_path = f"profiles/{_PROFILE}/documents.parquet"
    path = root / profile_path
    table = pq.read_table(path)
    ids = table["id"].to_pylist()
    ids[0] = "different"
    table = table.set_column(
        table.column_names.index("id"),
        "id",
        pa.array(ids, type=table.schema.field("id").type),
    )
    pq.write_table(table, path)
    _refresh_artifact(root, profile_path)

    with pytest.raises(ValueError, match="row identities"):
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


def _write_release(root: Path, artifacts: dict[str, ReleaseArtifact]) -> None:
    release = CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)
    (root / "release.json").write_text(json.dumps(release.to_record(), indent=2) + "\n")

from __future__ import annotations

import json
import math
from collections.abc import Mapping
from os import PathLike
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

from ..._constants import LANCE_DOCUMENT_TABLE
from ..manifest import manifest_digest
from ..model import Catalog, _load_catalog_bundle
from ..profile_layout import ProfileArtifacts, discover_profile_artifacts
from ..profiles import (
    MAX_PROFILE_BYTES,
    ProfileMetadata,
    embedding_bindings_from_bytes,
)
from ..releases import CatalogRelease
from ..releases.archive import extract_tar_archive
from ..releases.services import validate_runtime_release

if TYPE_CHECKING:
    from lancedb import Table

_DOCUMENT_COLUMNS = (
    "row_id",
    "id",
    "parent_id",
    "role",
    "labels",
    "content_hash",
    "text",
)
_DOCUMENT_EXPORT_COLUMNS = frozenset((*_DOCUMENT_COLUMNS, "vector"))
_PROJECTION_ID_COLUMNS = ("row_id", "id", "parent_id", "role")
_PROJECTION_VALUE_COLUMNS = ("projection_x", "projection_y", "neighbors")
_PROJECTION_COLUMNS = frozenset((*_PROJECTION_ID_COLUMNS, *_PROJECTION_VALUE_COLUMNS))


def validate_release(source: Path | str) -> CatalogRelease:
    """Validate all files and derived data in a local release."""

    root = Path(source)
    release = validate_runtime_release(root)
    try:
        catalog = _load_catalog_bundle(root / "MANIFEST.md", root / "entries.parquet")
    except Exception as exc:
        raise ValueError(f"Catalog bundle could not be loaded: {exc}") from exc
    profiles = discover_profile_artifacts(release.artifacts)
    for artifacts in profiles.values():
        _validate_profile(root, catalog, artifacts)
    return release


def _open_reusable_profile(
    catalog: Catalog,
    *,
    release: str | PathLike[str],
    profile: str,
    database: Path,
) -> tuple[Table, ProfileMetadata, Path]:
    """Open one verified local profile for a derived-export rebuild."""

    root = _exact_release_root(release)
    release_record = validate_runtime_release(root)
    if (
        len(root.name) == 64
        and all(character in "0123456789abcdef" for character in root.name)
        and root.name != release_record.digest
    ):
        raise ValueError(
            "Reusable release digest does not match its digest-addressed directory."
        )
    profiles = discover_profile_artifacts(release_record.artifacts)
    try:
        artifacts = profiles[profile]
    except KeyError as exc:
        raise ValueError(f"Reusable profile is not present: {profile!r}.") from exc
    reused_catalog = _load_catalog_bundle(
        root / "MANIFEST.md",
        root / "entries.parquet",
    )
    metadata = _read_profile_metadata(root, artifacts.metadata)
    if (metadata.projection is None) != (artifacts.projection is None):
        raise ValueError(
            f"Reusable profile {profile!r} has inconsistent projection metadata."
        )
    _validate_profile_identity(reused_catalog, metadata)
    archive = _local_path(root, artifacts.index)
    extract_tar_archive(archive, database)

    import lancedb

    table = lancedb.connect(database).open_table(LANCE_DOCUMENT_TABLE)
    expected = catalog.documents().to_arrow()
    indexed = _by_row_id(table.to_arrow())
    _validate_documents(indexed, expected, label="LanceDB")
    _vectors(indexed, metadata, label="LanceDB")
    _validate_binding(indexed, metadata, label="LanceDB")
    _validate_native_indexes(table, metadata, indexed.num_rows)
    return table, metadata, archive


def _validate_profile(
    root: Path,
    catalog: Catalog,
    artifacts: ProfileArtifacts,
) -> None:
    profile = artifacts.profile
    try:
        metadata = _read_profile_metadata(root, artifacts.metadata)
        _validate_profile_identity(catalog, metadata)
        expected = catalog.documents().to_arrow()

        with TemporaryDirectory(prefix="chartcoach-index-") as directory:
            database = Path(directory) / "index"
            extract_tar_archive(_local_path(root, artifacts.index), database)
            import lancedb

            table = lancedb.connect(database).open_table(LANCE_DOCUMENT_TABLE)
            indexed = _by_row_id(table.to_arrow())
            _validate_documents(indexed, expected, label="LanceDB")
            index_vectors = _vectors(indexed, metadata, label="LanceDB")
            _validate_binding(indexed, metadata, label="LanceDB")
            _validate_native_indexes(table, metadata, indexed.num_rows)

        if artifacts.documents is not None:
            documents = _by_row_id(
                pq.read_table(_local_path(root, artifacts.documents))
            )
            _validate_document_export(
                documents,
                expected,
                index_vectors,
                profile=profile,
                metadata=metadata,
            )

        if artifacts.projection is None:
            if metadata.projection is not None:
                raise ValueError("profile.json declares a missing projection.parquet")
        else:
            if metadata.projection is None:
                raise ValueError("projection.parquet is absent from profile.json")
            projection = _by_row_id(
                pq.read_table(_local_path(root, artifacts.projection))
            )
            _validate_projection(
                projection,
                expected,
                profile=profile,
                metadata=metadata,
            )
    except Exception as exc:
        raise ValueError(f"Profile {profile!r} is invalid: {exc}") from exc


def _read_profile_metadata(root: Path, path: str) -> ProfileMetadata:
    metadata_file = _local_path(root, path)
    if metadata_file.stat().st_size > MAX_PROFILE_BYTES:
        raise ValueError("profile.json exceeds the 64 KiB limit")
    with metadata_file.open("rb") as source:
        return ProfileMetadata.from_bytes(source.read(MAX_PROFILE_BYTES + 1))


def _validate_profile_identity(catalog: Catalog, metadata: ProfileMetadata) -> None:
    if metadata.entries_digest != catalog.entries_digest():
        raise ValueError("profile entries digest does not match the catalog entries")
    expected_manifest = manifest_digest(catalog.manifest.markdown)
    if metadata.manifest_digest != expected_manifest:
        raise ValueError("profile manifest digest does not match MANIFEST.md")


def _validate_native_indexes(
    table: Table, metadata: ProfileMetadata, rows: int
) -> None:
    indexes = list(table.list_indices())
    if rows and not any(
        index.index_type == "FTS" and index.columns == ["text"] for index in indexes
    ):
        raise ValueError("Index must provide full-text search on the text column.")
    for index in indexes:
        stats = table.index_stats(index.name)
        if (
            stats is not None
            and stats.distance_type is not None
            and stats.distance_type != metadata.distance_metric
        ):
            raise ValueError(
                f"Index {index.name!r} distance metric disagrees with the profile."
            )


def _validate_document_export(
    documents: pa.Table,
    expected: pa.Table,
    index_vectors: np.ndarray,
    *,
    profile: str,
    metadata: ProfileMetadata,
) -> None:
    if set(documents.column_names) != _DOCUMENT_EXPORT_COLUMNS:
        raise ValueError(
            "Profile Parquet columns must be the document contract plus vector"
        )
    if b"chartcoach_projection" in (documents.schema.metadata or {}):
        raise ValueError("documents.parquet cannot contain projection metadata")
    _validate_profile_name(documents, profile)
    _validate_documents(documents, expected, label="Profile Parquet")
    document_vectors = _vectors(documents, metadata, label="Profile Parquet")
    if not np.array_equal(document_vectors, index_vectors):
        raise ValueError("Profile Parquet vectors do not match the LanceDB vectors")
    _validate_binding(documents, metadata, label="Profile Parquet")


def _validate_profile_name(table: pa.Table, profile: str) -> None:
    value = (table.schema.metadata or {}).get(b"chartcoach_profile")
    if value != profile.encode("utf-8"):
        raise ValueError("profile metadata does not match its artifact path")


def _validate_documents(
    actual: pa.Table,
    expected: pa.Table,
    *,
    label: str,
) -> None:
    missing = set(_DOCUMENT_COLUMNS) - set(actual.column_names)
    if missing:
        raise ValueError(f"{label} is missing columns: {', '.join(sorted(missing))}")
    selected = actual.select(_DOCUMENT_COLUMNS).sort_by([("row_id", "ascending")])
    expected = expected.select(_DOCUMENT_COLUMNS).sort_by([("row_id", "ascending")])
    if not pa.types.is_integer(selected.schema.field("row_id").type):
        raise ValueError(f"{label} row_id must contain integers")
    if selected.num_rows != expected.num_rows:
        raise ValueError(f"{label} row count does not match the catalog documents")
    row_ids = selected["row_id"].to_pylist()
    if row_ids != list(range(selected.num_rows)) or len(set(row_ids)) != len(row_ids):
        raise ValueError(f"{label} row_id mapping must be unique and contiguous")
    ids = selected["id"].to_pylist()
    if len(set(ids)) != len(ids):
        raise ValueError(f"{label} document ids must be unique")
    if selected.to_pylist() != expected.to_pylist():
        raise ValueError(
            f"{label} document rows do not match the catalog derivation. "
            "Regenerate the affected index or document export from catalog.documents() "
            "before building or publishing the release."
        )


def _by_row_id(table: pa.Table) -> pa.Table:
    if "row_id" not in table.column_names:
        return table
    return table.sort_by([("row_id", "ascending")])


def _vectors(
    table: pa.Table,
    metadata: ProfileMetadata,
    *,
    label: str,
) -> np.ndarray:
    if "vector" not in table.column_names:
        raise ValueError(f"{label} is missing the vector column")
    vector_type = table.schema.field("vector").type
    if not (
        pa.types.is_fixed_size_list(vector_type)
        and pa.types.is_float32(vector_type.value_type)
    ):
        raise ValueError(f"{label} vectors must be fixed-size float32 lists")
    if vector_type.list_size != metadata.dimensions:
        raise ValueError(f"{label} vector dimensions do not match profile.json")
    values = table["vector"].combine_chunks()
    if values.null_count or values.values.null_count:
        raise ValueError(f"{label} vectors must not contain null values")
    matrix = np.array(values.values.to_numpy(), copy=True).reshape(
        table.num_rows, metadata.dimensions
    )
    if not np.isfinite(matrix).all():
        raise ValueError(f"{label} vectors must contain finite values")
    return matrix


def _validate_binding(
    table: pa.Table,
    metadata: ProfileMetadata,
    *,
    label: str,
) -> None:
    raw = (table.schema.metadata or {}).get(b"embedding_functions")
    if raw is None:
        raise ValueError(f"{label} is missing LanceDB embedding metadata")
    bindings = embedding_bindings_from_bytes(raw)
    if [binding.to_record() for binding in bindings] != [
        binding.to_record() for binding in metadata.embedding_functions
    ]:
        raise ValueError(f"{label} embedding metadata does not match profile.json")


def _validate_projection(
    table: pa.Table,
    expected: pa.Table,
    *,
    profile: str,
    metadata: ProfileMetadata,
) -> None:
    if set(table.column_names) != _PROJECTION_COLUMNS:
        raise ValueError(
            "projection.parquet columns do not match the projection contract"
        )
    _validate_profile_name(table, profile)
    identity = table.select(_PROJECTION_ID_COLUMNS).sort_by([("row_id", "ascending")])
    expected_identity = expected.select(_PROJECTION_ID_COLUMNS).sort_by(
        [("row_id", "ascending")]
    )
    if (
        not pa.types.is_integer(identity.schema.field("row_id").type)
        or identity.to_pylist() != expected_identity.to_pylist()
    ):
        raise ValueError("projection document identities do not match the catalog")
    raw = (table.schema.metadata or {}).get(b"chartcoach_projection")
    if (
        raw is None
        or metadata.projection is None
        or json.loads(raw.decode("utf-8")) != metadata.projection.to_record()
    ):
        raise ValueError("projection metadata does not match profile.json")
    for column in ("projection_x", "projection_y"):
        values = table[column].combine_chunks()
        if not pa.types.is_float32(values.type) or values.null_count:
            raise ValueError(f"{column} must contain non-null float32 values")
        if not np.isfinite(values.to_numpy()).all():
            raise ValueError(f"{column} must contain finite values")
    neighbors = table["neighbors"].to_pylist()
    for row_id, row in enumerate(neighbors):
        if not isinstance(row, Mapping):
            raise TypeError("neighbors must contain structured rows")
        ids = row.get("ids")
        distances = row.get("distances")
        if not isinstance(ids, list) or not isinstance(distances, list):
            raise TypeError("neighbors must contain id and distance lists")
        if len(ids) != len(distances) or not ids:
            raise ValueError(
                "neighbor id and distance lists must be non-empty and equal"
            )
        if ids[0] != row_id or not math.isclose(float(distances[0]), 0.0):
            raise ValueError("neighbors must begin with the row_id at zero distance")
        if any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or not 0 <= value < table.num_rows
            for value in ids
        ):
            raise ValueError("neighbor ids must reference profile row_id values")
        if any(
            isinstance(value, bool)
            or not isinstance(value, int | float)
            or not math.isfinite(float(value))
            or float(value) < 0
            for value in distances
        ):
            raise ValueError("neighbor distances must be finite and nonnegative")


def _exact_release_root(release: str | PathLike[str]) -> Path:
    path = Path(release).absolute()
    root = path.parent if path.name == "release.json" else path
    if not root.is_dir() or not (root / "release.json").is_file():
        raise ValueError(
            "Profile reuse release must be an exact local release directory."
        )
    return root


def _local_path(root: Path, path: str) -> Path:
    return root.joinpath(*PurePosixPath(path).parts)


__all__ = ["validate_release"]

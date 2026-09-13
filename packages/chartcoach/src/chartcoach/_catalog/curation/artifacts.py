from __future__ import annotations

import gzip
import json
import shutil
import tarfile
from collections.abc import Mapping
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, cast

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

from ..._constants import LANCE_DOCUMENT_TABLE
from ..manifest import manifest_digest
from ..model import Catalog
from ..profile_layout import (
    PROFILE_DOCUMENTS_FILE,
    PROFILE_INDEX_FILE,
    PROFILE_METADATA_FILE,
    PROFILE_PROJECTION_FILE,
    PROFILE_ROOT,
    profile_artifact_path,
)
from ..profiles import (
    DOCUMENTS_VERSION,
    JsonValue,
    ProfileMetadata,
    ProjectionAlgorithm,
    ProjectionMetadata,
    embedding_bindings_from_bytes,
)
from ..releases import ReleaseArtifact
from ..releases.hashing import sha256_file
from .lancedb_index import _index_rows, build_lancedb_index
from .projection import Projection, project_vectors

if TYPE_CHECKING:
    from lancedb import Table

    from .release_builder import ProfileBuild


_NEIGHBORS_TYPE = pa.struct(
    [
        pa.field("ids", pa.list_(pa.uint32())),
        pa.field("distances", pa.list_(pa.float32())),
    ]
)


def build_release_artifacts(
    catalog: Catalog,
    root: Path,
    *,
    profiles: Mapping[str, ProfileBuild],
) -> dict[str, ReleaseArtifact]:
    from .release_builder import EmbeddingProfile

    artifacts: dict[str, ReleaseArtifact] = {}
    with TemporaryDirectory(prefix="chartcoach-lancedb-") as temporary:
        prepared = {
            name: _profile_table(catalog, Path(temporary) / name, profile=profile)
            for name, profile in profiles.items()
            if not isinstance(profile, EmbeddingProfile)
        }
        for name, (table, metadata, _) in prepared.items():
            profile = profiles[name]
            projection = (
                None
                if profile.umap is None
                else ProjectionMetadata.from_mapping(
                    {"algorithm": "umap", "options": profile.umap}
                )
            )
            _profile_metadata(
                catalog,
                table,
                table.to_arrow(),
                profile=profile,
                reused_metadata=metadata,
                projection=projection,
            ).to_bytes()
        for profile_name, profile in profiles.items():
            directory = root / PROFILE_ROOT / profile_name
            documents_path = directory / PROFILE_DOCUMENTS_FILE
            archive_path = directory / PROFILE_INDEX_FILE
            metadata_path = directory / PROFILE_METADATA_FILE
            projection_path = directory / PROFILE_PROJECTION_FILE
            directory.mkdir(parents=True, exist_ok=True)
            database = Path(temporary) / profile_name
            table, reused_metadata, reused_archive = (
                prepared[profile_name]
                if profile_name in prepared
                else _profile_table(catalog, database, profile=profile)
            )
            documents = table.to_arrow().sort_by([("row_id", "ascending")])
            projection, projection_metadata = _projection_table(
                documents,
                profile=profile_name,
                umap=profile.umap,
            )
            profile_metadata = _profile_metadata(
                catalog,
                table,
                documents,
                profile=profile,
                reused_metadata=reused_metadata,
                projection=projection_metadata,
            )
            if profile.export_documents:
                pq.write_table(
                    _document_export(documents, profile=profile_name),
                    documents_path,
                )
            if projection is not None:
                pq.write_table(projection, projection_path)
            metadata_path.write_bytes(profile_metadata.to_bytes())
            if reused_archive is None:
                _write_lancedb_archive(database, archive_path)
            else:
                shutil.copyfile(reused_archive, archive_path)

            for path in (metadata_path, archive_path, documents_path, projection_path):
                if path.is_file():
                    artifacts[profile_artifact_path(profile_name, path.name)] = (
                        _artifact(path)
                    )
    return artifacts


def _profile_table(
    catalog: Catalog,
    database: Path,
    *,
    profile: ProfileBuild,
) -> tuple[Table, ProfileMetadata | None, Path | None]:
    from .release_builder import EmbeddingProfile, IndexProfile

    if isinstance(profile, IndexProfile):
        import lancedb
        from lancedb.index import FTS

        from .validation import _validate_documents

        source_table = profile.index
        if source_table.count_rows() != len(catalog.documents()):
            raise ValueError(
                "Native index row count does not match the catalog documents"
            )
        documents = source_table.to_arrow()
        _validate_documents(
            documents, catalog.documents().to_arrow(), label="Native index"
        )
        _vectors(documents, label="Native index")
        raw = (documents.schema.metadata or {}).get(b"embedding_functions")
        if raw is None:
            raise ValueError("Native index must declare its embedding binding.")
        documents = documents.select(
            [*catalog.documents().columns, "vector"]
        ).replace_schema_metadata({b"embedding_functions": raw})
        # Arrow supplies complete vectors and metadata. An explicit embedding
        # configuration would make LanceDB construct providers during ingestion.
        table = lancedb.connect(database).create_table(
            LANCE_DOCUMENT_TABLE, data=_index_rows(documents)
        )
        if documents.num_rows:
            table.create_index("text", config=FTS())
        if profile.configure is not None:
            profile.configure(table)
        return table, None, None

    if isinstance(profile, EmbeddingProfile):
        table = build_lancedb_index(
            catalog,
            database,
            embedding=profile.embedding,
        )
        if profile.configure is not None:
            profile.configure(table)
        return table, None, None

    from .validation import _open_reusable_profile

    return _open_reusable_profile(
        catalog,
        release=profile.release,
        profile=profile.profile,
        database=database,
    )


def _document_export(documents: pa.Table, *, profile: str) -> pa.Table:
    metadata = dict(documents.schema.metadata or {})
    metadata[b"chartcoach_profile"] = profile.encode("utf-8")
    return documents.replace_schema_metadata(metadata)


def _projection_table(
    documents: pa.Table,
    *,
    profile: str,
    umap: Mapping[str, object] | None,
) -> tuple[pa.Table | None, ProjectionMetadata | None]:
    if umap is None:
        return None, None
    vectors, _ = _vectors(documents, label="LanceDB")
    projection = project_vectors(vectors, umap=umap)
    projection_metadata = ProjectionMetadata(
        algorithm=cast(ProjectionAlgorithm, projection.algorithm),
        options=cast(Mapping[str, JsonValue], projection.options),
    )
    result = (
        documents.select(["row_id", "id", "parent_id", "role"])
        .append_column(
            "projection_x",
            pa.array(projection.coordinates[:, 0], type=pa.float32()),
        )
        .append_column(
            "projection_y",
            pa.array(projection.coordinates[:, 1], type=pa.float32()),
        )
        .append_column("neighbors", _neighbors(projection))
    )
    metadata = {
        b"chartcoach_profile": profile.encode("utf-8"),
        b"chartcoach_projection": json.dumps(
            projection_metadata.to_record(),
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8"),
    }
    return result.replace_schema_metadata(metadata), projection_metadata


def _profile_metadata(
    catalog: Catalog,
    table: Table,
    documents: pa.Table,
    *,
    profile: ProfileBuild,
    reused_metadata: ProfileMetadata | None,
    projection: ProjectionMetadata | None,
) -> ProfileMetadata:
    raw = (table.schema.metadata or {}).get(b"embedding_functions")
    if raw is None:
        raise ValueError("LanceDB table is missing embedding metadata.")
    bindings = embedding_bindings_from_bytes(raw)
    _, dimensions = _vectors(documents, label="Profile")

    if reused_metadata is None:
        from .release_builder import EmbeddingProfile, IndexProfile

        if not isinstance(profile, EmbeddingProfile | IndexProfile):
            raise TypeError(
                "Fresh profile metadata requires an embedding or index profile."
            )
        import lancedb

        distance_metric = profile.distance_metric
        python_requirements = profile.python_requirements
        lancedb_version = lancedb.__version__
    else:
        distance_metric = reused_metadata.distance_metric
        python_requirements = reused_metadata.python_requirements
        lancedb_version = reused_metadata.lancedb_version

    metadata = ProfileMetadata(
        schema_version=1,
        documents_version=DOCUMENTS_VERSION,
        entries_digest=catalog.entries_digest(),
        manifest_digest=manifest_digest(catalog.manifest.markdown),
        embedding_functions=bindings,
        dimensions=dimensions,
        distance_metric=distance_metric,
        python_requirements=python_requirements,
        lancedb_version=lancedb_version,
        projection=projection,
    )
    from .validation import (
        _validate_documents,
        _validate_native_indexes,
    )

    _validate_documents(documents, catalog.documents().to_arrow(), label="LanceDB")
    _validate_native_indexes(table, metadata, documents.num_rows)
    return metadata


def _vectors(documents: pa.Table, *, label: str) -> tuple[np.ndarray, int]:
    if "vector" not in documents.column_names:
        raise ValueError(f"{label} table does not contain a vector column.")
    vector_type = documents.schema.field("vector").type
    if not (
        pa.types.is_fixed_size_list(vector_type)
        and pa.types.is_float32(vector_type.value_type)
    ):
        raise ValueError(f"{label} vector column must be fixed-size float32 lists.")
    vector_array = documents["vector"].combine_chunks()
    if vector_array.null_count or vector_array.values.null_count:
        raise ValueError(f"{label} vector column must not contain null values.")
    vectors = np.array(vector_array.values.to_numpy(), copy=True).reshape(
        documents.num_rows, vector_type.list_size
    )
    if not np.isfinite(vectors).all():
        raise ValueError(f"{label} vector column must contain finite values.")
    return vectors, vector_type.list_size


def _neighbors(projection: Projection) -> pa.Array:
    return pa.array(
        [
            {
                "ids": ids.tolist(),
                "distances": distances.tolist(),
            }
            for ids, distances in zip(
                projection.neighbor_ids,
                projection.neighbor_distances,
                strict=True,
            )
        ],
        type=_NEIGHBORS_TYPE,
    )


def _write_lancedb_archive(database: Path, archive_path: Path) -> None:
    if archive_path.exists():
        archive_path.unlink()
    with (
        archive_path.open("wb") as output,
        gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as compressed,
        tarfile.open(fileobj=compressed, mode="w") as archive,
    ):
        for path in sorted(database.rglob("*")):
            archive.add(
                path,
                arcname=path.relative_to(database).as_posix(),
                recursive=False,
                filter=_normalized_tar_info,
            )


def _normalized_tar_info(info: tarfile.TarInfo) -> tarfile.TarInfo:
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""
    info.mtime = 0
    info.mode = 0o755 if info.isdir() else 0o644
    return info


def _artifact(path: Path) -> ReleaseArtifact:
    return ReleaseArtifact(
        sha256=sha256_file(path),
        bytes=path.stat().st_size,
    )


__all__ = ["build_release_artifacts"]

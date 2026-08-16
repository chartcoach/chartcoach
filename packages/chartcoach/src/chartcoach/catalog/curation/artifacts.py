from __future__ import annotations

import gzip
import json
import tarfile
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

from ..collection import Catalog
from ..releases import ReleaseArtifact
from ..releases.hashing import sha256_file
from ..releases.models import safe_relative_path
from .lancedb_index import build_lancedb_index
from .projection import Projection, project_vectors

if TYPE_CHECKING:
    from lancedb import Table

    from .release_builder import EmbeddingProfile


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
    profiles: Mapping[str, EmbeddingProfile],
) -> dict[str, ReleaseArtifact]:
    artifacts: dict[str, ReleaseArtifact] = {}
    for profile_name, profile in profiles.items():
        profile_name = _profile_path(profile_name)
        directory = root / "profiles" / Path(*PurePosixPath(profile_name).parts)
        documents = directory / "documents.parquet"
        archive = directory / "index.tar.gz"
        directory.mkdir(parents=True, exist_ok=True)

        with TemporaryDirectory(prefix="chartcoach-lancedb-") as temporary:
            database = Path(temporary)
            table = build_lancedb_index(
                catalog,
                database,
                embedding=profile.embedding,
            )
            pq.write_table(
                _profile_table(table, profile=profile_name, umap=profile.umap),
                documents,
            )
            _write_lancedb_archive(database, archive)
        artifacts[_artifact_path(documents, profile=profile_name)] = _artifact(
            documents
        )
        artifacts[_artifact_path(archive, profile=profile_name)] = _artifact(archive)
    return artifacts


def _profile_path(value: str) -> str:
    return safe_relative_path(value, label="Embedding profile")


def _profile_table(
    table: Table,
    *,
    profile: str,
    umap: Mapping[str, object],
) -> pa.Table:
    documents = table.to_arrow()
    if "vector" not in documents.column_names:
        raise ValueError("LanceDB table does not contain a vector column.")
    vector_type = documents.schema.field("vector").type
    if not (
        pa.types.is_fixed_size_list(vector_type)
        and pa.types.is_float32(vector_type.value_type)
    ):
        raise ValueError("LanceDB vector column must be fixed-size float32 lists.")
    vector_array = documents["vector"].combine_chunks()
    if vector_array.null_count or vector_array.values.null_count:
        raise ValueError("LanceDB vector column must not contain null values.")
    vectors = np.array(vector_array.values.to_numpy(), copy=True).reshape(
        documents.num_rows, vector_type.list_size
    )
    if not np.isfinite(vectors).all():
        raise ValueError("LanceDB vector column must contain finite values.")
    projection = project_vectors(vectors, umap=umap)
    result = documents.append_column(
        "projection_x",
        pa.array(projection.coordinates[:, 0], type=pa.float32()),
    ).append_column(
        "projection_y",
        pa.array(projection.coordinates[:, 1], type=pa.float32()),
    )
    result = result.append_column("neighbors", _neighbors(projection))
    metadata = dict(result.schema.metadata or {})
    metadata[b"chartcoach_profile"] = profile.encode("utf-8")
    metadata[b"chartcoach_projection"] = json.dumps(
        {"algorithm": projection.algorithm, **projection.options},
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return result.replace_schema_metadata(metadata)


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


def _artifact_path(path: Path, *, profile: str) -> str:
    return PurePosixPath("profiles", profile, path.name).as_posix()


def _artifact(path: Path) -> ReleaseArtifact:
    return ReleaseArtifact(
        sha256=sha256_file(path),
        bytes=path.stat().st_size,
    )


__all__ = ["build_release_artifacts"]

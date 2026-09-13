from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING

from ..._constants import LANCE_DOCUMENT_TABLE
from ..errors import (
    CatalogCapabilityError,
    CatalogError,
    CatalogLookupError,
    CatalogOperationError,
    CatalogProfileError,
    CatalogValidationError,
)
from ..profile_layout import ProfileArtifacts
from ..profiles import (
    MAX_PROFILE_BYTES,
    EmbeddingBinding,
    ProfileMetadata,
)
from ..releases.models import safe_relative_path
from .cache import cached_index, shared_index_cache_supported
from .release import ReleaseLocation

if TYPE_CHECKING:
    from lancedb import Table


def load_profile_metadata(
    location: ReleaseLocation,
    profile: str,
    *,
    profiles: Mapping[str, ProfileArtifacts],
    entries_digest: str,
    manifest_digest: str,
) -> ProfileMetadata:
    """Read and link one profile.json file while LanceDB stays unloaded."""

    profile_artifacts = _available_profile(profiles, profile)
    path = profile_artifacts.metadata
    artifact = location.release.artifact(path)
    if artifact.bytes > MAX_PROFILE_BYTES:
        raise CatalogProfileError(
            f"Profile {profile!r} metadata exceeds the 64 KiB limit.",
            details={"profile": profile, "bytes": artifact.bytes},
        )
    profile_path = location.artifact_path(path)
    with profile_path.open("rb") as source:
        data = source.read(MAX_PROFILE_BYTES + 1)
    metadata = ProfileMetadata.from_bytes(data)
    if (metadata.projection is None) != (profile_artifacts.projection is None):
        raise CatalogProfileError(
            f"Profile {profile!r} projection metadata disagrees with its release artifacts.",
            details={"profile": profile},
        )
    if metadata.entries_digest != entries_digest:
        raise CatalogProfileError(
            f"Profile {profile!r} belongs to different catalog entries.",
            details={
                "profile": profile,
                "expected_entries_digest": entries_digest,
                "profile_entries_digest": metadata.entries_digest,
            },
        )
    if metadata.manifest_digest != manifest_digest:
        raise CatalogProfileError(
            f"Profile {profile!r} belongs to a different catalog manifest.",
            details={
                "profile": profile,
                "expected_manifest_digest": manifest_digest,
                "profile_manifest_digest": metadata.manifest_digest,
            },
        )
    return metadata


def open_profile_index(
    location: ReleaseLocation,
    profile: str,
    *,
    profiles: Mapping[str, ProfileArtifacts],
    metadata: ProfileMetadata,
    directory: Path | None,
    public: bool,
) -> Table:
    """Open one verified LanceDB table from shared or caller-owned extraction."""

    profile_artifacts = _available_profile(profiles, profile)
    profile = profile_artifacts.profile
    archive_path = profile_artifacts.index
    artifact = location.release.artifact(archive_path)
    lancedb = _lancedb(profile)
    archive = location.artifact_path(archive_path)

    if directory is not None:
        target = directory.absolute()
        if target.exists():
            raise FileExistsError(f"{target} already exists.")
        from ..releases.archive import extract_tar_archive

        extract_tar_archive(archive, target)
        return _open_and_validate(lancedb, target, profile=profile, metadata=metadata)

    protected = shared_index_cache_supported()
    if public and not protected:
        raise CatalogCapabilityError(
            "Public index access requires a caller-owned directory on this platform.",
            details={"profile": profile},
            hints=["Pass a new directory to catalog.index(profile, directory=...)."],
        )
    target = cached_index(archive, artifact.sha256, protected=protected)
    try:
        table = _open_and_validate(lancedb, target, profile=profile, metadata=metadata)
    except (OSError, RuntimeError, ValueError):
        target = cached_index(
            archive,
            artifact.sha256,
            refresh=True,
            protected=protected,
        )
        table = _open_and_validate(lancedb, target, profile=profile, metadata=metadata)
    table.checkout(table.version)
    return table


def _open_and_validate(
    lancedb, target: Path, *, profile: str, metadata: ProfileMetadata
):
    try:
        table = lancedb.connect(target).open_table(LANCE_DOCUMENT_TABLE)
        _validate_lancedb_table(table, profile=profile, metadata=metadata)
    except CatalogError:
        raise
    except (OSError, RuntimeError, ValueError) as exc:
        raise CatalogOperationError(
            f"Profile {profile!r} LanceDB table could not be opened.",
            details={"profile": profile, "operation": "open_index"},
            hints=["Check that the local index directory is readable."],
        ) from exc
    return table


def _validate_lancedb_table(
    table: Table, *, profile: str, metadata: ProfileMetadata
) -> None:
    schema = table.schema
    raw = (schema.metadata or {}).get(b"embedding_functions")
    if raw is None:
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB table has no embedding binding."
        )
    if not isinstance(raw, bytes):
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB embedding binding must be bytes."
        )
    try:
        records = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB embedding binding is invalid."
        ) from exc
    if not isinstance(records, list) or len(records) != 1:
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB table must contain one embedding binding."
        )
    binding = EmbeddingBinding.from_mapping(records[0])
    if binding.to_record() != metadata.embedding_functions[0].to_record():
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB embedding binding disagrees with profile.json."
        )

    try:
        import pyarrow as pa
    except ModuleNotFoundError as exc:
        raise CatalogCapabilityError(
            "Index access requires PyArrow through chartcoach[index]."
        ) from exc
    try:
        vector = schema.field("vector").type
    except KeyError as exc:
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB table has no vector column."
        ) from exc
    if not (
        pa.types.is_fixed_size_list(vector) and pa.types.is_float32(vector.value_type)
    ):
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB vectors must be fixed-size float32 lists."
        )
    if vector.list_size != metadata.dimensions:
        raise CatalogProfileError(
            f"Profile {profile!r} LanceDB vector dimensions disagree with profile.json.",
            details={
                "profile": profile,
                "lancedb_dimensions": vector.list_size,
                "profile_dimensions": metadata.dimensions,
            },
        )


def _available_profile(
    profiles: Mapping[str, ProfileArtifacts], profile: str
) -> ProfileArtifacts:
    try:
        profile = safe_relative_path(profile, label="Index profile")
    except (TypeError, ValueError) as exc:
        raise CatalogValidationError(str(exc), details={"profile": profile}) from exc
    if profile not in profiles:
        choices = ", ".join(repr(value) for value in profiles)
        raise CatalogLookupError(
            f"Unknown profile: {profile}",
            details={"profile": profile, "available": list(profiles)},
            hints=[f"Available profiles: {choices or 'none'}."],
        )
    return profiles[profile]


def _lancedb(profile: str):
    try:
        import lancedb
    except ModuleNotFoundError as exc:
        raise CatalogCapabilityError(
            "Index access requires chartcoach[index].",
            details={"profile": profile},
            hints=["Install chartcoach[index]."],
        ) from exc
    return lancedb


__all__ = ["load_profile_metadata", "open_profile_index"]

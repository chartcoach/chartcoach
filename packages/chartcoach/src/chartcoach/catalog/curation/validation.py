from __future__ import annotations

import json
from os import PathLike
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from typing import Protocol, cast

import pyarrow.parquet as pq

from ...constants import LANCE_DOCUMENT_TABLE
from ..releases import CatalogRelease
from ..releases.archive import extract_tar_archive
from ..releases.services import validate_runtime_release

_EMBEDDING_BINDING_ERROR = (
    "Profile native LanceDB embedding metadata must define exactly one "
    "text-to-vector binding."
)
_EMBEDDING_CREDENTIAL_ERROR = (
    "Profile native LanceDB embedding metadata contains a literal value for a "
    "sensitive LanceDB field."
)
_EMBEDDING_REMOTE_CODE_ERROR = (
    "Profile native LanceDB embedding metadata must disable remote model code."
)
_PROFILE_REQUIRED_COLUMNS = frozenset(
    {"row_id", "id", "vector", "projection_x", "projection_y", "neighbors"}
)
_INDEX_IDENTITY_COLUMNS = ("row_id", "id")


class _EmbeddingDefinition(Protocol):
    model_fields: dict[str, object]

    def sensitive_keys(self) -> list[str]: ...


def validate_release(source: PathLike[str]) -> CatalogRelease:
    """Validate a complete release before publication."""

    root = Path(source)
    release = validate_runtime_release(root)
    for profile, paths in _profiles(release).items():
        _validate_profile(
            root,
            profile,
            documents_path=paths["documents"],
            index_path=paths["index"],
        )
    return release


def _profiles(release: CatalogRelease) -> dict[str, dict[str, str]]:
    profiles: dict[str, dict[str, str]] = {}
    for path in release.artifacts:
        if not path.startswith("profiles/"):
            continue
        if path.endswith("/documents.parquet"):
            kind = "documents"
            profile = path.removeprefix("profiles/").removesuffix("/documents.parquet")
        elif path.endswith("/index.tar.gz"):
            kind = "index"
            profile = path.removeprefix("profiles/").removesuffix("/index.tar.gz")
        else:
            continue
        profiles.setdefault(profile, {})[kind] = path

    for profile, artifacts in profiles.items():
        if set(artifacts) != {"documents", "index"}:
            missing = {"documents", "index"} - set(artifacts)
            raise ValueError(
                f"Profile {profile!r} is missing {', '.join(sorted(missing))}."
            )
    return profiles


def _validate_profile(
    root: Path,
    profile: str,
    *,
    documents_path: str,
    index_path: str,
) -> None:
    try:
        documents = pq.read_table(_local_path(root, documents_path))
        missing = _PROFILE_REQUIRED_COLUMNS - set(documents.column_names)
        if missing:
            raise ValueError(
                f"Profile Parquet is missing columns: {', '.join(sorted(missing))}."
            )
        metadata = documents.schema.metadata or {}
        if metadata.get(b"chartcoach_profile") != profile.encode("utf-8"):
            raise ValueError("Profile metadata does not match its artifact path.")
        embedding_metadata = metadata.get(b"embedding_functions")
        if embedding_metadata is None:
            raise ValueError("Profile is missing native LanceDB embedding metadata.")
        if issue := _embedding_metadata_issue(embedding_metadata):
            raise ValueError(issue)

        with TemporaryDirectory(prefix="chartcoach-index-") as directory:
            database = Path(directory) / "index"
            extract_tar_archive(_local_path(root, index_path), database)
            import lancedb

            indexed = (
                lancedb.connect(database).open_table(LANCE_DOCUMENT_TABLE).to_arrow()
            )
            if not set(_INDEX_IDENTITY_COLUMNS).issubset(indexed.column_names):
                raise ValueError("LanceDB table is missing row identity columns.")
            if not documents.select(_INDEX_IDENTITY_COLUMNS).equals(
                indexed.select(_INDEX_IDENTITY_COLUMNS)
            ):
                raise ValueError(
                    "LanceDB row identities do not match the profile Parquet file."
                )
    except Exception as exc:
        raise ValueError(f"Profile {profile!r} is invalid: {exc}") from exc


def _embedding_metadata_issue(raw: bytes) -> str | None:
    try:
        records = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return _EMBEDDING_BINDING_ERROR
    if not isinstance(records, list) or len(records) != 1:
        return _EMBEDDING_BINDING_ERROR
    record = records[0]
    if not (
        isinstance(record, dict)
        and isinstance(record.get("name"), str)
        and record["name"].strip()
        and isinstance(record.get("model"), dict)
        and record.get("source_column") == "text"
        and record.get("vector_column") == "vector"
    ):
        return _EMBEDDING_BINDING_ERROR

    name = record["name"].strip()
    model = record["model"]
    embedding = _registered_embedding(name)
    remote_code_field = embedding is not None and "trust_remote_code" in (
        embedding.model_fields
    )
    if ("trust_remote_code" in model or remote_code_field) and model.get(
        "trust_remote_code"
    ) is not False:
        return _EMBEDDING_REMOTE_CODE_ERROR

    sensitive_keys = () if embedding is None else embedding.sensitive_keys()
    if any(
        key in model and model[key] is not None and not _variable_reference(model[key])
        for key in sensitive_keys
    ):
        return _EMBEDDING_CREDENTIAL_ERROR
    return None


def _registered_embedding(name: str) -> _EmbeddingDefinition | None:
    from lancedb.embeddings import get_registry

    try:
        return cast(_EmbeddingDefinition, get_registry().get(name))
    except KeyError:
        return None


def _variable_reference(value: object) -> bool:
    return (
        isinstance(value, str)
        and value.startswith("$var:")
        and bool(value.removeprefix("$var:"))
        and ":" not in value.removeprefix("$var:")
    )


def _local_path(root: Path, path: str) -> Path:
    return root.joinpath(*PurePosixPath(path).parts)


__all__ = ["validate_release"]

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import PurePosixPath
from types import MappingProxyType
from typing import Literal

from .releases.models import safe_relative_path

PROFILE_ROOT = "profiles"
PROFILE_METADATA_FILE = "profile.json"
PROFILE_INDEX_FILE = "index.tar.gz"
PROFILE_DOCUMENTS_FILE = "documents.parquet"
PROFILE_PROJECTION_FILE = "projection.parquet"

ProfileArtifactKind = Literal["metadata", "index", "documents", "projection"]

_PROFILE_FILES: Mapping[str, ProfileArtifactKind] = MappingProxyType(
    {
        PROFILE_METADATA_FILE: "metadata",
        PROFILE_INDEX_FILE: "index",
        PROFILE_DOCUMENTS_FILE: "documents",
        PROFILE_PROJECTION_FILE: "projection",
    }
)
_PROFILE_ID_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?$")


@dataclass(frozen=True, slots=True)
class ProfileArtifacts:
    """Release artifact paths for one index profile."""

    profile: str
    metadata: str
    index: str
    documents: str | None
    projection: str | None


def validate_profile_id(value: str) -> str:
    """Return a lowercase portable single-component profile identifier."""

    try:
        profile = safe_relative_path(value, label="Profile ID")
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "Profile ID must be a lowercase portable single-component name."
        ) from exc
    if "/" in profile or _PROFILE_ID_PATTERN.fullmatch(profile) is None:
        raise ValueError(
            "Profile ID must be a lowercase portable single-component name."
        )
    return profile


def profile_artifact_path(profile: str, filename: str) -> str:
    """Return one artifact path for a newly produced profile."""

    profile = validate_profile_id(profile)
    if filename not in _PROFILE_FILES:
        raise ValueError(f"Unknown profile artifact filename: {filename!r}.")
    return PurePosixPath(PROFILE_ROOT, profile, filename).as_posix()


def discover_profile_artifacts(
    paths: Iterable[str],
) -> Mapping[str, ProfileArtifacts]:
    """Parse and validate profile ownership from a release artifact inventory."""

    profiles: dict[str, dict[ProfileArtifactKind, str]] = {}
    for path in paths:
        parts = PurePosixPath(path).parts
        if not parts or parts[0] != PROFILE_ROOT:
            continue
        if len(parts) < 3:
            raise ValueError(f"Invalid profile artifact path: {path!r}.")
        kind = _PROFILE_FILES.get(parts[-1])
        if kind is None:
            raise ValueError(f"Unknown profile artifact: {path!r}.")
        profile = "/".join(parts[1:-1])
        validate_profile_id(profile)
        profiles.setdefault(profile, {})[kind] = path

    result: dict[str, ProfileArtifacts] = {}
    for profile, artifacts in sorted(profiles.items()):
        metadata = artifacts.get("metadata")
        index = artifacts.get("index")
        if metadata is None:
            raise ValueError(f"Profile {profile!r} is missing profile.json.")
        if index is None:
            raise ValueError(f"Profile {profile!r} is missing index.tar.gz.")
        result[profile] = ProfileArtifacts(
            profile=profile,
            metadata=metadata,
            index=index,
            documents=artifacts.get("documents"),
            projection=artifacts.get("projection"),
        )
    return MappingProxyType(result)


__all__ = [
    "PROFILE_DOCUMENTS_FILE",
    "PROFILE_INDEX_FILE",
    "PROFILE_METADATA_FILE",
    "PROFILE_PROJECTION_FILE",
    "ProfileArtifacts",
    "discover_profile_artifacts",
    "profile_artifact_path",
    "validate_profile_id",
]

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import PurePosixPath
from types import MappingProxyType
from typing import cast

SCHEMA_VERSION = 1
REQUIRED_ARTIFACT_PATHS = ("MANIFEST.md", "entries.parquet")
_MAX_SAFE_INTEGER = 2**53 - 1
_FORBIDDEN_PATH_CHARACTERS = frozenset('<>:"\\|?*#%')
_WINDOWS_DEVICE_NAMES = frozenset({"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"})


@dataclass(frozen=True, slots=True)
class ReleaseArtifact:
    """The content descriptor for one release path."""

    sha256: str
    bytes: int

    def __post_init__(self) -> None:
        safe_sha256(self.sha256, label="Catalog release artifact sha256")
        object.__setattr__(
            self,
            "bytes",
            _non_negative_integer(self.bytes, label="Catalog release artifact bytes"),
        )

    @classmethod
    def from_mapping(cls, value: object) -> ReleaseArtifact:
        raw = _mapping(value, label="Catalog release artifact")
        _require_exact_keys(
            raw,
            expected={"sha256", "bytes"},
            label="Catalog release artifact",
        )
        return cls(
            sha256=_string(raw, "sha256", label="Catalog release artifact"),
            bytes=_integer(raw, "bytes", label="Catalog release artifact"),
        )

    def to_record(self) -> dict[str, object]:
        return {"sha256": self.sha256, "bytes": self.bytes}


@dataclass(frozen=True, slots=True)
class CatalogRelease:
    """An immutable artifact set addressed by its release digest."""

    digest: str
    artifacts: Mapping[str, ReleaseArtifact]
    schema_version: int = SCHEMA_VERSION

    def __post_init__(self) -> None:
        version = _non_negative_integer(
            self.schema_version,
            label="Catalog release schema_version",
        )
        if version != SCHEMA_VERSION:
            raise ValueError(f"Unsupported catalog release schema: {version!r}")
        safe_sha256(self.digest, label="Catalog release digest")

        artifacts: dict[str, ReleaseArtifact] = {}
        for path, artifact in sorted(self.artifacts.items()):
            path = safe_relative_path(path, label="Catalog artifact path")
            if not isinstance(artifact, ReleaseArtifact):
                raise TypeError(f"Catalog artifact descriptor is invalid: {path!r}")
            artifacts[path] = artifact
        _validate_artifact_paths(tuple(artifacts))
        for path in REQUIRED_ARTIFACT_PATHS:
            if path not in artifacts:
                raise ValueError(f"Catalog release is missing artifact {path!r}.")

        object.__setattr__(self, "schema_version", version)
        object.__setattr__(self, "artifacts", MappingProxyType(artifacts))

    @classmethod
    def from_mapping(cls, value: object) -> CatalogRelease:
        raw = _mapping(value, label="Catalog release")
        _require_exact_keys(
            raw,
            expected={"schema_version", "digest", "artifacts"},
            label="Catalog release",
        )
        artifact_records = _mapping(raw.get("artifacts"), label="Catalog artifacts")
        return cls(
            digest=_string(raw, "digest", label="Catalog release"),
            artifacts={
                path: ReleaseArtifact.from_mapping(record)
                for path, record in artifact_records.items()
            },
            schema_version=_integer(raw, "schema_version", label="Catalog release"),
        )

    def to_record(self) -> dict[str, object]:
        return {
            "schema_version": self.schema_version,
            "digest": self.digest,
            "artifacts": {
                path: artifact.to_record() for path, artifact in self.artifacts.items()
            },
        }

    def artifact(self, path: str) -> ReleaseArtifact:
        return self.artifacts[path]


def safe_relative_path(value: str, *, label: str) -> str:
    if not isinstance(value, str) or not value or not value.isascii():
        raise ValueError(f"{label} must be a portable relative path: {value!r}")
    parts = value.split("/")
    if any(not _is_portable_path_segment(part) for part in parts):
        raise ValueError(f"{label} must be a portable relative path: {value!r}")
    return PurePosixPath(*parts).as_posix()


def safe_sha256(value: object, *, label: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[a-f0-9]{64}", value) is None:
        raise ValueError(f"{label} must be a lowercase SHA-256 digest.")
    return value


def _validate_artifact_paths(paths: tuple[str, ...]) -> None:
    seen: dict[str, str] = {}
    for path in paths:
        folded = path.casefold()
        if previous := seen.get(folded):
            raise ValueError(f"Catalog artifact paths collide: {previous}, {path}")
        seen[folded] = path
    for folded, path in seen.items():
        parts = PurePosixPath(folded).parts
        if folded == "release.json":
            raise ValueError(f"Catalog artifact path is reserved: {path}")
        for length in range(1, len(parts)):
            ancestor = PurePosixPath(*parts[:length]).as_posix()
            if ancestor in seen:
                raise ValueError(
                    f"Catalog artifact paths collide: {seen[ancestor]}, {path}"
                )


def _mapping(value: object, *, label: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping) or not all(isinstance(key, str) for key in value):
        raise ValueError(f"{label} must be an object.")
    return cast(Mapping[str, object], value)


def _require_exact_keys(
    value: Mapping[str, object],
    *,
    expected: set[str],
    label: str,
) -> None:
    actual = set(value)
    if actual == expected:
        return
    if missing := expected - actual:
        raise ValueError(f"{label} is missing fields: {', '.join(sorted(missing))}.")
    raise ValueError(
        f"{label} has unsupported fields: {', '.join(sorted(actual - expected))}."
    )


def _string(value: Mapping[str, object], key: str, *, label: str) -> str:
    raw = value.get(key)
    if not isinstance(raw, str) or not raw:
        raise ValueError(f"{label} {key} must be a non-empty string.")
    return raw


def _integer(value: Mapping[str, object], key: str, *, label: str) -> int:
    return _non_negative_integer(value.get(key), label=f"{label} {key}")


def _non_negative_integer(value: object, *, label: str) -> int:
    if isinstance(value, bool):
        value = -1
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    if not isinstance(value, int) or not 0 <= value <= _MAX_SAFE_INTEGER:
        raise ValueError(
            f"{label} must be an integer from 0 through {_MAX_SAFE_INTEGER}."
        )
    return value


def _is_portable_path_segment(value: str) -> bool:
    if (
        not value
        or value in {".", ".."}
        or value.endswith(".")
        or any(character <= " " for character in value)
        or any(character in _FORBIDDEN_PATH_CHARACTERS for character in value)
    ):
        return False
    name = value.split(".", 1)[0].upper()
    return not (
        name in _WINDOWS_DEVICE_NAMES
        or re.fullmatch(r"(?:COM|LPT)[1-9]", name) is not None
    )


__all__ = ["CatalogRelease", "ReleaseArtifact"]

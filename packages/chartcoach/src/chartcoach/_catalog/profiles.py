from __future__ import annotations

import dataclasses as dc
import json
import math
import re
from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import Literal, TypeAlias, TypedDict, cast
from urllib.parse import parse_qsl, urlsplit

from .documents import DOCUMENTS_VERSION
from .errors import CatalogProfileError
from .releases.models import safe_sha256

PROFILE_SCHEMA_VERSION = 1
MAX_PROFILE_BYTES = 65_536

DistanceMetric: TypeAlias = Literal["cosine", "l2", "dot"]
ProjectionAlgorithm: TypeAlias = Literal["empty", "linear", "umap"]
JsonScalar: TypeAlias = bool | float | int | None | str
JsonValue: TypeAlias = JsonScalar | tuple["JsonValue", ...] | Mapping[str, "JsonValue"]

_PROFILE_FIELDS = frozenset(
    {
        "schema_version",
        "documents_version",
        "entries_digest",
        "manifest_digest",
        "embedding_functions",
        "dimensions",
        "distance_metric",
        "python_requirements",
        "lancedb_version",
        "projection",
    }
)
_BINDING_FIELDS = frozenset({"name", "model", "source_column", "vector_column"})
_PROJECTION_FIELDS = frozenset({"algorithm", "options"})
_DISTRIBUTION_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$")
_VERSION_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.!+_-]*$")
_VARIABLE_PATTERN = re.compile(r"^\$var:[^:]+$")
_SENSITIVE_NAME_PATTERN = re.compile(
    r"(?:^|[_-])(?:access[_-]?key|api[_-]?key|authorization|client[_-]?secret|cookie|credential|password|private[_-]?key|secret|signature|token)(?:$|[_-])",
    re.IGNORECASE,
)
_SENSITIVE_QUERY_NAMES = frozenset(
    {
        "access_key",
        "api_key",
        "apikey",
        "authorization",
        "credential",
        "password",
        "secret",
        "signature",
        "sig",
        "token",
    }
)


class ProfileInfo(TypedDict):
    """Index profile information returned by catalog description."""

    name: str
    profile_schema_version: int
    documents_version: int
    embedding_functions: list[dict[str, object]]
    dimensions: int
    distance_metric: DistanceMetric
    python_requirements: dict[str, str]
    lancedb_version: str
    projection: dict[str, object] | None


@dc.dataclass(frozen=True, slots=True)
class EmbeddingBinding:
    """One persisted LanceDB text-to-vector binding."""

    name: str
    model: Mapping[str, JsonValue]
    source_column: str = "text"
    vector_column: str = "vector"

    def __post_init__(self) -> None:
        if (
            not isinstance(self.name, str)
            or not self.name
            or self.name != self.name.strip()
        ):
            raise CatalogProfileError(
                "Profile embedding name must be a non-empty string."
            )
        if self.source_column != "text" or self.vector_column != "vector":
            raise CatalogProfileError(
                "Profile embedding binding must map text to vector."
            )
        model = _frozen_json_object(self.model, label="Profile embedding model")
        validate_embedding_model(model)
        object.__setattr__(self, "model", model)

    @classmethod
    def from_mapping(cls, value: object) -> EmbeddingBinding:
        record = _record(value, label="Profile embedding binding")
        _require_exact_fields(record, _BINDING_FIELDS, "Profile embedding binding")
        return cls(
            name=_string(record, "name", label="Profile embedding binding"),
            model=_frozen_json_object(
                _record(record.get("model"), label="Profile embedding model"),
                label="Profile embedding model",
            ),
            source_column=_string(
                record, "source_column", label="Profile embedding binding"
            ),
            vector_column=_string(
                record, "vector_column", label="Profile embedding binding"
            ),
        )

    def to_record(self) -> dict[str, object]:
        return {
            "name": self.name,
            "model": _thaw_json(self.model),
            "source_column": self.source_column,
            "vector_column": self.vector_column,
        }


@dc.dataclass(frozen=True, slots=True)
class ProjectionMetadata:
    """Generated projection algorithm and effective options."""

    algorithm: ProjectionAlgorithm
    options: Mapping[str, JsonValue]

    def __post_init__(self) -> None:
        if self.algorithm not in {"empty", "linear", "umap"}:
            raise CatalogProfileError(
                f"Unsupported profile projection algorithm: {self.algorithm!r}."
            )
        object.__setattr__(
            self,
            "options",
            _frozen_json_object(self.options, label="Profile projection options"),
        )

    @classmethod
    def from_mapping(cls, value: object) -> ProjectionMetadata:
        record = _record(value, label="Profile projection")
        _require_exact_fields(record, _PROJECTION_FIELDS, "Profile projection")
        algorithm = _string(record, "algorithm", label="Profile projection")
        if algorithm not in {"empty", "linear", "umap"}:
            raise CatalogProfileError(
                f"Unsupported profile projection algorithm: {algorithm!r}."
            )
        return cls(
            algorithm=algorithm,
            options=_frozen_json_object(
                _record(record.get("options"), label="Profile projection options"),
                label="Profile projection options",
            ),
        )

    def to_record(self) -> dict[str, object]:
        return {
            "algorithm": self.algorithm,
            "options": _thaw_json(self.options),
        }


@dc.dataclass(frozen=True, slots=True)
class ProfileMetadata:
    """Verified metadata for one release-owned index profile."""

    entries_digest: str
    manifest_digest: str
    embedding_functions: tuple[EmbeddingBinding, ...]
    dimensions: int
    distance_metric: DistanceMetric
    python_requirements: Mapping[str, str]
    lancedb_version: str
    projection: ProjectionMetadata | None
    schema_version: int = PROFILE_SCHEMA_VERSION
    documents_version: int = DOCUMENTS_VERSION

    def __post_init__(self) -> None:
        if (
            isinstance(self.schema_version, bool)
            or not isinstance(self.schema_version, int)
            or self.schema_version != PROFILE_SCHEMA_VERSION
        ):
            raise CatalogProfileError(
                f"Unsupported profile schema version: {self.schema_version!r}."
            )
        if (
            isinstance(self.documents_version, bool)
            or not isinstance(self.documents_version, int)
            or self.documents_version != DOCUMENTS_VERSION
        ):
            raise CatalogProfileError(
                f"Unsupported document derivation version: {self.documents_version!r}."
            )
        safe_sha256(self.entries_digest, label="Profile entries digest")
        safe_sha256(self.manifest_digest, label="Profile manifest digest")
        bindings = tuple(self.embedding_functions)
        if len(bindings) != 1 or not isinstance(bindings[0], EmbeddingBinding):
            raise CatalogProfileError(
                "Profile must contain exactly one embedding binding."
            )
        if isinstance(self.dimensions, bool) or not isinstance(self.dimensions, int):
            raise CatalogProfileError(
                "Profile dimensions must be a positive safe integer."
            )
        if not 1 <= self.dimensions <= 2**53 - 1:
            raise CatalogProfileError(
                "Profile dimensions must be a positive safe integer."
            )
        if self.distance_metric not in {"cosine", "l2", "dot"}:
            raise CatalogProfileError(
                f"Unsupported profile distance metric: {self.distance_metric!r}."
            )
        requirements = validate_requirements(self.python_requirements)
        _exact_version(self.lancedb_version, label="Profile LanceDB version")
        if self.projection is not None and not isinstance(
            self.projection, ProjectionMetadata
        ):
            raise CatalogProfileError("Profile projection metadata is invalid.")
        object.__setattr__(self, "embedding_functions", bindings)
        object.__setattr__(self, "python_requirements", MappingProxyType(requirements))

    @classmethod
    def from_mapping(cls, value: object) -> ProfileMetadata:
        record = _record(value, label="Profile metadata")
        _require_exact_fields(record, _PROFILE_FIELDS, "Profile metadata")
        schema_version = _integer(record, "schema_version", label="Profile metadata")
        documents_version = _integer(
            record, "documents_version", label="Profile metadata"
        )
        raw_bindings = record.get("embedding_functions")
        if not isinstance(raw_bindings, Sequence) or isinstance(
            raw_bindings, str | bytes
        ):
            raise CatalogProfileError(
                "Profile embedding_functions must be a JSON array."
            )
        projection_value = record.get("projection")
        projection = (
            None
            if projection_value is None
            else ProjectionMetadata.from_mapping(projection_value)
        )
        distance_metric = _string(record, "distance_metric", label="Profile metadata")
        if distance_metric not in {"cosine", "l2", "dot"}:
            raise CatalogProfileError(
                f"Unsupported profile distance metric: {distance_metric!r}."
            )
        return cls(
            schema_version=schema_version,
            documents_version=documents_version,
            entries_digest=_string(record, "entries_digest", label="Profile metadata"),
            manifest_digest=_string(
                record, "manifest_digest", label="Profile metadata"
            ),
            embedding_functions=tuple(
                EmbeddingBinding.from_mapping(item) for item in raw_bindings
            ),
            dimensions=_positive_integer(
                record, "dimensions", label="Profile metadata"
            ),
            distance_metric=distance_metric,
            python_requirements=validate_requirements(
                _record(
                    record.get("python_requirements"),
                    label="Profile Python requirements",
                )
            ),
            lancedb_version=_string(
                record, "lancedb_version", label="Profile metadata"
            ),
            projection=projection,
        )

    @classmethod
    def from_bytes(cls, data: bytes) -> ProfileMetadata:
        if len(data) > MAX_PROFILE_BYTES:
            raise CatalogProfileError("Profile metadata exceeds the 64 KiB limit.")
        try:
            value = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise CatalogProfileError(
                "Profile metadata must be valid UTF-8 JSON."
            ) from exc
        return cls.from_mapping(value)

    def to_record(self) -> dict[str, object]:
        return {
            "schema_version": self.schema_version,
            "documents_version": self.documents_version,
            "entries_digest": self.entries_digest,
            "manifest_digest": self.manifest_digest,
            "embedding_functions": [
                binding.to_record() for binding in self.embedding_functions
            ],
            "dimensions": self.dimensions,
            "distance_metric": self.distance_metric,
            "python_requirements": dict(self.python_requirements),
            "lancedb_version": self.lancedb_version,
            "projection": (
                None if self.projection is None else self.projection.to_record()
            ),
        }

    def to_bytes(self) -> bytes:
        data = (
            json.dumps(self.to_record(), indent=2, ensure_ascii=False, sort_keys=True)
            + "\n"
        ).encode("utf-8")
        if len(data) > MAX_PROFILE_BYTES:
            raise CatalogProfileError("Profile metadata exceeds the 64 KiB limit.")
        return data

    def info(self, name: str) -> ProfileInfo:
        return {
            "name": name,
            "profile_schema_version": self.schema_version,
            "documents_version": self.documents_version,
            "embedding_functions": [
                binding.to_record() for binding in self.embedding_functions
            ],
            "dimensions": self.dimensions,
            "distance_metric": self.distance_metric,
            "python_requirements": dict(self.python_requirements),
            "lancedb_version": self.lancedb_version,
            "projection": (
                None if self.projection is None else self.projection.to_record()
            ),
        }


def embedding_bindings_from_bytes(data: bytes) -> tuple[EmbeddingBinding, ...]:
    """Parse LanceDB embedding metadata while the provider stays unconstructed."""

    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CatalogProfileError(
            "LanceDB embedding metadata must be valid UTF-8 JSON."
        ) from exc
    if not isinstance(value, Sequence) or isinstance(value, str | bytes):
        raise CatalogProfileError("LanceDB embedding metadata must be a JSON array.")
    return tuple(EmbeddingBinding.from_mapping(item) for item in value)


def validate_embedding_model(
    model: Mapping[str, JsonValue],
    *,
    allowed_fields: frozenset[str] | None = None,
    sensitive_fields: frozenset[str] = frozenset(),
) -> None:
    """Validate portable embedding arguments while variables stay unresolved."""

    if allowed_fields is not None:
        unknown = sorted(set(model) - allowed_fields)
        if unknown:
            raise CatalogProfileError(
                "Profile embedding model contains unsupported setting(s): "
                + ", ".join(unknown)
                + "."
            )
    variable_fields = sensitive_fields | {"device", "max_retries"}
    for key, value in model.items():
        nested_variables = _variable_paths(value, path=key)
        if nested_variables:
            if isinstance(value, str) and _VARIABLE_PATTERN.fullmatch(value):
                if allowed_fields is not None and key not in variable_fields:
                    raise CatalogProfileError(
                        f"Profile embedding setting {key!r} cannot use a registry variable."
                    )
            else:
                raise CatalogProfileError(
                    f"Profile embedding setting {key!r} contains an invalid registry variable."
                )
        if (
            (key in sensitive_fields or _SENSITIVE_NAME_PATTERN.search(key))
            and value is not None
            and not (isinstance(value, str) and _VARIABLE_PATTERN.fullmatch(value))
        ):
            raise CatalogProfileError(
                f"Profile embedding setting {key!r} must use a registry variable."
            )
        if (
            key == "default_headers"
            and value is not None
            and (not isinstance(value, Mapping) or value)
        ):
            raise CatalogProfileError(
                "Profile embedding default_headers must be empty."
            )
        if _contains_sensitive_key(value):
            raise CatalogProfileError(
                f"Profile embedding setting {key!r} contains authentication data."
            )
        _reject_credential_urls(value, path=key)
    remote_code_field = (
        allowed_fields is not None and "trust_remote_code" in allowed_fields
    )
    if ("trust_remote_code" in model or remote_code_field) and model.get(
        "trust_remote_code"
    ) is not False:
        raise CatalogProfileError("Profile embedding must disable remote model code.")


def validate_requirements(value: Mapping[str, object]) -> dict[str, str]:
    """Return copied exact Python distribution requirements."""

    if not isinstance(value, Mapping) or not all(
        isinstance(name, str) and _DISTRIBUTION_PATTERN.fullmatch(name)
        for name in value
    ):
        raise CatalogProfileError(
            "Profile requirement names must be Python distributions."
        )
    result: dict[str, str] = {}
    for name, version in sorted(value.items()):
        if not isinstance(version, str):
            raise CatalogProfileError(
                f"Profile requirement {name!r} must use an exact version."
            )
        _exact_version(version, label=f"Profile requirement {name!r}")
        result[name] = version
    return result


def _exact_version(value: object, *, label: str) -> None:
    if (
        not isinstance(value, str)
        or _VERSION_PATTERN.fullmatch(value) is None
        or not any(character.isdigit() for character in value)
    ):
        raise CatalogProfileError(f"{label} must be a non-empty exact version.")


def _variable_paths(value: JsonValue, *, path: str) -> list[str]:
    if isinstance(value, str):
        return [path] if value.startswith("$var:") else []
    if isinstance(value, Mapping):
        return [
            nested
            for key, item in value.items()
            for nested in _variable_paths(item, path=f"{path}.{key}")
        ]
    if isinstance(value, tuple):
        return [
            nested
            for index, item in enumerate(value)
            for nested in _variable_paths(item, path=f"{path}[{index}]")
        ]
    return []


def _contains_sensitive_key(value: JsonValue) -> bool:
    if isinstance(value, Mapping):
        return any(
            _SENSITIVE_NAME_PATTERN.search(key) or _contains_sensitive_key(item)
            for key, item in value.items()
        )
    if isinstance(value, tuple):
        return any(_contains_sensitive_key(item) for item in value)
    return False


def _reject_credential_urls(value: JsonValue, *, path: str) -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            _reject_credential_urls(item, path=f"{path}.{key}")
        return
    if isinstance(value, tuple):
        for index, item in enumerate(value):
            _reject_credential_urls(item, path=f"{path}[{index}]")
        return
    if not isinstance(value, str):
        return
    parsed = urlsplit(value)
    if parsed.scheme.casefold() not in {"http", "https"}:
        return
    if parsed.username is not None or parsed.password is not None:
        raise CatalogProfileError(
            f"Profile embedding URL setting {path!r} contains credentials."
        )
    query_names = {
        name.casefold() for name, _ in parse_qsl(parsed.query, keep_blank_values=True)
    }
    if query_names & _SENSITIVE_QUERY_NAMES or any(
        _SENSITIVE_NAME_PATTERN.search(name) for name in query_names
    ):
        raise CatalogProfileError(
            f"Profile embedding URL setting {path!r} contains authentication parameters."
        )


def _frozen_json_object(
    value: Mapping[str, object], *, label: str
) -> Mapping[str, JsonValue]:
    if not all(isinstance(key, str) for key in value):
        raise CatalogProfileError(f"{label} keys must be strings.")
    return MappingProxyType(
        {key: _frozen_json(item, label=f"{label}.{key}") for key, item in value.items()}
    )


def _frozen_json(value: object, *, label: str) -> JsonValue:
    if isinstance(value, float) and not math.isfinite(value):
        raise CatalogProfileError(f"{label} must contain finite JSON numbers.")
    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, Mapping) and all(isinstance(key, str) for key in value):
        return _frozen_json_object(cast(Mapping[str, object], value), label=label)
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return tuple(_frozen_json(item, label=label) for item in value)
    raise CatalogProfileError(f"{label} must contain JSON values.")


def _thaw_json(value: JsonValue) -> object:
    if isinstance(value, Mapping):
        return {key: _thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw_json(item) for item in value]
    return value


def _record(value: object, *, label: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping) or not all(isinstance(key, str) for key in value):
        raise CatalogProfileError(f"{label} must be a JSON object.")
    return cast(Mapping[str, object], value)


def _require_exact_fields(
    value: Mapping[str, object], expected: frozenset[str], label: str
) -> None:
    actual = set(value)
    missing = sorted(expected - actual)
    unknown = sorted(actual - expected)
    if missing:
        raise CatalogProfileError(f"{label} is missing fields: {', '.join(missing)}.")
    if unknown:
        raise CatalogProfileError(
            f"{label} has unsupported fields: {', '.join(unknown)}."
        )


def _string(value: Mapping[str, object], key: str, *, label: str) -> str:
    raw = value.get(key)
    if not isinstance(raw, str) or not raw:
        raise CatalogProfileError(f"{label} {key} must be a non-empty string.")
    return raw


def _integer(value: Mapping[str, object], key: str, *, label: str) -> int:
    raw = value.get(key)
    if isinstance(raw, bool) or not isinstance(raw, int):
        raise CatalogProfileError(f"{label} {key} must be an integer.")
    return raw


def _positive_integer(value: Mapping[str, object], key: str, *, label: str) -> int:
    raw = value.get(key)
    if isinstance(raw, bool) or not isinstance(raw, int) or not 1 <= raw <= 2**53 - 1:
        raise CatalogProfileError(f"{label} {key} must be a positive safe integer.")
    return raw


__all__ = [
    "DOCUMENTS_VERSION",
    "MAX_PROFILE_BYTES",
    "DistanceMetric",
    "EmbeddingBinding",
    "ProfileInfo",
    "ProfileMetadata",
    "ProjectionMetadata",
    "embedding_bindings_from_bytes",
    "validate_embedding_model",
    "validate_requirements",
]

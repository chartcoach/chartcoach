from __future__ import annotations

import dataclasses as dc
import hashlib
import json
import sqlite3
import time
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from os import PathLike
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import platformdirs
from chromadb.api.types import (
    Documents,
    Embedding,
    EmbeddingFunction,
    Embeddings,
    Space,
    normalize_embeddings,
    optional_base64_strings_to_embeddings,
    optional_embeddings_to_base64_strings,
    validate_embedding_function,
)
from chromadb.utils.embedding_functions import (
    config_to_embedding_function,
    known_embedding_functions,
)

EmbeddingIdentityStrategy: TypeAlias = Literal["first_non_empty", "all_non_empty"]
EmbeddingCacheMode: TypeAlias = Literal["document", "query"]
IdentityExtractor: TypeAlias = Callable[[EmbeddingFunction[Documents]], str | None]

DEFAULT_CACHE_FILENAME = "chroma-embedding-cache.sqlite3"
DEFAULT_IDENTITY_PARTS = ("model_name", "name")
SQLITE_READ_CHUNK_SIZE = 500
_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS embedding_cache_entries (
    namespace TEXT NOT NULL,
    mode TEXT NOT NULL,
    text_sha256 TEXT NOT NULL,
    text TEXT NOT NULL,
    embedding_b64 TEXT NOT NULL,
    updated_at INTEGER NOT NULL,
    PRIMARY KEY (namespace, mode, text_sha256)
)
"""


@dc.dataclass(frozen=True, slots=True)
class EmbeddingIdentityRule:
    """Declarative rule for deriving an embedding cache identity."""

    parts: tuple[str, ...]
    strategy: EmbeddingIdentityStrategy = "first_non_empty"

    def __post_init__(self) -> None:
        if not self.parts:
            raise ValueError("identity_rule.parts must contain at least one part.")
        if self.strategy not in {"first_non_empty", "all_non_empty"}:
            raise ValueError(
                "identity_rule.strategy must be 'first_non_empty' or 'all_non_empty'."
            )

    def to_config(self) -> dict[str, Any]:
        """Return a serializable representation of the rule."""
        return {"parts": list(self.parts), "strategy": self.strategy}

    @staticmethod
    def from_config(config: Mapping[str, Any]) -> "EmbeddingIdentityRule":
        """Build a rule from serialized config."""
        parts = config.get("parts", DEFAULT_IDENTITY_PARTS)
        if not isinstance(parts, Sequence) or isinstance(parts, (str, bytes)):
            raise ValueError("identity_rule.parts must be a sequence of strings.")

        parsed_parts: list[str] = []
        for part in parts:
            if not isinstance(part, str) or not part:
                raise ValueError(
                    "identity_rule.parts entries must be non-empty strings."
                )
            parsed_parts.append(part)

        strategy = config.get("strategy", "first_non_empty")
        if not isinstance(strategy, str):
            raise ValueError("identity_rule.strategy must be a string.")

        return EmbeddingIdentityRule(
            parts=tuple(parsed_parts),
            strategy=cast(EmbeddingIdentityStrategy, strategy),
        )


@dc.dataclass(frozen=True, slots=True)
class _ResolvedEmbeddingIdentity:
    primary_value: str
    namespace: str


def _extract_model_name(embedding_function: EmbeddingFunction[Documents]) -> str | None:
    model_name = getattr(embedding_function, "model_name", None)
    return model_name if isinstance(model_name, str) and model_name else None


def _extract_name(embedding_function: EmbeddingFunction[Documents]) -> str | None:
    try:
        name = embedding_function.name()
    except Exception:
        return None
    return name if isinstance(name, str) and name else None


EMBEDDING_IDENTITY_EXTRACTORS: dict[str, IdentityExtractor] = {
    "model_name": _extract_model_name,
    "name": _extract_name,
}

DEFAULT_EMBEDDING_IDENTITY_RULE = EmbeddingIdentityRule(parts=DEFAULT_IDENTITY_PARTS)


def with_embedding_cache(
    embedding_function: EmbeddingFunction[Documents],
    *,
    cache_path: str | PathLike[str] | None = None,
    app_name: str = "chartcoach",
    identity_rule: EmbeddingIdentityRule = DEFAULT_EMBEDDING_IDENTITY_RULE,
) -> "CachedEmbeddingFunction":
    """Wrap a Chroma text embedding function with persistent per-text caching."""
    return CachedEmbeddingFunction(
        embedding_function,
        cache_path=cache_path,
        app_name=app_name,
        identity_rule=identity_rule,
    )


class CachedEmbeddingFunction(EmbeddingFunction[Documents]):
    """Persistent SQLite-backed cache for Chroma text embedding functions."""

    def __init__(
        self,
        embedding_function: EmbeddingFunction[Documents],
        *,
        cache_path: str | PathLike[str] | None = None,
        app_name: str = "chartcoach",
        identity_rule: EmbeddingIdentityRule = DEFAULT_EMBEDDING_IDENTITY_RULE,
    ) -> None:
        validate_embedding_function(cast(Any, embedding_function))
        if not isinstance(app_name, str) or not app_name:
            raise ValueError("app_name must be a non-empty string.")

        self._embedding_function = embedding_function
        self._raw_cache_path = (
            Path(cache_path).expanduser() if cache_path is not None else None
        )
        self._app_name = app_name
        self._identity_rule = identity_rule
        self.cache_path = _resolve_cache_path(cache_path=cache_path, app_name=app_name)

        resolved_identity = _resolve_embedding_identity(
            embedding_function=embedding_function,
            identity_rule=identity_rule,
        )
        self.embedding_identity = resolved_identity.primary_value
        self.cache_namespace = resolved_identity.namespace
        self.model_name = resolved_identity.primary_value

    def __call__(self, input: Documents) -> Embeddings:
        if not input:
            return self._embedding_function(input=input)
        return self._embed(
            input=input,
            mode="document",
            compute=self._embedding_function,
        )

    def embed_query(self, input: Documents) -> Embeddings:
        if not self._uses_distinct_query_cache():
            return self.__call__(input)
        if not input:
            return _coerce_embeddings(self._embedding_function.embed_query(input=input))
        return self._embed(
            input=input,
            mode="query",
            compute=self._embedding_function.embed_query,
        )

    @staticmethod
    def name() -> str:
        return "cached_embedding_function"

    @staticmethod
    def build_from_config(config: Mapping[str, Any]) -> "CachedEmbeddingFunction":
        CachedEmbeddingFunction.validate_config(config)

        wrapped = _as_mapping(config["wrapped"], "wrapped")
        wrapped_name = _as_non_empty_str(wrapped.get("name"), "wrapped.name")
        wrapped_config = _as_mapping(wrapped.get("config"), "wrapped.config")

        rebuilt = cast(
            EmbeddingFunction[Documents],
            config_to_embedding_function(
                {"name": wrapped_name, "config": dict(wrapped_config)}
            ),
        )

        raw_cache_path = config.get("cache_path")
        if raw_cache_path is not None and not isinstance(raw_cache_path, str):
            raise ValueError("cache_path must be a string or null.")

        app_name = _as_non_empty_str(config.get("app_name"), "app_name")
        identity_rule = EmbeddingIdentityRule.from_config(
            _as_mapping(config.get("identity_rule"), "identity_rule")
        )
        return CachedEmbeddingFunction(
            rebuilt,
            cache_path=raw_cache_path,
            app_name=app_name,
            identity_rule=identity_rule,
        )

    def get_config(self) -> dict[str, Any]:
        wrapped_config = self._wrapped_config()
        return {
            "wrapped": wrapped_config,
            "cache_path": (
                None if self._raw_cache_path is None else str(self._raw_cache_path)
            ),
            "app_name": self._app_name,
            "identity_rule": self._identity_rule.to_config(),
        }

    @staticmethod
    def validate_config(config: Mapping[str, Any]) -> None:
        wrapped = _as_mapping(config.get("wrapped"), "wrapped")
        wrapped_name = _as_non_empty_str(wrapped.get("name"), "wrapped.name")
        wrapped_config = _as_mapping(wrapped.get("config"), "wrapped.config")

        raw_cache_path = config.get("cache_path")
        if raw_cache_path is not None and not isinstance(raw_cache_path, str):
            raise ValueError("cache_path must be a string or null.")

        _as_non_empty_str(config.get("app_name"), "app_name")
        EmbeddingIdentityRule.from_config(
            _as_mapping(config.get("identity_rule"), "identity_rule")
        )

        wrapped_class = known_embedding_functions.get(wrapped_name)
        if wrapped_class is None:
            raise ValueError(
                f"Wrapped embedding function {wrapped_name!r} is not registered."
            )
        wrapped_class.validate_config(dict(wrapped_config))

    def validate_config_update(
        self, old_config: Mapping[str, Any], new_config: Mapping[str, Any]
    ) -> None:
        CachedEmbeddingFunction.validate_config(old_config)
        CachedEmbeddingFunction.validate_config(new_config)

        old_wrapped = _as_mapping(old_config.get("wrapped"), "old_config.wrapped")
        new_wrapped = _as_mapping(new_config.get("wrapped"), "new_config.wrapped")
        old_name = _as_non_empty_str(old_wrapped.get("name"), "old_config.wrapped.name")
        new_name = _as_non_empty_str(new_wrapped.get("name"), "new_config.wrapped.name")

        if old_name != new_name:
            return

        self._embedding_function.validate_config_update(
            dict(_as_mapping(old_wrapped.get("config"), "old_config.wrapped.config")),
            dict(_as_mapping(new_wrapped.get("config"), "new_config.wrapped.config")),
        )

    def default_space(self) -> Space:
        return self._embedding_function.default_space()

    def supported_spaces(self) -> list[Space]:
        return self._embedding_function.supported_spaces()

    def _embed(
        self,
        *,
        input: Documents,
        mode: EmbeddingCacheMode,
        compute: Callable[[Documents], Embeddings],
    ) -> Embeddings:
        unique_texts = list(dict.fromkeys(input))
        cached_embeddings = self._read_embeddings(texts=unique_texts, mode=mode)
        missing_texts = [text for text in unique_texts if text not in cached_embeddings]

        if missing_texts:
            computed_embeddings = _coerce_embeddings(compute(missing_texts))
            if len(computed_embeddings) != len(missing_texts):
                raise ValueError(
                    "Embedding function returned a different number of embeddings than requested texts."
                )

            new_entries = {
                text: embedding
                for text, embedding in zip(
                    missing_texts, computed_embeddings, strict=True
                )
            }
            self._write_embeddings(entries=new_entries, mode=mode)
            cached_embeddings.update(new_entries)

        return _coerce_embeddings([cached_embeddings[text] for text in input])

    def _read_embeddings(
        self, *, texts: Sequence[str], mode: EmbeddingCacheMode
    ) -> dict[str, Embedding]:
        if not texts:
            return {}

        texts_by_hash: dict[str, set[str]] = {}
        for text in texts:
            texts_by_hash.setdefault(_text_digest(text), set()).add(text)
        hits: dict[str, Embedding] = {}

        with self._connect() as conn:
            for hash_chunk in _batched(
                tuple(texts_by_hash.keys()), SQLITE_READ_CHUNK_SIZE
            ):
                placeholders = ", ".join("?" for _ in hash_chunk)
                rows = conn.execute(
                    f"""
                    SELECT text_sha256, text, embedding_b64
                    FROM embedding_cache_entries
                    WHERE namespace = ?
                      AND mode = ?
                      AND text_sha256 IN ({placeholders})
                    """,
                    (self.cache_namespace, mode, *hash_chunk),
                ).fetchall()

                for row in rows:
                    row_hash = cast(str, row["text_sha256"])
                    expected_texts = texts_by_hash.get(row_hash)
                    actual_text = row["text"]
                    payload = row["embedding_b64"]

                    if (
                        expected_texts is None
                        or not isinstance(actual_text, str)
                        or actual_text not in expected_texts
                        or not isinstance(payload, str)
                        or not payload
                    ):
                        continue

                    try:
                        hits[actual_text] = _deserialize_embedding(payload)
                    except ValueError:
                        continue

        return hits

    def _write_embeddings(
        self, *, entries: Mapping[str, Embedding], mode: EmbeddingCacheMode
    ) -> None:
        if not entries:
            return

        updated_at = int(time.time())
        rows = [
            (
                self.cache_namespace,
                mode,
                _text_digest(text),
                text,
                _serialize_embedding(embedding),
                updated_at,
            )
            for text, embedding in entries.items()
        ]

        with self._connect() as conn:
            conn.executemany(
                """
                INSERT INTO embedding_cache_entries (
                    namespace,
                    mode,
                    text_sha256,
                    text,
                    embedding_b64,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(namespace, mode, text_sha256)
                DO UPDATE SET
                    text = excluded.text,
                    embedding_b64 = excluded.embedding_b64,
                    updated_at = excluded.updated_at
                """,
                rows,
            )

    def _wrapped_config(self) -> dict[str, Any]:
        wrapped_name = _extract_name(self._embedding_function)
        if wrapped_name is None:
            raise ValueError(
                "Wrapped embedding function must expose a non-empty name()."
            )
        if wrapped_name not in known_embedding_functions:
            raise ValueError(
                f"Wrapped embedding function {wrapped_name!r} is not registered."
            )

        raw_config = self._embedding_function.get_config()
        if not isinstance(raw_config, Mapping):
            raise ValueError("Wrapped embedding function config must be a mapping.")

        return {"name": wrapped_name, "config": dict(raw_config)}

    def _uses_distinct_query_cache(self) -> bool:
        return (
            type(self._embedding_function).embed_query
            is not EmbeddingFunction.embed_query
        )

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.cache_path)
        conn.row_factory = sqlite3.Row

        try:
            conn.execute("PRAGMA busy_timeout = 5000")
            try:
                conn.execute("PRAGMA journal_mode = WAL")
            except sqlite3.DatabaseError:
                pass
            conn.execute(_SCHEMA_SQL)
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()


def _resolve_cache_path(
    *, cache_path: str | PathLike[str] | None, app_name: str
) -> Path:
    if cache_path is not None:
        return Path(cache_path).expanduser()
    return Path(platformdirs.user_cache_dir(app_name)) / DEFAULT_CACHE_FILENAME


def _resolve_embedding_identity(
    *,
    embedding_function: EmbeddingFunction[Documents],
    identity_rule: EmbeddingIdentityRule,
) -> _ResolvedEmbeddingIdentity:
    extracted_parts: list[dict[str, str]] = []
    for part in identity_rule.parts:
        extractor = EMBEDDING_IDENTITY_EXTRACTORS.get(part)
        if extractor is None:
            raise ValueError(f"Unknown embedding identity part: {part!r}.")
        value = extractor(embedding_function)
        if value:
            extracted_parts.append({"name": part, "value": value})

    if not extracted_parts:
        available = ", ".join(identity_rule.parts)
        raise ValueError(
            f"Could not derive an embedding identity from any of: {available}."
        )

    primary_value = extracted_parts[0]["value"]
    if identity_rule.strategy == "first_non_empty":
        namespace_payload: Mapping[str, Any] = {
            "strategy": identity_rule.strategy,
            "candidates": list(identity_rule.parts),
            "selected": extracted_parts[0],
        }
    else:
        namespace_payload = {
            "strategy": identity_rule.strategy,
            "candidates": list(identity_rule.parts),
            "selected": extracted_parts,
        }

    return _ResolvedEmbeddingIdentity(
        primary_value=primary_value,
        namespace=_canonical_json(namespace_payload),
    )


def _canonical_json(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _text_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _serialize_embedding(embedding: Embedding) -> str:
    payloads = optional_embeddings_to_base64_strings([embedding])
    if not payloads or payloads[0] is None:
        raise ValueError("Could not serialize embedding for cache storage.")
    return payloads[0]


def _deserialize_embedding(payload: str) -> Embedding:
    decoded = optional_base64_strings_to_embeddings([payload])
    if not decoded or decoded[0] is None:
        raise ValueError("Could not deserialize cached embedding payload.")
    return _coerce_embeddings([decoded[0]])[0]


def _coerce_embeddings(value: Any) -> Embeddings:
    normalized = normalize_embeddings(value)
    if normalized is None:
        raise ValueError("Embedding function returned no embeddings.")
    return normalized


def _as_mapping(value: Any, field_name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{field_name} must be a mapping.")
    return cast(Mapping[str, Any], value)


def _as_non_empty_str(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value


def _batched(values: Sequence[str], size: int) -> Iterator[tuple[str, ...]]:
    for index in range(0, len(values), size):
        yield tuple(values[index : index + size])


__all__ = [
    "CachedEmbeddingFunction",
    "DEFAULT_EMBEDDING_IDENTITY_RULE",
    "EMBEDDING_IDENTITY_EXTRACTORS",
    "EmbeddingIdentityRule",
    "with_embedding_cache",
]

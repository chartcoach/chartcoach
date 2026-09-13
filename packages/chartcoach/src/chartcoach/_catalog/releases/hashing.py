from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path

from .models import SCHEMA_VERSION, ReleaseArtifact


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def release_digest(artifacts: Mapping[str, ReleaseArtifact]) -> str:
    data = json.dumps(
        release_digest_record(artifacts),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def release_digest_record(
    artifacts: Mapping[str, ReleaseArtifact],
) -> dict[str, object]:
    """Return the canonical artifact envelope used for release identity."""

    return {
        "schema_version": SCHEMA_VERSION,
        "artifacts": {path: artifacts[path].to_record() for path in sorted(artifacts)},
    }


__all__ = ["release_digest", "release_digest_record", "sha256_file"]

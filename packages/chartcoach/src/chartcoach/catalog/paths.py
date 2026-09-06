"""Namespaced API for constructing catalog object keys."""

from __future__ import annotations

from dataclasses import dataclass
from posixpath import join

from .releases.models import safe_relative_path, safe_sha256


@dataclass(frozen=True, slots=True)
class _ProfilePaths:
    release: "_ReleasePaths"
    profile: str

    def documents(self) -> str:
        """catalog/releases/{digest}/profiles/{profile}/documents.parquet"""

        return self.release.artifact(
            join("profiles", self.profile, "documents.parquet")
        )

    def index(self) -> str:
        """catalog/releases/{digest}/profiles/{profile}/index.tar.gz"""

        return self.release.artifact(join("profiles", self.profile, "index.tar.gz"))


@dataclass(frozen=True, slots=True)
class _ReleasePaths:
    digest: str

    def root(self) -> str:
        """catalog/releases/{digest}"""

        return join("catalog/releases", self.digest)

    def json(self) -> str:
        """catalog/releases/{digest}/release.json"""

        return join(self.root(), "release.json")

    def artifact(self, path: str) -> str:
        """catalog/releases/{digest}/{path}"""

        return join(self.root(), safe_relative_path(path, label="artifact path"))

    def manifest(self) -> str:
        """catalog/releases/{digest}/MANIFEST.md"""

        return self.artifact("MANIFEST.md")

    def entries(self) -> str:
        """catalog/releases/{digest}/entries.parquet"""

        return self.artifact("entries.parquet")

    def profile(self, profile: str) -> _ProfilePaths:
        """Paths for one embedding profile."""

        return _ProfilePaths(
            self,
            safe_relative_path(profile, label="profile"),
        )


@dataclass(frozen=True, slots=True)
class _CatalogPaths:
    def selected(self) -> str:
        """catalog.json"""

        return "catalog.json"

    def release(self, digest: str) -> _ReleasePaths:
        """Paths for one immutable catalog release."""

        return _ReleasePaths(safe_sha256(digest, label="Catalog release digest"))


paths = _CatalogPaths()


__all__ = ["paths"]

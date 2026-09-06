from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from .manifest import manifest_digest

if TYPE_CHECKING:
    from .model import Catalog


class CatalogIdentity(TypedDict):
    """Entry, manifest, and release digests for one catalog."""

    entries_digest: str
    manifest_digest: str
    release_digest: str | None


def catalog_identity(catalog: Catalog) -> CatalogIdentity:
    """Return the three digests attached to a catalog."""

    return {
        "entries_digest": catalog.entries_digest(),
        "manifest_digest": manifest_digest(catalog.manifest.markdown),
        "release_digest": (None if catalog.release is None else catalog.release.digest),
    }


__all__ = ["CatalogIdentity", "catalog_identity"]

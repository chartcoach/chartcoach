from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from .errors import CatalogLookupError, CatalogValidationError
from .identity import catalog_identity
from .profiles import ProfileInfo
from .relations import TABLE_SCHEMAS

if TYPE_CHECKING:
    from .manifest import ManifestDefinition
    from .model import Catalog


class TableColumnInfo(TypedDict):
    """One named column in a catalog table."""

    name: str
    type: str


class TableInfo(TypedDict):
    """One catalog table and its current row count."""

    name: str
    rows: int
    columns: list[TableColumnInfo]


class VocabularyInfo(TypedDict):
    """One manifest-defined role or label family."""

    name: str
    description: str
    examples: list[str]


class CatalogInfo(TypedDict):
    """Catalog identity, tables, vocabulary, and optional profile information."""

    resolved_location: str | None
    release_digest: str | None
    entries_digest: str
    manifest_digest: str
    tables: list[TableInfo]
    section_roles: list[VocabularyInfo]
    label_families: list[VocabularyInfo]
    profiles: list[str]
    profile: ProfileInfo | None


def describe_catalog(catalog: Catalog, *, profile: str | None = None) -> CatalogInfo:
    """Return catalog information while the index and provider stay unloaded."""

    if profile is not None and (not isinstance(profile, str) or not profile):
        raise CatalogValidationError("Profile must be a non-empty string.")
    if profile is not None and profile not in catalog._profile_names:
        raise CatalogLookupError(
            f"Unknown profile: {profile}",
            details={"profile": profile, "available": list(catalog._profile_names)},
            hints=[_available_profiles(catalog)],
        )

    selected_profile: ProfileInfo | None = None
    if profile is not None:
        selected_profile = catalog._profile_metadata(profile).info(profile)
    identity = catalog_identity(catalog)
    return {
        "resolved_location": catalog._resolved_location,
        **identity,
        "tables": [
            {
                "name": name,
                "rows": catalog.table(name).height,
                "columns": [
                    {"name": column, "type": str(dtype)}
                    for column, dtype in schema.items()
                ],
            }
            for name, schema in TABLE_SCHEMAS.items()
        ],
        "section_roles": _vocabulary(catalog.manifest.section_roles),
        "label_families": _vocabulary(catalog.manifest.label_families),
        "profiles": list(catalog._profile_names),
        "profile": selected_profile,
    }


def _vocabulary(
    definitions: Mapping[str, ManifestDefinition],
) -> list[VocabularyInfo]:
    return [
        {
            "name": name,
            "description": definition.description,
            "examples": list(definition.examples),
        }
        for name, definition in definitions.items()
    ]


def _available_profiles(catalog: Catalog) -> str:
    choices = ", ".join(repr(name) for name in catalog._profile_names)
    return f"Available profiles: {choices or 'none'}."


__all__ = [
    "CatalogInfo",
    "TableColumnInfo",
    "TableInfo",
    "VocabularyInfo",
    "describe_catalog",
]

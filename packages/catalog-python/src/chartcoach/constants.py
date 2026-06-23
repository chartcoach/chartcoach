from __future__ import annotations

from urllib.parse import urljoin

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel


class ChartCoachDefaults(BaseModel):
    """Default package-pinned project settings."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        frozen=True,
        populate_by_name=True,
        validate_default=True,
    )

    catalog_artifact_base_url: str = Field(
        default="https://artifacts.chartcoach.dev",
        min_length=1,
    )
    guideline_url_template: str = Field(
        default="https://chartcoach.dev/guidelines/{id}",
        min_length=1,
    )
    catalog_digest: str = Field(
        default="7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19",
        min_length=1,
    )
    catalog_version: str = Field(default="0.1.6", min_length=1)
    index_top_k: int = Field(default=10, ge=1)
    lance_document_table: str = Field(default="catalog_documents", min_length=1)

    @field_validator("guideline_url_template")
    @classmethod
    def _validate_guideline_url_template(cls, value: str) -> str:
        if "{id}" not in value:
            raise ValueError("Guideline URL template must include `{id}`.")
        return value

    @property
    def catalog_release_root_url(self) -> str:
        """Return the release root URL for the package-pinned catalog."""

        return urljoin(
            self.catalog_artifact_base_url.rstrip("/") + "/",
            f"catalog/releases/{self.catalog_version}/{self.catalog_digest}/",
        )

    def to_record(self) -> dict[str, object]:
        """Return the JSON shape shared with JavaScript defaults."""

        return self.model_dump(by_alias=True)


CHARTCOACH_DEFAULTS = ChartCoachDefaults()

SOURCE_ENV = "CHARTCOACH_SOURCE"
INDEX_ENV = "CHARTCOACH_INDEX"
ARTIFACT_BASE_URL_ENV = "CHARTCOACH_ARTIFACT_BASE_URL"
CACHE_DIR_ENV = "CHARTCOACH_CACHE_DIR"
DEFAULT_INDEX_TOP_K = CHARTCOACH_DEFAULTS.index_top_k
DEFAULT_CATALOG_ARTIFACT_BASE_URL = CHARTCOACH_DEFAULTS.catalog_artifact_base_url
DEFAULT_GUIDELINE_URL_TEMPLATE = CHARTCOACH_DEFAULTS.guideline_url_template
DEFAULT_CATALOG_DIGEST = CHARTCOACH_DEFAULTS.catalog_digest
DEFAULT_CATALOG_VERSION = CHARTCOACH_DEFAULTS.catalog_version
LANCE_DOCUMENT_TABLE = CHARTCOACH_DEFAULTS.lance_document_table

__all__ = [
    "ARTIFACT_BASE_URL_ENV",
    "CACHE_DIR_ENV",
    "CHARTCOACH_DEFAULTS",
    "ChartCoachDefaults",
    "DEFAULT_CATALOG_ARTIFACT_BASE_URL",
    "DEFAULT_CATALOG_DIGEST",
    "DEFAULT_GUIDELINE_URL_TEMPLATE",
    "DEFAULT_INDEX_TOP_K",
    "DEFAULT_CATALOG_VERSION",
    "INDEX_ENV",
    "LANCE_DOCUMENT_TABLE",
    "SOURCE_ENV",
]

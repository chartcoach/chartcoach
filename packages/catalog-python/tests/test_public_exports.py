from __future__ import annotations

from chartcoach import (
    Catalog,
    CatalogManifest,
    Guideline,
    ParsedLabel,
    Section,
    open as open_chartcoach,
    parse_label,
)
from chartcoach.catalog import CatalogManifestError, ManifestDefinition
from chartcoach.catalog import Catalog as CatalogExport
from chartcoach.catalog import CatalogManifest as CatalogManifestExport
from chartcoach.catalog import references
from chartcoach.catalog import relations
from chartcoach.catalog.entries import Section as CatalogSection
from chartcoach.catalog.markdown import parse_guideline
from chartcoach.constants import DEFAULT_GUIDELINE_URL_TEMPLATE
from chartcoach.constants import CHARTCOACH_DEFAULTS, ChartCoachDefaults
from chartcoach.duckdb import connect_catalog, register_catalog, write_duckdb
from chartcoach.search import index, query


def test_package_exports_intentional_public_models() -> None:
    assert Catalog is CatalogExport
    assert CatalogManifest is CatalogManifestExport
    assert CatalogSection is Section
    assert callable(open_chartcoach)
    assert callable(parse_label)
    assert callable(parse_guideline)
    assert Guideline.__name__ == "Guideline"
    assert ParsedLabel.__name__ == "ParsedLabel"
    assert CatalogManifestError.__name__ == "CatalogManifestError"
    assert ManifestDefinition.__name__ == "ManifestDefinition"


def test_duckdb_exports_owned_integration_api() -> None:
    import chartcoach.duckdb as duckdb_api

    assert set(duckdb_api.__all__) == {
        "DuckDBConfigValue",
        "connect_catalog",
        "register_catalog",
        "write_duckdb",
    }
    assert connect_catalog is duckdb_api.connect_catalog
    assert register_catalog is duckdb_api.register_catalog
    assert write_duckdb is duckdb_api.write_duckdb


def test_relation_names_are_owned_by_catalog_relations() -> None:
    assert relations.GUIDELINES_RELATION == "guidelines"
    assert relations.SECTIONS_RELATION == "sections"
    assert relations.LABELS_RELATION == "labels"
    assert callable(relations.iter_catalog_tables)


def test_search_package_exports_search_primitives() -> None:
    assert callable(index)
    assert callable(query)


def test_guideline_url_template_is_owned_by_constants() -> None:
    assert isinstance(CHARTCOACH_DEFAULTS, ChartCoachDefaults)
    assert CHARTCOACH_DEFAULTS.guideline_url_template == DEFAULT_GUIDELINE_URL_TEMPLATE

    guideline_id = "compare-percentages-with-bars-not-pies"
    assert CHARTCOACH_DEFAULTS.guideline_url_template.format(id=guideline_id).endswith(
        f"/{guideline_id}"
    )

    dumped = CHARTCOACH_DEFAULTS.to_record()
    assert dumped["guidelineUrlTemplate"] == DEFAULT_GUIDELINE_URL_TEMPLATE
    assert dumped["catalogVersion"] == CHARTCOACH_DEFAULTS.catalog_version
    assert CHARTCOACH_DEFAULTS.catalog_release_root_url.endswith(
        f"/catalog/releases/{CHARTCOACH_DEFAULTS.catalog_version}/"
        f"{CHARTCOACH_DEFAULTS.catalog_digest}/"
    )
    assert references.DEFAULT_GUIDELINE_URL_TEMPLATE == DEFAULT_GUIDELINE_URL_TEMPLATE

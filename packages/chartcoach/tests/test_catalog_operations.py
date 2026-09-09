from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogError, Guideline, Section, open_catalog
from chartcoach._catalog.read import SourceDetail
from chartcoach._catalog.search import catalog_search
from chartcoach._catalog.sql import catalog_sql
from chartcoach.curation import EmbeddingProfile, build_release

_CONTRACT = (
    Path(__file__).parents[3] / "fixtures" / "catalog-contract" / "operations.json"
)
_RELEASE = Path(__file__).parents[3] / "fixtures" / "catalog-release"


def test_source_fields_survive_citation_metadata_recovery(
    sample_catalog: Catalog,
) -> None:
    expected = json.loads(_CONTRACT.read_text())["bibliography_render_recovery"]
    catalog = _catalog_with_references(sample_catalog, [expected["reference"]])
    record = catalog.read(ids=["reference-0"], source_detail="full")[0]
    assert record["sources"][0]["year"] == expected["year"]
    assert record["references"] == [expected["reference"]]
    assert (
        catalog.cite(ids=["reference-0"])[0]["sources"][0]["citation"]
        == expected["citation"]
    )


def test_source_reads_and_citations_preserve_bibtex_grouping(
    sample_catalog: Catalog,
) -> None:
    expected = json.loads(_CONTRACT.read_text())["protected_bibliography"]
    catalog = _catalog_with_references(sample_catalog, [expected["reference"]])
    source = catalog.read(ids=["reference-0"], source_detail="full")[0]["sources"][0]
    assert source["source_title"] == expected["source_title"]
    assert source["authors_text"] == expected["authors_text"]
    assert (
        catalog.cite(ids=["reference-0"])[0]["sources"][0]["citation"]
        == expected["citation"]
    )


@pytest.mark.parametrize(
    "case",
    json.loads(_CONTRACT.read_text(encoding="utf-8"))["bibliography_urls"],
    ids=lambda case: case["name"],
)
def test_source_urls_agree_across_reads_citations_and_tables(
    sample_catalog: Catalog, case: dict[str, str | None]
) -> None:
    reference = cast(str, case["reference"])
    catalog = _catalog_with_references(sample_catalog, [reference])
    minimal = catalog.read(ids=["reference-0"])[0]
    full = catalog.read(ids=["reference-0"], source_detail="full")[0]
    citation = catalog.cite(ids=["reference-0"])[0]["sources"][0]

    for source in (minimal["sources"][0], full["sources"][0], citation):
        assert source["url"] == case["url"]
        assert source["doi"] == case["doi"]
    assert citation["citation"] == case["citation"]
    assert full["references"] == [reference]
    for name in ("references", "guideline_sources"):
        assert catalog.table(name).select("url", "doi").to_dicts() == [
            {"url": case["url"], "doi": case["doi"]}
        ]


def test_python_matches_the_shared_catalog_operation_contract() -> None:
    contract = json.loads(_CONTRACT.read_text(encoding="utf-8"))
    catalog = open_catalog(_RELEASE)

    for case in contract["query_cases"]:
        options = case["options"]
        assert (
            catalog.query(
                ids=options.get("ids", ()),
                labels=options.get("labels", ()),
                label_prefixes=options.get("labelPrefixes", ()),
                contains=options.get("contains"),
                limit=options.get("limit", 50),
            ).to_dicts()
            == case["records"]
        )
    read_options = contract["read"]["options"]
    assert (
        catalog.read(
            ids=read_options["ids"],
            source_detail=read_options["sourceDetail"],
        )
        == contract["read"]["records"]
    )
    full_options = contract["read_full"]["options"]
    assert (
        catalog.read(
            ids=full_options["ids"],
            source_detail=full_options["sourceDetail"],
        )
        == contract["read_full"]["records"]
    )
    assert (
        catalog.cite(ids=contract["cite"]["options"]["ids"])
        == contract["cite"]["records"]
    )
    description = catalog.describe()
    assert {
        field: description[field]
        for field in (
            "release_digest",
            "entries_digest",
            "manifest_digest",
            "section_roles",
            "label_families",
            "profiles",
            "profile",
        )
    } == contract["description"]


def test_reference_keys_deduplicate_equivalent_definitions_and_reject_conflicts(
    sample_catalog: Catalog,
) -> None:
    contract = json.loads(_CONTRACT.read_text(encoding="utf-8"))
    equivalent = _catalog_with_references(
        sample_catalog,
        contract["bibliography"]["equivalent"],
    )

    assert equivalent.table("references").get_column("id").to_list() == ["shared2024"]

    conflicting = _catalog_with_references(
        sample_catalog,
        contract["bibliography"]["conflicting"],
    )
    with pytest.raises(CatalogError, match="Conflicting BibTeX definitions"):
        conflicting.table("references")


def test_entries_digest_uses_unicode_code_point_order(
    sample_catalog: Catalog,
) -> None:
    contract = json.loads(_CONTRACT.read_text(encoding="utf-8"))
    catalog = Catalog.from_guidelines(
        [Guideline.from_mapping(row) for row in contract["identity"]["records"]],
        manifest=sample_catalog.manifest,
    )

    assert catalog.entries_digest() == contract["identity"]["entries_digest"]


def test_catalog_methods_reject_invalid_argument_types(sample_catalog: Catalog) -> None:
    with pytest.raises(CatalogError, match="ids must be a sequence"):
        sample_catalog.read(ids="direct-labels")
    with pytest.raises(CatalogError, match="labels must be a sequence"):
        sample_catalog.query(labels="chart:line")
    with pytest.raises(CatalogError, match="Unknown source detail"):
        sample_catalog.read(
            ids=["direct-labels"],
            source_detail=cast(SourceDetail, "everything"),
        )


def test_catalog_query_preserves_unicode_case_matching(
    sample_catalog: Catalog,
) -> None:
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id="street",
                title="Straße",
                description="Street label guidance.",
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Keep the street label visible.",
                    ),
                ),
            )
        ],
        manifest=sample_catalog.manifest,
    )

    assert catalog.query(contains="STRAẞE").get_column("id").to_list() == ["street"]


def test_catalog_query_rejects_separator_only_text(
    sample_catalog: Catalog,
) -> None:
    with pytest.raises(CatalogError, match="must not consist only"):
        sample_catalog.query(contains="-_ ")


def test_catalog_sql_returns_bounded_rows_and_catalog_identity(
    sample_catalog: Catalog,
) -> None:
    result = catalog_sql(
        sample_catalog,
        "select id, title from guidelines order by id",
        limit=1,
    )

    assert result["columns"] == [
        {"name": "id", "type": "VARCHAR"},
        {"name": "title", "type": "VARCHAR"},
    ]
    assert result["rows"] == [{"id": "direct-labels", "title": "Use direct labels"}]
    assert result["row_count"] == 1
    assert result["truncated"] is True
    assert result["limit"] == 1
    assert result["entries_digest"] == sample_catalog.entries_digest()
    assert len(result["manifest_digest"]) == 64
    assert result["release_digest"] is None


def test_catalog_sql_returns_json_values(sample_catalog: Catalog) -> None:
    result = catalog_sql(
        sample_catalog, "select date '2026-07-11' as day, 1.25::decimal(4, 2) as value"
    )

    assert result["rows"] == [{"day": "2026-07-11", "value": "1.25"}]


@pytest.mark.parametrize(
    "statement",
    ["create table x as select 1", "select 1; select 2"],
)
def test_catalog_sql_rejects_non_read_only_queries(
    sample_catalog: Catalog,
    statement: str,
) -> None:
    with pytest.raises(CatalogError) as exc_info:
        catalog_sql(sample_catalog, statement)

    assert exc_info.value.code == "invalid_input"


def test_catalog_sql_disables_external_file_access(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    external_csv = tmp_path / "external.csv"
    external_csv.write_text("x\n1\n")

    with pytest.raises(CatalogError, match="Cannot access file"):
        catalog_sql(
            sample_catalog, f"select * from read_csv_auto({external_csv.as_posix()!r})"
        )


@pytest.mark.search
@pytest.mark.curation
def test_catalog_search_returns_bounded_fts_matches(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root = tmp_path / "release"
    profile = "test-deterministic"
    build_release(
        sample_catalog,
        release_root,
        profiles={
            profile: EmbeddingProfile(
                deterministic_embedding("chartcoach-operation-search")
            )
        },
    )
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    catalog = open_catalog(release_root)
    assert catalog.release is not None

    result = catalog_search(
        catalog, "direct labels", profile=profile, limit=2, mode="fts"
    )

    assert result["profile"] == profile
    assert result["mode"] == "fts"
    assert result["score_kind"] == "relevance"
    assert result["documents_considered"] <= 2
    assert isinstance(result["documents_truncated"], bool)
    assert result["release_digest"] == catalog.release.digest
    match = result["matches"][0]
    assert match["id"] == "direct-labels"
    assert match["matched_document_id"] == "direct-labels---overview"
    assert match["matched_role"] == "overview"
    assert len(match["matched_excerpt"]) <= 360
    assert match["excerpt_truncated"] is False
    assert match["score_kind"] == "relevance"


def test_in_memory_catalog_reports_unavailable_index(
    sample_catalog: Catalog,
) -> None:
    with pytest.raises(CatalogError) as exc_info:
        sample_catalog.index("test")

    assert exc_info.value.code == "unavailable_capability"


@pytest.mark.search
@pytest.mark.curation
def test_catalog_search_marks_bounded_match_excerpts(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id="long-guideline",
                title="Long guideline",
                description="needle " + "context " * 100,
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Keep the complete evidence available through read.",
                    ),
                ),
            )
        ],
        manifest=sample_catalog.manifest,
    )
    release = tmp_path / "release"
    profile = "test-long"
    build_release(
        catalog,
        release,
        profiles={
            profile: EmbeddingProfile(deterministic_embedding("bounded-search-excerpt"))
        },
    )
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )

    result = catalog_search(open_catalog(release), "needle", profile=profile, limit=1)
    match = result["matches"][0]

    assert len(match["matched_excerpt"]) == 360
    assert match["excerpt_truncated"] is True
    assert catalog.read(ids=["long-guideline"], source_detail="none")[0][
        "description"
    ].endswith("context ")


def test_sql_json_conversion_rejects_non_finite_values(
    sample_catalog: Catalog,
) -> None:
    with pytest.raises(CatalogError, match="cannot be represented as JSON"):
        catalog_sql(sample_catalog, "select 'NaN'::double as value")


def _catalog_with_references(catalog: Catalog, references: list[str]) -> Catalog:
    return Catalog.from_guidelines(
        [
            Guideline(
                id=f"reference-{index}",
                title=f"Reference {index}",
                description="Reference identity fixture.",
                sections=(
                    Section(role="advice", title="Advice", content="Read the source."),
                ),
                references=(reference,),
            )
            for index, reference in enumerate(references)
        ],
        manifest=catalog.manifest,
    )

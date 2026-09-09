from __future__ import annotations

from typing import cast

import pytest
from chartcoach import Catalog, CatalogError, CatalogManifest, Guideline, Section
from chartcoach._catalog.references import (
    parse_bibtex,
    parse_bibtex_reference,
)

BIBTEX = """% generated note
@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""


@pytest.mark.parametrize(
    ("bibtex", "expected_fragments", "excluded_fragments"),
    [
        (
            BIBTEX,
            ("@article{smith2024", "Readable charts"),
            ("% generated note",),
        ),
        (
            r"""@misc{contact2024,
  title = {Contact chart-team@example.com},
  url = {https://example.com/chart@coach}
}
""",
            ("chart-team@example.com", "https://example.com/chart@coach"),
            (),
        ),
    ],
)
def test_parse_bibtex_handles_comments_and_at_signs(
    bibtex: str,
    expected_fragments: tuple[str, ...],
    excluded_fragments: tuple[str, ...],
) -> None:
    parsed = parse_bibtex(bibtex)

    assert len(parsed) == 1
    for fragment in expected_fragments:
        assert fragment in parsed[0]
    for fragment in excluded_fragments:
        assert fragment not in parsed[0]


def test_parse_bibtex_reference_rejects_empty_entries() -> None:
    with pytest.raises(ValueError, match="No BibTeX entry parsed"):
        parse_bibtex_reference("% empty bibliography")


def test_parse_bibtex_reference_preserves_tex_commands() -> None:
    bibtex = r"""@article{macro2024,
  title = {Readable\! charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""

    parsed = parse_bibtex_reference(bibtex)
    assert parsed["key"] == "macro2024"
    assert parsed["fields"]["title"] == "Readable\\! charts"


def test_authored_bibliography_retains_unicode_and_macro_context() -> None:
    bibliography = (
        '@string{journal = "Revue des références"}\n'
        "@article{first, title={Données}, journal=journal}\n"
        "@article{second, title={Échelles}, journal=journal}"
    )

    first, second = parse_bibtex(bibliography)

    assert first == (
        '@string{journal = "Revue des références"}\n'
        "@article{first, title={Données}, journal=journal}"
    )
    assert second == (
        '@string{journal = "Revue des références"}\n'
        "@article{second, title={Échelles}, journal=journal}"
    )


def test_catalog_citations_are_cached_and_preserve_raw_source(
    sample_manifest: CatalogManifest, monkeypatch: pytest.MonkeyPatch
) -> None:
    import polars_refkit

    calls = 0
    original = polars_refkit.full_bibliography

    def render(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(polars_refkit, "full_bibliography", render)
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id=guideline_id,
                title="Inspect sources",
                description="Read the original publication.",
                sections=(
                    Section(role="advice", title="Advice", content="Read sources."),
                ),
                references=(BIBTEX,),
            )
            for guideline_id in ("first", "second")
        ],
        manifest=sample_manifest,
    )

    first = catalog.cite(ids=["first"])
    first[0]["sources"][0]["citation"] = "Changed by caller"
    second = catalog.cite(ids=["second", "first"])

    assert calls == 1
    assert catalog.table("references").height == 1
    assert catalog.table("references").item(0, "bibtex") == BIBTEX
    assert [row["sources"][0]["citation"] for row in second] == [
        "Smith, A. (2024). Readable charts. Journal of Charts.",
        "Smith, A. (2024). Readable charts. Journal of Charts.",
    ]


def test_catalog_rejects_ambiguous_reference_fields(
    sample_manifest: CatalogManifest,
) -> None:
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id="source",
                title="Inspect sources",
                description="Read the original publication.",
                sections=(
                    Section(role="advice", title="Advice", content="Read sources."),
                ),
                references=("@article{source,title={First},title={Second}}",),
            )
        ],
        manifest=sample_manifest,
    )

    with pytest.raises(CatalogError) as error:
        catalog.read(ids=["source"], source_detail="full")
    diagnostics = cast(list[dict[str, object]], error.value.details["diagnostics"])
    assert diagnostics[0]["code"] == "duplicate_field"

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


@pytest.mark.parametrize(("reference_count", "workers"), [(1, 1), (40, 1), (40, 4)])
def test_catalog_citations_are_cached_and_preserve_raw_source(
    sample_manifest: CatalogManifest,
    monkeypatch: pytest.MonkeyPatch,
    reference_count: int,
    workers: int,
) -> None:
    from concurrent.futures import ThreadPoolExecutor
    from threading import Lock

    import polars as pl
    import refkit

    calls = 0
    lock = Lock()
    original = refkit.Document

    def render(*args, **kwargs):
        nonlocal calls
        with lock:
            calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(pl, "thread_pool_size", lambda: workers)
    monkeypatch.setattr(refkit, "Document", render)
    sources = tuple(
        BIBTEX.replace("smith2024", f"smith{i:03}") for i in range(reference_count)
    )
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id=guideline_id,
                title="Inspect sources",
                description="Read the original publication.",
                sections=(
                    Section(role="advice", title="Advice", content="Read sources."),
                ),
                references=sources,
            )
            for guideline_id in ("first", "second")
        ],
        manifest=sample_manifest,
    )

    with ThreadPoolExecutor(max_workers=4) as readers:
        results = list(readers.map(lambda _: catalog.cite(ids=["first"]), range(4)))
    assert all(result == results[0] for result in results)
    first = results[0]
    first[0]["sources"][0]["citation"] = "Changed by caller"
    second = catalog.cite(ids=["second", "first"])

    assert calls == reference_count
    assert catalog.table("references").get_column("bibtex").to_list() == list(sources)
    for row in second:
        assert [source["reference_id"] for source in row["sources"]] == [
            f"smith{i:03}" for i in range(reference_count)
        ]
        assert [source["citation"] for source in row["sources"]] == [
            "Smith, A. (2024). Readable charts. Journal of Charts."
        ] * reference_count


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


def test_failed_citation_render_can_be_retried(
    sample_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    import polars as pl
    import refkit

    sources = [BIBTEX.replace("smith2024", f"smith{i:03}") for i in range(40)]
    catalog = Catalog(
        sample_catalog.to_frame().with_columns(pl.lit(sources).alias("references")),
        manifest=sample_catalog.manifest,
    )
    original = refkit.Document

    def render(library, *args, **kwargs):
        if "smith020" in library:
            raise refkit.RefkitError("Rendering failed")
        return original(library, *args, **kwargs)

    monkeypatch.setattr(pl, "thread_pool_size", lambda: 4)
    monkeypatch.setattr(refkit, "Document", render)
    with pytest.raises(
        CatalogError, match="Could not render BibTeX reference"
    ) as error:
        catalog.cite(ids=["direct-labels"])
    assert error.value.details == {"reference_id": "smith020"}

    monkeypatch.setattr(refkit, "Document", original)
    assert len(catalog.cite(ids=["direct-labels"])[0]["sources"]) == len(sources)

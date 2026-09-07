from __future__ import annotations

import pytest
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


def test_parse_bibtex_reference_keeps_serialized_bibtex() -> None:
    bibtex = r"""@article{macro2024,
  title = {Readable\! charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""

    parsed = parse_bibtex_reference(bibtex)
    assert parsed.id == "macro2024"
    assert "Readable\\! charts" in parsed.bibtex

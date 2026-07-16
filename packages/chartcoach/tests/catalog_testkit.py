from __future__ import annotations

from collections.abc import Callable, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction


GUIDELINE_MD = """---
id: direct-labels
title: Use direct labels
description: Label marks directly when space permits.
bibliography: references.bib
labels:
  - chart:line
  - goal:comparison
---

## Advice <!-- role: advice -->

Place the label close to the mark it names [@smith2024].
"""

BIBTEX = """% generated note
@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""

MANIFEST_MD = """# Sample Catalog

## Section Roles

### advice

Actionable guidance for applying the guideline.

## Label Families

### chart

Chart-family labels such as `chart:line`.

### goal

Task-goal labels such as `goal:comparison`.
"""


def write_manifest(root: Path, manifest: str = MANIFEST_MD) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "MANIFEST.md").write_text(manifest)


def write_catalog_entry(root: Path, entry_id: str = "direct-labels") -> Path:
    entry_dir = root / "entries" / entry_id
    entry_dir.mkdir(parents=True)
    (entry_dir / "guideline.md").write_text(
        GUIDELINE_MD.replace("id: direct-labels", f"id: {entry_id}")
        .replace("title: Use direct labels", f"title: {entry_id}")
        .replace(
            "description: Label marks directly when space permits.",
            f"description: {entry_id} description.",
        )
    )
    (entry_dir / "references.bib").write_text(BIBTEX)
    return entry_dir


def deterministic_embedding(
    name: str,
    vector: Callable[[str, int], Sequence[float]] | None = None,
) -> "EmbeddingFunction":
    """Return a registered native LanceDB embedding for contract tests."""

    import numpy as np
    from lancedb.embeddings import TextEmbeddingFunction, get_registry

    make_vector = vector or (
        lambda text, index: (
            float(len(text)),
            float(sum(map(ord, text)) % 997),
            float(index + 1),
            1.0,
        )
    )
    registry = get_registry()
    try:
        embedding = registry.get(name)
    except KeyError:
        dimensions = len(make_vector("", 0))

        @registry.register(name)
        class TestEmbedding(TextEmbeddingFunction):
            def ndims(self) -> int:
                return dimensions

            def generate_embeddings(
                self,
                texts: list[str] | np.ndarray,
                *args: Any,
                **kwargs: Any,
            ) -> list[np.ndarray | None]:
                return [
                    np.asarray(make_vector(str(text), index), dtype=np.float32)
                    for index, text in enumerate(texts)
                ]

        embedding = TestEmbedding
    return cast("EmbeddingFunction", embedding.create())

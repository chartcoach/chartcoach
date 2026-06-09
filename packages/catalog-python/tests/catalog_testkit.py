from __future__ import annotations

import hashlib
from pathlib import Path


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


def sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

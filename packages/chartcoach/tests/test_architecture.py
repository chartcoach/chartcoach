from __future__ import annotations

import ast
from collections.abc import Callable, Iterator
from pathlib import Path

_CATALOG_ROOT = Path(__file__).parents[1] / "src" / "chartcoach" / "catalog"
_CATALOG_FACADES = frozenset({"chartcoach", "chartcoach.catalog"})
_RELATIVE_FACADES = frozenset({".", "..", "..."})


def test_catalog_read_path_does_not_import_curation() -> None:
    sources = [
        path
        for path in _CATALOG_ROOT.rglob("*.py")
        if "curation" not in path.relative_to(_CATALOG_ROOT).parts
    ]

    violations = _matching_imports(
        sources,
        lambda target: (
            _is_facade_import(target)
            or target.startswith(
                ("chartcoach.catalog.curation", ".curation", "..curation")
            )
        ),
    )

    assert violations == []


def test_curation_does_not_import_runtime_or_cache_owners() -> None:
    sources = sorted((_CATALOG_ROOT / "curation").rglob("*.py"))

    violations = _matching_imports(
        sources,
        lambda target: (
            _is_facade_import(target)
            or target.startswith(
                (
                    "chartcoach.open_catalog",
                    "chartcoach.catalog.open_catalog",
                    "chartcoach.catalog.runtime",
                    ".open_catalog",
                    ".runtime",
                    "..open_catalog",
                    "..runtime",
                )
            )
        ),
    )

    assert violations == []


def test_agent_interfaces_do_not_import_cli_adapters() -> None:
    package_root = _CATALOG_ROOT.parent
    sources = [package_root / "agent.py", package_root / "skills.py"]

    violations = _matching_imports(
        sources,
        lambda target: target.startswith(("chartcoach.cli", ".cli")),
    )

    assert violations == []


def test_import_targets_include_from_import_aliases() -> None:
    tree = ast.parse(
        """
from . import curation
from .. import runtime
from chartcoach.catalog import runtime as catalog_runtime
from chartcoach.catalog.runtime import open_catalog
from chartcoach import Catalog
from chartcoach.catalog import CatalogRelease
import chartcoach.catalog.curation
"""
    )

    assert [target for _, target in _import_targets(tree)] == [
        ".",
        ".curation",
        "..",
        "..runtime",
        "chartcoach.catalog",
        "chartcoach.catalog.runtime",
        "chartcoach.catalog.runtime",
        "chartcoach.catalog.runtime.open_catalog",
        "chartcoach",
        "chartcoach.Catalog",
        "chartcoach.catalog",
        "chartcoach.catalog.CatalogRelease",
        "chartcoach.catalog.curation",
    ]


def _matching_imports(
    sources: list[Path],
    matches: Callable[[str], bool],
) -> list[str]:
    violations: list[str] = []
    for path in sources:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for line, target in _import_targets(tree):
            if matches(target):
                relative = path.relative_to(_CATALOG_ROOT.parent)
                violations.append(f"{relative}:{line}: {target}")
    return violations


def _import_targets(tree: ast.AST) -> Iterator[tuple[int, str]]:
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                yield node.lineno, alias.name
            continue
        if not isinstance(node, ast.ImportFrom):
            continue
        base = f"{'.' * node.level}{node.module or ''}"
        yield node.lineno, base
        separator = "" if not base or base.endswith(".") else "."
        for alias in node.names:
            yield node.lineno, f"{base}{separator}{alias.name}"


def _is_facade_import(target: str) -> bool:
    return target in _CATALOG_FACADES or target in _RELATIVE_FACADES

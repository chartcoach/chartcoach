from __future__ import annotations

import dataclasses as dc
import re
from collections.abc import Iterable, Mapping
from hashlib import sha256
from os import PathLike
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING

from .errors import CatalogValidationError
from .guidelines import Section
from .labels import parse_label

if TYPE_CHECKING:
    from .model import Catalog


REQUIRED_MANIFEST_HEADINGS = ("Section Roles", "Label Families")

_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
_CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")


class CatalogManifestError(CatalogValidationError):
    """Raised when a catalog manifest is missing a required contract."""


@dc.dataclass(frozen=True, slots=True)
class ManifestDefinition:
    """One prose definition under a manifest heading."""

    name: str
    description: str
    examples: tuple[str, ...] = ()


@dc.dataclass(frozen=True, slots=True)
class CatalogManifest:
    """Manifest semantics for one catalog instance."""

    markdown: str
    section_roles: Mapping[str, ManifestDefinition]
    label_families: Mapping[str, ManifestDefinition]

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "section_roles",
            MappingProxyType(dict(self.section_roles)),
        )
        object.__setattr__(
            self,
            "label_families",
            MappingProxyType(dict(self.label_families)),
        )

    @classmethod
    def from_text(cls, markdown: str) -> CatalogManifest:
        """Parse a `MANIFEST.md` string."""

        return parse_catalog_manifest(markdown)

    @classmethod
    def from_path(cls, path: str | PathLike[str]) -> CatalogManifest:
        """Read and parse `MANIFEST.md`."""

        return parse_catalog_manifest(Path(path).read_text(encoding="utf-8"))

    def write(self, path: str | PathLike[str]) -> None:
        """Write the manifest markdown."""

        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.markdown, encoding="utf-8")


def parse_catalog_manifest(markdown: str) -> CatalogManifest:
    """Parse manifest headings and required subheadings."""

    required_seen: set[str] = set()
    definitions: dict[str, dict[str, ManifestDefinition]] = {
        "Section Roles": {},
        "Label Families": {},
    }
    current_heading: str | None = None
    current_name: str | None = None
    current_lines: list[str] = []

    def flush_definition() -> None:
        nonlocal current_name, current_lines
        if current_heading not in definitions or current_name is None:
            current_lines = []
            return
        description = "\n".join(current_lines).strip()
        if not description:
            raise CatalogManifestError(
                f"Manifest definition {current_heading}/{current_name} must include prose."
            )
        examples = tuple(_CODE_SPAN_RE.findall(description))
        definitions[current_heading][current_name] = ManifestDefinition(
            name=current_name,
            description=description,
            examples=examples,
        )
        current_name = None
        current_lines = []

    for line in markdown.splitlines():
        match = _HEADING_RE.match(line)
        if not match:
            if current_name is not None:
                current_lines.append(line)
            continue

        level = len(match.group(1))
        title = match.group(2).strip()

        if level == 2:
            flush_definition()
            current_heading = title
            current_name = None
            current_lines = []
            if title in definitions:
                required_seen.add(title)
            continue

        if level == 3 and current_heading in definitions:
            flush_definition()
            if not title:
                raise CatalogManifestError(
                    f"Manifest heading {current_heading} contains an empty subheading."
                )
            current_name = title
            current_lines = []
            continue

        if current_name is not None:
            current_lines.append(line)

    flush_definition()

    missing_headings = [
        heading
        for heading in REQUIRED_MANIFEST_HEADINGS
        if heading not in required_seen
    ]
    if missing_headings:
        raise CatalogManifestError(
            f"MANIFEST.md is missing required heading(s): {', '.join(missing_headings)}."
        )

    for heading in REQUIRED_MANIFEST_HEADINGS:
        if not definitions[heading]:
            raise CatalogManifestError(
                f"Manifest heading {heading} must contain definitions."
            )

    _validate_label_family_examples(definitions["Label Families"].values())

    normalized_markdown = markdown if markdown.endswith("\n") else f"{markdown}\n"
    return CatalogManifest(
        markdown=normalized_markdown,
        section_roles=definitions["Section Roles"],
        label_families=definitions["Label Families"],
    )


def validate_catalog_manifest(catalog: Catalog, manifest: CatalogManifest) -> None:
    """Validate catalog section roles and label families against a manifest."""

    errors: list[str] = []

    used_roles = set(_catalog_section_roles(catalog))
    missing_roles = sorted(used_roles - set(manifest.section_roles))
    if missing_roles:
        errors.append("undefined section role(s): " + ", ".join(missing_roles))

    used_families = set(_catalog_label_families(catalog))
    missing_families = sorted(used_families - set(manifest.label_families))
    if missing_families:
        errors.append("undefined label family/families: " + ", ".join(missing_families))

    if errors:
        raise CatalogManifestError(
            "Catalog manifest validation failed: " + "; ".join(errors) + "."
        )


def manifest_digest(markdown: str) -> str:
    """Return the SHA-256 digest of emitted UTF-8 manifest bytes."""

    return sha256(markdown.encode("utf-8")).hexdigest()


def _catalog_section_roles(catalog: Catalog) -> Iterable[str]:
    for role in catalog.table("sections").get_column("role").to_list():
        if not isinstance(role, str):
            raise CatalogManifestError("Section role values must be strings.")
        trimmed = role.strip()
        if not trimmed:
            raise CatalogManifestError("Section role values must not be empty.")
        if trimmed == Section.DANGLING_ROLE:
            continue
        yield trimmed


def _catalog_label_families(catalog: Catalog) -> Iterable[str]:
    for label in catalog.table("guideline_labels").get_column("label").to_list():
        yield parse_label(label, context=f"label {label!r}").family


def _validate_label_family_examples(definitions: Iterable[ManifestDefinition]) -> None:
    for definition in definitions:
        family_examples: list[str] = []
        invalid_examples: list[str] = []
        for example in definition.examples:
            try:
                parsed = parse_label(
                    example, context=f"manifest label example {example!r}"
                )
            except (TypeError, ValueError):
                continue
            if parsed.family == definition.name:
                family_examples.append(parsed.label)
            elif ":" in example:
                invalid_examples.append(example)

        if invalid_examples:
            raise CatalogManifestError(
                f"Label family {definition.name} has example(s) from another family: {', '.join(invalid_examples)}."
            )
        if not family_examples:
            raise CatalogManifestError(
                f"Label family {definition.name} must include at least one label example."
            )


__all__ = [
    "REQUIRED_MANIFEST_HEADINGS",
    "CatalogManifest",
    "CatalogManifestError",
    "ManifestDefinition",
    "manifest_digest",
    "parse_catalog_manifest",
    "validate_catalog_manifest",
]

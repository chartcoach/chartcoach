from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast


def entry_records_to_markdown(records: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for record in records:
        lines.append(f"## {record['id']}")
        lines.append("")
        lines.append(f"**{record['title']}**")
        lines.append("")
        lines.append(str(record["description"]))
        lines.append("")
        labels = cast(Sequence[str], record.get("labels") or ())
        if labels:
            lines.append("Labels: " + ", ".join(f"`{label}`" for label in labels))
            lines.append("")
        for section in cast(Sequence[Mapping[str, str]], record.get("sections") or ()):
            lines.append(f"### {section['role']}: {section['title']}")
            lines.append("")
            lines.append(section["content"].strip())
            lines.append("")
        sources = cast(Sequence[Mapping[str, object]], record.get("sources") or ())
        if sources:
            lines.append("### Sources")
            lines.append("")
            for source in sources:
                lines.append(f"- {source_label(source)}")
            lines.append("")
    return "\n".join(lines)


def citation_records_to_markdown(records: Sequence[Mapping[str, object]]) -> str:
    lines: list[str] = []
    for record in records:
        lines.append(f"## {record['id']}")
        lines.append("")
        lines.append(f"Guideline: {record['guideline_citation']}")
        lines.append("")
        lines.append("Sources:")
        sources = cast(Sequence[Mapping[str, object]], record.get("sources") or ())
        if sources:
            for source in sources:
                lines.append(f"- {source['citation']}")
        else:
            lines.append("- None.")
        lines.append("")
    return "\n".join(lines)


def source_label(source: Mapping[str, object]) -> str:
    authors = str(source.get("authors_text") or "").strip()
    year = str(source.get("year") or "").strip()
    title = str(source.get("source_title") or "").strip()
    doi = str(source.get("doi") or "").strip()
    url = str(source.get("url") or "").strip()
    parts = [part for part in (authors, year, title) if part]
    label = ", ".join(parts) if parts else str(source.get("reference_id") or "source")
    links = [value for value in (doi, url) if value]
    if links:
        return f"{label} ({', '.join(links)})"
    return label

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "duckdb==1.4.1",
#     "embedding-atlas==0.11.0",
#     "numpy==2.3.4",
#     "polars==1.34.0",
#     "pyarrow==21.0.0",
#     "pyyaml==6.0.3",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="columns")


@app.cell(column=0)
def _(guidelines):
    len(guidelines)
    return


@app.cell
def _(GUIDELINE_PATHS, parse_guideline):
    guidelines = []
    for path in GUIDELINE_PATHS:
        try:
            content = path.read_text(encoding="utf-8")
            guideline = parse_guideline(content)
            guidelines.append(guideline)
        except Exception as e:
            print(f"Error parsing {path}: {e}")
    return (guidelines,)


@app.cell
def _(List, Literal, Optional, dataclass, field, re, yaml):
    @dataclass
    class Evidence:
        strength: Literal["high", "medium", "low"]
        summary: str


    @dataclass
    class Source:
        type: Literal["research", "standard", "practitioner", "personal"]
        ref: str
        url: Optional[str] = None
        note: Optional[str] = None
        role: Optional[Literal["primary", "supporting", "related"]] = None


    @dataclass
    class Tool:
        type: Literal["implement", "validate", "learn"]
        name: str
        url: str
        description: str


    @dataclass
    class Example:
        type: Literal["good", "bad"]
        description: str
        url: Optional[str] = None
        caption: Optional[str] = None


    @dataclass
    class Guideline:
        id: str
        title: str
        tags: List[str]
        evidence: Evidence
        sources: List[Source] = field(default_factory=list)
        tools: List[Tool] = field(default_factory=list)
        examples: List[Example] = field(default_factory=list)

        guidance: str = ""
        why: str = ""
        core_principle: str = ""
        when_it_applies: List[str] = field(default_factory=list)
        exceptions: List[str] = field(default_factory=list)
        trade_offs: List[str] = field(default_factory=list)
        signs_of_trouble: List[str] = field(default_factory=list)
        how_to_improve: List[str] = field(default_factory=list)


    def parse_guideline(content: str) -> Guideline:
        # Split frontmatter and body
        parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].strip()

        # Parse evidence
        evidence = Evidence(**frontmatter["evidence"])

        # Parse sources
        sources = [Source(**s) for s in frontmatter.get("sources", [])]

        # Parse tools
        tools = [Tool(**t) for t in frontmatter.get("tools", [])]

        # Parse examples
        examples = [Example(**e) for e in frontmatter.get("examples", [])]

        # Extract sections from body
        sections = re.split(r"^## ", body, flags=re.MULTILINE)
        section_map = {
            s.split("\n")[0]: "\n".join(s.split("\n")[1:]).strip()
            for s in sections[1:]
        }

        # Extract core principle if present
        core_principle = ""
        if "Why" in section_map:
            why_parts = re.split(
                r"^### Core Principle", section_map["Why"], flags=re.MULTILINE
            )
            section_map["Why"] = why_parts[0].strip()
            if len(why_parts) > 1:
                core_principle = why_parts[1].strip()

        # Extract list items
        def extract_list(text: str) -> List[str]:
            return [
                re.sub(r"^\s*[-*]\s+", "", line).strip()
                for line in text.split("\n")
                if re.match(r"^\s*[-*]\s+", line)
            ]

        return Guideline(
            id=frontmatter["id"],
            title=frontmatter["title"],
            tags=frontmatter["tags"],
            evidence=evidence,
            sources=sources,
            tools=tools,
            examples=examples,
            guidance=section_map.get("Guidance", ""),
            why=section_map.get("Why", ""),
            core_principle=core_principle,
            when_it_applies=extract_list(section_map.get("When it applies", "")),
            exceptions=extract_list(section_map.get("Exceptions", "")),
            trade_offs=extract_list(section_map.get("Trade-offs", "")),
            signs_of_trouble=extract_list(section_map.get("Signs of Trouble", "")),
            how_to_improve=extract_list(section_map.get("How to Improve", "")),
        )
    return (parse_guideline,)


@app.cell
def _():
    import yaml
    import re
    from typing import List, Dict, Optional, Literal
    from dataclasses import dataclass, field
    return List, Literal, Optional, dataclass, field, re, yaml


@app.cell(column=1)
def _(
    GUIDELINES_CH_ROOT,
    GUIDELINES_DW_ROOT,
    GUIDELINES_PC_ROOT,
    GUIDELINES_TC_ROOT,
):
    GUIDELINE_PATHS = sorted(
        [
            *GUIDELINES_CH_ROOT.glob("*.md"),
            *GUIDELINES_DW_ROOT.glob("*.md"),
            *GUIDELINES_PC_ROOT.glob("*.md"),
            *GUIDELINES_TC_ROOT.glob("*.md"),
        ]
    )
    GUIDELINE_PATHS
    return (GUIDELINE_PATHS,)


@app.cell
def _(pathlib):
    INGEST_ROOT_PATH = pathlib.Path("workbench/ingest")
    GUIDELINES_CH_ROOT = INGEST_ROOT_PATH / "chartability" / "generated"
    GUIDELINES_DW_ROOT = INGEST_ROOT_PATH / "datawrapper" / "generated"
    GUIDELINES_PC_ROOT = INGEST_ROOT_PATH / "graphical-perception-knowledge" / "generated"
    GUIDELINES_TC_ROOT = INGEST_ROOT_PATH / "talking-charts" / "generated"
    return (
        GUIDELINES_CH_ROOT,
        GUIDELINES_DW_ROOT,
        GUIDELINES_PC_ROOT,
        GUIDELINES_TC_ROOT,
    )


@app.cell
def _():
    import marimo as mo
    import pathlib
    from typing import TypedDict
    return (pathlib,)


if __name__ == "__main__":
    app.run()

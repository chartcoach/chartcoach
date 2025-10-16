# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anywidget==0.9.18",
#     "duckdb==1.4.1",
#     "embedding-atlas==0.11.0",
#     "numpy==2.3.4",
#     "pandas==2.3.3",
#     "polars==1.34.0",
#     "pyarrow==21.0.0",
#     "pyyaml==6.0.3",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(make_section, mo, section_selector, section_title_map):
    mo.vstack([
        section_selector,
        make_section(section_title_map[section_selector.value]),
    ])
    return


@app.cell(hide_code=True)
def _(SPACE_FNS):
    section_title_map = {
        fn.__doc__.split("\n")[1].strip()[1:].strip(): fn for fn in SPACE_FNS
    }
    section_titles = list(section_title_map.keys())
    return section_title_map, section_titles


@app.cell(hide_code=True)
def _(mo, section_titles):
    section_selector = mo.ui.dropdown(
        section_titles,
        label="Select Embedding Space",
        value=section_titles[0],
    )
    return (section_selector,)


@app.cell(column=1, hide_code=True)
def _(guidelines, make_atlas_widget, make_df, mo):
    def make_section(space_fn: callable):
        df = make_df(
            guidelines,
            space_fn,
        )
        widget = make_atlas_widget(df)
        md = mo.md(space_fn.__doc__)
        return mo.vstack([md, widget])
    return (make_section,)


@app.cell(hide_code=True)
def _(
    EmbeddingAtlasWidget,
    Guideline,
    compute_text_projection,
    derive_guideline_categories,
    pl,
):
    def make_atlas_widget(df: pl.DataFrame) -> EmbeddingAtlasWidget:
        pdf = df.to_pandas()
        compute_text_projection(
            pdf,
            text="content",
            x="projection_x",
            y="projection_y",
            neighbors="neighbors",
        )

        return EmbeddingAtlasWidget(
            pdf,
            text="content",
            x="projection_x",
            y="projection_y",
            neighbors="neighbors",
            labels="automatic",
        )


    def make_df(
        guidelines: list[Guideline],
        space_fn: callable,
    ) -> pl.DataFrame:
        categories_col = [derive_guideline_categories(g) for g in guidelines]
        new_col = [space_fn(g) for g in guidelines]

        return pl.from_dict(
            {
                "content": new_col,
                "categories": categories_col,
            }
        ).unnest("categories")
    return make_atlas_widget, make_df


@app.cell(hide_code=True)
def _():
    from embedding_atlas.widget import EmbeddingAtlasWidget
    from embedding_atlas.projection import compute_text_projection
    import polars as pl
    import duckdb
    return EmbeddingAtlasWidget, compute_text_projection, pl


@app.cell(column=2, hide_code=True)
def _(
    build_author_intent_space,
    build_improvement_space,
    build_principle_space,
    build_scenario_space,
    build_trouble_space,
):
    SPACE_FNS = [
        build_author_intent_space,
        build_principle_space,
        build_scenario_space,
        build_trouble_space,
        build_improvement_space,
    ]
    return (SPACE_FNS,)


@app.cell(hide_code=True)
def _(Guideline, stringify_tag):
    def build_author_intent_space(guideline: Guideline) -> str:
        """
        # Author Intent Space

        Guideline items close to each other are highly similar in terms of what they cover and aim to address.

        Allows discovering items with “similar guidance” deduplicate near‑identical rules, grouping by conceptual intent.
        """
        title = guideline.title
        guidance = guideline.guidance
        why = guideline.why
        core_principle = guideline.core_principle

        return "\n".join(
            filter(
                bool,
                [
                    f"# {title}",
                    guidance,
                    why,
                    core_principle,
                ],
            )
        )


    def build_principle_space(guideline: Guideline) -> str:
        """
        # Core Principle Space

        Guidelines close together share similar core principles.
        """
        core_principle = guideline.core_principle
        return core_principle or "No core principle provided."


    def build_scenario_space(guideline: Guideline) -> str:
        """
        # Scenario Space

        Guideline items close together in this space are marked to have similar or identical applicability / trigger conditions.

        Shows how items are distributed based on their contextual similarity. Large, dense clusters mean that it will be difficult for us to identify the most relevant guidelines given contextual cues such as tags, "when it applies" section, etc.
        """
        title = guideline.title
        when_it_applies = "\n".join(guideline.when_it_applies)
        tags = ", ".join([stringify_tag(tag) for tag in sorted(guideline.tags)])

        return "\n".join(
            filter(
                bool,
                [
                    f"# {title}",
                    when_it_applies,
                    tags,
                ],
            )
        )


    def build_trouble_space(guideline: Guideline) -> str:
        """
        # Trouble Space

        Guideline items close together in this space are violated by similar or the same mistakes in visualization design.
        """
        title = guideline.title
        trouble = "\n".join(sorted(guideline.signs_of_trouble))
        return "\n".join(
            [
                f"Signs of '{title}' being violated:",
                trouble,
            ]
        )


    def build_improvement_space(guideline: Guideline) -> str:
        """
        # Improvement Space

        Guideline items close together in this space can be fixed by similar or the same design improvements.
        """
        title = guideline.title
        how_to_improve = "\n".join(sorted(guideline.how_to_improve))
        return "\n".join(
            [
                f"Ways to improve adherence to '{title}':",
                how_to_improve,
            ]
        )
    return (
        build_author_intent_space,
        build_improvement_space,
        build_principle_space,
        build_scenario_space,
        build_trouble_space,
    )


@app.cell(hide_code=True)
def _(GUIDELINE_PATHS, parse_guideline):
    guidelines = []
    for path in GUIDELINE_PATHS:
        try:
            guideline = parse_guideline(path)
            guidelines.append(guideline)
        except Exception as e:
            print(f"Error parsing {path}: {e}")
    return (guidelines,)


@app.cell(hide_code=True)
def _(Guideline, re):
    def stringify_tag(tag: str) -> str:
        """{family}:{value}.{specific-value} --> {family} is {specific-value} {value}"""
        family, value, specific_value = re.match(
            r"^([^:]+):([^\.]+)\.?(.*)$",
            tag,
        ).groups()

        if value == "*":
            return f"applies to all {family}"

        specific_value = specific_value or ""
        return f"{family} is {specific_value} {value}".strip().replace("  ", " ")


    def derive_guideline_categories(guideline: Guideline) -> dict:
        stem = guideline.file.split("/")[-1].split(".")[0]
        source_abbreviation = "PK" if "-" in stem else stem.split("_")[0]
        source_map = {
            "PK": "Perception Knowledge Papers",
            "CH": "Chartability",
            "DW": "Datawrapper",
            "TC": "Talking Charts",
        }
        is_universal = any(":*" in tag for tag in guideline.tags)
        impacts_perceptual = any(
            tag == "impact:perceptual" for tag in guideline.tags
        )
        impacts_rhetorical = any(
            tag in ["impact:ethos", "impact:logos", "impact:pathos"]
            for tag in guideline.tags
        )
        impacts_accessibility = any(
            tag == "impact:accessibility" for tag in guideline.tags
        )
        evidence_strength = guideline.evidence.strength

        return {
            "source": source_map[source_abbreviation],
            "is_universal": is_universal,
            "impacts_perceptual": impacts_perceptual,
            "impacts_accessibility": impacts_accessibility,
            "impacts_rhetorical": impacts_rhetorical,
            "evidence_strength": evidence_strength,
        }
    return derive_guideline_categories, stringify_tag


@app.cell(hide_code=True)
def _(List, Literal, Optional, dataclass, field, pathlib, re, yaml):
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
        file: str
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


    def parse_guideline(path: pathlib.Path) -> Guideline:
        file = str(path)
        content = path.read_text()

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
            file=file,
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
    return Guideline, parse_guideline


@app.cell(hide_code=True)
def _():
    import yaml
    import re
    from typing import List, Dict, Optional, Literal
    from dataclasses import dataclass, field, asdict
    return List, Literal, Optional, dataclass, field, re, yaml


@app.cell(column=3)
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
    return mo, pathlib


if __name__ == "__main__":
    app.run()

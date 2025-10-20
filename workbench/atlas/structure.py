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
app = marimo.App(width="columns", layout_file="layouts/structure.grid.json")


@app.cell(column=0, hide_code=True)
def _(make_section, mo, section_selector, section_title_map):
    mo.vstack(
        [
            section_selector,
            make_section(section_title_map[section_selector.value]),
        ]
    )
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
            model="ibm-granite/granite-embedding-125m-english",
        )

        return EmbeddingAtlasWidget(
            pdf,
            text="content",
            x="projection_x",
            y="projection_y",
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
def _(build_author_intent_space):
    build_author_intent_space
    SPACE_FNS = [
        fn
        for fn_name, fn in sorted(globals().items(), key=lambda x: x[0])
        if fn_name.startswith("build_") and fn_name.endswith("_space")
    ]
    return (SPACE_FNS,)


@app.cell(hide_code=True)
def _(Guideline, stringify_tag):
    def build_categorical_tag_space(guideline: Guideline) -> str:
        """
        # Categorical Tag Space

        Guidelines close together share the same high-level **categorical tags**.

        This provides a purely structural, taxonomic view of the guideline corpus, divorced
        from free-text descriptions. Useful for identifying broad thematic clusters (e.g., all
        "color" guidelines, all "interaction" guidelines) and understanding the high-level
        organization and balance of topics in the guideline set.

        *Uses:*
        - `tags`
        """
        return ", ".join(sorted(guideline.tags))


    def build_negative_example_space(guideline: Guideline) -> str:
        """
        # Negative Example (Anti-Pattern) Space

        Guidelines close together are violated in ways that produce similar **concrete bad examples**.

        This space moves from abstract "signs of trouble" to tangible, described anti-patterns.
        It's invaluable for training visual recognition models or for designers learning to spot
        specific flaws. Clusters reveal groups of guidelines whose violations manifest in
        visually or functionally similar ways.

        *Uses:*
        - `examples[].description` (where type is 'bad')
        """
        bad_examples = [
            ex.description for ex in guideline.examples if ex.type == "bad"
        ]
        return (
            "\n".join(sorted(bad_examples))
            if bad_examples
            else "No bad examples provided."
        )


    def build_title_space(guideline: Guideline) -> str:
        """
        # Title Space

        Guidelines close together have similar **titles**, indicating surface-level naming conventions.

        This is the most basic similarity measure - useful for finding guidelines that might
        have been named inconsistently or finding natural language patterns in how rules are
        expressed. Dense clusters suggest redundant naming or thematic groupings.

        *Uses:*
        - `title`
        """
        return guideline.title


    def build_author_intent_space(guideline: Guideline) -> str:
        """
        # Author Intent Space

        Guidelines close together share similar **underlying intent, purpose, and conceptual coverage**.

        Combines title, guidance text, rationale, and core principles to capture what the
        author *meant* to communicate. Useful for discovering conceptually similar guidelines,
        deduplicating near-identical rules, and understanding the semantic organization of
        the guideline corpus. **Dense clusters indicate overlapping or redundant guidance.**

        *Uses:*
        - `title`
        - `guidance`
        - `why`
        - `core_principle`
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

        Guidelines close together are grounded in similar **fundamental design principles**.

        Reveals the *philosophical underpinnings* and theoretical foundations that guidelines
        share. Useful for organizing guidelines by their theoretical basis (e.g., perceptual
        principles, cognitive load theory, accessibility standards). Helps identify gaps in
        principle coverage and understand the theoretical diversity of the corpus.

        *Uses:*
        - `core_principle`
        """
        core_principle = guideline.core_principle
        return core_principle or "No core principle provided."


    def build_scenario_space(guideline: Guideline) -> str:
        """
        # Scenario Space

        Guidelines close together apply to similar **contexts, situations, and use cases**.

        Combines applicability conditions and categorical tags to map *when* guidelines should
        be triggered. Critical for **context-aware guideline retrieval** - helps answer "which
        guidelines apply to my current design situation?" Dense clusters indicate overlapping
        applicability, making it harder to select relevant guidelines without additional context.

        *Uses:*
        - `when_it_applies`
        - `tags`
        """
        when_it_applies = "\n".join(guideline.when_it_applies)
        tags = ", ".join([stringify_tag(tag) for tag in sorted(guideline.tags)])

        return "\n".join(
            filter(
                bool,
                [
                    when_it_applies,
                    tags,
                ],
            )
        )


    def build_trouble_space(guideline: Guideline) -> str:
        """
        # Trouble Space

        Guidelines close together are violated by similar **symptoms, mistakes, or warning signs**.

        Maps the *diagnostic space* - what problems look like when guidelines are broken. Essential
        for **automated violation detection** and design critique tools. Dense clusters suggest that
        multiple guidelines share violation symptoms, which could complicate root cause analysis
        but also enables more robust pattern detection.

        *Uses:*
        - `signs_of_trouble`
        """
        trouble = "\n".join(sorted(guideline.signs_of_trouble))
        return trouble


    def build_improvement_space(guideline: Guideline) -> str:
        """
        # Improvement Space

        Guidelines close together can be addressed through similar **actionable fixes or improvements**.

        Maps the *solution space* - what to do when guidelines are violated. Essential for generating
        practical recommendations and building **refactoring tools**. Reveals which improvements are
        broadly applicable across multiple guidelines versus those that are highly specific.

        *Uses:*
        - `how_to_improve`
        """
        how_to_improve = "\n".join(sorted(guideline.how_to_improve))
        return how_to_improve


    def build_evidence_space(guideline: Guideline) -> str:
        """
        # Evidence Space

        Guidelines close together have similar **evidentiary support** in terms of strength and nature.

        Reveals the *empirical grounding* of guidelines - which are strongly backed by research
        versus based on heuristics or conventions. Useful for **prioritizing guidelines when
        conflicts arise**, understanding confidence levels, and identifying areas needing more
        research. Helps distinguish evidence-based from opinion-based recommendations.

        *Uses:*
        - `evidence.strength`
        - `evidence.summary`
        """
        strength = guideline.evidence.strength
        summary = guideline.evidence.summary
        return f"{strength}: {summary}"


    def build_source_type_space(guideline: Guideline) -> str:
        """
        # Source Type Space

        Guidelines close together draw from similar **types of knowledge sources**.

        Reveals whether guidelines come from *academic research*, *industry standards*, *practitioner
        experience*, or *personal expertise*. Useful for understanding the epistemological diversity
        of the corpus and identifying potential biases toward certain types of knowledge. Helps
        balance theoretical rigor with practical applicability.

        *Uses:*
        - `sources[].type`
        """
        source_types = sorted(set(source.type for source in guideline.sources))
        return ", ".join(source_types) if source_types else "No sources"


    def build_tool_ecosystem_space(guideline: Guideline) -> str:
        """
        # Tool Ecosystem Space

        Guidelines close together are supported by similar **implementation, validation, or learning tools**.

        Maps the *practical tooling landscape* around guidelines. Reveals which guidelines have
        strong tool support versus those requiring manual effort. Useful for understanding
        **automation potential**, identifying tool gaps, and guiding tool development priorities.
        Distinguishes easily-automated guidelines from those requiring human judgment.

        *Uses:*
        - `tools[].type`
        - `tools[].name`
        """
        tools = "\n".join(
            [f"{tool.type}: {tool.name}" for tool in guideline.tools]
        )
        return tools if tools else "No tools specified"


    def build_exception_space(guideline: Guideline) -> str:
        """
        # Exception Space

        Guidelines close together have similar **edge cases, exemptions, or boundary conditions**.

        Maps *when guidelines should NOT be applied* despite seeming relevant. Critical for
        avoiding **false positives in automated systems** and understanding guideline scope limits.
        Similar exception patterns suggest related boundary conditions or shared conceptual
        limitations across guidelines.

        *Uses:*
        - `exceptions`
        """
        exceptions = "\n".join(sorted(guideline.exceptions))
        return exceptions if exceptions else "No exceptions"


    def build_tradeoff_space(guideline: Guideline) -> str:
        """
        # Trade-off Space

        Guidelines close together involve similar **competing concerns or design compromises**.

        Reveals the *tension landscape* - where following one guideline may conflict with another
        or involve costs. Essential for understanding when guidelines compete and how to make
        informed decisions when perfect compliance is impossible. Helps identify **fundamental
        dilemmas in visualization design** that require contextual judgment.

        *Uses:*
        - `trade_offs`
        """
        trade_offs = "\n".join(sorted(guideline.trade_offs))
        return trade_offs if trade_offs else "No trade-offs"


    def build_comprehensive_space(guideline: Guideline) -> str:
        """
        # Comprehensive Space

        Guidelines close together are **holistically similar across all dimensions** of content.

        Combines intent, applicability, problems, solutions, and evidence into a *single
        unified similarity measure*. Represents overall guideline similarity regardless of
        which specific aspects align. Most useful for **general-purpose retrieval**, finding
        truly related guidelines, and understanding the overall structure of the guideline
        space. The richest but also most computationally expensive embedding space.

        *Uses:*
        - `title`
        - `guidance`
        - `why`
        - `when_it_applies`
        - `signs_of_trouble`
        - `how_to_improve`
        - `evidence.summary`
        """
        title = guideline.title
        guidance = guideline.guidance
        why = guideline.why
        when_it_applies = "\n".join(guideline.when_it_applies)
        trouble = "\n".join(guideline.signs_of_trouble)
        how_to_improve = "\n".join(guideline.how_to_improve)
        evidence = guideline.evidence.summary

        return "\n".join(
            filter(
                bool,
                [
                    f"# {title}",
                    guidance,
                    why,
                    when_it_applies,
                    trouble,
                    how_to_improve,
                    evidence,
                ],
            )
        )
    return (build_author_intent_space,)


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
            "title": guideline.title,
            "url": f"https://github.com/peter-gy/chartcoach/tree/main/{guideline.file}",
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


@app.cell(column=3, hide_code=True)
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


@app.cell(hide_code=True)
def _(pathlib):
    INGEST_ROOT_PATH = pathlib.Path("workbench/ingest")
    GUIDELINES_CH_ROOT = INGEST_ROOT_PATH / "chartability" / "generated"
    GUIDELINES_DW_ROOT = INGEST_ROOT_PATH / "datawrapper" / "generated"
    GUIDELINES_PC_ROOT = (
        INGEST_ROOT_PATH / "graphical-perception-knowledge" / "generated"
    )
    GUIDELINES_TC_ROOT = INGEST_ROOT_PATH / "talking-charts" / "generated"
    return (
        GUIDELINES_CH_ROOT,
        GUIDELINES_DW_ROOT,
        GUIDELINES_PC_ROOT,
        GUIDELINES_TC_ROOT,
    )


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pathlib
    from typing import TypedDict
    return mo, pathlib


if __name__ == "__main__":
    app.run()

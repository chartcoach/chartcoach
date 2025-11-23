import marimo

__generated_with = "0.18.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cross-Domain Isomorphisms (Analogical Transfer)

    **Objective:**
    To uncover "wormholes" in the design space—instances where the same design principle applies to two completely unrelated domains.

    **The Logic:**
    We search for guideline pairs that exhibit **Low Context Similarity** (different domains/tasks) but **High Advice Similarity** (conceptually similar solutions).

    $$ S_{transfer} = \text{Sim}(\vec{v}_{advice}^A, \vec{v}_{advice}^B) - \text{Sim}(\vec{v}_{context}^A, \vec{v}_{context}^B) $$

    **Interpretation:**
    A high score identifies "Structural Isomorphisms"—abstract problems that look different on the surface but share the same underlying mathematical or perceptual structure. This allows us to "transfer" a solution from a well-studied domain (like map design) to a less-studied one (like risk communication).

    **Output Metrics:**
    *   `advice_similarity`: Indicates the solutions are effectively the same.
    *   `context_similarity`: Indicates the domains are different.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    advice_sim_threshold = 0.6
    context_diff_threshold = 0.4

    conn.query(f"""
    WITH 
    advice AS (
        SELECT id, embedding FROM embeddings WHERE role = 'advice'
    ),
    contexts AS (
        SELECT id, embedding FROM embeddings WHERE role = 'context'
    )
    SELECT 
        a1.id AS domain_A, 
        a2.id AS domain_B,
        list_cosine_similarity(a1.embedding, a2.embedding) AS advice_similarity,
        list_cosine_similarity(c1.embedding, c2.embedding) AS context_similarity
    FROM advice a1
    JOIN advice a2 ON a1.id < a2.id
    JOIN contexts c1 ON a1.id = c1.id
    JOIN contexts c2 ON a2.id = c2.id
    WHERE 
        advice_similarity > {advice_sim_threshold}      -- The solution is the same
        AND context_similarity < {context_diff_threshold} -- The domain is different
    ORDER BY advice_similarity DESC
    LIMIT 100;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Case Study: The "Discretization" Isomorphism**

    In the results below, the system finds a structural link between:

    - **Domain A (Risk Comm):** `separate-severity-from-probability` (Context: High-stakes health decisions).
    - **Domain B (Survey Vis):** `use-classed-scales-for-ordinal-data` (Context: Likert scales & rankings).

    **The Isomorphism:** Despite the contexts being unrelated, the system detects that both advise against mixing "Severity" or "Rank" with continuous visual scales.

    **The Transfer:** The principle from `Domain B` ("Continuous gradients imply non-existent intermediate values") effectively explains *why* the bad practice in `Domain A` fails ("Severity gradients distract from discrete probability statistics").

    This suggests a universal rule: *Categorical concepts must have categorical visual boundaries.*
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "separate-severity-from-probability",
                "use-classed-scales-for-ordinal-data",
            ]
        )
    )
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exploring Universal Solutions

    **Objective:**
    To explore distinct design problems that appear to share similar solutions.

    **The Logic:**
    We search for pairs of guidelines where the **Mistakes** are semantically distinct (low similarity), but the **Fixes** are highly similar.

    $$ S_{convergence} = \text{Sim}(\vec{v}_{fix}^A, \vec{v}_{fix}^B) - \text{Sim}(\vec{v}_{mistake}^A, \vec{v}_{mistake}^B) $$

    **Interpretation:**
    High convergence scores may point to fundamental design heuristics—such as "Simplification" or "Direct Labeling"—that serve as common correctives for a variety of visual issues. Identifying these clusters could help prioritize which core design concepts are most broadly applicable.

    **Output Metrics:**
    *   `fix_similarity`: Cosine similarity (0-1) between the solutions. Higher values indicate the fixes are semantically close.
    *   `mistake_similarity`: Cosine similarity (0-1) between the problems. Lower values indicate the problems are distinct.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    fix_sim_threshold = 0.75
    mistake_diff_threshold = 0.45

    conn.query(f"""
    WITH 
    fixes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'fix'
    ),
    mistakes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'mistakes'
    )
    SELECT 
        f1.id AS problem_A, 
        f2.id AS problem_B,
        list_cosine_similarity(f1.embedding, f2.embedding) AS fix_similarity,
        list_cosine_similarity(m1.embedding, m2.embedding) AS mistake_similarity
    FROM fixes f1
    JOIN fixes f2 ON f1.id < f2.id
    JOIN mistakes m1 ON f1.id = m1.id
    JOIN mistakes m2 ON f2.id = m2.id
    WHERE 
        fix_similarity > {fix_sim_threshold}     -- The solutions are the same
        AND mistake_similarity < {mistake_diff_threshold} -- The problems are different
    ORDER BY fix_similarity DESC;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Case Study: The "Faceting" Attractor**

    In the results above, the system identifies a solution convergence between:

    - **Problem A:** `avoid-redundant-retinal-encodings` (Issue: **Perceptual Interference** caused by mapping too many variables to shape/color).

    - **Problem B:** `szafir-2018-avoid-3d` (Issue: **Geometric Distortion** and occlusion caused by 3D projections).

    **The Convergence:** Despite the problems being distinct (2D Clutter vs. 3D Distortion), both guidelines prescribe **Small Multiples (Faceting)** as the optimal fix.

    **The Insight:** This suggests that *Spatial Separation* (Faceting) acts as a universal strategy for managing high-dimensional data, consistently outperforming both "Over-encoding" and "3D Projection" strategies.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "avoid-redundant-retinal-encodings",
                "szafir-2018-avoid-3d",
            ]
        )
    )
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Linking Guidelines via Context and Exceptions

    **Objective:**
    To propose potential logical links between guidelines by analyzing where the scope of one guideline ends and another begins.

    **The Logic:**
    We measure the similarity between the **Context** of `Guideline A` (when it applies) and the **Exceptions** of `Guideline B` (when it should be ignored).

    $$ S_{link}(A, B) = \text{Sim}(\vec{v}_{context}^A, \vec{v}_{exception}^B) $$

    **Interpretation:**
    This operation attempts to approximate the implicit "decision logic" of the design space. If the conditions triggering `Guideline A` align with the exception cases of `Guideline B`, it suggests a potential hand-off point. This relationship could be useful for automated systems to dynamically adjust recommendations based on changing context.

    **Output Metrics:**
    *   `match_score`: The cosine similarity between the context vector and the exception vector. A higher score suggests a stronger semantic link between the rule's trigger and the other rule's exclusion criteria.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    boundary_match_threshold = 0.7

    conn.sql(f"""
    WITH 
    situations AS (
        SELECT id, embedding FROM embeddings WHERE role = 'context'
    ),
    exceptions AS (
        SELECT id, embedding FROM embeddings WHERE role = 'exceptions'
    )
    SELECT 
        s.id AS standard_rule_id,
        e.id AS exception_case_id,
        list_cosine_similarity(s.embedding, e.embedding) AS match_score
    FROM situations s
    CROSS JOIN exceptions e
    WHERE 
        s.id != e.id
        AND match_score > {boundary_match_threshold}
    ORDER BY match_score DESC;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    **Case Study: The Density Threshold**

    In the results above, the system detects a link (Score: $0.744$) between:

    **The Trigger:** `group-bars-adjacently` (Context: Pairwise comparisons).

    **The Handoff:** `use-dot-plots-for-aggregation` (Exception: "The user needs to compare the exact difference between two specific items").

    **The Insight:** The system effectively "learns" that while Dot Plots are superior for high-volume aggregation, there is a specific boundary condition (pairwise precision) where control should be handed back to Bar Charts.

    This creates a dynamic graph: *Start with Dot Plot $\to$ If User needs Precision $\to$ Switch to Grouped Bar.*
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "group-bars-adjacently",
                "use-dot-plots-for-aggregation",
            ]
        )
    )
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Screening for Conflicting Advice

    **Objective:**
    To highlight instances where guidelines appear to agree on the context but differ in their recommendations.

    **The Logic:**
    We look for pairs of guidelines that have very similar **Contexts** (high similarity) but divergent **Advice** (low similarity).

    $$ S_{friction} = \text{Sim}(\vec{v}_{context}^A, \vec{v}_{context}^B) - \text{Sim}(\vec{v}_{advice}^A, \vec{v}_{advice}^B) $$

    **Interpretation:**
    This metric aims to surface potential trade-offs or debates within the catalog. If two sources address the same scenario but offer different instructions, it suggests a nuance that might require human judgment or further investigation, rather than automatic application.

    **Output Metrics:**
    *   `situation_sim`: Measures overlap in the problem context.
    *   `advice_sim`: Measures overlap in the recommended solution.
    *   `friction_score`: The difference between context similarity and advice similarity. High positive values indicate guidelines that effectively describe the same problem but offer significantly different solutions.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    situation_sim_threshold = 0.8

    conn.query(f"""
    WITH 
    situations AS (
        SELECT id, embedding FROM embeddings WHERE role = 'context'
    ),
    advice AS (
        SELECT id, embedding FROM embeddings WHERE role = 'advice'
    )
    SELECT 
        s1.id AS id_A, 
        s2.id AS id_B,
        list_cosine_similarity(s1.embedding, s2.embedding) AS situation_sim,
        list_cosine_similarity(a1.embedding, a2.embedding) AS advice_sim,

        -- Friction = High Context Overlap - Low Advice Overlap
        (situation_sim - advice_sim) AS friction_score
    FROM situations s1
    JOIN situations s2 ON s1.id < s2.id 
    JOIN advice a1 ON s1.id = a1.id
    JOIN advice a2 ON s2.id = a2.id
    -- Add a filter to make the results meaningful (otherwise you get 500k rows)
    WHERE situation_sim > {situation_sim_threshold}
    ORDER BY friction_score DESC
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Case Study: Precision vs. Aesthetics**

    In the results above, the system flags a friction between:
    *   `prioritize-position-encodings` (Advice: Use Bar Charts for precision).
    *   `avoid-extreme-donut-thinness` (Advice: Use Donut Charts, just make them thick).

    **The Context:** Both apply to "Quantitative data" where "Precise reading of values" is a goal.

    **The Insight:** The high friction score correctly identifies the tension between the *optimal* choice for precision (Bar) and the *acceptable* choice for aesthetics (Thick Donut). This tells a designer: "You can use a donut, but you are trading optimal precision for shape".
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "avoid-extreme-donut-thinness",
                "prioritize-position-encodings",
            ]
        )
    )
    return


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Estimating Remediation Effort

    **Objective:**
    To define a proxy metric for the difficulty of applying a specific guideline.

    **The Logic:**
    We calculate the semantic distance (difference) between the description of the **Mistake** and the description of the **Fix** within a single guideline.

    $$ \text{Effort} = 1 - \text{Sim}(\vec{v}_{fix}, \vec{v}_{mistake}) $$

    **Interpretation:**
    *   **Low Distance:** Suggests the mistake and fix are semantically adjacent (e.g., "Small Label" vs "Large Label"), which may correlate with a simple parameter adjustment.
    *   **High Distance:** Suggests the solution uses a distinct vocabulary from the problem (e.g., "Distorted Pie Chart" vs "Bar Chart"). This semantic gap might indicate a need for more significant changes to the visualization structure.

    **Output Metrics:**
    *   `effort_score`: Represents the cosine distance (1 minus similarity). Higher values indicate a larger semantic gap between the problem state and the solution state, serving as a proxy for implementation difficulty.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    conn.query("""
    WITH 
    fixes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'fix'
    ),
    mistakes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'mistakes'
    )
    SELECT 
        f.id,
        -- Cosine distance = 1 - Cosine Similarity
        (1 - list_cosine_similarity(f.embedding, m.embedding)) AS effort_score
    FROM fixes f
    JOIN mistakes m ON f.id = m.id
    ORDER BY effort_score DESC;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Case Study: Pie Chart Labeling**

    In the results above, `group-small-pie-slices` receives a high effort score ($0.647$):

    **The Mistake:** "Using a pointer line for every single tiny slice" (A layout/annotation attempt).

    **The Fix:** "Aggregate the smallest 3-4 values into one category" (A data aggregation).

    **The Insight:** The system flags this as "High Effort" because the vocabulary shifts from *drawing lines* to *modifying data*.

    This correctly identifies that the solution isn't just a better pointer line—it requires a fundamental change to the underlying data structure.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "group-small-pie-slices",
            ]
        )
    )
    return


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Analyzing Divergent Viewpoints

    **Objective:**
    To explore how different guidelines might interpret similar design choices from opposing perspectives.

    **The Logic:**
    We cross-reference guidelines to find cases where the **Advice** of one guideline is semantically equivalent to the **Mistake** (anti-pattern) of another.

    $$ S_{contrast}(A, B) = \text{Sim}(\vec{v}_{advice}^A, \vec{v}_{mistake}^B) $$

    **Interpretation:**
    A high similarity score here highlights areas of potential debate. By identifying instances where one recommendation aligns with another's anti-pattern, we can better understand the diverse schools of thought in the field. This view encourages users to consider context rather than treating guidelines as universal truths.

    **Output Metrics:**
    *   `collision_score`: The cosine similarity between the recommender's advice and the critic's mistake description. Higher values indicate a stronger semantic match, suggesting a direct contradiction between the two guidelines.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    collision_threshold = 0.675

    conn.query(f"""
    WITH 
    advice_vectors AS (
        SELECT id, embedding FROM embeddings WHERE role = 'advice'
    ),
    mistake_vectors AS (
        SELECT id, embedding FROM embeddings WHERE role = 'mistakes'
    )
    SELECT 
        a.id AS recommender_id,
        m.id AS critic_id,
        list_cosine_similarity(a.embedding, m.embedding) AS collision_score
    FROM advice_vectors a
    CROSS JOIN mistake_vectors m
    WHERE 
        a.id != m.id -- Don't compare a guideline to itself
        AND collision_score > {collision_threshold} -- Threshold for contradiction
    ORDER BY collision_score DESC;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Case Study: The Rainbow Colormap Debate**

    In the results above, the system detects a collision ($0.682$) between two guidelines regarding **Rainbow Colormaps**:

    **The Recommender:** `consider-rainbow-for-lookup-tasks` advises using rainbow scales specifically for "rapid location" tasks (Advice).

    **The Critic:** `replace-rainbow-with-uniform-multi-hue` explicitly lists "Using a rainbow scale" as a "Common Mistake" due to perceptual banding.

    **The Insight:** The high score confirms that this is not a universal truth but a trade-off: the *Advice* of one (optimized for lookup speed) is the *Mistake* of the other (optimized for value estimation accuracy).
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df().filter(
        pl.col("id").is_in(
            [
                "replace-rainbow-with-uniform-multi-hue",
                "consider-rainbow-for-lookup-tasks",
            ]
        )
    )
    return


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Semantic Atlas of Design Knowledge

    **Objective:**
    To visualize the global topology of the knowledge catalog. By projecting the high-dimensional vector space into two dimensions, we can inspect the structural relationships between different types of design knowledge.

    **The Method: Dimensionality Reduction (UMAP)**
    To render the 1536-dimensional embeddings on a 2D screen, we employ **UMAP (Uniform Manifold Approximation and Projection)**. Unlike linear projections (like PCA), UMAP is a manifold learning technique designed to preserve the **local neighborhood structure** of the data.

    This ensures that guidelines that are semantically close in the high-dimensional space remain close in the 2D visualization, identifying natural clusters of knowledge.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid(r"""
    graph LR
        subgraph "High-Dimensional Space"
            V[Vector Embeddings]
            N[Dimensions: 1536]
        end

        subgraph "Manifold Learning"
            U[UMAP Algorithm]
            T[Topology Preservation]
        end

        subgraph "Projected Space"
            P[2D Coordinates]
            C[Clusters]
        end

        V --> U
        N -.-> V
        U --> |Minimize Cross-Entropy| P
        U -.-> T
        T -.-> P
        P --> |Visualized As| C

        style V fill:#e1f5fe,stroke:#01579b
        style P fill:#e8f5e9,stroke:#1b5e20
        style U fill:#fff3e0,stroke:#e65100
    """)
    return


@app.cell
def _(projected_sections_df):
    projected_sections_df.select("role").unique("role")
    return


@app.cell(hide_code=True)
def _(EmbeddingAtlasWidget, catalog, os, pl):
    projected_sections_df = catalog.projected_sections_df(
        select=[
            pl.col("guideline").struct.field("title"),
            pl.col("guideline").struct.field("description"),
            pl.col("guideline").struct.field("labels"),
            pl.col("references"),
        ],
        model="openai/openai/text-embedding-3-small",
        batch_size=1024,
        text_projector_type="litellm",
        api_base="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )
    EmbeddingAtlasWidget(
        projected_sections_df.drop("embedding").to_pandas(),
        x="projection_x",
        y="projection_y",
        neighbors="neighbors",
    )
    return (projected_sections_df,)


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Formalization and Implementation

    This section details the transformation pipeline that converts the human-readable Markdown catalog into the mathematical structure utilized in the analyses presented in this notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    graph LR
            subgraph "Curated Guidelines"
                MD[Markdown Files]
            end

            subgraph "Parsing & Structure (Catalog)"
                MD --> |Parse| G[Guideline Object]
                G --> C_Txt[Context Text]
                G --> A_Txt[Advice Text]
                G --> M_Txt[Mistake Text]
            end

            subgraph "Vector Space (R^d)"
                C_Txt --> |Phi| V_Ctx[Vector: Context]
                A_Txt --> |Phi| V_Adv[Vector: Advice]
                M_Txt --> |Phi| V_Mis[Vector: Mistake]
            end

            subgraph "Storage & Index"
                V_Ctx --> DB[(DuckDB)]
                V_Adv --> DB
                V_Mis --> DB
                DB --> Index[HNSW Index]
            end

            style MD fill:#f9f,stroke:#333,stroke-width:2px
            style DB fill:#ff9,stroke:#333,stroke-width:2px
            style Index fill:#9f9,stroke:#333,stroke-width:2px
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The Pipeline Workflow

    The ingestion process moves from raw text to a queryable vector space through three distinct stages:

    1.  **Parsing:** The `Catalog` extracts semantic sections (`context`, `advice`, `mistake`, etc.) from the raw Markdown files.
    2.  **Embedding:** Each section is embedded independently via a Transformer model ($\Phi$). This ensures that the vector representation of an "Advice" section contains only the semantics of the solution, unpolluted by the context or rationale.
    3.  **Indexing:** The resulting vectors are stored in DuckDB and indexed using HNSW (Hierarchical Navigable Small World graphs) to enable real-time similarity operations.

    ### Formal Notation

    To ground the arithmetic operations used in this notebook, we define the following notation:

    Let $\mathcal{C}$ be the **Catalog**, a set of unique guidelines $\{ g_1, \dots, g_N \}$.
    Each guideline $g_i$ is a tuple of role-specific text sections:

    $$ g_i = \{ (r, t_{i,r}) \mid r \in \{\text{context}, \text{advice}, \text{mistake}, \dots\} \} $$

    We define an embedding function $\Phi: \mathcal{T} \rightarrow \mathbb{R}^d$ that maps text to a high-dimensional vector space. The computable representation of a section is:

    $$ \vec{v}_{i,r} = \Phi(t_{i,r}) $$

    All similarity metrics reported above are derived from the cosine similarity between these specific section vectors:

    $$ \text{Sim}(\vec{v}_{A, r1}, \vec{v}_{B, r2}) = \frac{\vec{v}_{A, r1} \cdot \vec{v}_{B, r2}}{\|\vec{v}_{A, r1}\| \|\vec{v}_{B, r2}\|} $$
    """)
    return


@app.cell(hide_code=True)
def _(index_sections, projected_sections_df):
    embedded_sections_df = projected_sections_df.drop(
        "projection_x",
        "projection_y",
        "neighbors",
    )
    conn = index_sections(embedded_sections_df)
    return (conn,)


@app.cell(column=8, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _(Catalog, catalog_parquet, pl):
    catalog = Catalog.from_df(pl.read_parquet(catalog_parquet.absolute()))
    catalog.df()
    return (catalog,)


@app.cell(hide_code=True)
def _(mo, pathlib):
    NB_ROOT = pathlib.Path(__file__).parent
    CATALOG_PARQUET_PATH = NB_ROOT.parent / "curation" / "catalog.parquet"
    catalog_parquet = mo.watch.file(CATALOG_PARQUET_PATH)
    return (catalog_parquet,)


@app.cell(hide_code=True)
def _():
    import nest_asyncio

    nest_asyncio.apply()
    return


@app.cell(hide_code=True)
def _():
    import os
    import pathlib

    import duckdb
    import marimo as mo
    import polars as pl

    from chartcoach_catalog.catalog import Catalog
    from chartcoach_catalog.embeddings import index_sections
    from embedding_atlas.widget import EmbeddingAtlasWidget

    return Catalog, EmbeddingAtlasWidget, index_sections, mo, os, pathlib, pl


if __name__ == "__main__":
    app.run()

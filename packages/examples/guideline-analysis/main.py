import marimo

__generated_with = "0.21.1"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # Structural Analysis of the Knowledge Space

    This notebook accompanies Section 5.3 of the paper. It demonstrates the four operators defined in Equations 4–7:

    1. [Analogical Transfer](#sec:analogical-transfer) -- similar advice, different contexts
    2. [Conflict Detection](#sec:conflict-detection) -- similar contexts, divergent advice
    3. [Viewpoint Divergence](#sec:viewpoint-divergence) -- one source's advice matches another's mistake
    4. [Boundary Detection](#sec:boundary-detection) -- context-exception alignment across guidelines

    Additional analyses include:
    - [Solution Convergence](#sec:solution-convergence) -- distinct problems, convergent fixes
    - [Remediation Distance](#sec:remediation-distance) -- proxy for implementation effort
    - [Projection](#sec:projection) -- 2D visualization of the knowledge space

    Each section includes a worked example from the current catalog. Several sections also illustrate a recurring limitation of embedding similarity: it often captures topic overlap before it captures applicability.

    **Reproducibility.** All queries execute over the embedded catalog described in Section 5.2. The current notebook uses OpenAI `text-embedding-3-large` ($d = 3072$). Vector indexing uses HNSW via DuckDB.
    """)
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Analogical Transfer
    <a id="sec:analogical-transfer"></a>

    This analysis surfaces guideline pairs that recommend a similar move in different situations: what Section 5.3 of the paper terms *analogical transfer*.

    **Method.** We compute:

    $$ S_{\text{transfer}} = \text{Sim}(\vec{v}_{\text{advice}}^A, \vec{v}_{\text{advice}}^B) - \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{context}}^B) $$

    A high score indicates guidelines whose advice is semantically close but whose contexts overlap less. Such pairs often reflect a shared perceptual or rhetorical principle expressed through different task descriptions.

    **Output columns:**
    - `advice_similarity`: Cosine similarity between advice sections.
    - `context_similarity`: Cosine similarity between context sections.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    advice_sim_threshold = 0.5
    context_diff_threshold = 0.4

    conn.query(f"""
    WITH 
    advice AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.advice'
    ),
    contexts AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.context'
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
    ### Example: Bar Charts Across Tasks

    The query returns a pair linking:

    - **`use-bar-charts-instead-of-line-charts-for-cluster-detection`**: recommends bars when readers must count groups of similar values.
    - **`use-bar-charts-to-support-main-effect-inferences-from-familiar-multivariate-data`**: recommends grouped bars when readers should recover an overall effect rather than focus only on interactions.

    The tasks differ, but both guidelines prefer discrete bars over connected lines when readers must segment comparisons instead of follow continuity. The operator surfaces that shared principle even though one pair is about cluster finding and the other is about reading an overall effect from multivariate data.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "use-bar-charts-instead-of-line-charts-for-cluster-detection",
                "use-bar-charts-to-support-main-effect-inferences-from-familiar-multivariate-data",
            ]
        )
    )
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Solution Convergence
    <a id="sec:solution-convergence"></a>

    This analysis identifies guideline pairs where distinct problems lead to similar solutions.

    **Method.** We compute:

    $$ S_{\text{convergence}} = \text{Sim}(\vec{v}_{\text{fix}}^A, \vec{v}_{\text{fix}}^B) - \text{Sim}(\vec{v}_{\text{mistake}}^A, \vec{v}_{\text{mistake}}^B) $$

    High scores indicate guidelines whose fixes are semantically close even though their mistakes are less similar. In the current catalog, these pairs often point to a shared repair move rather than to a shared visual form.

    **Output columns:**
    - `fix_similarity`: Cosine similarity between fix sections.
    - `mistake_similarity`: Cosine similarity between mistake sections.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    fix_sim_threshold = 0.7
    mistake_diff_threshold = 0.45

    conn.query(f"""
    WITH 
    fixes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.fix'
    ),
    mistakes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.mistakes'
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
    ### Example: Audience Validation

    The current thresholds return a pair linking:

    - **`match-chart-encodings-to-audience-visual-literacy`**: addresses overestimating what lay readers can decode from statistically demanding encodings.
    - **`validate-chart-takeaways-with-less-informed-readers`**: addresses expert overprojection about what less-informed readers will infer from a chart.

    The problems differ, but the fixes converge on the same practical move: check the chart with the intended audience instead of relying on expert self-review. In the current catalog, this operator often highlights shared evaluation workflow rather than a shared chart form.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "match-chart-encodings-to-audience-visual-literacy",
                "validate-chart-takeaways-with-less-informed-readers",
            ]
        )
    )
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boundary Detection
    <a id="sec:boundary-detection"></a>

    This analysis proposes handoff points where one guideline's scope ends and another's begins, corresponding to Equation 7 in Section 5.3 of the paper.

    **Method.** We measure similarity between the context of one guideline and the exceptions of another:

    $$ S_{\text{link}}(A, B) = \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{exception}}^B) $$

    A high score suggests that the context of Guideline A aligns with the exception of Guideline B. Such pairs often mark a handoff point: one rule stops applying where the other one should take over.

    **Output columns:**
    - `match_score`: Cosine similarity between context and exception vectors.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    boundary_match_threshold = 0.7

    conn.sql(f"""
    WITH 
    situations AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.context'
    ),
    exceptions AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.exceptions'
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
    mo.md(r"""
    ### Example: Irregular Intervals and Few Dates

    The query returns a strong link (score: 0.739) between:

    - **`use-area-chart-for-irregular-time-intervals`**
    - **`use-stacked-column-chart-when-there-are-few-dates`**

    The relationship is reciprocal. The area-chart guideline says to break the rule when dates are few and evenly spaced; the stacked-column guideline says to break the rule when intervals are unequal. The operator recovers the handoff: preserve elapsed time with an area chart when spacing is irregular, but switch to stacked columns when a short, evenly spaced series makes labels and values easier to read.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "use-area-chart-for-irregular-time-intervals",
                "use-stacked-column-chart-when-there-are-few-dates",
            ]
        )
    )
    return


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conflict Detection
    <a id="sec:conflict-detection"></a>

    This analysis identifies guideline pairs that address similar contexts but pull the designer toward different interventions.

    **Method.** In this notebook, we operationalize the overall recommended move with each guideline's embedded overview text and compute:

    $$ S_{\text{friction}} = \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{context}}^B) - \text{Sim}(\vec{v}_{\text{overview}}^A, \vec{v}_{\text{overview}}^B) $$

    High positive values indicate guidelines that describe a similar task but summarize different remedies at the whole-guideline level. In the current catalog, these pairs more often surface competing design levers than a direct contradiction.

    **Output columns:**
    - `situation_sim`: Cosine similarity between context sections.
    - `recommendation_sim`: Cosine similarity between overview sections.
    - `friction_score`: Difference between context and overview similarity.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    situation_sim_threshold = 0.8

    conn.query(f"""
    WITH 
    situations AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.context'
    ),
    overviews AS (
        SELECT id, embedding FROM embeddings WHERE role = 'overview'
    )
    SELECT 
        s1.id AS id_A, 
        s2.id AS id_B,
        list_cosine_similarity(s1.embedding, s2.embedding) AS situation_sim,
        list_cosine_similarity(o1.embedding, o2.embedding) AS recommendation_sim,

        -- Friction = High Context Overlap - Low Overview Overlap
        (situation_sim - recommendation_sim) AS friction_score
    FROM situations s1
    JOIN situations s2 ON s1.id < s2.id 
    JOIN overviews o1 ON s1.id = o1.id
    JOIN overviews o2 ON s2.id = o2.id
    -- Add a filter to make the results meaningful (otherwise you get 500k rows)
    WHERE situation_sim > {situation_sim_threshold}
    ORDER BY friction_score DESC
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example: Same Task, Different Lever

    The query links:

    - **`encode-primary-quantity-with-position-for-value-tasks`**
    - **`use-single-panel-instead-of-row-facets-for-individual-value-reading`**

    Both guidelines target exact value lookup and pairwise comparison in point-based displays. One intervenes by changing the encoding channel: put the primary quantity on position. The other intervenes by changing layout: collapse row facets into a single panel. This example shows what the friction operator often finds in the current catalog: not a head-on contradiction, but two different ways to support the same reading task.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "encode-primary-quantity-with-position-for-value-tasks",
                "use-single-panel-instead-of-row-facets-for-individual-value-reading",
            ]
        )
    )
    return


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Remediation Distance
    <a id="sec:remediation-distance"></a>

    This analysis defines a proxy for the scope of change a guideline requires.

    **Method.** We compute the cosine distance between a guideline's mistake description and its fix:

    $$ \text{Effort} = 1 - \text{Sim}(\vec{v}_{\text{fix}}, \vec{v}_{\text{mistake}}) $$

    **Interpretation:**
    - **Low distance**: The mistake and fix share vocabulary (e.g., "small label" vs. "large label"), suggesting a parameter adjustment.
    - **High distance**: The fix uses distinct vocabulary from the mistake (e.g., "cluttered pie chart" vs. "grouped bar chart"), suggesting structural change.

    **Output columns:**
    - `effort_score`: Cosine distance (1 minus similarity). Higher values indicate larger semantic gaps between problem and solution states.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    conn.query("""
    WITH 
    fixes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.fix'
    ),
    mistakes AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.mistakes'
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
    ### Example: Thumbnail Redesign

    The query assigns a high effort score (0.702) to **`use-pictographic-data-marks-to-attract-initial-attention`**:

    - **Mistake**: assuming that any nearby picture will attract attention.
    - **Fix**: redesign the thumbnail so the data marks themselves become pictographic.

    The semantic gap is large because the fix does not tweak the original preview. It changes the representation itself. The operator therefore treats this case as a redesign of the thumbnail's visual strategy rather than as a small local adjustment.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "use-pictographic-data-marks-to-attract-initial-attention",
            ]
        )
    )
    return


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Viewpoint Divergence
    <a id="sec:viewpoint-divergence"></a>

    This analysis identifies cases where one guideline's advice is close to another guideline's mistake description.

    **Method.** We compute:

    $$ S_{\text{contrast}}(A, B) = \text{Sim}(\vec{v}_{\text{advice}}^A, \vec{v}_{\text{mistake}}^B) $$

    A high score indicates that what one guideline recommends is close to what another guideline describes as a mistake. Some pairs do reflect a real dispute. Others expose a limitation of embedding similarity: it can capture shared aboutness before it captures rule direction. In practice, this operator works best as a review queue, not as an automatic contradiction detector.

    **Output columns:**
    - `collision_score`: Cosine similarity between one guideline's advice and another's mistake description.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    collision_threshold = 0.675

    conn.query(f"""
    WITH 
    advice_vectors AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.advice'
    ),
    mistake_vectors AS (
        SELECT id, embedding FROM embeddings WHERE role = 'section.mistakes'
    )
    SELECT 
        a.id AS recommender_id,
        m.id AS critic_id,
        list_cosine_similarity(a.embedding, m.embedding) AS collision_score
    FROM advice_vectors a
    CROSS JOIN mistake_vectors m
    WHERE 
        a.id != m.id -- Don't compare a guideline to itself
        AND collision_score > {collision_threshold} -- Threshold for a potential collision
    ORDER BY collision_score DESC;
    """).pl()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example: Hue Semantics

    The query surfaces a high collision between:

    - **`avoid-hue-only-encoding-for-ordered-values`**
    - **`use-categorical-hues-for-unordered-categories`**

    At first glance this looks like a contradiction about color. It is not. Both guidelines talk about hue, so the embeddings place them close together. But they apply to different data semantics: ordered values in the first case, unordered categories in the second. This pair therefore illustrates the aboutness-versus-applicability problem directly.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "avoid-hue-only-encoding-for-ordered-values",
                "use-categorical-hues-for-unordered-categories",
            ]
        )
    )
    return


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Projection of the Knowledge Space
    <a id="sec:projection"></a>

    This visualization projects the high-dimensional embedding space into two dimensions for inspection.

    **Method.** We use UMAP (Uniform Manifold Approximation and Projection), a manifold learning technique that preserves local neighborhood structure. Guidelines that are semantically close in the 3072-dimensional embedding space tend to remain close in the 2D projection, revealing local clusters.

    The interactive widget below displays all guideline sections. Points are colored by section role; hovering reveals guideline metadata.
    """)
    return


@app.cell(hide_code=True)
def _(index):
    index.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Implementation Details
    <a id="sec:implementation"></a>

    This section documents the pipeline that transforms the Markdown catalog into the queryable vector structure used in the analyses above.
    """)
    return


@app.cell(column=8, hide_code=True)
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
    2.  **Embedding:** Each section is embedded independently via `text-embedding-3-large` ($d = 3072$). This keeps the representation of an "Advice" section separate from the context or rationale.
    3.  **Indexing:** The resulting vectors are stored in DuckDB and indexed using HNSW (Hierarchical Navigable Small World graphs) to enable real-time similarity operations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Formal Notation

    Let $\mathcal{C}$ denote the catalog, a finite set of guidelines $\{g_1, \ldots, g_N\}$. Each guideline $g_i$ comprises role-specific text sections:

    $$ g_i = \{(r, t_{i,r}) \mid r \in \mathcal{R}\} $$

    where $\mathcal{R} = \{\texttt{context}, \texttt{advice}, \texttt{mistake}, \texttt{fix}, \texttt{exceptions}, \ldots\}$ is the set of section roles.

    Let $\mathcal{T}$ denote the space of natural-language text strings. The embedding function $\Phi: \mathcal{T} \rightarrow \mathbb{R}^d$ maps text to a $d$-dimensional vector space. For a guideline $g_i$ with a section of role $r$, the vector representation is:

    $$ \vec{v}_{i,r} = \Phi(t_{i,r}) $$

    where $t_{i,r} \in \mathcal{T}$ is the text content of that section.

    Similarity between sections is measured by cosine similarity:

    $$ \text{Sim}(\vec{v}_{A,r_1}, \vec{v}_{B,r_2}) = \frac{\vec{v}_{A,r_1} \cdot \vec{v}_{B,r_2}}{\|\vec{v}_{A,r_1}\| \, \|\vec{v}_{B,r_2}\|} $$

    The operators in this notebook combine similarity scores across different section roles to surface structural relationships. For example, analogical transfer (Equation 4 in the paper) computes:

    $$ S_{\text{transfer}}(A, B) = \text{Sim}(\vec{v}_{A,\texttt{advice}}, \vec{v}_{B,\texttt{advice}}) - \text{Sim}(\vec{v}_{A,\texttt{context}}, \vec{v}_{B,\texttt{context}}) $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    <a id="sec:setup"></a>

    The cells below load the catalog and establish the database connection. Implementation uses:

    - **Polars** for dataframe operations
    - **DuckDB** for SQL queries over embedded vectors
    - **OpenAI text-embedding-3-large** ($d = 3072$) for section embeddings
    """)
    return


@app.cell(column=9, hide_code=True)
def _(Catalog, catalog_parquet, pl):
    catalog = Catalog.from_df(pl.read_parquet(catalog_parquet.absolute()))
    return (catalog,)


@app.cell(hide_code=True)
def _(cache_dir, create_chroma_client):
    import chromadb.utils.embedding_functions as embedding_functions
    import os

    openrouter_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ["OPENROUTER_API_KEY"],
        api_base="https://openrouter.ai/api/v1",
        model_name="openai/text-embedding-3-large",
    )

    client = create_chroma_client(cache_dir / "analysis_chroma_db")

    collection = client.get_or_create_collection(
        name="catalog",
        embedding_function=openrouter_ef,
    )
    return (collection,)


@app.cell(hide_code=True)
def _(Index, cache_dir, catalog, collection, create_duckdb_conn):
    conn = create_duckdb_conn(cache_dir / "duckdb_catalog.db")
    index = Index(catalog, collection=collection, conn=conn)
    index.build()
    return conn, index


@app.cell(hide_code=True)
def _(mo, pathlib):
    NB_ROOT = pathlib.Path(__file__).parent
    REPO_ROOT = NB_ROOT.parent.parent.parent
    CATALOG_PARQUET_PATH = REPO_ROOT / "guidelines" / "catalog.parquet"
    catalog_parquet = mo.watch.file(CATALOG_PARQUET_PATH)
    return (catalog_parquet,)


@app.cell(hide_code=True)
def _():
    import nest_asyncio

    nest_asyncio.apply()
    return


@app.cell(hide_code=True)
def _():
    import pathlib

    import marimo as mo
    import polars as pl
    import platformdirs

    from chartcoach import Catalog, Index
    from chartcoach.catalog.clients import create_chroma_client, create_duckdb_conn

    cache_dir = pathlib.Path(platformdirs.user_cache_dir("chartcoach"))
    return (
        Catalog,
        Index,
        cache_dir,
        create_chroma_client,
        create_duckdb_conn,
        mo,
        pathlib,
        pl,
    )


if __name__ == "__main__":
    app.run()

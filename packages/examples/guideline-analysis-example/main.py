import marimo

__generated_with = "0.22.4"
app = marimo.App(width="columns", app_title="Guideline Analysis")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # ::lucide:compass:: Structural Analysis of the Knowledge Space

    This notebook accompanies Section 5.3 of the paper. It demonstrates how vector operations can surface latent relationships between guidelines, executing the operators depicted in Figure 2:

    1. [Analogical Transfer](#sec:analogical-transfer)
    2. [Solution Convergence](#sec:solution-convergence)
    3. [Boundary Detection](#sec:boundary-detection)
    4. [Conflict Detection](#sec:conflict-detection)

    Additional analyses not explicitly covered in the paper are included as well:

    5. [Remediation Distance](#sec:remediation-distance)
    6. [Viewpoint Divergence](#sec:viewpoint-divergence)
    7. [Space Projection](#sec:projection)

    Each section includes a worked example from the current catalog. Several queries also highlight a practical limitation of dense embeddings: they often capture shared vocabulary or topical overlap before they capture precise logical intent (such as rule polarity or strict conditionality). As such, these operators function best as discovery tools rather than perfect semantic classifiers.

    All queries execute over the embedded catalog described in Section 5.2 using OpenAI [`text-embedding-3-large`](https://developers.openai.com/api/docs/models/text-embedding-3-large) ($d = 3072$) and HNSW indexing via DuckDB.
    """)
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:map:: Projection of the Knowledge Space
    <a id="sec:projection"></a>

    This visualization using [Embedding Atlas](https://apple.github.io/embedding-atlas/) projects the high-dimensional embedding space into two dimensions using UMAP. This technique preserves the local neighborhood structure, causing semantically related guidelines to form local clusters. You can hover over points to inspect metadata and section roles.

    > This widget needs a live Python connection. Open the notebook with marimo to explore the embedding space.
    """)
    return


@app.cell(hide_code=True)
def _(conn, index):
    from embedding_atlas.projection import compute_vector_projection
    from embedding_atlas.widget import EmbeddingAtlasWidget

    embeddings_df = index.embeddings_df.to_pandas()
    compute_vector_projection(embeddings_df, vector="embedding")
    conn.execute(
        "CREATE OR REPLACE TABLE embedding_projections AS ("
        "SELECT id, projection_x, projection_y, neighbors FROM embeddings_df"
        ")"
    )
    EmbeddingAtlasWidget(
        embeddings_df,
        x="projection_x",
        y="projection_y",
        neighbors="neighbors",
        connection=conn,
    )
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:arrow-right-left:: Analogical Transfer
    <a id="sec:analogical-transfer"></a>

    This operator identifies pairs of guidelines that give similar advice but apply to different situations.

    We calculate it by subtracting context similarity from advice similarity:

    $$ S_{\text{transfer}} = \text{Sim}(\vec{v}_{\text{advice}}^A, \vec{v}_{\text{advice}}^B) - \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{context}}^B) $$

    A high score suggests that the design advice is semantically close while the contexts are distinct. This tends to surface shared perceptual or rhetorical principles that remain valid across different tasks.
    """)
    return


@app.cell(hide_code=True)
def _(conn):
    advice_sim_threshold = 0.65
    context_diff_threshold = 0.5

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


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:shrink:: Solution Convergence
    <a id="sec:solution-convergence"></a>

    This operator finds guideline pairs where distinct problems are resolved by the same repair move.

    We calculate this by subtracting mistake similarity from fix similarity:

    $$ S_{\text{convergence}} = \text{Sim}(\vec{v}_{\text{fix}}^A, \vec{v}_{\text{fix}}^B) - \text{Sim}(\vec{v}_{\text{mistake}}^A, \vec{v}_{\text{mistake}}^B) $$

    High scores suggest the fixes are semantically similar even when the triggering mistakes are different. In the current catalog, this helps identify versatile repair actions that apply to a variety of design issues.
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


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:signpost:: Boundary Detection
    <a id="sec:boundary-detection"></a>

    This analysis identifies potential handoff points where the applicability of one guideline ends and another begins.

    We measure the similarity between the "context" of one guideline and the "exceptions" of another:

    $$ S_{\text{link}}(A, B) = \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{exception}}^B) $$

    A high score suggests that Guideline A's context aligns with Guideline B's exceptions. This often marks a structural boundary where one rule should take over because the conditions for the other are no longer met.
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


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:git-branch:: Conflict Detection
    <a id="sec:conflict-detection"></a>

    This identifies guidelines that address similar situations but recommend different design choices.

    We calculate this by comparing context similarity against overview (summary) similarity:

    $$ S_{\text{friction}} = \text{Sim}(\vec{v}_{\text{context}}^A, \vec{v}_{\text{context}}^B) - \text{Sim}(\vec{v}_{\text{overview}}^A, \vec{v}_{\text{overview}}^B) $$

    High positive values indicate guidelines that share a situation but offer different remedies. In the current catalog, these often surface competing design levers—different ways to solve the same problem—rather than direct contradictions.
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


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:ruler:: Remediation Distance
    <a id="sec:remediation-distance"></a>

    This provides a proxy for the scope of change a guideline requires.

    We compute the cosine distance between a guideline's "mistake" description and its "fix":

    $$ \text{Effort} = 1 - \text{Sim}(\vec{v}_{\text{fix}}, \vec{v}_{\text{mistake}}) $$

    A low distance suggests the mistake and fix share similar vocabulary, which tends to indicate a minor parameter adjustment. A high distance suggests a larger semantic gap, often implying a more significant structural redesign or change in visual strategy.
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


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:messages-square:: Viewpoint Divergence
    <a id="sec:viewpoint-divergence"></a>

    This identifies cases where the advice recommended by one guideline is close to what another guideline describes as a mistake.

    We compute this by comparing advice and mistake vectors:

    $$ S_{\text{contrast}}(A, B) = \text{Sim}(\vec{v}_{\text{advice}}^A, \vec{v}_{\text{mistake}}^B) $$

    This operator helps surface potential disagreements in the literature or areas where guidelines share a topic but differ in their specific design instructions.
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

    - **`use-ordered-lightness-scales-for-ordered-values`**
    - **`avoid-hue-only-encoding-for-ordered-values`**

    These guidelines reflect different viewpoints on encoding ordered data with color. **`avoid-hue-only-encoding-for-ordered-values`** warns against the mistake of treating changes in hue as if they naturally imply a clear low-to-high sequence. In contrast, **`use-ordered-lightness-scales-for-ordered-values`** recommends using sequential or diverging scales with ordered lightness, since lightness progression more clearly communicates magnitude and direction for inherently ordered values.
    """)
    return


@app.cell(hide_code=True)
def _(catalog, pl):
    catalog.df.filter(
        pl.col("id").is_in(
            [
                "avoid-hue-only-encoding-for-ordered-values",
                "use-ordered-lightness-scales-for-ordered-values",
            ]
        )
    )
    return


@app.cell(column=8, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:cog:: Implementation Details
    <a id="sec:implementation"></a>

    The ingestion process transforms raw Markdown into a queryable vector space through three stages:

    1. **Parsing:** The `Catalog` extracts semantic sections (`context`, `advice`, `mistake`, etc.) from the raw files.
    2. **Embedding:** Each section is embedded independently via `text-embedding-3-large`. This ensures the representation of design advice is kept separate from its context or rationale.
    3. **Indexing:** Vectors are stored in DuckDB and indexed using HNSW graphs to enable real-time similarity operations across the catalog.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart LR
        subgraph stage1 ["Curated Guidelines"]
            MD[Markdown Files]
        end

        subgraph stage2 ["Parsing & Structure"]
            MD --> |Parse| G[Guideline Object]
            G --> C_Txt[Context Text]
            G --> A_Txt[Advice Text]
            G --> M_Txt[Mistake Text]
        end

        subgraph stage3 ["Vector Space"]
            direction TB
            C_Txt --> |Phi| V_Ctx[Vector: Context]
            A_Txt --> |Phi| V_Adv[Vector: Advice]
            M_Txt --> |Phi| V_Mis[Vector: Mistake]
        end

        subgraph stage4 ["Storage & Index"]
            V_Ctx --> DB[(DuckDB)]
            V_Adv --> DB
            V_Mis --> DB
            DB --> Index{{HNSW Index}}
        end

        %% Professional Color Palette
        classDef source fill:#f8f9fa,stroke:#343a40,stroke-width:2px,color:#343a40
        classDef process fill:#ffffff,stroke:#adb5bd,stroke-width:1px,stroke-dasharray: 5 5
        classDef vector fill:#e7f5ff,stroke:#228be6,stroke-width:2px,color:#1864ab
        classDef storage fill:#ebfbee,stroke:#40c057,stroke-width:2px,color:#2b8a3e
        classDef subgraphStyle fill:#f1f3f5,stroke:#dee2e6,stroke-width:1px,color:#495057,font-weight:bold

        %% Apply Classes
        class MD source
        class G,C_Txt,A_Txt,M_Txt process
        class V_Ctx,V_Adv,V_Mis vector
        class DB,Index storage
        class stage1,stage2,stage3,stage4 subgraphStyle
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


@app.cell(column=9, hide_code=True)
def _(Catalog, catalog_parquet, pl):
    catalog = Catalog.from_df(pl.read_parquet(catalog_parquet.absolute()))
    return (catalog,)


@app.cell(hide_code=True)
def _(cache_dir, create_chroma_client):
    import os

    import chromadb.utils.embedding_functions as embedding_functions

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
    conn = create_duckdb_conn(cache_dir / "catalog_index.db")
    index = Index(catalog, collection=collection, conn=conn)
    index.build()
    return conn, index


@app.cell(hide_code=True)
def _(mo):
    NB_ROOT = mo.notebook_dir()
    REPO_ROOT = NB_ROOT.parent.parent.parent
    CATALOG_PARQUET_PATH = REPO_ROOT / "guidelines" / "catalog.parquet"
    catalog_parquet = mo.watch.file(CATALOG_PARQUET_PATH)
    return (catalog_parquet,)


@app.cell(hide_code=True)
def _():
    import pathlib

    import marimo as mo
    import platformdirs
    import polars as pl
    from chartcoach import Catalog
    from chartcoach.catalog.clients import create_chroma_client, create_duckdb_conn
    from chartcoach.catalog.index import Index

    cache_dir = pathlib.Path(platformdirs.user_cache_dir("chartcoach"))
    return (
        Catalog,
        Index,
        cache_dir,
        create_chroma_client,
        create_duckdb_conn,
        mo,
        pl,
    )


if __name__ == "__main__":
    app.run()

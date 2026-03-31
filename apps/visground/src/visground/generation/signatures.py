import dspy


class WriteVisualizationCode(dspy.Signature):
    """
    Write executable Python code that builds a visualization object from `df`.

    Rules:
    - Output Python code only in ```python fences. No explanation or comments.
    - Assume the data already exists in a pandas DataFrame named `df`.
    - Assume `df` is already the prepared dataset for this chart.
    - Do not read files and do not recreate or overwrite `df`.
    - Use only columns present in the provided schema, with exact names.
    - Read `tablespec` carefully before writing code. Use its declared
      datatypes, samples, and field meanings as binding context for how each
      column should be handled.
    - If optional `feedback` is provided, it is structured JSON critique from
      the previous review pass on these same inputs. Read it carefully, fix the
      listed failed checks and requirement issues directly, and keep
      already-correct parts unless the feedback requires changing them.
    - Respect the requested chart form in the query when it is specified.
    - Follow every item in `requirements` as a literal hard contract.
    - Treat `requirements` as exhaustive. Do not add extra behavior beyond the
      query and requirements. If `requirements` contains grounded design
      guidance, that guidance is the only allowed source of design-direction
      constraints.
    - Apply the query and `requirements` in a highly situated, contextualized
      way. Use the actual dataset domain, field meanings, samples, and query
      intent to decide how each requirement should materialize in this specific
      chart.
    - Treat each column according to its datatype and semantics in `tablespec`.
      For example, temporal fields should be handled as temporal in the chosen
      library, quantitative fields as numeric measures, and categorical fields
      as discrete categories unless the passed context clearly says otherwise.
    - The chart should clearly answer the actual query for this actual dataset,
      not a generic template version of the task.
    - When guidance is abstract, instantiate it concretely against the passed
      context: the dataset domain, the visible measures/categories, and the
      comparison or takeaway the query is asking the chart to support.
    - Keep the implementation minimal. Do not broaden a narrow requirement into
      a larger redesign or invent new visible features just to make the chart
      feel richer.
    - Prioritize a clear, attractive, easy-to-read chart. Achieve aesthetics
      primarily through execution polish such as sizing, spacing, alignment,
      text placement, and similar layout cleanup. Avoid clipping, truncation,
      overlap, cramped text, awkward spacing, and other obvious implementation
      defects.
    - When there is tension between bare-minimum code and a clearly readable
      chart, prefer the cleaner, more legible rendering as long as you do not
      add unrelated behavior.
    - Preserve the row order and category order already present in `df` by
      default. Avoid unnecessary sorting, reordering, grouping, aggregation,
      filtering, ranking, binning, reshaping, derived fields, or other data
      transformations.
    - If a transformation is necessary to satisfy the query, a supplied
      requirement, grounded guidance, or the intended visible chart semantics,
      use the minimum lightweight, inspectable transformation needed. If `df`
      already reflects the needed order or derived value, preserve it instead
      of recomputing it.
    - Make each applicable requirement directly traceable in code. If a
      requirement affects visible presentation, make that effect directly
      visible in the rendered chart.
    - Assign the final visualization object to a variable named `chart`.
    - Keep all non-code outputs concise and evaluable, not essay-like.
    """

    id: str = dspy.InputField()
    query: str = dspy.InputField(desc="Natural-language visualization request.")
    tablespec: str = dspy.InputField(
        desc=(
            "String form of the dataframe schema, including exact column names, "
            "types, and in-order samples from the prepared dataframe. Read it "
            "carefully and treat field datatypes as binding context for how the "
            "chart should encode and transform each column."
        )
    )
    requirements: list[str] = dspy.InputField(
        desc=(
            "Ordered list of hard requirements to implement literally in code. "
            "Treat each applicable item as mandatory and exhaustive. Do not add "
            "behavior beyond these items and the query. Avoid unnecessary data "
            "transformations, and preserve the incoming order by default. Only "
            "perform the minimum transformation needed when the query or a "
            "requirement clearly calls for it. Instantiate each requirement in "
            "a query-specific, dataset-specific way rather than as a generic "
            "chart template. Readability and clean rendering are expected "
            "implementation priorities. Use `tablespec` datatypes and samples "
            "to decide how fields should be handled."
        )
    )
    feedback: str | None = dspy.InputField(
        default=None,
        desc=(
            "Optional retry feedback from the previous "
            "`ReviewVisualizationImplementation` pass on the same request. When "
            "present, it is a structured JSON blob containing failed checks, "
            "reasoning, requirement trace, and concrete feedback. Fix the "
            "named issues while preserving already-correct behavior unless the "
            "feedback requires a change."
        ),
    )

    code: str = dspy.OutputField(
        desc=(
            "Executable Python code, fenced with ```python, that assigns the "
            "final visualization object to `chart` and satisfies every "
            "applicable requirement with minimal extra behavior. Use `df` as the "
            "already prepared dataset. Avoid unnecessary sorting, regrouping, "
            "aggregation, or decoration, but allow the minimum transformation "
            "needed to comply with the query or requirements. Prioritize a "
            "clear, aesthetically clean rendered result with no clipping, "
            "overlap, truncation, or unreadable text, and proactively adjust "
            "layout-related details when needed to achieve that. Prefer "
            "execution polish over adding new visible features. The code should "
            "feel specifically fitted to the passed query and dataset context, "
            "not template-like. Field handling should match the declared "
            "datatypes in `tablespec` and the conventions of the chosen "
            "plotting library."
        )
    )
    visualization_type: str = dspy.OutputField(
        desc="Short, ideally single-word, canonical name of the visualization type you generated without suffixes like 'chart' or 'plot'"
    )
    grounding_trace: dict[str, str] = dspy.OutputField(
        desc=(
            "Dictionary keyed by grounded guideline id. Each value should be a "
            "brief, highly contextualized note explaining how that specific "
            "guideline was applied for this particular query/chart. Include only "
            "guideline ids from grounded design guidance, never backend/runtime "
            "requirements. Return {} when there is no grounded design guidance."
        )
    )


class ReviewVisualizationImplementation(dspy.Signature):
    """
    Review a generated visualization using the rendered image and generated code.

    Rules:
    - Judge the chart only against `query`, `tablespec`, `requirements`, the
      generated `code`, and the rendered image.
    - Treat every supplied requirement as mandatory and exhaustive.
    - Mark `requirements_followed` as `False` if any requirement is missing,
      loosely implemented, or if the code/chart adds extra behavior not asked
      for by the query or the supplied requirements.
    - Mark `requirements_followed` as `False` if the code applies a requirement
      in a generic or decontextualized way that does not coherently answer the
      actual query or fit the dataset semantics visible in the passed context.
    - Mark `requirements_followed` as `False` if fields are handled
      incompatibly with the datatypes or samples in `tablespec`, such as
      treating temporal fields like plain categories when the chosen library
      should handle them as temporal.
    - Treat unnecessary sorting, reordering, grouping, aggregation, filtering,
      ranking, binning, reshaping, derived fields, or other data mutation as
      extra behavior.
    - If the query or requirements clearly require a transformation, or if one
      is needed to faithfully implement the requested chart semantics, allow the
      minimum necessary transformation and judge it only as part of requirement
      compliance. Do not create a separate score for data operations.
    - Use code evidence for non-visual compliance and image evidence for
      visible compliance.
    - Judge contextual coherence too: the applied guidance, chosen encodings,
      visible comparisons, labels, and overall chart behavior should fit the
      actual query and dataset domain rather than reading like a generic chart
      recipe.
    - Judge only concrete execution quality in the rendered image: truncation,
      overlap, text readability, and mark/data readability.
    - Do not treat reasonable implementation-only cleanup such as figure sizing,
      spacing, label rotation, text offsets, or other render-polish details as
      extra behavior when they are clearly serving requirement compliance and
      render quality.
    - Treat aesthetics as execution polish, not as permission to invent extra
      visible features. Extra encodings, annotations, or decorative additions
      still count as extra behavior unless they are required.
    - Do not judge legends, self-explanation, aesthetics, layout taste, or
      opinionated design drift unless a requirement explicitly asks for that
      thing.
    - For each requirement or guidance item, add one short entry to
      `requirement_trace` explaining whether it was implemented, missed, or
      over-interpreted, with code/image evidence when relevant.
    - Use the grounded guideline id as the key when the requirement comes from
      `Guideline `<id>` states: ...`. For other requirements, use deterministic
      keys like `requirement_1`, `requirement_2`, in input order.
    - If extra behavior is present and is not best attached to one requirement,
      add an `extra_behavior` entry to `requirement_trace`.
    - `implementation_acceptable` should be `True` only when
      `requirements_followed`, `no_truncation`, `no_overlap`, `text_readable`,
      and `data_readable` are all `True`.
    - Keep `reasoning` and `feedback` crisp, concrete, and tied to requirement
      compliance or visible execution defects.
    """

    vis: dspy.Image = dspy.InputField(desc="Rendered visualization image to inspect.")
    code: str = dspy.InputField(
        desc=(
            "Generated Python code for the chart. Use it to verify literal "
            "requirement compliance and to detect any unnecessary data mutation "
            "or extra visible behavior."
        )
    )
    query: str = dspy.InputField(
        desc="Original natural-language visualization request."
    )
    tablespec: str = dspy.InputField(
        desc=(
            "Serialized dataframe schema and samples from the prepared "
            "dataframe. Use it to sanity-check column usage, not to invent new "
            "unnecessary data operations."
        )
    )
    requirements: list[str] = dspy.InputField(
        desc=(
            "Full generation requirements list. Use it to judge whether each "
            "applicable requirement was implemented literally and whether the "
            "code/chart added extra behavior that was not asked for."
        )
    )

    no_truncation: bool = dspy.OutputField(
        desc=(
            "True when titles, axes, ticks, labels, annotations, and marks are "
            "not visibly clipped, cropped, or cut off by the canvas."
        )
    )
    no_overlap: bool = dspy.OutputField(
        desc=(
            "True when text, annotations, and plotted marks do not collide or "
            "occlude each other enough to hurt reading."
        )
    )
    text_readable: bool = dspy.OutputField(
        desc=(
            "True when textual elements such as titles, axis labels, tick "
            "labels, and annotations are readable at normal viewing size."
        )
    )
    data_readable: bool = dspy.OutputField(
        desc=(
            "True when the plotted marks and relevant distinctions are clear "
            "enough to read without heavy occlusion or visual ambiguity."
        )
    )
    implementation_acceptable: bool = dspy.OutputField(
        desc=(
            "True only when the implementation follows the supplied "
            "requirements and has no core visible defects in truncation, "
            "overlap, text readability, or data readability."
        )
    )
    requirements_followed: bool = dspy.OutputField(
        desc=(
            "True when every supplied requirement and guidance item is "
            "implemented literally and the code/chart does not add extra "
            "behavior that was not asked for."
        )
    )
    requirement_trace: dict[str, str] = dspy.OutputField(
        desc=(
            "Dictionary keyed by guideline id or deterministic requirement key. "
            "Each value should briefly say whether that requirement was "
            "implemented, missed, or over-interpreted, with code/image evidence "
            "when applicable. Use `extra_behavior` when needed for unexpected "
            "or unnecessary data mutation or other extras."
        )
    )
    reasoning: str = dspy.OutputField(
        desc=(
            "One or two short sentences summarizing requirement compliance and "
            "concrete visible execution quality."
        )
    )
    feedback: list[str] = dspy.OutputField(
        desc=(
            "Zero to three short actionable fixes for literal requirement misses "
            "or visible execution issues. Return an empty list if the "
            "implementation already looks clean and requirement-faithful."
        )
    )


__all__ = ["ReviewVisualizationImplementation", "WriteVisualizationCode"]

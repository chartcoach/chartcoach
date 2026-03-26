import dspy


class WriteVisualizationCode(dspy.Signature):
    """
    Write executable Python code that builds a visualization object from `df`.

    Rules:
    - Output Python code only in ```python fences. No explanation or comments.
    - Assume the data already exists in a pandas DataFrame named `df`.
    - Do not read files and do not recreate or overwrite `df`.
    - Use only columns present in the provided schema, with exact names.
    - Respect both the analytical intent and the requested chart form in the query.
    - Follow every item in `requirements` strictly. These may include required imports,
      library constraints, design guidance, or output conventions.
    - If `requirements` contains grounded design guidance, those grounded design
      requirements are the ONLY allowed source of design-direction constraints.
      Do not add made-up chart-choice, encoding, annotation, palette, layout,
      rhetoric, or polish heuristics beyond what those requirements specify.
    - When grounded design guidance is present, only non-design implementation
      defaults remain allowed: valid library usage, readable labels implied by
      the query, syntactic completeness, and the minimum operational defaults
      required to produce a functioning chart.
    - If no grounded design guidance is present in `requirements`, use your own
      embedded visualization knowledge to the fullest degree, especially for
      chart-family, encoding, and comparison decisions. In that ungrounded case,
      do not suppress model-specific visualization judgment into generic sameness.
    - Assign the final visualization object to a variable named `chart`.
    - Keep all non-code outputs concise and evaluable, not essay-like.
    """

    id: str = dspy.InputField()
    query: str = dspy.InputField(desc="Natural-language visualization request.")
    tablespec: str = dspy.InputField(
        desc=(
            "String form of the dataframe schema, including exact column names, "
            "statistical properties and samples."
        )
    )
    requirements: list[str] = dspy.InputField(
        desc=(
            "Ordered list of requirements to follow strictly, such as required imports, "
            "library-specific rules, design guidance, or output constraints. "
            "If grounded design guidance is present here, it is authoritative and "
            "must be followed exactly without inventing extra design heuristics. "
            "If no grounded design guidance is present, the model should rely on "
            "its own visualization knowledge aggressively."
        )
    )

    code: str = dspy.OutputField(
        desc=(
            "Executable Python code, fenced with ```python, that follows all requirements "
            "and assigns the final visualization object to `chart`. When grounded "
            "design requirements are present, the code must not reflect additional "
            "made-up design guidance beyond those requirements."
        )
    )
    visualization_type: str = dspy.OutputField(
        desc="Short, ideally single-word, canonical name of the visualization type you generated without suffixes like 'chart' or 'plot'"
    )
    query_interpretation: str = dspy.OutputField(
        desc=(
            "One short sentence restating what the chart should help the user see "
            "or compare."
        )
    )
    design_rationale: list[str] = dspy.OutputField(
        desc=(
            "Two to four short bullets explaining why the chosen chart type and "
            "encoding was chosen. If grounded design guidance is present, explain "
            "the choice through those supplied requirements rather than through "
            "invented extra visualization heuristics."
        )
    )
    grounding_trace: list[str] = dspy.OutputField(
        desc=(
            "Zero to three short bullets naming the requirement or guidance items "
            "that most influenced the design choice. Quote brief phrases from the requirements when possible. "
            "If grounded design guidance is present, only cite actually supplied requirement items. "
            "Empty list if you were not provided with any design-specific guidance. "
            "Library-specific rules are not considered design guidance."
        )
    )


__all__ = ["WriteVisualizationCode"]

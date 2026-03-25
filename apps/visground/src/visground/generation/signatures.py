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
            "library-specific rules, design guidance, or output constraints."
        )
    )

    code: str = dspy.OutputField(
        desc=(
            "Executable Python code, fenced with ```python, that follows all requirements "
            "and assigns the final visualization object to `chart`."
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
            "encoding was chosen"
        )
    )
    grounding_trace: list[str] = dspy.OutputField(
        desc=(
            "Zero to three short bullets naming the requirement or guidance items "
            "that most influenced the design choice. Quote brief phrases from the requirements when possible. "
            "Empty list if you were not provided with any design-specific guidance. Library-specific rules are not considered design guidance."
        )
    )


__all__ = ["WriteVisualizationCode"]

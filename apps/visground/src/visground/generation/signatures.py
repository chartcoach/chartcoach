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
    - Follow every item in `requirements` as a hard contract without exception.
      Every applicable requirement must be implemented in the emitted code.
      None of them are optional.
    - Do not treat any requirement as an example, hint, or loose style direction.
      Treat each requirement literally and satisfy it directly in code.
    - Requirements override your prior preferences, default heuristics, and
      stylistic instincts. Do not weaken, reinterpret, or replace a supplied
      requirement with a nearby alternative that you prefer.
    - Satisfy all applicable requirements jointly. Do not cherry-pick only the
      ones you like, and do not trade one requirement away for another unless
      that is logically unavoidable.
    - Do not generalize a narrow requirement into a broader redesign. If a
      requirement mentions one specific chart decision, change that decision and
      only the minimum adjacent behavior needed to make it work coherently.
    - If `requirements` contains grounded design guidance, those grounded design
      requirements are the ONLY allowed source of design-direction constraints.
      Do not add made-up chart-choice, encoding, annotation, palette, layout,
      rhetoric, or polish heuristics beyond what those requirements specify.
    - When `requirements` call for a non-mainstream, non-default, or otherwise
      non-trivial design decision, do not implement it loosely, approximately,
      or as a shallow imitation. Think through exactly how to realize that
      design in the chosen plotting library.
    - For non-default design decisions, prefer precise, library-native,
      publication-ready implementation over brittle hacks, accidental-looking
      workarounds, or half-working approximations.
    - For non-default design decisions, preserve semantic correctness as well as
      appearance. Axes, scales, encodings, grouping, ordering, coordinate
      systems, legends, annotations, and interactions must still mean exactly
      what the design intends them to mean.
    - For non-default designs, reason about the whole chart as a system. Layers,
      marks, scales, legends, labels, annotations, ordering, faceting, and any
      interactive or compositional pieces must work together coherently rather
      than each being handled in isolation.
    - Whenever requirements constrain the result, do not perturb or mutate
      unrelated design decisions. Keep the chart coherent and as close as
      possible to only the supplied requirements plus the query.
    - If a requirement constrains one aspect of the chart, preserve the rest of
      the design unless a change is strictly necessary to satisfy that
      requirement, avoid a contradiction, or produce a functioning chart.
    - The absence of a requirement is not permission to redesign nearby aspects
      of the chart. Leave unconstrained neighboring choices alone unless the
      query, the library, or strict compliance forces a change.
    - Prefer omission over invention. If a design move is not required by the
      query, the library, or the supplied requirements, do not add it just
      because it seems tasteful or clever.
    - When grounded design guidance is present, only non-design implementation
      defaults remain allowed: valid library usage, readable labels implied by
      the query, syntactic completeness, and the minimum operational defaults
      required to produce a functioning chart.
    - If no grounded design guidance is present in `requirements`, use your own
      embedded visualization knowledge to the fullest degree, especially for
      chart-family, encoding, and comparison decisions. In that ungrounded case,
      do not suppress model-specific visualization judgment into generic sameness.
    - If a non-default design is required, invest the extra implementation care
      needed to make it correct, aesthetically pleasing, visually apparent,
      production-ready, publication-ready, and free of bugs or awkward artifacts.
      The worst outcome is a potentially strong non-trivial design implemented
      poorly.
    - Do not silently collapse a required unusual design into a safer default,
      decorative substitute, or semantically weaker approximation. If the
      library makes the design difficult, implement the highest-fidelity robust
      version available without misrepresenting what the chart means.
    - Do not let one custom part of the chart quietly break another. A non-
      default design is only successful if the final composition is internally
      consistent: scales align, layers read in the right order, annotations
      support the right evidence, legends match the encodings, and nothing
      feels patched together.
    - Before finalizing the code, mentally inspect the rendered chart as if you
      were reviewing the actual output. Do not stop at "the code compiles" or
      "the API call is valid"; check whether the resulting chart would really
      look correct.
    - For non-default designs or dense compositions, do an extra internal QA
      pass before returning code. Look for wrong scales, misleading defaults,
      occluded marks, broken layering, legend drift, clipped elements,
      mismatched annotations, unreadable text, awkward whitespace, alignment
      issues, and anything else that would make the final render look buggy or
      unprofessional.
    - Ensure the rendered chart is production-ready: choose figure size, margins,
      padding, spacing, label rotation, legend placement, facet spacing, and
      mark sizing so there are no clips, overlaps, truncation, crowding,
      cropped legends, cropped labels, or other layout defects.
    - Treat clipping, overlap, truncation, and cropped elements as failures to
      fix in code, not as optional polish to ignore.
    - Whenever you add text for any purpose, place it deliberately. Text should
      be easy to notice, easy to read, and clearly associated with the marks,
      region, or evidence it explains.
    - Keep added text sparse and high-signal. Do not add so many labels or
      annotations that the chart becomes crowded, noisy, or harder to read.
    - Be especially careful with annotations or text placed inside the plot
      area. Do not let them overlap marks or each other, sit in visually noisy
      regions, blend into the background, drift too far from the evidence they
      describe, or end up in hard-to-spot positions.
    - Prefer fewer, more informative annotations over many weak ones. If
      annotating everything would clutter the chart, annotate only the most
      important evidence instead of forcing dense text into the figure.
    - If in-plot text or annotations are needed, adjust offsets, alignment,
      surrounding whitespace, contrast, font size, font weight, annotation
      boxes, leader lines, or chart size until the text is readable and easy to
      find without obscuring the chart.
    - Never solve annotation crowding by making text tiny, faint, cramped, or
      visually subordinate to the point that readers will miss it or struggle to
      read it.
    - If a requirement affects visual presentation, implement it so the effect
      is directly visible and inspectable in the rendered chart. Do not satisfy
      a visual requirement only nominally, indirectly, or in hidden code paths.
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
            "Ordered list of hard requirements to implement literally in the code, "
            "such as required imports, library-specific rules, design guidance, or "
            "output constraints. Treat every applicable item as mandatory, not as "
            "an example or suggestion. If grounded design guidance is present here, "
            "it is authoritative: follow it exactly. More generally, all supplied "
            "requirements override model preferences, should be satisfied jointly, "
            "and should not cause unrelated design mutations unless strict compliance "
            "or chart validity requires that change. A narrow requirement should "
            "remain narrow; do not expand it into a broader redesign. If a "
            "requirement specifies a non-default design decision, implement that "
            "decision with extra library-specific care rather than approximating it "
            "loosely or semantically degrading it. Treat the resulting chart as a "
            "coherent system, not as a bag of disconnected custom tweaks. Before "
            "returning code, internally review the likely rendered output for "
            "quality and correctness."
        )
    )

    code: str = dspy.OutputField(
        desc=(
            "Executable Python code, fenced with ```python, that fully implements "
            "every applicable requirement in the rendered chart and assigns the "
            "final visualization object to `chart`. Do not merely acknowledge "
            "requirements in prose; satisfy them in code. When grounded design "
            "requirements are present, keep the result as close as possible to "
            "only those requirements and the query, without additional made-up "
            "design mutations. If the requirements constrain only part of the "
            "chart, keep the unconstrained remainder conservative and minimally "
            "mutated. If a requirement affects visual presentation, the rendered "
            "chart must show that compliance clearly and directly. Any added "
            "text or annotation must be placed so it is legible, easy to spot, "
            "non-overlapping, and not overcrowded. Prefer fewer high-signal "
            "annotations over dense low-value text. If requirements call for a "
            "non-default design, implement it cleanly and expertly in the given "
            "plotting library so the result looks intentional, polished, correct, "
            "and non-buggy rather than like a rough approximation. Preserve the "
            "intended semantics of that design rather than faking its appearance "
            "with a weaker substitute. All interacting parts of the chart must "
            "work together coherently rather than appearing locally fixed but "
            "globally inconsistent. Before returning, the code should already "
            "reflect an internal render-level QA pass over likely failure modes. "
            "The rendered chart must have clean layout and sizing with no "
            "clipping, overlap, truncation, crowding, or cropped elements."
        )
    )
    visualization_type: str = dspy.OutputField(
        desc="Short, ideally single-word, canonical name of the visualization type you generated without suffixes like 'chart' or 'plot'"
    )
    query_interpretation: str = dspy.OutputField(
        desc=(
            "One short sentence restating what the chart should help the user see "
            "or compare, without broadening the request beyond the query and the "
            "supplied requirements or generalizing narrow requirements into a "
            "larger redesign story."
        )
    )
    design_rationale: list[str] = dspy.OutputField(
        desc=(
            "Two to four short bullets explaining why the chosen chart type and "
            "encoding was chosen. If grounded design guidance is present, explain "
            "the choice through those supplied requirements rather than through "
            "invented extra visualization heuristics, and do not claim a "
            "requirement was followed unless the emitted code actually implements it. "
            "When requirements constrain only part of the design, explain how the "
            "remaining choices stayed conservative and coherent. If text or "
            "annotations were added, explain how their placement stays readable, "
            "discoverable, and appropriately sparse. If a non-default design was "
            "required, explain how the implementation makes it correct, apparent, "
            "polished, semantically faithful, library-appropriate, and coherent "
            "across all interacting chart components. Mention any important render-"
            "level failure modes you actively avoided when that was material to "
            "the design."
        )
    )
    grounding_trace: list[str] = dspy.OutputField(
        desc=(
            "Zero to three short bullets naming the requirement or guidance items "
            "that most influenced the design choice. Quote brief phrases from the requirements when possible. "
            "If grounded design guidance is present, only cite actually supplied requirement items. "
            "Never cite a requirement that the emitted code does not implement. "
            "Empty list if you were not provided with any design-specific guidance. "
            "Library-specific rules are not considered design guidance."
        )
    )


__all__ = ["WriteVisualizationCode"]

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
    - Every requirement should be traceable to explicit code. Do not rely on a
      library default, an implicit side effect, or vague nearby code when the
      requirement can be implemented directly and inspectably.
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
    - Treat decoding aids as mandatory implementation, not optional polish. If
      any semantically meaningful visual distinction is not already spelled out
      directly on the marks or by nearby text, the chart must include a legend
      or another equally explicit visible decoding aid.
    - Never rely on the reader to infer what a color, shape, line style, size,
      facet, highlight, reference region, layer role, or other visible chart
      decision means from context alone. If that meaning is not self-evident in
      the rendered chart, make it explicit.
    - Missing decode aids are correctness failures, not tasteful omissions. If
      multiple parts of the chart would otherwise be hard to identify or map
      back to their meaning, add the legend, direct labels, or local callouts
      needed to remove that ambiguity.
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
    - If the query or requirements imply filtering, grouping, aggregation,
      sorting, ranking, binning, reshaping, or derived fields, write those
      operations explicitly in code so a reviewer can point to where they
      happen. Do not rely on plotting-library shorthand to hide required data
      logic when explicit dataframe operations would make the implementation
      clearer and more faithful.
    - When grounded design guidance is present, only non-design implementation
      defaults remain allowed: valid library usage, readable labels implied by
      the query, syntactic completeness, and the minimum operational defaults
      required to produce a functioning chart.
    - Those allowed implementation defaults include the minimum visible
      decoding aids needed to make the chart understandable, such as legends,
      direct labels, or short local explanations for otherwise unlabeled
      encodings, highlights, or visual distinctions.
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
    - Do not rely on hope or a single generic auto-layout call when the
      composition is tight. Adjust figure size, constrained or tight layout,
      subplot parameters, legend anchors, and surrounding whitespace
      deliberately until titles, labels, legends, and annotations have enough
      room.
    - Treat clipping, overlap, truncation, and cropped elements as failures to
      fix in code, not as optional polish to ignore.
    - Whenever you add text for any purpose, place it deliberately. Text should
      be easy to notice, easy to read, and clearly associated with the marks,
      region, or evidence it explains.
    - When the requirements or guidance make one specific mark, bar, point, or
      region the intended focal comparison, implement the visible explanation
      as one coherent local package. If the prescribed effect calls for
      highlighting, direct value display, and a short explanatory callout,
      satisfy those visibly on or near the focal mark rather than scattering
      them across disconnected surfaces like only the title, subtitle, or axis.
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
            "coherent system, not as a bag of disconnected custom tweaks. Also "
            "treat basic decoding aids as mandatory implementation: if an "
            "important visible distinction is not directly labeled on the marks "
            "or by nearby text, include a legend or equally explicit visible "
            "decode aid rather than making the viewer guess. Make each "
            "requirement inspectably traceable in code, including required data "
            "operations. Before returning code, internally review the likely "
            "rendered output for quality and correctness."
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
            "Required dataframe operations should be explicit and easy to audit "
            "in code rather than hidden in ambiguous shorthand. "
            "Any meaningful visible distinction that is not directly labeled on "
            "the marks must be decoded by a legend or equally explicit visible "
            "aid; unexplained encodings or highlights are implementation "
            "failures. "
            "The rendered chart must have clean layout and sizing with no "
            "clipping, overlap, truncation, crowding, or cropped elements."
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
    Review the implementation quality of a generated visualization using the
    rendered image and the generated code.

    Rules:
    - Judge the final chart against `query`, `tablespec`, `requirements`,
      generated `code`, and the rendered image.
    - Treat every supplied requirement as mandatory. If any requirement is
      missing, only approximately implemented, or only implied rather than
      explicitly realized in code and/or the chart, mark
      `requirements_followed` as `False`.
    - Use code evidence for non-visual or data-operation requirements, and use
      rendered-image evidence for visible requirements.
    - If the final chart makes visible non-default, opinionated design
      decisions that are not prescribed by the query or the supplied
      requirements, mark `no_unprescribed_design` as `False`.
    - Treat unprescribed visible design drift as a hard negative. If it occurs,
      `implementation_acceptable` should also be `False`.
    - For each requirement or guidance item, add one short entry to
      `requirement_trace` explaining whether it was explicitly implemented,
      missed, or over-interpreted, and cite code evidence and visible evidence
      when applicable.
    - Use the grounded guideline id as the key when the requirement comes from
      `Guideline `<id>` states: ...`. For other requirements, use deterministic
      keys like `requirement_1`, `requirement_2`, in their input order among
      non-guideline requirements.
    - Still judge execution quality visible in the image, including clipping,
      overlap, readability, and layout balance.
    - Judge code-level faithfulness too. If the query or requirements imply
      filtering, grouping, aggregation, sorting, ranking, binning, reshaping,
      or derived fields, verify those operations are present and semantically
      aligned with the rendered chart. If they are missing or wrong, mark
      `data_operations_correct` as `False`.
    - Judge understandability, not just cleanliness. The chart should be easy
      to decode without guesswork: important encodings, highlights, groups,
      layers, and focal marks must be explained by legends, direct labels, or
      other explicit visible cues when they are not already self-labeled.
    - If a meaningful visible distinction lacks a legend or another explicit
      decoding aid, mark `self_explanatory` as `False` even if the chart is
      otherwise attractive and uncluttered.
    - Treat missing or ambiguous legends, unexplained color/style mappings,
      unexplained highlights, weak series identification, or other "the reader
      can probably figure it out" situations as failures of understandability.
    - Be strict about cramped layout even when nothing is literally clipped.
      If titles, legends, annotations, or plotting regions feel crowded or do
      not have enough padding and whitespace to read comfortably, mark
      `layout_balanced` as `False`.
    - Be strict about cropped, clipped, truncated, overlapped, or partly
      obscured text and marks. Do not give benefit of the doubt just because a
      reader could guess what the text says or infer the intended mapping.
    - If text is cut off, annotation boxes collide with marks, labels overlap,
      or the viewer would need effort to reconstruct the intended reading, mark
      the relevant booleans as `False`.
    - Keep `reasoning` and `feedback` crisp, concrete, and tied to requirement
      compliance, data operations, or execution quality.
    """

    vis: dspy.Image = dspy.InputField(desc="Rendered visualization image to inspect.")
    code: str = dspy.InputField(
        desc=(
            "Generated Python code for the chart. Use it to verify that "
            "requirements and required data operations are implemented "
            "explicitly rather than merely implied."
        )
    )
    query: str = dspy.InputField(
        desc="Original natural-language visualization request."
    )
    tablespec: str = dspy.InputField(
        desc=(
            "Serialized dataframe schema and samples. Use it to sanity-check "
            "column usage and requirement-bound data operations."
        )
    )
    requirements: list[str] = dspy.InputField(
        desc=(
            "Full generation requirements list. Use it to judge whether visible "
            "and non-visual requirements are explicitly implemented in the code "
            "and reflected in the chart when applicable."
        )
    )

    no_truncation: bool = dspy.OutputField(
        desc=(
            "True when titles, axes, ticks, legends, labels, annotations, and "
            "marks are not visibly clipped, cropped, or cut off by the canvas. "
            "Any cut-off or truncated text should make this `False`."
        )
    )
    no_overlap: bool = dspy.OutputField(
        desc=(
            "True when text, legends, annotations, and plotted marks do not "
            "collide or occlude each other enough to hurt reading. Any overlap "
            "that requires inference rather than easy reading should make this `False`."
        )
    )
    text_readable: bool = dspy.OutputField(
        desc=(
            "True when textual elements such as titles, axis labels, tick "
            "labels, legends, and annotations are readable at normal viewing size. "
            "If text is cramped, partly hidden, clipped, or hard to parse, make this `False`."
        )
    )
    data_readable: bool = dspy.OutputField(
        desc=(
            "True when the plotted data itself is visually decipherable: marks, "
            "lines, bars, points, and relevant distinctions are clear enough to read. "
            "If overlaps or occlusion materially hinder reading, make this `False`."
        )
    )
    layout_balanced: bool = dspy.OutputField(
        desc=(
            "True when figure size, padding, spacing, legend placement, title "
            "placement, and surrounding whitespace feel deliberate and roomy "
            "enough to read comfortably. If the chart feels cramped, crowded, "
            "or awkwardly packed even without literal clipping, make this `False`."
        )
    )
    data_operations_correct: bool = dspy.OutputField(
        desc=(
            "True when the code explicitly includes the filtering, grouping, "
            "aggregation, sorting, ranking, binning, reshaping, or derivations "
            "required by the query and requirements, and those operations align "
            "with the rendered chart. Missing or mismatched operations should "
            "make this `False`."
        )
    )
    self_explanatory: bool = dspy.OutputField(
        desc=(
            "True when a normal reader can understand what the important visual "
            "distinctions mean without guesswork because legends, direct labels, "
            "axis/context labels, or nearby annotations decode them clearly. "
            "Missing or ambiguous legends, unlabeled encodings, or unexplained "
            "highlights should make this `False`."
        )
    )
    implementation_acceptable: bool = dspy.OutputField(
        desc=(
            "True when the chart looks decently implemented overall, regardless "
            "of whether the design choice is good or bad, as long as it follows "
            "the requirements and does not add unprescribed visible design "
            "drift. If any core visual-quality boolean is `False`, if required "
            "data operations are wrong, or if the chart is not self-explanatory, "
            "this should also be `False`."
        )
    )
    requirements_followed: bool = dspy.OutputField(
        desc=(
            "True when every supplied requirement and guidance item is "
            "explicitly implemented in code and reflected in the chart when it "
            "should be visible. Implicit, partial, or approximate compliance "
            "should make this `False`."
        )
    )
    no_unprescribed_design: bool = dspy.OutputField(
        desc=(
            "True when the final chart does not introduce visible non-default, "
            "opinionated design decisions that were not prescribed by the query "
            "or requirements."
        )
    )
    requirement_trace: dict[str, str] = dspy.OutputField(
        desc=(
            "Dictionary keyed by guideline id or deterministic requirement key. "
            "Each value should briefly say whether that requirement was "
            "explicitly implemented, missed, or over-interpreted, with code "
            "evidence and visible evidence when applicable."
        )
    )
    reasoning: str = dspy.OutputField(
        desc=(
            "One or two short sentences summarizing requirement compliance, "
            "data-operation correctness, execution quality, and whether "
            "unprescribed visible design drift was detected."
        )
    )
    feedback: list[str] = dspy.OutputField(
        desc=(
            "Zero to three short actionable fixes for requirement, data-"
            "operation, or execution issues. Return an empty list if the "
            "implementation already looks clean and requirement-faithful."
        )
    )


__all__ = ["ReviewVisualizationImplementation", "WriteVisualizationCode"]

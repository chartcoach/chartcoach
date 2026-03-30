---
# PERMANENT ID: URL-friendly kebab-case.
id: "unique-guideline-slug"

# TITLE: Specific imperative instruction. State the portable principle at the design-lever level.
# Keep the title retrieval-stable and principle-level. Reserve concrete supported instances for `advice`, not the title,
# unless that named item is itself the supported finding.
title: "Use a precise action when the condition is met"

# METADATA
bibliography: references.bib

# DESCRIPTION: A structured summary capturing the guideline's logic.
# Keep the description retrieval-stable and principle-level. Let `advice` carry the concrete supported instances.
# Do not narrow a broader supported principle into a niche named recommendation here unless the source makes that narrow form the real finding.
# Use [use/prefer] and [improve/maximize] for constructive guidance.
# Use [avoid/minimize] and [prevent/mitigate] for proscriptive guidance.
description: "For [task/scope/time context], [use|prefer|avoid] [design lever] on [chart/structure/data context] to [improve|maximize|prevent] [quality target or risk] and [mitigate|address] [common mistakes] for [audience/literacy/situational context]."

# LABELS: High-signal key:value tags for filtering and retrieval.
# Treat labels as a sparse retrieval index, not a restatement of the whole guideline.
# Most guidelines should have 4-8 labels total; add more only when each extra label materially changes retrieval.
# Use only the taxonomy below. Never invent new categories or `custom:*` labels.
# By default, emit at most one value per category. Add multiple values only for explicit, inseparable contrasts.
# Only include a label when the source makes that condition materially relevant to applicability.
# Never backfill likely defaults from general datavis knowledge.
# Format: "category:value" (NEUTRAL) means "this rule applies under this condition."
# Format: "category:value:use" means "this rule recommends this choice."
# Format: "category:value:avoid" means "this rule warns against this choice."
labels:
  # REQUIRED CORE (Low-cardinality)
  # purpose: emit exactly one. Use `select` only for bounded chart-family or structure contrasts. Use `refine` for improving an already-chosen design, including encoding, annotation, palette, accessibility, and rhetoric moves inside that design.
  - "purpose:[select|refine]"
  # basis: emit exactly one conceptual evidence role. Use empirical for controlled findings, heuristic for practitioner/editorial rules, accessibility for inclusive-design criteria, rhetorical for framing/communication guidance.
  - "basis:[empirical|heuristic|accessibility|rhetorical]"
  # task: emit only if the rule materially changes with analytic intent. Do not emit just because the source mentions a task in passing.
  - "task:[retrieve|compare|distribute|trend|compose|relate|extreme][:use|:avoid]?"
  # scope: emit only if single-result vs record-list vs grouped-result changes applicability.
  - "scope:[single-result|record-list|grouped-result][:use|:avoid]?"
  # time: emit only when temporal structure is causal to the advice. Do not default `non-temporal`.
  - "time:[non-temporal|timepoint|ordered-time|cyclic-time|time-interval][:use|:avoid]?"
  # chart: emit only when chart family is the actual intervention target. For `select`, `:use` and `:avoid` must belong to the same decision contrast.
  - "chart:[bar|line|area|dotplot|scatter|histogram|box-violin|heatmap|pie-donut|map|choropleth|table|treemap|network|parallel|timeline|candlestick|funnel|gauge|radar|sankey|word-cloud|text][:use|:avoid]?"
  # structure: emit only when layout arrangement is the manipulated object of the rule.
  - "structure:[single-view|multi-view|small-multiples|dashboard][:use|:avoid]?"
  # data: emit only when data modality materially gates the rule.
  - "data:[quantitative|categorical|ordinal|temporal|geospatial|hierarchical|network|text|tabular][:use|:avoid]?"
  # quality: emit one primary intended outcome the rule optimizes.
  - "quality:[fidelity|readability|insight|aesthetics|accessibility|trust][:use|:avoid]?"

  # DECISION / APPLICABILITY EXTENSIONS
  # lever: emit exactly one primary design object being changed.
  - "lever:[chart-family|encoding|scale-order|layout-structure|text-annotation|interaction-access]"
  # operator: emit only when a specific readout or comparison mode is essential to the rule.
  - "operator:[lookup|rank|difference|part-whole|association|distribution|uncertainty]"
  # reading-mode: emit only when overview vs lookup vs exact reading materially changes the advice.
  - "reading-mode:[overview|lookup|exact]"
  # density: emit only when sparse vs dense displays materially change the rule.
  - "density:[sparse|dense]"
  # measure: emit only when single vs multi-measure structure changes the advice.
  - "measure:[single|multi]"
  # group-cardinality: emit only when binary/few/many grouping materially changes the choice.
  - "group-cardinality:[binary|few|many]"
  # shape: emit only when skew or outlier structure is essential.
  - "shape:[skewed|outlier-rich]"
  # temporal-pattern: emit only when dynamic temporal behavior is essential.
  - "temporal-pattern:[dynamic]"

  # RHETORIC / POLISH EXTENSIONS
  # communication: emit only when the rule is about framing, context, credibility, resonance, or workflow rather than the base chart choice itself.
  - "communication:[framing|context|credibility|resonance|workflow]"
  # polish: emit only when the rule is a cross-grammar finishing move that makes charts visibly better.
  - "polish:[declutter|hierarchy|spacing|palette|annotation|focus|consistency]"
  # aesthetic: emit only when visible style, composition, or color treatment is the core lever.
  - "aesthetic:[style|composition|color][:use|avoid]?"
  # channel: emit only when a visual encoding channel is the manipulated object.
  - "channel:[position|length|angle|area|color-hue|color-lightness|color-saturation|shape|texture|line-style|opacity|orientation|text][:use|:avoid]?"
  # component: emit only when a chart component is the manipulated object.
  - "component:[axis|legend|label|annotation|title|caption|tooltip][:use|:avoid]?"

  # AUDIENCE / ACCESS EXTENSIONS
  # knowledge: emit only when reader capability level materially changes applicability.
  - "knowledge:[low|mixed|high]"
  # literacy: emit only when chart literacy explicitly changes applicability.
  - "literacy:[novice|general|expert]"
  # audience: emit only when reader type is explicit and causal.
  - "audience:[general-public|domain-expert|analyst|decision-maker|designer|reviewer]"
  # needs: emit only when accessibility or knowledge needs are causal to the rule.
  - "needs:[low-vision|screen-reader|color-vision-deficiency|keyboard-only|motor|cognitive|low-domain-knowledge]"
  # access: emit only when accessibility treatment is the direct intervention.
  - "access:[contrast|noncolor|screen-reader|keyboard|reflow|zoom|plain-language|motion-safe][:use|:avoid]?"
---

<!--
STRICT CONTRACT
- This document records one directly actionable visualization guideline.
- The language is clear, direct, precise, and accessible. It avoids fluff, hype, academic padding, and narrative source attribution.
- Source faithfulness is strict. Every claim, condition, label, exception, check, fix, and example must be explicitly discussed in the processed source or be a minimal operational rewrite of it.
- `title` and `description` are the portable retrieval surfaces. Keep them principle-level whenever the source supports a broader rule.
- `advice` is the operational generation surface. It starts with the portable rule, then immediately grounds that rule in 1-3 concrete source-faithful instances.
- Named exemplars, tools, palettes, devices, platforms, or domain-specific artifacts stay out of `title` and `description` unless they are themselves the supported finding. `advice` may name supported concrete instances when that is necessary to make the rule directly actionable.
- Concrete instances in `advice` should stay portable. Abstract away source-specific domain nouns, row labels, one-off measures, literal question text, and scenario details unless that specificity is itself the supported finding.
- `advice` must not stop at broad adjectives such as `familiar`, `basic`, `clear`, `readable`, `simple`, or `appropriate` without also naming the manipulated design lever and at least one concrete action or contrast.
- Each guideline advocates one well-defined principle or one bounded contrast. Do not mix multiple acceptable alternatives into the same guideline.
- If X is appropriate in one condition and Y is appropriate in another, emit separate guidelines with separate contexts rather than one `use X or Y` rule.
- Prefer omission to hallucinated specificity, generic cleanup advice, or plausible-but-unsupported applicability.
- Each section is semantically pure, self-contained, and efficient for embedding. The first sentence names the concrete chart element, encoding, task, audience, or constraint directly.
- The same design lever is named with the same words across sections. Decorative synonyms and pronoun-only openings are avoided.
- Each sentence carries one main idea. Stacked caveats and abstract framing are kept out of the section body.
- Citekeys appear only in the reason section, only inside **Evidence:**, and each citekey appears at most once within that section.
- Advice and mistakes use mirrored vocabulary when they address the same design lever. Context and exceptions describe the same situation space from different sides. Fixes remain concrete enough to compare against mistakes and alternative fixes.
- Every emitted guideline includes exactly one purpose label: "purpose:select" (choice between chart families or structural arrangements) or "purpose:refine" (improvement of a chosen chart type or chosen structure).
- Every emitted guideline includes exactly one basis label describing the conceptual role of the evidence: empirical, heuristic, accessibility, or rhetorical.
- Directional guidance uses a tripartite "category:value:polarity" format.
    1. Polarity is ":use" if the guideline explicitly RECOMMENDS or PROMOTES a choice.
    2. Polarity is ":avoid" if the guideline explicitly WARNS AGAINST or DISCOURAGES a choice.
    3. NO polarity (Neutral) is used if the label represents a CONTEXTUAL CONDITION (e.g., "task:compare" means "this guideline applies when the user wants to compare").
- Guidelines with "purpose:select" MUST include at least one ":use" label and at least one ":avoid" label for the relevant chart or structure contrast to clarify the recommended design choice.
- Guidelines with "purpose:select" MUST encode one bounded contrast. Recommend one option against one alternative in the same family; do not bundle several acceptable choices into the same rule. If the rule cannot state when to use X instead of Y, it should be emitted as `refine` or omitted.
- Encoding, channel, component, palette, caption, annotation, accessibility, and framing choices belong to `purpose:refine` even when they contrast alternatives.
- Guidelines with "purpose:refine" primarily use neutral contextual labels and ":use" labels for the specific components or channels being polished.
- Labels are a sparse retrieval index rather than a restatement of the whole guideline.
- Most guidelines carry 4-8 labels total. Prefer omission to a weak, generic, or speculative label.
- Use only the declared taxonomy below. Never invent freeform categories such as `custom:*`.
- By default, use at most one label per category. Multiple labels in one category require an explicit contrast or an inseparable multi-condition rule.
- Contextual labels appear only when they materially narrow applicability. Broad defaults and exhaustive chart/data/task lists are omitted.
- Emit profile-facing labels (`density`, `measure`, `group-cardinality`, `shape`, `temporal-pattern`, `reading-mode`, `operator`, `lever`) only when the source makes that condition explicit enough to guide retrieval.
- `communication` and `polish` are orthogonal lanes: use them only for framing/communication or cross-grammar finishing guidance, not as broad style decoration.
- When advice applies across many charts, encode the shared lever (component, channel, quality, access, or audience need) instead of enumerating many chart families.
- `context`, `exceptions`, `check`, `fix`, and labels may include only conditions and actions that the source actually supports. Do not fill missing sections with generic datavis defaults.
- The generated output retains only the role comments after headings; all other comments are omitted.
-->

## [Portable advice heading naming the design move] <!-- role: advice -->

<!--
Section form:
- The heading is short, portable, and design-lever focused.
- The heading names the action or manipulated object, not the exact source scenario, domain entity, row label, or literal question text.
- The heading should read like a reusable control label for downstream generation, not like a source-specific note.
- Two short imperative sentences.
- The first sentence names one controllable design lever directly and states the portable principle.
- The second sentence gives 1-3 inline concrete source-faithful instances, preferably introduced with `For example, ...`.
- Concrete instances name chart families, components, annotations, labels, layout changes, or other explicit design actions, not only broad quality words.
- Keep the concrete example portable. Name the design role, comparison, summary field, annotation, or structural move, not the exact source scenario, domain entity, or literal question text unless that specificity is itself the finding.
- For `purpose:select`, name at least one supported `use` option and one supported `avoid` option when the evidence supports a contrast.
- For `purpose:refine`, name at least one explicit manipulated object such as the axis, legend, label, annotation, title, caption, baseline, order, palette, mark size, or spacing.
- Do not pad the advice with unsupported canonical option lists or generic chart inventories.
- Do not hedge with unresolved `or` choices between alternative chart types, components, or actions. If the alternatives require different contexts, they belong in separate guidelines.
- The structure is action + object + condition or goal.
- Multi-part recommendations appear only when the parts are inseparable steps of one action, not alternative branches.
- No rationale.
- No citations.
- No lists.
-->

[Portable advice heading plus two short imperative sentences: first the portable principle, then an inline concrete `For example, ...` sentence naming 1-3 supported portable actions.]

## [Specific evidence heading about why X works] <!-- role: reason -->

<!--
Section form:
- One short mechanism paragraph.
- One **Mechanism:** field.
- One **Evidence:** field.
- One optional **Notes:** field.
- Concrete reader, task, or interpretation language rather than abstract scientific phrasing.
- Direct claims rather than source-attribution phrasing.
- Citekeys only at the end of **Evidence:** sentences.
-->

[One short paragraph explaining the mechanism in concrete terms.]

**Mechanism:** [What changes in reading, comparison, interpretation, or workflow when the advice is followed?]

**Evidence:** [1-2 short evidence sentences with citekeys at the end, e.g. "... [@key1; @key2]".]

**Notes:** [Optional nuance that is not context, exception, or fix.]

## [Specific context heading for where X applies] <!-- role: context -->

<!--
Section form:
- Keyed bullets only.
- Retrieval-oriented situation cues.
- Observable conditions rather than abstract intent alone.
- Include only conditions that are explicitly supported by the source.
- The same dimension names are reused across guidelines when possible.
- No citations.
-->

- **User Goal:** [Decision, comparison, explanation, recall, monitoring, etc.]
- **Task:** [Optional analytic or communicative task.]
- **Data:** [Type, structure, density, uncertainty, missingness.]
- **Chart Setting:** [Medium, constraints, interaction, layout, annotation.]
- **Audience:** [Who is reading, including domain literacy or accessibility needs.]
- **Success Criterion:** [What counts as good: accuracy, speed, trust, accessibility, recall, etc.]

## [Specific exception heading for when X fails] <!-- role: exceptions -->

<!--
Section form:
- One sentence when there is one exception.
- Bullets only when there are several exceptions.
- Each item includes **Break it when:** and **Why:**.
- The wording reuses the same situation dimensions named in `context` when possible.
- Do not invent boundary conditions to make the section look complete. Omit the guideline instead if no real source-supported boundary exists.
- No citations.
-->

**Break it when:** [Describe the boundary condition in the same situation space used in context.] **Why:** [Explain why the rule fails here.]

## [Specific tradeoff heading for the costs of X] <!-- role: costs -->

<!--
Section form:
- 2-4 short labeled sentences.
- The tradeoff stays tied to the same design lever named in `advice`.
- No citations.
-->

**Sacrifice:** [What you give up.]
**Risk:** [What can go wrong if applied blindly.]
**Mitigation:** [Optional: how to reduce the risk without restating the rule.]

## [Specific mistake heading for common failure modes around X] <!-- role: mistakes -->

<!--
Section form:
- One sentence when there is one mistake.
- Bullets only when there are several mistakes.
- Each item includes **Mistake:** and **Why it fails:**.
- The mistake names the same design lever vocabulary used in `advice` when possible.
- The failure is described in direct operational terms, not broad moral judgment.
- No citations.
-->

**Mistake:** [Common failure mode on the same design lever.] **Why it fails:** [Why it does not solve the problem in practice.]

## [Specific check heading for how to test X] <!-- role: check -->

<!--
Section form:
- 2-4 short labeled sentences.
- Runnable by a reviewer or a simple script.
- Observable and concrete enough to support comparison across guidelines.
- Keep checks source-faithful. Do not add generic QA procedures that the source does not support.
- No citations.
-->

**Failure Sign:** [What the problem looks like.]
**Quick Check:** [Fast heuristic.]
**Stronger Test:** [Optional: more reliable validation.]

## [Specific fix heading for what to change] <!-- role: fix -->

<!--
Section form:
- 2-4 imperative bullets.
- Each bullet is a distinct edit operation.
- The edits stay concrete enough to compare fixes across related guidelines.
- Only include edits that the source supports directly or as a minimal operational rewrite.
- No citations.
-->

- [A small change that addresses the failure mode.]
- [A different change that avoids the failure mode.]
- [A structural change if the current form cannot support the task.]
- [Optional: a constraint-aware fallback.]

---
# PERMANENT ID: URL-friendly kebab-case.
id: "unique-guideline-slug"

# TITLE: Specific imperative instruction. Name the design lever and condition plainly.
title: "Use a precise action when the condition is met"

# METADATA
bibliography: references.bib

# DESCRIPTION: A structured summary capturing the guideline's logic.
# Use [use/prefer] and [improve/maximize] for constructive guidance.
# Use [avoid/minimize] and [prevent/mitigate] for proscriptive guidance.
description: "For [task/scope/time context], [use|prefer|avoid] [design lever] on [chart/structure/data context] to [improve|maximize|prevent] [quality target or risk] and [mitigate|address] [common mistakes] for [audience/literacy/situational context]."

# LABELS: High-signal key:value tags for filtering and retrieval.
# Treat labels as a sparse retrieval index, not a full summary of the guideline.
# Most guidelines should have 4-8 labels total; include more only when each extra label materially changes retrieval.
# Use only the taxonomy below. Do not invent new categories or `custom:*` labels.
# By default, emit at most one label per category. Add multiple values only for explicit contrasts or inseparable multi-condition guidance.
# Only include contextual labels when they materially narrow applicability. Omit generic defaults and broad chart/data/task enumerations.
# Format: "category:value" (NEUTRAL) indicates the guideline applies when this condition is true.
# Format: "category:value:use" (PRESCRIPTIVE) indicates the guideline recommends this choice.
# Format: "category:value:avoid" (PROSCRIPTIVE) indicates the guideline warns against this choice.
labels:
  # REQUIRED CORE (Low-cardinality)
  - "purpose:[select|refine]"
  - "task:[retrieve|compare|distribute|trend|compose|relate|extreme][:use|:avoid]?"
  - "scope:[single-result|record-list|grouped-result][:use|:avoid]?"
  - "time:[non-temporal|timepoint|ordered-time|cyclic-time|time-interval][:use|:avoid]?"
  - "chart:[bar|line|area|dotplot|scatter|histogram|box-violin|heatmap|pie-donut|map|choropleth|table|treemap|network|parallel|timeline|candlestick|funnel|gauge|radar|sankey|word-cloud|text][:use|:avoid]?"
  - "structure:[single-view|multi-view|small-multiples|dashboard][:use|:avoid]?"
  - "data:[quantitative|categorical|ordinal|temporal|geospatial|hierarchical|network|text|tabular][:use|:avoid]?"
  - "quality:[fidelity|readability|insight|aesthetics|accessibility|trust][:use|:avoid]?"

  # RECOMMENDED EXTENSIONS (Use for specific design levers)
  - "aesthetic:[style|composition|color][:use|avoid]?"
  - "channel:[position|length|angle|area|color-hue|color-lightness|color-saturation|shape|texture|line-style|opacity|orientation|text][:use|:avoid]?"
  - "component:[axis|legend|label|annotation|title|caption|tooltip][:use|:avoid]?"
  - "literacy:[novice|general|expert]"
  - "audience:[general-public|domain-expert|analyst|decision-maker|designer|reviewer]"
  - "needs:[low-vision|screen-reader|color-vision-deficiency|keyboard-only|motor|cognitive|low-domain-knowledge]"
  - "access:[contrast|noncolor|screen-reader|keyboard|reflow|zoom|plain-language|motion-safe][:use|:avoid]?"
---

<!--
STRICT CONTRACT
- This document records one directly actionable visualization guideline.
- The language is clear, direct, precise, and accessible. It avoids fluff, hype, academic padding, and narrative source attribution.
- Each section is semantically pure, self-contained, and efficient for embedding. The first sentence names the concrete chart element, encoding, task, audience, or constraint directly.
- The same design lever is named with the same words across sections. Decorative synonyms and pronoun-only openings are avoided.
- Each sentence carries one main idea. Stacked caveats and abstract framing are kept out of the section body.
- Citekeys appear only in the reason section, only inside **Evidence:**, and each citekey appears at most once within that section.
- Advice and mistakes use mirrored vocabulary when they address the same design lever. Context and exceptions describe the same situation space from different sides. Fixes remain concrete enough to compare against mistakes and alternative fixes.
- Every emitted guideline includes exactly one purpose label: "purpose:select" (choice between chart families) or "purpose:refine" (improvement of a chosen chart type).
- Directional guidance uses a tripartite "category:value:polarity" format.
    1. Polarity is ":use" if the guideline explicitly RECOMMENDS or PROMOTES a choice.
    2. Polarity is ":avoid" if the guideline explicitly WARNS AGAINST or DISCOURAGES a choice.
    3. NO polarity (Neutral) is used if the label represents a CONTEXTUAL CONDITION (e.g., "task:compare" means "this guideline applies when the user wants to compare").
- Guidelines with "purpose:select" MUST include at least one ":use" label and at least one ":avoid" label for the relevant chart families or encodings to clarify the recommended design choice.
- Guidelines with "purpose:refine" primarily use neutral contextual labels and ":use" labels for the specific components or channels being polished.
- Labels are a sparse retrieval index rather than a restatement of the whole guideline.
- Most guidelines carry 4-8 labels total. Prefer omission to a weak, generic, or speculative label.
- Use only the declared taxonomy below. Never invent freeform categories such as `custom:*`.
- By default, use at most one label per category. Multiple labels in one category require an explicit contrast or an inseparable multi-condition rule.
- Contextual labels appear only when they materially narrow applicability. Broad defaults and exhaustive chart/data/task lists are omitted.
- When advice applies across many charts, encode the shared lever (component, channel, quality, access, or audience need) instead of enumerating many chart families.
- The generated output retains only the role comments after headings; all other comments are omitted.
-->

## [Specific advice heading about X] <!-- role: advice -->

<!--
Section form:
- 1-2 imperative sentences.
- The first sentence names one controllable design lever directly.
- The structure is action + object + condition or goal.
- Multi-part recommendations appear only when the parts are inseparable.
- No rationale.
- No citations.
- No lists.
-->

[1-2 imperative sentences naming one concrete design move.]

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
- No citations.
-->

- [A small change that addresses the failure mode.]
- [A different change that avoids the failure mode.]
- [A structural change if the current form cannot support the task.]
- [Optional: a constraint-aware fallback.]

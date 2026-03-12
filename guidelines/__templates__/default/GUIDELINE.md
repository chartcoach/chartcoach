---
# PERMANENT ID: URL-friendly kebab-case.
id: "unique-guideline-slug"

# TITLE: Specific imperative instruction. Name the design lever and condition plainly.
title: "Use a precise action when the condition is met"

# METADATA
bibliography: references.bib
description: "One-sentence summary for retrieval, ranking, and disambiguation."

# LABELS: High-signal key:value tags for filtering and retrieval.
labels:
  - "chart:[type]"
  - "task:[action]"
  - "visual:[channel]"
  - "impact:[goal]"
  - "data:[type]"
  - "audience:[group]"
  - "workflow:[create|feedback|rework]"
  - "[custom]:[value]"
---

<!--
STRICT CONTRACT
- This document records one directly actionable visualization guideline.
- The language is clear, direct, precise, and accessible. It avoids fluff, hype, academic padding, and narrative source attribution.
- Technical terms appear only when they add meaning. When a technical term is needed, it is used plainly and consistently.
- Each section is semantically pure, self-contained, and efficient for embedding. The first sentence names the concrete chart element, encoding, task, audience, or constraint directly.
- The same design lever is named with the same words across sections. Decorative synonyms and pronoun-only openings are avoided.
- Each sentence carries one main idea. Stacked caveats and abstract framing are kept out of the section body.
- The H2 titles are content-specific and name the actual concept rather than generic placeholders such as "Rule" or "Logic".
- Citekeys appear only in the reason section, only inside **Evidence:**, and each citekey appears at most once within that section.
- If one source supports multiple points, those points are synthesized into one evidence span and cited once.
- All non-reason sections contain zero citekeys.
- Advice and mistakes use mirrored vocabulary when they address the same design lever. Context and exceptions describe the same situation space from different sides. Fixes remain concrete enough to compare against mistakes and alternative fixes.
- The label set includes at least one workflow label when the guideline is generated for create, feedback, or rework retrieval.
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

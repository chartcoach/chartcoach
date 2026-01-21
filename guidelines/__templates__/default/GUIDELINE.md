---
# PERMANENT ID: URL-friendly kebab-case.
id: "unique-guideline-slug"

# TITLE: A highly specific, imperative command (include the condition if needed).
# Avoid vague titles like "Use Color Carefully". Prefer "Use a diverging palette only for signed data (with a meaningful zero)".
title: "Strong Action Verb Object (With Condition)"

# METADATA:
bibliography: references.bib
description: "A single-sentence summary for search results."

# LABELS: DISCOVERY & FILTERING
# Use the standard categories below to ensure your guideline is found in common searches.
# You are also free to add CUSTOM tags for your specific domain (e.g., tool:tableau, industry:finance).
labels:
  - "chart:[type]" # e.g., chart:bar, chart:scatter
  - "task:[action]" # e.g., task:compare, task:rank
  - "visual:[channel]" # e.g., visual:color, visual:position
  - "impact:[goal]" # e.g., impact:clarity, impact:accessibility
  - "data:[type]" # e.g., data:temporal, data:categorical
  - "audience:[group]" # e.g., audience:novice, audience:expert
  - "[custom]:[value]" # e.g., complexity:advanced, source:internal-policy
---

<!--
  AUTHORING TIP: MAKE IT ACCESSIBLE + MAKE IT SEPARABLE

  Accessibility (baseline)
  - Write so a reader can understand it without seeing a figure: avoid "above/below/left/right" references.
  - Prefer plain language, short sentences, and concrete terms; define jargon.
  - Use consistent terminology (same concept, same words) so retrieval works.

  Abbreviations / acronyms (body text)
  - On first use in the BODY, expand each abbreviation once: "Full Term (ABBR)". Use ABBR after.
  - It's fine to use ABBR in the title/slug/labels, but do not assume readers know it in the body.

  Citations / citekeys ([@...])
  - INCLUDE citekeys for traceability, but do not sprinkle them throughout the guideline.
  - Prefer putting citekeys ONLY in the Logic section under **Evidence:**.
  - If a non-Logic section truly needs a citekey (rare), move that claim into Logic instead.

  Section titles (for the static site TOC)
  - Do NOT leave headings as "The Rule", "The Logic", etc.
  - Rename every H2 heading to be content-specific (include the key concept from the title).
  - Keep the role annotation exactly: `<!-- role: ... -->`.

Role purity (semantic separation)
To make this useful for AI, keep each section pure.

- Don't put "Why" in the "Advice" section.
- Don't put "Exceptions" in the "Context" section.
- Trust the structure.
  -->

## [Rule: Specific, content-based heading] <!-- role: advice -->

<!--
  GOAL: A delightful, scannable command that embeds cleanly.

  FORMAT
  - Start with a single imperative sentence (no rationale, no citations).
  - Then add 2–4 keyed bullets (Do / Avoid / Prefer / Threshold).
  - Keep it specific enough to act on without reading the rest.

  DON'T
  - Explain "why" (belongs in The Logic).
  - List edge cases (belongs in When to Break It).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

State the rule clearly and immediately.

- **Do:** [The recommended action.]
- **Avoid:** [The common alternative to avoid.]
- **Prefer:** [Optional: a ranked preference among options.]
- **Threshold:** [Optional: a simple cutoff like “≥ 20 series”, “≤ 3 categories”, etc.]

## [Logic: Why this works here] <!-- role: reason -->

<!--
  GOAL: Explain the mechanism without leaking advice/context.

  FORMAT
  - 1 short paragraph describing the mechanism.
  - Then 2–3 keyed bullets: Mechanism / Evidence / Notes.

  DON'T
  - Repeat the rule verbatim.
  - Introduce new conditions (belongs in Where to Apply / When to Break It).
-->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **Mechanism:** [What changes in perception/interpretation when the rule is followed?]
- **Evidence:** [@citationKey] [Optional: effect direction + condition name.]
- **Notes:** [Optional: clarifying nuance that is not an exception.]

## [Context: When this applies] <!-- role: context -->

<!--
  GOAL: Define the triggering situation as a schema.

  FORMAT
  - No prose-only paragraphs. Use keyed bullets so this section embeds as "situation" not "argument".
  - Prefer observable signals (about the data/task/chart) over intentions.

  DON'T
  - Explain why the rule works (belongs in The Logic).
  - List break-glass edge cases (belongs in When to Break It).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

- **User Goal:** [What is the user trying to do/decide?]
- **Task:** [Optional: the specific analytic task or judgment.]
- **Data:** [Type, shape, cardinality, density, uncertainty, missingness.]
- **Chart Setting:** [Medium, constraints, interaction, annotation, layout.]
- **Audience:** [Who is reading; domain literacy; accessibility needs.]
- **Success Criterion:** [What “good” means: accuracy, speed, trust, accessibility, etc.]

## [Exceptions: When not to follow it] <!-- role: exceptions -->

<!--
  GOAL: Provide crisp, itemized exceptions that can be compared across guidelines.

  FORMAT
  - Use numbered items.
  - Each item must be self-contained and have exactly: Break when / Why.

  DON'T
  - Provide the full alternative solution (belongs in How to Fix).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

List the specific scenarios where you should ignore this rule.

1. **Break it when:** [Describe the situation.]
   - **Why:** [Why the rule fails here.]

## [Costs: Tradeoffs and risks] <!-- role: costs -->

<!--
  GOAL: Make tradeoffs explicit without introducing new advice.

  FORMAT
  - 2–4 keyed bullets.

  DON'T
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

Be honest about the downsides.

- **Sacrifice:** [What you give up: space, time, complexity, flexibility.]
- **Risk:** [What can go wrong if applied blindly.]
- **Mitigation:** [Optional: a non-prescriptive way to reduce the risk.]

## [Mistakes: Common failure modes] <!-- role: mistakes -->

<!--
  GOAL: Capture anti-patterns as atomic, comparable units.

  FORMAT
  - Use numbered items.
  - Each item must have exactly: Mistake / Why it fails.

  DON'T
  - Put the proper fix here (belongs in How to Fix).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

1. **Mistake:** [Common bad practice.]
   - **Why it fails:** [Brief explanation.]

## [Check: Quick tests] <!-- role: check -->

<!--
  GOAL: Provide a quick heuristic and a stronger test.

  FORMAT
  - 2–4 keyed bullets.
  - The check should be runnable by a person (or a simple script) without extra context.

  DON'T
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

- **Failure Sign:** [What the problem looks like.]
- **Quick Check:** [A fast heuristic.]
- **Stronger Test:** [Optional: a more reliable test, e.g., small user pilot, A/B.]

## [Fix: What to do instead] <!-- role: fix -->

<!--
  GOAL: Actionable, ordered fixes.

  FORMAT
  - 2–5 keyed bullets, ordered from easiest → best.
  - Each bullet should be a single action a practitioner can take.

  DON'T
  - Re-explain the rule or justify the fix (belongs in The Logic).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

- **Minimal Fix:** [The smallest change that resolves the failure.]
- **Better Fix:** [A more robust change.]
- **Best Fix:** [The ideal solution, even if it changes chart type/workflow.]
- **If You Can't:** [Optional: what to prioritize when constraints block the best fix.]

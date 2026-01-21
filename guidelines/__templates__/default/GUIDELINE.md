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
  - "[custom]:[value]" # e.g., complexity:advanced, tool:tableau, industry:finance
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

  List formatting
  - Never use numbered lists anywhere in the guideline. Use bullets only.
  - Prefer short paragraphs over bullets unless list structure improves comparability (Context, Exceptions, Mistakes, Fix).

  Lint checklist (quick)
  - Advice section is 1–2 sentences, with no lists and no citekeys.
  - Citekeys ([@...]) appear only in Logic → **Evidence:**.
  - Exceptions and Mistakes use single-line items with: “Break it when … Why …” / “Mistake … Why it fails …” (use bullets only if you have multiple items).
  - Every H2 title is content-specific (do not leave bracket placeholders or generic headings).

  Citations / citekeys ([@...])
  - In the body, do not sprinkle citekeys throughout the guideline.
  - Prefer putting all in-body citekeys ONLY in the Logic section under **Evidence:**.
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
  - Optionally add ONE short clarifying sentence (still no rationale, no citations).
  - Do not use lists here (no bullets, no numbering).
  - Keep it specific enough to act on without reading the rest.

  EXAMPLE (turn checklist-y guidance into text)
  Bad: "Use X. Don't use Y. Choose Z. Apply cutoff T."
  Good: "Use X when Y. If T, switch to Z instead."

  DON'T
  - Explain "why" (belongs in The Logic).
  - List edge cases (belongs in When to Break It).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

[Write the rule here in 1–2 sentences.]

## [Logic: Why this works here] <!-- role: reason -->

<!--
  GOAL: Explain the mechanism without leaking advice/context.

  FORMAT
  - 1 short paragraph describing the mechanism.
  - Then 1–3 short labeled paragraphs: **Mechanism:** / **Evidence:** / **Notes:**.
  - Evidence is 1–2 short sentences: summarize the key result and, if known, name the study type or source (experiment, observational study, review, standard, blog, internal memo).
  - End each Evidence sentence with one or more citekeys like `[@key1; @key2]` (multiple citekeys are common).

  DON'T
  - Repeat the rule verbatim.
  - Introduce new conditions (belongs in Where to Apply / When to Break It).
  - Write placeholders like "(No linked studies provided.)"; add a source to `references.bib` instead (paper, standard, blog, or internal memo).
-->

Explain the principle at work here. Connect the rule to human perception or clear communication.

**Mechanism:** [What changes in perception/interpretation when the rule is followed?]

**Evidence:** [Write 1–2 sentences and end each with citekeys, e.g., "In Experiment 1, viewers were faster/more accurate under condition X than Y [@key1]. A review reports the same direction across related tasks [@key2]."]

**Notes:** [Optional: clarifying nuance that is not an exception.]

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
  - If there is only ONE exception, write it as a single sentence (no list).
  - If there are multiple exceptions, use bullets (not numbered lists).
  - Each item must be self-contained and include exactly: Break it when / Why.

  DON'T
  - Provide the full alternative solution (belongs in How to Fix).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

List the specific scenarios where you should ignore this rule.

**Break it when:** [Describe the situation.] **Why:** [Why the rule fails here.]

## [Costs: Tradeoffs and risks] <!-- role: costs -->

<!--
  GOAL: Make tradeoffs explicit without introducing new advice.

  FORMAT
  - 2–4 short sentences (no lists).
  - Prefer labeled sentences: **Sacrifice:** … **Risk:** … **Mitigation:** …

  DON'T
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

Be honest about the downsides.

**Sacrifice:** [What you give up: space, time, complexity, flexibility.]
**Risk:** [What can go wrong if applied blindly.]
**Mitigation:** [Optional: a non-prescriptive way to reduce the risk.]

## [Mistakes: Common failure modes] <!-- role: mistakes -->

<!--
  GOAL: Capture anti-patterns as atomic, comparable units.

  FORMAT
  - If there is only ONE mistake, write it as a single sentence (no list).
  - If there are multiple mistakes, use bullets (not numbered lists).
  - Each item must have exactly: Mistake / Why it fails.

  DON'T
  - Put the proper fix here (belongs in How to Fix).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

**Mistake:** [Common bad practice.] **Why it fails:** [Brief explanation.]

## [Check: Quick tests] <!-- role: check -->

<!--
  GOAL: Provide a quick heuristic and a stronger test.

  FORMAT
  - 2–4 short sentences (no lists).
  - The check should be runnable by a person (or a simple script) without extra context.
  - Prefer labeled sentences: **Failure Sign:** … **Quick Check:** … **Stronger Test:** …

  DON'T
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

**Failure Sign:** [What the problem looks like.]
**Quick Check:** [A fast heuristic.]
**Stronger Test:** [Optional: a more reliable test, e.g., small user pilot, A/B.]

## [Fix: What to do instead] <!-- role: fix -->

<!--
  GOAL: Actionable alternatives.

  FORMAT
  - 2–4 bullets (not numbered), each a distinct action a practitioner can take.
  - Write each bullet as a complete imperative sentence.
  - Avoid tier ladders ("minimal/better/best") and avoid near-duplicates that only differ by intensity.

  DON'T
  - Re-explain the rule or justify the fix (belongs in The Logic).
  - Add citekeys here (keep citekeys in Logic → Evidence).
-->

- [A small change that addresses the failure mode.]
- [A different approach that avoids the failure mode (e.g., change encoding, layout, annotation strategy, or interaction).]
- [A structural change if the current form cannot support the task (e.g., switch chart type/workflow).]
- [Optional: a constraint-aware fallback that preserves the core intent.]

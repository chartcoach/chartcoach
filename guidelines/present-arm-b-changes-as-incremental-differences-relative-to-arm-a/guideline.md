---
id: present-arm-b-changes-as-incremental-differences-relative-to-arm-a
title: Present Arm B outcomes as incremental differences relative to Arm A
bibliography: references.bib
description: Show the change from the baseline arm to clarify comparative differences
  in risks and benefits.
labels:
- chart:pictograph
- task:compare
- visual:annotation
- impact:comprehension
- data:probabilistic
- audience:novice
- domain:health
---

## Show incremental differences for the comparison arm <!-- role: advice -->

When comparing two arms, present Arm A as absolute frequencies and present Arm B as the incremental increase or decrease relative to Arm A. Highlight the changed portion so the reader can see the baseline and the delta at the same time.

## Why incremental presentation supports comparisons <!-- role: reason -->

Presenting the comparison as a delta focuses attention on what changes between options rather than requiring readers to subtract two absolute frequencies on their own, which can be error-prone in comparative risk/benefit tasks.

**Mechanism:** A baseline-plus-change representation reduces the need for mental subtraction and makes the direction and magnitude of differences more immediately interpretable.

**Evidence:** The study used absolute frequencies for Drug A and incremental differences for Drug B across text, tables, and pictographs to communicate comparative risks/benefits in a randomized design, and comprehension outcomes were measured using gist and verbatim questions aligned with both absolute and incremental information [@taitEffectFormatParents2010]. In that context, pictographs (which visually highlighted the incremental change) produced higher gist and verbatim understanding than text or tables [@taitEffectFormatParents2010].

**Notes:** This guideline captures the comparative framing used in the tested materials; the paper’s primary tested contrast was format (text vs table vs pictograph) under this incremental scheme.

## When incremental differences apply <!-- role: context -->

- **User Goal:** Judge how a new option changes risks and benefits versus a standard option.
- **Task:** Detect direction (more/less) and magnitude (how many more/fewer) of changes.
- **Data:** Two-option comparisons where one option serves as a natural baseline.
- **Chart Setting:** Side-by-side or sequential presentation where both baseline and change can be shown together.
- **Audience:** Lay readers who may struggle with arithmetic comparisons.
- **Success Criterion:** Readers can answer both “how many total” and “how many more/fewer” questions with fewer errors.

## When not to use incremental-only for the comparison arm <!-- role: exceptions -->

**Break it when:** Users must know the comparison arm’s absolute totals and you cannot provide a way to recover them from the display. **Why:** Incremental-only presentation can make the absolute level of the comparison option less directly accessible.

## Tradeoffs of incremental presentation <!-- role: costs -->

**Sacrifice:** Requires careful labeling and visual highlighting to prevent confusion about what is absolute versus incremental. **Risk:** Readers may misinterpret the delta as the total if cues are weak. **Mitigation:** Validate with verbatim questions that include both totals and differences.

## Common incremental framing mistakes <!-- role: mistakes -->

**Mistake:** Showing a delta for Arm B without keeping the Arm A baseline visible in the same view. **Why it fails:** Readers lose the reference and must reconstruct the comparison from memory, undermining the intent of incremental framing.

## Quick checks for incremental clarity <!-- role: check -->

**Failure Sign:** Readers answer “how many in Arm B” with the delta value rather than the total. **Quick Check:** Ask one verbatim question for Arm B total and one for the Arm B vs Arm A difference while the display is visible. **Stronger Test:** Compare correct-response rates on difference questions with and without the baseline-plus-delta display in a pilot.

## What to do instead if incremental display is too confusing <!-- role: fix -->

- Present both arms as absolute frequencies and add an explicit “difference” line beneath each outcome.
- Keep the absolute totals in a table and use a small visual marker to indicate direction of change (more/fewer).
- Split the content into two panels: one for absolute levels and one for differences, with consistent outcome ordering.
- Add a short legend that states whether each number is a total or a change.

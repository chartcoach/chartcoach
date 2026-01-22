---
id: separate-treated-and-untreated-risks-into-two-icon-arrays
title: Use separate icon arrays for treated and untreated groups to show the full
  denominator for each
bibliography: references.bib
description: "Two distinct icon arrays\u2014one per group\u2014help readers map events\
  \ to the correct population size."
labels:
- chart:icon-array
- task:compare
- visual:grouping
- impact:clarity
- data:binary-outcome
- audience:novice
- domain:health-risk
---

## Use one icon array per group to preserve numerator–denominator mapping <!-- role: advice -->

Use two distinct icon arrays—one for the treated group and one for the untreated group—so each event count is visually tied to its own total population.

## Group separation reduces numerator-only reasoning <!-- role: reason -->

When outcomes are compared across groups, viewers can mistakenly compare only event counts if the population totals are not tightly coupled to each group’s events; separate arrays keep each numerator embedded within its own denominator.

**Mechanism:** Clear grouping supports proportional interpretation by making “how many out of how many” available for each group simultaneously.

**Evidence:** Accuracy in estimating treatment risk reduction depended strongly on denominator size when information was numeric-only, consistent with mismapping numerators to denominators; adding icon arrays (presented for both “with treatment” and “without treatment”) removed the denominator-size effect on accuracy [@garcia-retameroCommunicatingTreatmentRisk2009].

**Notes:** This design particularly benefited low-numeracy participants, who otherwise showed stronger denominator neglect.

## When presenting two-group treatment outcomes <!-- role: context -->

- **User Goal:** Understand how risk differs with and without a treatment.
- **Task:** Compare two proportions (event rate in treated vs untreated).
- **Data:** Two populations (treated and untreated) with event subsets, possibly with unequal denominators.
- **Chart Setting:** Decision aids, survey-like explanations, or patient education screens where both groups must be compared.
- **Audience:** Broad public, including low numeracy.
- **Success Criterion:** Viewers can correctly estimate risk reduction regardless of whether denominators are equal or unequal.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are only communicating a single group’s absolute risk (no comparison group). **Why:** A second array adds redundant structure for a single-proportion task.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Two arrays require more space than one. **Risk:** If the arrays use very different sizes (e.g., 800 vs 100 icons), readers may focus on layout differences rather than rates. **Mitigation:** Keep labeling and structure consistent across the two arrays.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Presenting treated and untreated event counts together but the totals separately (or only in text). **Why it fails:** Readers can compare event counts directly and overlook the different population sizes.
- **Mistake:** Mixing both groups into one display without explicit segmentation. **Why it fails:** The denominator for each numerator becomes ambiguous.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers say the treatment is “more effective” mainly because the treated event count is smaller, even when the treated group is much smaller. **Quick Check:** Ask which group has a higher death rate; if many answer based on absolute deaths, mapping is failing. **Stronger Test:** Have users estimate deaths per 1000 in each group; large systematic errors indicate denominator neglect.

## What to do instead <!-- role: fix -->

- Visually separate groups into distinct panels with repeated headers (“With treatment” vs “Without treatment”).
- Pair each event count immediately with its population total in the same visual block.
- Use a consistent visual structure for both groups so comparisons are made on rates, not formatting differences.
- If space-constrained, reduce the icon count per array while preserving the one-array-per-group structure.

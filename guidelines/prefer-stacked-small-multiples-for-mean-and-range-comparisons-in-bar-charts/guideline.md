---
id: prefer-stacked-small-multiples-for-mean-and-range-comparisons-in-bar-charts
title: Prefer vertically stacked small-multiple bar charts for mean and range comparisons
bibliography: references.bib
description: Stacked (vertically juxtaposed) bar charts support more precise set-to-set
  comparisons of mean and range than other tested arrangements.
labels:
- chart:bar
- task:aggregate
- task:determine-range
- visual:position
- visual:layout
- impact:accuracy
- data:quantitative
- audience:novice
- comparison:set-to-set
---

## Prefer vertically stacked small-multiple bar charts for mean and range comparisons <!-- role: advice -->

Use vertically stacked small-multiple bar charts when readers need to compare the mean (average) or the range (min-to-max spread) between two sets of values.

## Why stacked arrangements improve precision for mean/range comparisons <!-- role: reason -->

Stacking aligns corresponding bars so viewers can compare lengths with minimal scanning and reduced alignment error, which supports more precise set-to-set judgments than layouts that separate sets horizontally or mix them in the same space.

**Mechanism:** Vertical stacking supports direct perceptual alignment of bar lengths across sets, improving discrimination of small differences in the compared summary property.

**Evidence:** For both aggregate (mean) and determine-range comparisons, the stacked arrangement ranked best (lowest just noticeable difference, JND), outperforming mirrored and adjacent layouts, and clearly outperforming the color-saturation encoding condition in the extracted rankings [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023].

**Notes:** This guideline only applies to the specific bar-chart comparison setting captured in the extracted designs and rankings, not to other chart types or tasks.

## When stacked bar-chart comparisons apply <!-- role: context -->

- **User Goal:** Decide which of two groups has the larger mean or the larger range.
- **Task:** Aggregate; Determine Range.
- **Data:** Two sets of quantitative values (each set treated as a group for comparison).
- **Chart Setting:** Static horizontal bar charts shown as small multiples.
- **Audience:** General audiences doing quick analytic judgments.
- **Success Criterion:** Lower discrimination threshold (more precise comparisons).

## When not to default to stacking <!-- role: exceptions -->

**Break it when:** You cannot allocate vertical space for two full small multiples (e.g., tight dashboard tile). **Why:** The stacked layout may be infeasible even if it is more precise.

## Tradeoffs and risks of stacking <!-- role: costs -->

**Sacrifice:** More vertical space than side-by-side arrangements. **Risk:** If the page is short, stacking can force scrolling, which may reduce the chance that both sets are viewed together. **Mitigation:** Keep both panels fully visible at once when possible.

## Common mistakes with mean/range comparisons across groups <!-- role: mistakes -->

**Mistake:** Using a combined or alternative encoding arrangement without checking whether it supports the specific comparison task. **Why it fails:** Precision for these comparisons varies substantially by arrangement, so a convenient layout can be systematically less precise.

## Quick tests for whether stacking is needed <!-- role: check -->

**Failure Sign:** Readers hesitate or disagree when deciding which group’s average or range is larger. **Quick Check:** Show both stacked and an alternative arrangement to a colleague and see which yields faster, more consistent answers. **Stronger Test:** Run a small pilot where you measure which layout produces fewer errors on mean/range questions.

## What to do instead if stacking is impossible <!-- role: fix -->

- Use a mirrored arrangement as a fallback when vertical space is constrained.
- Use an adjacent (side-by-side) arrangement if mirroring would confuse the audience.
- Reduce the number of categories shown per group so a stacked layout fits without scrolling.
- Provide a direct numeric summary (mean or range) alongside the charts when layout constraints prevent a precise visual comparison.

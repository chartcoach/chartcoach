---
id: avoid-color-saturation-as-a-stand-in-for-layout-in-bar-set-comparisons
title: Avoid using color saturation encoding as a substitute for spatial separation
  in bar-set comparisons
bibliography: references.bib
description: Color saturation performed worst among tested options for supporting
  precise mean and range comparisons between bar sets.
labels:
- chart:bar
- task:aggregate
- task:determine-range
- visual:color
- visual:color-saturation
- impact:accuracy
- data:quantitative
- audience:novice
- comparison:set-to-set
---

## Avoid using color saturation encoding as a substitute for spatial separation in bar-set comparisons <!-- role: advice -->

When comparing which of two sets has the larger mean or range, do not rely on color saturation alone to distinguish sets; separate the sets spatially instead.

## Why color-saturation separation is less precise for these comparisons <!-- role: reason -->

When multiple bars must be integrated into a summary judgment (mean or range), relying on a non-spatial channel to segregate sets can weaken the perceptual signal for the comparison relative to layouts that separate sets by position.

**Mechanism:** Spatial separation supports grouping and alignment of bars per set, while color-based separation can increase grouping ambiguity and reduce precision for summary comparisons.

**Evidence:** The color-saturation condition ranked worst for both aggregate and determine-range tasks in the extracted JND rankings, and it was significantly worse than several other conditions in the aggregate task’s recorded significant pair list [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023].

**Notes:** This guideline is specific to using color saturation to distinguish sets in this bar-chart comparison setting, not a general ban on color saturation.

## When this applies <!-- role: context -->

- **User Goal:** Compare two groups to decide which has the larger mean or larger range.
- **Task:** Aggregate; Determine Range.
- **Data:** Two groups of quantitative values mapped to bar length.
- **Chart Setting:** Static displays where group identity is encoded via appearance rather than separate panels.
- **Audience:** Broad audiences; need fast, accurate judgments.
- **Success Criterion:** Lower discrimination threshold (better precision).

## When it may be acceptable <!-- role: exceptions -->

**Break it when:** Spatial separation is impossible and the comparison is not required to be precise. **Why:** The evidence supports lower precision with saturation-based separation for these tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Spatially separating sets typically uses more space than a single combined view. **Risk:** If you remove saturation and still keep sets in one space, you may need other cues to maintain group identity. **Mitigation:** Maintain consistent labels and grouping cues even when separated.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Encoding the two sets using saturation differences and assuming it will compare like small multiples. **Why it fails:** The extracted results show saturation performed worst for mean and range comparisons in this context.

## Quick tests <!-- role: check -->

**Failure Sign:** People confuse which bars belong to which set or misjudge which set has the larger mean/range. **Quick Check:** Convert the design to stacked small multiples; if answers become noticeably faster and more consistent, saturation was likely the bottleneck. **Stronger Test:** Run a small timed quiz comparing saturation vs stacked and track error rates.

## What to do instead <!-- role: fix -->

- Use vertically stacked small multiples with shared axes for the two sets.
- Use a mirrored or adjacent small-multiple arrangement if stacking is not feasible.
- Add clear per-set labels close to the bars to reinforce grouping.
- Provide direct summary annotations (mean or range) for each set when precision is critical.

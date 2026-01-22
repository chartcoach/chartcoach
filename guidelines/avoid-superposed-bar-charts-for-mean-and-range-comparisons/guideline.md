---
id: avoid-superposed-bar-charts-for-mean-and-range-comparisons
title: Avoid superposed (overlaid) bar charts for mean and range comparisons
bibliography: references.bib
description: Overlaid bar charts support less precise mean and range comparisons between
  two sets than separated small-multiple arrangements.
labels:
- chart:bar
- task:aggregate
- task:determine-range
- visual:layout
- impact:accuracy
- data:quantitative
- audience:novice
- comparison:set-to-set
---

## Avoid superposed (overlaid) bar charts for mean and range comparisons <!-- role: advice -->

Do not overlay the two bar sets in the same plotting space when the goal is to compare which group has the larger mean or larger range.

## Why superposition reduces precision for mean/range comparisons <!-- role: reason -->

Superposition forces viewers to separate the two sets by a non-spatial cue while also judging summary properties across multiple bars, which increases interference and makes fine discrimination harder than when sets are spatially separated.

**Mechanism:** Overlaid marks compete for attention and make it harder to isolate each set’s bar-length pattern, degrading the perceptual signal needed to judge which set’s mean or range is larger.

**Evidence:** In the extracted experimental results, superposed performance is worse than stacked for both aggregate and determine-range comparisons, reflected by the ranking that places the non-superposed stacked arrangement above the other conditions for both tasks [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about set-to-set summary comparisons (mean/range), not item-to-item change detection.

## When this applies <!-- role: context -->

- **User Goal:** Decide which group’s average or spread is larger.
- **Task:** Aggregate; Determine Range.
- **Data:** Two groups of quantitative values displayed as bars.
- **Chart Setting:** Static bar-based displays comparing two datasets/conditions.
- **Audience:** Mixed expertise; speed and correctness matter.
- **Success Criterion:** High precision in discriminating small differences.

## When you might still overlay <!-- role: exceptions -->

**Break it when:** The task is not a set-to-set mean/range comparison but a different judgment where overlay is required for a separate reason. **Why:** This guideline only reflects evidence for the mean and range comparison tasks.

## Tradeoffs and risks of avoiding overlays <!-- role: costs -->

**Sacrifice:** You may lose the compactness of a single combined plot. **Risk:** Switching away from overlay can reduce perceived direct comparability for individual bars if viewers expect a single shared space. **Mitigation:** Keep consistent ordering and scales across separated views.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Overlaying bars and relying on viewers to “mentally separate” the sets while also estimating mean or range. **Why it fails:** The arrangement can make the visual signal for mean/range discrimination weaker than necessary.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers report that the chart “looks cluttered” or they misjudge which group has the higher average/spread. **Quick Check:** If bars overlap in ways that hide lengths or create frequent occlusion, the design is likely unsuitable. **Stronger Test:** Ask a few users to answer mean/range questions under time pressure and compare error rates versus a stacked alternative.

## What to do instead <!-- role: fix -->

- Separate the two sets into vertically stacked small multiples with a shared scale.
- Use a mirrored or adjacent small-multiple layout if stacking is not feasible.
- Reduce the number of bars per set to make separated views fit comfortably.
- Add explicit mean/range annotations for each set to reduce reliance on difficult visual discrimination.

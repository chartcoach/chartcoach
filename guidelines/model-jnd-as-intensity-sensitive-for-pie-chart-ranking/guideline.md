---
id: model-jnd-as-intensity-sensitive-for-pie-chart-ranking
title: Treat pie-slice discriminability as intensity-sensitive when ranking slices
bibliography: references.bib
description: Account for increasing just noticeable difference (JND) with larger slice
  angles when users must visually rank pie-chart segments.
labels:
- chart:pie
- task:sort
- visual:angle
- visual:color
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Pie-chart ranking: account for slice-angle-driven JND <!-- role: advice -->

When a pie chart is used for sorting, assume that the minimum noticeable difference between slice sizes increases with slice angle (intensity). Do not assume that making slices adjacent (changing angular separation) will reliably improve discriminability.

## Why slice angle drives pie-chart JND in sorting <!-- role: reason -->

In pie charts, discriminability for comparing two slices is primarily tied to the slice magnitude (angle), not how far apart the slices are around the circle. For sorting, this means “small differences” among larger slices can be harder to notice than equally small differences among smaller slices.

**Mechanism:** As slice angle increases, the perceptual threshold for noticing a difference increases, so larger segments require larger absolute differences to be reliably distinguished.

**Evidence:** In pie charts, slice angle (intensity) had a statistically significant main effect on JND, while angular separation distance did not show a significant main effect under the tested discrimination task [@luModelingJustNoticeable2022]. This finding is collated into a machine-actionable graphical-perception knowledge base intended to support visualization recommendation decisions [@zengReviewCollationGraphical2023].

**Notes:** This guidance concerns perceptual thresholds for distinguishing nearby values, not whether pie charts are generally preferable for ranking.

## When this pie-angle JND guideline applies <!-- role: context -->

- **User Goal:** Rank categories by their quantitative shares using a pie chart.
- **Task:** Sort.
- **Data:** Quantitative values shown as proportions by category.
- **Chart Setting:** Static pie chart with colored slices.
- **Audience:** General audiences, including viewers without specialized visualization training.
- **Success Criterion:** Accurate ordering of slices with similar proportions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is not to rank but only to spot a clearly dominant slice. **Why:** JND sensitivity matters most when differences are small and ordering among similar slices is required.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the ability to rely on adjacency tricks (reordering slices) as a primary way to improve slice-to-slice discrimination. **Risk:** Over-applying this assumption may lead you to add unnecessary extra cues in simple pies with large, obvious differences. **Mitigation:** Focus on cases with many similarly sized slices or when rank decisions hinge on small differences.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Reordering slices to place two close-valued slices next to each other and expecting discrimination to improve materially. **Why it fails:** Angular separation was not a significant main effect on JND in the tested pie-chart discrimination setting, while slice angle was [@luModelingJustNoticeable2022; @zengReviewCollationGraphical2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers hesitate or disagree when ranking large slices that differ only slightly.\
**Quick Check:** Compare two similarly sized slices and see if you can confidently pick the larger without re-checking.\
**Stronger Test:** Ask a few readers to do rapid “which slice is larger?” judgments across several slice magnitudes and note where errors cluster.

## What to do instead <!-- role: fix -->

- Add a secondary cue for slices likely to be below JND for your audience (for example, annotate slice values for the compared items).
- Reduce reliance on visual-only ranking by providing a sorted list of the same category values alongside the pie.
- If ordering is central, switch to a representation that supports more precise ranking of close values (for example, a bar-based view).

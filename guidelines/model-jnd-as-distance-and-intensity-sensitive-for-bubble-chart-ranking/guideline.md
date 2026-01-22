---
id: model-jnd-as-distance-and-intensity-sensitive-for-bubble-chart-ranking
title: Treat bubble-chart discriminability as distance-and-intensity-sensitive when
  ranking bubbles
bibliography: references.bib
description: Account for increasing just noticeable difference (JND) with both bubble
  size (intensity) and bubble separation distance when users must visually rank values.
labels:
- chart:bubble
- task:sort
- visual:area
- visual:position
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Bubble-chart ranking: account for size- and distance-driven JND <!-- role: advice -->

When a bubble chart is used for sorting, assume that the minimum noticeable difference increases with both bubble size (intensity) and the distance between the compared bubbles. Avoid assuming that either keeping bubbles close or using larger bubbles alone will guarantee discriminability for small differences.

## Why both size and distance drive bubble-chart JND in sorting <!-- role: reason -->

In bubble charts, the perceptual threshold for noticing differences is jointly influenced by how large the bubbles are and how far apart they are. This affects sorting because small value differences can become imperceptible either due to large bubble sizes or due to increased separation.

**Mechanism:** Larger bubbles and greater separation both increase the JND threshold, which increases the chance that close-valued bubbles become indistinguishable for pairwise comparisons needed in ranking.

**Evidence:** In bubble charts, both separation distance and intensity (radius) showed statistically significant main effects on JND, indicating discriminability depends on both variables for the tested comparison task [@luModelingJustNoticeable2022]. This result is recorded and made available as structured guidance for visualization recommendation contexts [@zengReviewCollationGraphical2023].

**Notes:** This guidance is about perceptual discrimination of close values, not about layout aesthetics or packing efficiency.

## When this bubble JND guideline applies <!-- role: context -->

- **User Goal:** Rank categories by a quantitative value using bubble sizes.
- **Task:** Sort.
- **Data:** Quantitative values mapped to bubble size; categories used to identify items.
- **Chart Setting:** Static bubble chart where items have varying positions and sizes.
- **Audience:** General audiences, including viewers without specialized visualization training.
- **Success Criterion:** Accurate ordering when values are close.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is coarse grouping (e.g., “small vs. large”) rather than strict ordering. **Why:** JND-based indistinguishability matters most when fine-grained ranking is required.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Accounting for both distance and size can constrain layout choices and may require extra design effort to support ranking. **Risk:** Treating all close pairs as problematic can lead to clutter if you add too many secondary cues. **Mitigation:** Focus enhancements on the smallest set of likely ambiguous comparisons.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Packing bubbles tightly (or spreading them out) and assuming that alone solves discrimination problems for close values. **Why it fails:** Bubble-chart JND is affected by both separation distance and intensity, so changing only one factor may not restore discriminability [@luModelingJustNoticeable2022; @zengReviewCollationGraphical2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers cannot reliably decide which of two similar bubbles is larger, especially when bubbles are far apart or very large.\
**Quick Check:** Pick several close-valued bubble pairs at different separations and sizes and see whether “which is larger?” feels effortless.\
**Stronger Test:** Run a short timed discrimination check (“pick the larger”) for a handful of representative pairs and track error rates.

## What to do instead <!-- role: fix -->

- Add a secondary cue for the subset of bubble pairs likely to be below JND (for example, show values for the compared bubbles).
- Adjust layout to reduce separation for bubbles that users must compare directly during ranking.
- Provide an alternate ranking aid (for example, a sorted list of the same values) when precise ordering is required.

---
id: permute-within-segments-to-improve-colorfield-accuracy-for-aggregate-average-judgments
title: Permute values within each time segment to improve colorfield accuracy for
  aggregate average judgments
bibliography: references.bib
description: When using a colorfield to judge which time segment has the highest average,
  permuting values within segments improves accuracy.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- custom:within-segment-permutation
---

## Permute values within each segment in colorfields for maximum-average selection <!-- role: advice -->

When a colorfield is used to select which time segment has the highest average, permute (shuffle) the values within each segment so that local color mixtures better represent the segment’s overall average.

## Why within-segment permutation can improve aggregate accuracy in colorfields <!-- role: reason -->

Rearranging values within a segment changes the spatial arrangement of colors without changing the set of values in that segment. This can make the segment’s overall appearance less dependent on within-segment order, supporting a more consistent aggregate impression of that segment compared to an ordered arrangement.

**Mechanism:** Permutation reduces reliance on the original within-segment sequence pattern for forming an overall segment impression, encouraging judgments based on the segment’s aggregate color appearance.

**Evidence:** In an aggregate task (select the month with the highest average) using time-series data, a permuted colorfield outperformed an ordered colorfield in accuracy (reported as a significant interaction and higher mean accuracy for permuted colorfields), indicating that within-segment permutation improved performance for colorfields in this aggregate judgment setting [@correllComparingAveragesTime2012; @zengReviewCollationGraphical2023].

**Notes:** This evidence concerns the aggregate judgment task recorded; it does not establish that permutation is beneficial for tasks that depend on within-segment temporal order.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Choose which pre-defined time segment has the highest average value.
- **Task:** Aggregate (average-over-range) judgment.
- **Data:** One quantitative measure over an ordered sequence with clear segment boundaries (e.g., days grouped into months).
- **Chart Setting:** A colorfield where each segment is visually separable as a block.
- **Audience:** General audiences making segment-level comparisons rather than sequence-level interpretations.
- **Success Criterion:** Higher accuracy in selecting the segment with the maximum average.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The within-segment ordering itself is meaningful (e.g., you need to see trends or events inside the segment). **Why:** Permutation destroys within-segment order information, and this guideline is only supported for segment-average selection.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up interpretability of within-segment temporal structure. **Risk:** Viewers may incorrectly assume the permuted arrangement preserves the original time order. **Mitigation:** Make segment boundaries explicit and communicate that the display is optimized for segment-average comparison.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Permuting values when users need to interpret within-segment patterns (spikes, runs, or timing). **Why it fails:** Permutation removes the temporal order cues that such interpretations rely on.

## Quick tests before you ship <!-- role: check -->

**Failure Sign:** Viewers report confusion about whether the within-segment arrangement reflects time order. **Quick Check:** Ask a few readers to explain what the within-segment arrangement means; if they describe it as chronological, the design is likely misleading. **Stronger Test:** Compare accuracy on the maximum-average question for ordered vs permuted colorfields with the intended audience.

## What to do instead if this rule doesn’t fit <!-- role: fix -->

- Use an ordered colorfield (no permutation) when within-segment time patterns must remain interpretable.
- Keep the ordered time encoding and compute/show explicit segment averages if segment summaries are required without losing order.
- Provide a separate summary view for segment-level averages alongside an ordered view for within-segment patterns.
- If permutation is used, add clear labeling that the within-segment arrangement is not chronological and is intended for segment-average comparison.

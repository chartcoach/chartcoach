---
id: permute-within-segment-in-colorfields-to-improve-average-judgment-accuracy
title: Randomly permute values within each segment in a colorfield to improve average-comparison
  accuracy
bibliography: references.bib
description: Shuffling values within each aggregation block improves accuracy for
  choosing the highest-average segment in colorfield displays.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- task:aggregate
- technique:permutation
---

## Permute within blocks for colorfield average judgments <!-- role: advice -->

Randomly permute the values within each segment’s block in a colorfield when the viewer’s job is to compare segment averages. Preserve the segment boundaries so the shuffling happens only inside each segment.

## Why permutation helps in colorfields <!-- role: reason -->

Permuting within a segment breaks up local streaks and clusters so that small-area samples within the block are more representative of the segment’s overall distribution, making the perceived average color more stable and easier to compare.

**Mechanism:** If perceptual averaging pools color locally, a block whose colors are more uniformly mixed provides many small regions with similar average color, reducing reliance on integrating across the entire block.

**Evidence:** In the maximum-average month task, permuted colorfields produced higher accuracy than ordered colorfields (reported means: ~0.914 vs ~0.815) with a significant display-type-by-permutation interaction [@correllComparingAveragesTime2012a]. Permutation did not improve performance for line graphs, aligning the benefit specifically with the colorfield case [@correllComparingAveragesTime2012a].

**Notes:** This is a task-specific transformation; it intentionally discards within-segment temporal patterns.

## When block permutation fits the problem <!-- role: context -->

- **User Goal:** Choose which segment has the highest average.
- **Task:** Average comparison across known, fixed segment boundaries (e.g., months).
- **Data:** Time series where within-segment ordering is not needed for the decision.
- **Chart Setting:** Colorfield display where each segment is shown as a distinct block.
- **Audience:** Viewers who can use a color legend and are not screened out by color vision issues for the chosen palette.
- **Success Criterion:** Improved correctness in selecting the highest-average segment, especially under harder stimuli.

## When not to permute within segments <!-- role: exceptions -->

**Break it when:** The viewer must detect within-segment trends, sequences, or recurring patterns. **Why:** Permutation destroys ordering information and can create patterns in the display that are not present in the underlying temporal data [@correllComparingAveragesTime2012a].

## Tradeoffs and risks of permutation <!-- role: costs -->

**Sacrifice:** Temporal interpretability inside each segment. **Risk:** Users may infer false fine-scale structure from the randomized arrangement or assume the shown micro-patterns are meaningful. **Mitigation:** Treat the view as an aggregation aid and ensure the narrative and labeling focus on averages by segment.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Permuting across segment boundaries instead of only within segments. **Why it fails:** It mixes values from different aggregation units and invalidates the comparison the viewer is trying to make [@correllComparingAveragesTime2012a].

## Quick tests for whether permutation helps <!-- role: check -->

**Failure Sign:** In an ordered colorfield, viewers struggle most when the top segment is only slightly higher than close competitors. **Quick Check:** Compare a permuted and ordered version on a few difficult examples and see if agreement and confidence improve. **Stronger Test:** Run a small forced-choice accuracy check using your own data and measure correctness under both variants.

## If permutation is inappropriate, what to do instead <!-- role: fix -->

- Keep the ordered colorfield when within-segment temporal structure is part of the question.
- Use a non-permuted encoding and add explicit segment summaries if the key need is average comparison without losing order.
- Split the display into two coordinated views: one summary-first (colorfield) and one order-preserving (line graph) for follow-up.

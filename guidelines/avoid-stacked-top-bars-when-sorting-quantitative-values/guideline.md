---
id: avoid-stacked-top-bars-when-sorting-quantitative-values
title: Avoid sorting by the length of stacked bars, especially when only the top segment
  varies
bibliography: references.bib
description: "When sorting values, stacked-bar designs that require judging segment\
  \ length\u2014especially top segments\u2014reduce accuracy compared to position-based\
  \ bar designs."
labels:
- chart:bar
- task:sort
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- source:collated
---

## Don’t make sorting depend on stacked-segment length judgments <!-- role: advice -->

When people must sort quantitative values, avoid designs where they must compare the lengths of stacked bar segments, particularly when the compared segment sits on top of another bar segment. Prefer designs where the values can be compared by position on a common scale.

## Why stacked-segment length comparisons reduce sorting accuracy <!-- role: reason -->

Stacking removes a shared baseline for the segment being compared, forcing viewers to judge segment lengths without consistent alignment.

**Mechanism:** Without a common baseline, viewers must estimate segment extent rather than align endpoints on a shared axis, increasing error during ordering.

**Evidence:** In sorting tasks, a position-on-common-scale bar design ranked higher in accuracy than length-based stacked bar variants, including a variant where the compared bars are the top segments of stacked bars. [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023]

**Notes:** This guideline is limited to the specific sorting comparisons tested among bar chart variants.

## When this guidance applies (stacked bars used for ordering) <!-- role: context -->

- **User Goal:** Rank items by magnitude.
- **Task:** Sort.
- **Data:** Quantitative values for items, shown as parts within stacked bars.
- **Chart Setting:** Static stacked bar chart where comparisons are made between segments.
- **Audience:** General.
- **Success Criterion:** Accurate ordering.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The chart is not used for sorting segments by value. **Why:** The evidence addresses ordering accuracy, not other goals like showing composition.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding stacked-segment comparisons may reduce the ability to show part-to-whole structure in a single compact mark. **Risk:** Overcorrecting by removing stacking can change what the chart communicates. **Mitigation:** Keep the part-to-whole view if needed, but add a separate view that supports sorting.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Asking viewers to rank categories by the size of the top piece of each stacked bar. **Why it fails:** The compared segment lacks a shared baseline, which can lower sorting accuracy.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers make frequent swaps among similarly sized segments when ranking. **Quick Check:** Hide axis labels and see if people can still produce a consistent ordering. **Stronger Test:** Collect sorting accuracy across a few representative datasets and compare to a shared-axis position alternative.

## What to do instead <!-- role: fix -->

- Replace stacked-segment comparisons with a shared-axis position encoding for the values being sorted.
- If composition is required, keep the stacked bar for composition but provide a separate position-based chart for ranking.
- Re-encode the values intended for ordering so they share a common baseline.

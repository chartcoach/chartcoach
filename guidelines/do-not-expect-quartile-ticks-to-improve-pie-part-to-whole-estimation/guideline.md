---
id: do-not-expect-quartile-ticks-to-improve-pie-part-to-whole-estimation
title: Do Not Rely on Quartile Ticks to Improve Pie Part-to-Whole Estimation
bibliography: references.bib
description: Adding quartile tick cues to a pie chart did not show a significant accuracy
  improvement over a baseline pie in the reported comparison.
labels:
- chart:pie
- task:estimate
- visual:angle
- visual:annotation
- impact:accuracy
- data:part-to-whole
- audience:general
- detail:quartile-ticks
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If your goal is higher estimation accuracy in a pie chart, do not assume adding quartile tick marks will help.

## The Logic <!-- role: reason -->

In the reported comparison, the pie-with-quartile-ticks variant did not produce a statistically significant improvement over the baseline pie chart.

- **The Principle:** Not all added reference cues reliably reduce error; some may be redundant with existing cues.
- **The Evidence:** The collation records pie with quartile ticks (E-5) ranked above baseline bar (E-1) but with no significant pairs reported for that comparison set, indicating no significant improvement attributable to the added quartile ticks in the reported test context [@redmondVisualCuesEstimation2019], as structured in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating a highlighted segment’s percentage in a two-segment pie chart.
- **Data Type:** Part-to-whole proportions (percentages).
- **Audience:** General users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your objective is not accuracy improvement (e.g., you are adding ticks for stylistic or instructional reasons).
- **Reason:** The evidence summarized here addresses accuracy outcomes only, not aesthetics or training effects [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual elements without demonstrated accuracy gain in this comparison.
- **The Risk:** Increased visual complexity may distract from the segment itself.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding quartile ticks to a pie and presenting it as an “accuracy upgrade.”
- **Why it fails:** The reported results (as collated) do not provide evidence of a significant accuracy improvement from those ticks [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The pie looks busier, but users’ estimates remain similarly variable.
- **The Test:** A/B test baseline pie vs. pie-with-quartile-ticks and compute mean absolute error; do not assume improvement without seeing a measurable reduction [@redmondVisualCuesEstimation2019], consistent with the collation outcome [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove quartile ticks if they were added solely for accuracy improvement.
- **Best Fix:** If you need better estimation accuracy and can switch encodings, use the pie baseline (vs. plain bar) or use a bar with an explicit scale (best-performing bar variant) depending on your constraints [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

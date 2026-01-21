---
id: stack-horizontal-bar-charts-vertically-for-precise-mean-comparisons
title: Stack Bar-Chart Small Multiples Vertically for Mean Comparisons
bibliography: references.bib
description: For comparing which group has the larger mean, use vertically stacked
  horizontal bar-chart small multiples rather than adjacent, mirrored, or superposed
  arrangements.
labels:
- chart:bar
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- comparison:set-to-set
---

## The Rule <!-- role: advice -->

When you need to judge which of two groups has the larger mean using horizontal bar charts, place the two charts in a **vertically stacked** small-multiples layout.

## The Logic <!-- role: reason -->

Vertically stacking keeps corresponding bars aligned across the vertical axis, enabling more precise set-to-set comparisons of average level (lower JND threshold) than alternative arrangements. This guideline is derived from collated graphical-perception evidence in [@zengReviewCollationGraphical2023] and is supported by experimental results on MAXMEAN-style comparisons in [@jardinePerceptualProxiesVisual2020].

- **The Principle:** Arrangement affects comparison precision (set-to-set comparison benefits from stacked alignment).
- **The Evidence:** [@jardinePerceptualProxiesVisual2020], as collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two sets has the larger mean (aggregate comparison).
- **Data Type:** Two groups of quantitative values shown as horizontal bars (small multiples).
- **Audience:** General audiences doing quick, perceptual comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must emphasize within-item deltas via overlap (e.g., you need the two series drawn in the same space for another purpose).
- **Reason:** This rule is specific to mean comparisons and does not claim superiority for other comparison tasks; [@jardinePerceptualProxiesVisual2020] shows arrangement effectiveness depends on task, as summarized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** More vertical space than adjacent layouts.
- **The Risk:** On short screens, stacked charts may require scrolling, reducing at-a-glance comparison.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Overlaying/superposing the two bar charts (e.g., differentiating groups by an additional visual encoding).
- **Why it fails:** In the reported ranking, superposed performed worst for the mean-comparison task (higher JND threshold) relative to stacked, mirrored, and adjacent [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or frequently misjudge which group is “higher overall.”
- **The Test:** Compare a stacked version vs. your current arrangement with a few representative cases; if stacked yields faster/more consistent judgments, your current layout is likely hurting precision (as expected from the ranking reported in [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rearrange the two bar-chart panels into a vertical stack.
- **Best Fix:** Use vertical stacking and keep both panels on the same scale and visible simultaneously to preserve direct visual comparison, aligning with the evidence summarized in [@zengReviewCollationGraphical2023] from [@jardinePerceptualProxiesVisual2020].

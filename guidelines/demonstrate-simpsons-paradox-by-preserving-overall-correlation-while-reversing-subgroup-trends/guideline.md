---
id: demonstrate-simpsons-paradox-by-preserving-overall-correlation-while-reversing-subgroup-trends
title: "Visualize Simpson\u2019s Paradox by Contrasting Overall and Group Trends"
bibliography: references.bib
description: "Construct plots where the combined data show one correlation while subgroups\
  \ show the opposite, to teach Simpson\u2019s Paradox."
labels:
- chart:scatter
- task:explain
- visual:position
- impact:insight
- data:bivariate
- audience:novice
- custom:simpsons-paradox
---

## The Rule <!-- role: advice -->

To teach Simpson’s Paradox, show a scatterplot where the overall dataset preserves a strong correlation, while clearly segmented subgroups each show the opposite correlation.

## The Logic <!-- role: reason -->

- **The Principle:** Aggregation can mask or reverse relationships present within subgroups; visualization reveals both levels simultaneously.
- **The Evidence:** The paper demonstrates starting from a positively correlated dataset, coercing points into negatively sloped subgroup lines, and retaining the same overall Pearson correlation while subgroups become negatively correlated [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how group structure changes interpretation of correlation.
- **Data Type:** Scatter data with meaningful subgrouping (explicit groups or implied clusters/lines).
- **Audience:** Learners or decision-makers interpreting correlations in aggregated reports.

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is no defensible grouping variable or subgroup concept for the data.
- **Reason:** Without meaningful groups, the paradox framing becomes contrived.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual complexity (group encoding and potentially multiple correlation summaries).
- **The Risk:** Viewers may focus on only one level (overall or subgroup) unless prompted.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only the aggregated correlation line without making subgroup structure visible.
- **Why it fails:** The paradox depends on seeing the subgroup patterns that contradict the aggregate [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Subgroups are not visually separable, so the viewer can’t perceive within-group trends.
- **The Test:** Compute the overall correlation and each subgroup correlation and confirm they differ in sign/direction as intended [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Encode groups explicitly (e.g., by color) and spatially separate subgroup structures (as distinct sloped bands/lines).
- **Best Fix:** Present both aggregate and subgroup summaries together (overall correlation plus per-group correlations) to make the reversal unmissable [@matejkaSameStatsDifferent2017].

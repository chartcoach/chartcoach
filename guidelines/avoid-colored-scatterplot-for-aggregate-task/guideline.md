---
id: avoid-colored-scatterplot-for-aggregate-task
title: Avoid Colored Scatterplots When the Task Is Aggregation
bibliography: references.bib
description: For aggregation tasks on trivariate data, avoid mappings where categories
  are encoded by color-hue on a scatterplot, as they rank lower in aggregate accuracy.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:position
- impact:accuracy
- data:quantitative
- data:categorical
- complexity:multivariate
---

## The Rule <!-- role: advice -->

For aggregate tasks (e.g., comparing category averages), do not default to a colored scatterplot where N is color-hue and Q1/Q2 are x/y (E-5/E-6).

## The Logic <!-- role: reason -->

In the aggregate accuracy results, the colored-scatterplot mappings (E-5/E-6) are ranked in a worse group than a large set of other encodings that share the top rank group (including many position+row or position+color-saturation/size variants) [@kimAssessingEffectsTask2018]. The collation captures this task-dependent reversal explicitly as a caution for recommendation systems [@zengReviewCollationGraphical2023].

- **The Principle:** Task-dependent effectiveness (value vs. summary/aggregate)
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare aggregates across categories (aggregate task).
- **Data Type:** Trivariate: Q1 (primary quantitative), Q2 (secondary quantitative), N (nominal categories).
- **Audience:** Users making summary judgments rather than point read-offs.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user simultaneously needs to perform value tasks on both Q1 and Q2 while still wanting some aggregate sense.
- **Reason:** The same encodings (E-5/E-6) are strong for retrieve-value/sort, so you may accept aggregate-accuracy loss to keep value-task performance [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to use alternative mappings (e.g., faceting by row, or encoding a quantitative with size/saturation) that can reduce ease of bivariate relationship reading.
- **The Risk:** Switching away from x/y + color-hue may reduce performance for point-level tasks if users pivot tasks mid-analysis [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always recommend the same colored scatterplot for “two quantitative + one categorical,” regardless of task.
- **Why it fails:** Aggregate accuracy ranks for E-5/E-6 are worse than many alternatives, demonstrating that a one-size-fits-all recommendation underperforms for aggregation [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Aggregation questions require users to mentally average differently colored points in the same shared x/y space.
- **The Test:** If your aggregate recommendation is equivalent to E-5 or E-6, treat it as lower-confidence for aggregate accuracy than designs in the top group [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** For aggregation, deprioritize E-5/E-6 and elevate designs from the top aggregate-accuracy group reported (e.g., E-1/E-2/E-3/E-4/E-7/E-8/E-9/E-10/E-11/E-12) depending on your system’s constraints.
- **Best Fix:** Implement task-aware ranking so aggregation queries do not reuse value-task defaults [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

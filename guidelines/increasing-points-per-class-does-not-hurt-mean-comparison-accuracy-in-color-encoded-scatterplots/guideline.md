---
id: increasing-points-per-class-does-not-hurt-mean-comparison-accuracy-in-color-encoded-scatterplots
title: "Don\u2019t Reduce Point Count to Improve Mean Comparison"
bibliography: references.bib
description: For mean-comparison aggregation in color-encoded scatterplots, increasing
  points per class from 50 to 75 did not reduce accuracy in the evaluated conditions.
labels:
- chart:scatter
- task:aggregate
- visual:position
- visual:color
- impact:accuracy
- data:quantitative
- data:categorical
- audience:general
- custom:density
- source:collated
---

## The Rule <!-- role: advice -->

Do not assume you must downsample points (reduce point count per class) to make class-mean comparison more accurate in a color-encoded scatterplot.

## The Logic <!-- role: reason -->

Within the tested range, more points per class did not reduce aggregate mean-comparison accuracy.

- **The Principle:** Aggregate judgements can remain stable with increased set size (within reasonable bounds).
- **The Evidence:** The 75-points-per-class color-hue design (E-3) is grouped with other high-performing color-hue designs in aggregate accuracy, and specific comparisons (aggregate-5) ranked E-3 over E-1 without significance pairs recorded [@gleicherPerceptionAverageValue2013]. This result is captured as reusable evidence in the collation dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which class is on average higher (mean position comparison).
- **Data Type:** Multiclass scatterplot with moderate-to-high point counts per class (e.g., ~50–75).
- **Audience:** Users performing aggregate comparisons where retaining all points is important (no forced aggregation shown).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Point overlap becomes so severe that classes are no longer visually separable.
- **Reason:** The evidence here only covers the tested cardinalities and rendering constraints; extreme overplotting beyond that scope may behave differently [@gleicherPerceptionAverageValue2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher density can make individual points harder to inspect for non-aggregate tasks.
- **The Risk:** Keeping all points may increase perceived clutter even if mean-comparison accuracy is unaffected.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Downsampling aggressively to “help users see the mean.”
- **Why it fails:** In the extracted evidence, increasing point count did not show an accuracy penalty for the aggregate mean-comparison task under color-hue encoding [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** You removed many points but users still struggle (or accuracy does not improve) on mean-comparison questions.
- **The Test:** Compare user accuracy on the same mean-comparison question before vs. after downsampling; if unchanged, the downsampling isn’t helping the target task.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Restore the original point count for the classes involved in the comparison.
- **Best Fix:** Keep point count intact and prioritize a strong class encoding (color hue) for the aggregate task, relying on aggregation robustness rather than sampling away data [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

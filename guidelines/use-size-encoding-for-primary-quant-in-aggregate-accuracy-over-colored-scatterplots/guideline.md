---
id: use-size-encoding-for-primary-quant-in-aggregate-accuracy-over-colored-scatterplots
title: Prefer Q1 Size/Area Encodings Over Colored Scatterplots for Aggregate Accuracy
bibliography: references.bib
description: For aggregate tasks, designs that encode Q1 using size/area can outperform
  colored scatterplots in accuracy rankings.
labels:
- chart:scatter
- task:aggregate
- visual:area
- visual:color
- impact:accuracy
- data:quantitative
- data:categorical
- complexity:multivariate
---

## The Rule <!-- role: advice -->

When optimizing for aggregate-task accuracy, allow encodings where the primary quantitative field (Q1) is mapped to size/area (Q1:area) rather than forcing a colored scatterplot (N:color-hue on x/y).

## The Logic <!-- role: reason -->

In aggregate accuracy, size/area-based Q1 designs (E-7/E-8) are in the top rank group, while colored scatterplots (E-5/E-6) are in a lower rank group [@kimAssessingEffectsTask2018]. The collation frames this as task-dependent guidance: summary/aggregate objectives can change what “best” means [@zengReviewCollationGraphical2023].

- **The Principle:** Task-dependent channel effectiveness for aggregates
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare aggregate properties across categories (aggregate).
- **Data Type:** Trivariate point-based displays (Q1, Q2, N).
- **Audience:** Analysts making summary judgments rather than reading precise individual values.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user must also do retrieve-value or sort tasks on Q1 with high precision.
- **Reason:** For value tasks, Q1:area designs (E-7/E-8) rank worse than many position-based Q1 designs for accuracy/time (e.g., retrieve-value accuracy/time) [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Precision for reading exact Q1 values.
- **The Risk:** Size/area encodings can make fine-grained comparisons harder when users switch back to value tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always forbid size/area for quantitative fields because it is typically worse for value reading.
- **Why it fails:** For aggregate accuracy in this study, Q1:area designs are not penalized and can rank above colored scatterplots [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Q1 is encoded by bubble size/area rather than an axis.
- **The Test:** If your task is aggregate and your current recommendation is a colored scatterplot (E-5/E-6-like), compare against a Q1:area alternative (E-7/E-8-like) and expect potentially better aggregate accuracy per the ranking groups [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a Q1:area design (E-7/E-8-like) for aggregate-task modes.
- **Best Fix:** Implement task-aware policies: include Q1:area candidates for aggregate tasks, while still reserving Q1-on-position designs for retrieve-value/sort tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

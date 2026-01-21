---
id: prefer-cool-warm-for-aggregate-task-condition-2
title: Prefer Cool-Warm for Aggregate Accuracy (When the Task Matches Aggregate-2)
bibliography: references.bib
description: In the extracted aggregate-2 condition, the cool-warm colormap ranked
  highest for accuracy.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- condition:aggregate-2
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If your aggregate task matches the extracted “aggregate-2” condition, use a cool-warm colormap to maximize accuracy among the tested options.

## The Logic <!-- role: reason -->

In the extracted aggregate-2 accuracy ranking, cool-warm (E-6) is ranked first, ahead of rainbow (E-9) and blue-yellow (E-8), with significance pairs indicating cool-warm outperformed multiple other colormaps in that condition.

- **The Principle:** For some aggregate judgments, particular colormap families can improve accuracy.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as collated for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Aggregate judgment corresponding to the extracted “aggregate-2” task entry.
- **Data Type:** Continuous quantitative spatial field.
- **Audience:** General audiences or analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s real goal is pointwise value lookup (retrieve-value).
- **Reason:** The extracted retrieve-value ranking places rainbow above cool-warm. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may reduce performance on tasks that do not align with aggregate-2 (e.g., retrieve-value).
- **The Risk:** Misapplying the aggregate-2 rule to a different aggregate formulation could negate the expected benefit. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using rainbow by default for every quantitative map task.
- **Why it fails:** The extracted knowledge shows at least one aggregate condition (aggregate-2) where cool-warm is ranked above rainbow. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Users make frequent errors on your aggregate question even though they can do pointwise reading.
- **The Test:** A/B test cool-warm vs. your current scheme on the specific aggregate question matching aggregate-2; verify accuracy improvement. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the colormap to cool-warm for this view.
- **Best Fix:** If your product supports task-aware recommendations, conditionally select cool-warm only when the user is performing an aggregate-2-like task. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

---
id: do-not-expect-colormap-to-matter-for-aggregate-task-condition-1
title: Do Not Rely on Colormap Choice to Improve Aggregate Accuracy (When No Differences
  Are Observed)
bibliography: references.bib
description: In one aggregate condition from the extracted results, all tested colormaps
  were grouped as equivalent for accuracy.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- condition:aggregate-1
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When your aggregate task matches the extracted “aggregate-1” condition, do not choose a colormap expecting accuracy gains—treat the tested colormaps as equivalent.

## The Logic <!-- role: reason -->

In the extracted results, the aggregate-1 accuracy ranking places all nine designs in a single tied group and records no significant pairwise differences.

- **The Principle:** For some aggregate judgments, colormap choice may not change accuracy among common schemes.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as structured and reported for visualization recommendation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Aggregate judgment corresponding to the extracted “aggregate-1” task entry (as encoded in the knowledge record).
- **Data Type:** Continuous quantitative spatial field.
- **Audience:** General audiences or analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your aggregate task matches a different condition than “aggregate-1” (e.g., the extracted “aggregate-2” condition).
- **Reason:** The extracted results show a non-tied ranking and significance relationships in aggregate-2, so colormap can matter there. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a potential tuning knob (colormap) for improving accuracy in this condition.
- **The Risk:** If you misclassify the user task and it actually aligns with aggregate-2, you may miss a meaningful accuracy improvement. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Spending time iterating colormaps to “optimize accuracy” for this aggregate condition without validating task alignment.
- **Why it fails:** The extracted aggregate-1 ranking reports no differentiation among the tested colormaps. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple colormap variants yield indistinguishable user accuracy in quick tests for your aggregate question.
- **The Test:** Run a small within-subject pilot across a few colormaps; if accuracy stays flat, treat colormap as a non-accuracy decision for this task condition. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pick colormap based on non-accuracy constraints you care about (e.g., consistency within your product), since accuracy improvements are not evidenced here.
- **Best Fix:** Re-evaluate the task framing; if the real user goal is closer to the extracted aggregate-2 condition, follow the aggregate-2 guideline instead. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

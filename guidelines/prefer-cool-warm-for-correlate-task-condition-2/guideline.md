---
id: prefer-cool-warm-for-correlate-task-condition-2
title: Prefer Cool-Warm for Correlate Accuracy (When the Task Matches Correlate-2)
bibliography: references.bib
description: In the extracted correlate-2 condition, cool-warm ranked highest for
  accuracy, with significant advantages over multiple schemes.
labels:
- chart:heatmap
- task:correlate
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- condition:correlate-2
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If your correlate task matches the extracted “correlate-2” condition, use a cool-warm colormap to maximize accuracy among the tested options.

## The Logic <!-- role: reason -->

The extracted correlate-2 ranking places cool-warm (E-6) first, ahead of spectral (E-7), blue-yellow (E-8), and cubehelix (E-4). The recorded significance pairs show cool-warm significantly outperformed multiple other colormaps in that condition.

- **The Principle:** For some correlation-related judgments in continuous maps, colormap choice can measurably change accuracy.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as collated into structured recommendation knowledge by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correlate judgment corresponding to the extracted “correlate-2” task entry.
- **Data Type:** Continuous quantitative spatial field.
- **Audience:** General audiences or analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is retrieve-value (pointwise quantity lookup).
- **Reason:** The extracted retrieve-value ranking places rainbow above cool-warm. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may trade off performance for other tasks that rank different colormaps higher.
- **The Risk:** If your “correlate” interaction is actually closer to correlate-1 (the other extracted correlate condition), you may not see gains. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing a colormap based solely on its performance for retrieve-value and assuming it also helps correlation judgments.
- **Why it fails:** The extracted evidence shows task-conditional rankings; correlate-2 differs from retrieve-value. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently misjudge the correlate-2-like relationship even when the same map supports value lookups.
- **The Test:** A/B test cool-warm vs. your current colormap on the exact correlate question; verify accuracy improvement. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the colormap to cool-warm for this correlate view.
- **Best Fix:** Implement task-aware colormap selection: cool-warm for correlate-2-like tasks, rainbow for retrieve-value tasks. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

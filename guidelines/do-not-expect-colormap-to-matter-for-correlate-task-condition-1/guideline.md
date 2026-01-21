---
id: do-not-expect-colormap-to-matter-for-correlate-task-condition-1
title: Do Not Rely on Colormap Choice to Improve Correlate Accuracy (When Only Cool-Warm
  Differs)
bibliography: references.bib
description: In the extracted correlate-1 condition, most colormaps were tied, with
  cool-warm separated; do not expect fine-grained differences among the tied set.
labels:
- chart:heatmap
- task:correlate
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- condition:correlate-1
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If your correlate task matches the extracted “correlate-1” condition, do not expect accuracy differences among the tied colormaps; treat them as interchangeable unless you are specifically comparing against cool-warm.

## The Logic <!-- role: reason -->

The extracted correlate-1 ranking groups eight colormaps together and places cool-warm (E-6) as the only separated item, while recording no significant pairs for that condition.

- **The Principle:** For some correlation-related judgments, many colormap choices may be effectively equivalent in accuracy.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as collated and encoded in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correlate judgment corresponding to the extracted “correlate-1” task entry.
- **Data Type:** Continuous quantitative spatial field.
- **Audience:** General audiences or analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your correlation task aligns with the extracted “correlate-2” condition.
- **Reason:** Correlate-2 has a ranked ordering with recorded significant pairs; colormap choice can matter there. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may stop searching for marginal accuracy gains via colormap tweaks among the tied options.
- **The Risk:** If your task is actually closer to correlate-2, you could miss a measurable improvement. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Over-optimizing within the tied set (e.g., swapping cubehelix vs. spectral) to chase accuracy in correlate-1.
- **Why it fails:** The extracted ranking treats these colormaps as a single equivalence class for that condition. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Changing colormaps does not change user accuracy on the correlate-1-like question.
- **The Test:** Compare at least one tied colormap vs. another tied colormap on your correlate-1-like task; if accuracy is indistinguishable, stop tuning within the tied set. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pick a colormap based on constraints other than accuracy (since accuracy differences are not evidenced among the tied set).
- **Best Fix:** If accuracy is still insufficient, revise the task framing or interaction rather than swapping among the tied colormaps. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

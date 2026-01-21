---
id: use-rainbow-for-quantity-estimation-in-continuous-maps
title: Use a Rainbow Colormap for Quantity Estimation in Continuous Maps
bibliography: references.bib
description: For point-specific quantity lookup in continuous pseudocolor maps, prefer
  a rainbow colormap over the other tested schemes.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a rainbow colormap when users must estimate a numeric value at a specific location in a continuous quantitative map.

## The Logic <!-- role: reason -->

A rainbow colormap produced the best (rank-1) accuracy for the retrieve-value task among the nine tested colormaps in the extracted results.

- **The Principle:** Colormap choice can materially change pointwise quantity estimation accuracy in continuous maps.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as collated and structured for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve/estimate the value at a particular map location (point lookup).
- **Data Type:** Continuous quantitative spatial field displayed as a pseudocolor map.
- **Audience:** General audiences or analysts doing pointwise reading.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are optimizing for tasks other than retrieve-value (e.g., gradient or pattern tasks as represented by separate task entries in the extracted results).
- **Reason:** The extracted knowledge reports different rankings for other tasks (e.g., aggregate-2, correlate-2), so this rule is only supported for retrieve-value. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may be choosing a colormap that is not top-ranked for other tasks in the same knowledge record.
- **The Risk:** If users actually need pattern/structure judgments instead of pointwise lookup, performance may not match this rule’s intended benefit. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using greyscale (or other lower-ranked schemes) for pointwise quantity lookup because it “looks neutral.”
- **Why it fails:** In the extracted retrieve-value ranking, greyscale is last and rainbow is first. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or disagree when asked to click/identify a location matching a target value.
- **The Test:** Run a quick pilot where users perform point-value lookup; if errors are high, compare against a rainbow mapping as the baseline recommended by this rule. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the continuous map’s colormap to rainbow.
- **Best Fix:** If the overall analysis task isn’t retrieve-value, change colormap strategy to match the task-specific guideline (see other rules derived from the same extracted results). [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

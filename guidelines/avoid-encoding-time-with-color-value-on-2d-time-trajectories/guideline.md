---
id: avoid-encoding-time-with-color-value-on-2d-time-trajectories
title: Avoid Encoding Time with Color Value
bibliography: references.bib
description: Encoding time with color value/saturation on 2D+time trajectories ranks
  worse than length- or size-based time encodings for time judgments.
labels:
- chart:trajectory
- task:aggregate
- visual:color
- impact:accuracy
- data:temporal
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

Do not use **color value/saturation** as the primary encoding for **time** on a 2D+time trajectory; prefer a non-color time encoding among the studied options.

## The Logic <!-- role: reason -->

Color value ramps require fine discrimination to identify intermediate positions along a gradient. In the collated time-task rankings, the time-as-color designs appear below length- and/or size-based time encodings in the ranked outcomes, indicating worse accuracy for the time-related task [@zengReviewCollationGraphical2023].

- **The Principle:** Fine-grained time estimation along a continuous value gradient is perceptually demanding.
- **The Evidence:** Perin et al.’s experimental comparisons of time encodings, as recorded and ranked in the collation [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate or locate time along a trajectory (recorded as aggregate in the collation dataset for this paper).
- **Data Type:** Quantitative time progression along a path.
- **Audience:** General users doing quick lookups, not careful measurement.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking users to judge intermediate time positions (e.g., your task does not require locating 25/50/75% time points).
- **Reason:** The evidence in the structured results is tied to the recorded task setup for time judgments; if your goal differs substantially, this specific tradeoff may not apply [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a simple, continuous-looking “timeline” gradient along the path.
- **The Risk:** Switching away from time-as-color may require tick marks (length) or thickness changes (size), which can add clutter [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep time on a subtle value ramp and just add a legend.
- **Why it fails:** The limitation is perceptual discrimination along the path; a legend does not improve the ability to pinpoint intermediate locations on the ramp [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot reliably locate midpoints (e.g., “halfway through time”) and answers cluster near endpoints.
- **The Test:** Ask users to click the 50% time point on several trajectories and observe consistent deviations relative to a tick-based ground truth [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace time-as-color with segment-length ticks for time.
- **Best Fix:** Use segment-length ticks for time and reserve color value/saturation for speed (if needed), aligning with the best-performing family of encodings in the collated outcomes [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

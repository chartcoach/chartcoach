---
id: avoid-encoding-speed-with-size-on-curved-2d-time-trajectories
title: Avoid Encoding Speed with Size on Curved Trajectories
bibliography: references.bib
description: On curved 2D+time trajectories, encoding speed by size performs worse
  than color- or length-based alternatives for speed judgments.
labels:
- chart:trajectory
- task:find-extremum
- visual:area
- impact:accuracy
- data:temporal
- data:quantitative
- audience:general
- shape:curved
---

## The Rule <!-- role: advice -->

Do not encode **speed** with **size/width** on **curved** 2D+time trajectories; prefer a non-size alternative among the studied options.

## The Logic <!-- role: reason -->

On curved paths, size/width changes are harder to decode consistently along varying curvature. In the collated accuracy rankings for the extrema-finding task, the speed-as-color design outranks the speed-as-size designs for curved paths, and size-based speed encodings appear lower in the ranked lists [@zengReviewCollationGraphical2023].

- **The Principle:** Curvature interferes with perception of width/size along a path, reducing reliability for locating extrema.
- **The Evidence:** Perin et al.’s experiment results on curved trajectories, as captured in Zeng & Battle’s structured rankings [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find fastest/slowest points on a curved trajectory (find-extremum).
- **Data Type:** Quantitative speed varying along a curved 2D path with time as an additional dimension.
- **Audience:** General users who need quick read-offs.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your trajectory is straight (not curved).
- **Reason:** The rule is specifically about the curved-shape condition where size-based speed performs relatively poorly in the collated results [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose an encoding option if color is already reserved for another purpose.
- **The Risk:** Switching away from size may require adding another channel or introducing ticks, which can add complexity [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increase stroke-width range dramatically to “make size more obvious.”
- **Why it fails:** The problem is not only salience; it’s the interaction between curvature and size perception along the path, which still leads to worse performance relative to other tested encodings [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly pick the wrong point for max/min speed on curved segments.
- **The Test:** Run a quick extrema-picking test on a few curved paths; compare error rates between size-based speed and a non-size speed variant (as in the study’s task style) [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move speed from size/width to color value/saturation.
- **Best Fix:** Use segment-length ticks to support time, and encode speed with color value/saturation (or rely on segment-length alone if you must stay single-channel) [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

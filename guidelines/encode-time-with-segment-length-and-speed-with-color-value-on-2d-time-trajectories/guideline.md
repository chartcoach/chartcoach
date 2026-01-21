---
id: encode-time-with-segment-length-and-speed-with-color-value-on-2d-time-trajectories
title: Encode Time with Segment Length and Speed with Color Value
bibliography: references.bib
description: For 2D+time trajectories, prefer segment-length ticks for time and color
  value/saturation for speed to support accurate time and speed judgments.
labels:
- chart:trajectory
- task:find-extremum
- task:aggregate
- visual:length
- visual:color
- impact:accuracy
- data:temporal
- data:quantitative
- audience:general
- domain:movement-data
---

## The Rule <!-- role: advice -->

Encode **time** using **segment length** (ticks along the path) and encode **speed** using **color value/saturation** on the same 2D+time trajectory.

## The Logic <!-- role: reason -->

Using segment-length ticks externalizes time progression along the path, while color value/saturation provides a direct visual cue for speed variations. In the collated results, the time+speed design using **length + color-saturation** ranked at/near the top for both tasks compared to alternatives that relied on size or time-only encodings [@zengReviewCollationGraphical2023].

- **The Principle:** Separate the two quantitative variables into distinct, readily decodable channels (length for time structure; color value for speed signal).
- **The Evidence:** Rankings from Perin et al.’s trajectory study, collated and structured by Zeng & Battle [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify speed extrema and/or estimate time position along a trajectory (tasks recorded as find-extremum and aggregate in the collation) [@zengReviewCollationGraphical2023].
- **Data Type:** 2D+time trajectories with quantitative time and speed.
- **Audience:** General users performing quick perceptual judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot add ticks/segment-length encoding (e.g., design constraints that prohibit tick marks).
- **Reason:** This rule depends on segment-length being available as a time carrier; without it, you must choose a different time encoding [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra visual elements (ticks) and a second visual channel (color) increase visual complexity.
- **The Risk:** Over-encoding can create clutter, especially when multiple trajectories are shown (risk implied by the need to compare multiple alternatives in the same encoding family) [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encode both time and speed via width/size and color together without segment-length.
- **Why it fails:** In the collated rankings, size-based combinations were often not top-performing relative to the length+color approach for the recorded tasks [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to point to a requested time location or misidentify fast/slow regions despite clear variation.
- **The Test:** Ask someone to (1) pick the fastest point and (2) pick the 50% time point; compare error rates across your encoding variants (the original study used these kinds of judgments) [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add tick marks to create segment-length encoding for time; keep speed on color value/saturation.
- **Best Fix:** Rebuild the trajectory styling so time is primarily carried by segment-length and speed is primarily carried by color value/saturation, minimizing reliance on size/width for either variable [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

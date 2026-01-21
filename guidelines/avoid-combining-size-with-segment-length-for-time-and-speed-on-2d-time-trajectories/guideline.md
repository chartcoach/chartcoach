---
id: avoid-combining-size-with-segment-length-for-time-and-speed-on-2d-time-trajectories
title: Avoid Combining Size with Segment Length for Time and Speed
bibliography: references.bib
description: On 2D+time trajectories, the size+segment-length combination ranks poorly
  relative to other tested designs for time and speed judgments.
labels:
- chart:trajectory
- task:find-extremum
- task:aggregate
- visual:area
- visual:length
- impact:accuracy
- data:temporal
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

Avoid pairing **size/width** with **segment-length ticks** as a combined time–speed encoding strategy on 2D+time trajectories when accuracy matters.

## The Logic <!-- role: reason -->

In the collated rankings for this study, the size+length double-encoding variants sit below the best-performing length-only or length+color families for the recorded tasks. This indicates interference or reduced clarity when both cues coexist in the tested setting [@zengReviewCollationGraphical2023].

- **The Principle:** Two simultaneous structural cues along a path (width changes plus tick segmentation) can conflict or reduce discriminability.
- **The Evidence:** Perin et al.’s comparative performance outcomes across the nine studied encodings, as collated by Zeng & Battle [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find extrema in speed and/or estimate time position (find-extremum, aggregate as recorded in the collation).
- **Data Type:** Quantitative time and speed along a 2D path.
- **Audience:** General users under time pressure or performing quick readings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are only encoding one variable (time-only or speed-only) and segment-length is not used.
- **Reason:** This guideline is specifically about the combined size+segment-length pairing, not about size or length used alone [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer redundant cues along the path (you give up “extra” visual emphasis from thickness).
- **The Risk:** If color is unavailable and you remove size, you may need to rely on length alone, which may increase reliance on inference for speed [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add both ticks and thick–thin variation “to make it obvious.”
- **Why it fails:** The collated rankings indicate this pairing is not among the most accurate for the recorded tasks, suggesting added complexity does not translate into better judgments [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users misread either the time location (tick progression) or the speed change (thickness), especially where changes co-occur.
- **The Test:** A/B test your size+length encoding against length-only (ticks) and length+color; compare extrema selection and time-point selection accuracy [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep segment-length ticks and remove size/width variation.
- **Best Fix:** Use segment-length ticks for time, and if you need a second channel for speed, use color value/saturation instead of size [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

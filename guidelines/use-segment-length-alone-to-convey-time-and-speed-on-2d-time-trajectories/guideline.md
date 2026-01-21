---
id: use-segment-length-alone-to-convey-time-and-speed-on-2d-time-trajectories
title: Use Segment Length Alone to Convey Both Time and Speed
bibliography: references.bib
description: When you need one channel, encode time via segment-length ticks so speed
  can be inferred from tick spacing on 2D+time trajectories.
labels:
- chart:trajectory
- task:find-extremum
- task:aggregate
- visual:length
- impact:accuracy
- data:temporal
- data:quantitative
- audience:general
- constraint:single-encoding
---

## The Rule <!-- role: advice -->

If you must use a single visual mechanism, encode the trajectory with **segment-length ticks** so **time is represented by tick progression** and **speed is inferred from spacing**.

## The Logic <!-- role: reason -->

Segment-length provides a structured discretization along the path: the placement of ticks provides time progression, and the gaps between ticks imply speed. In the collated results, the length-based time encoding appears among the top performers for both recorded tasks relative to several alternatives that rely on size or time-only color encoding [@zengReviewCollationGraphical2023].

- **The Principle:** Let one structured encoding support two readings: direct time position + inferred speed through spacing.
- **The Evidence:** Perin et al.’s tested trajectory encodings as collated into ranked outcomes by Zeng & Battle [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quick judgments of speed extrema and approximate time position when display space or channels are limited.
- **Data Type:** Single-path 2D+time trajectories where both time and speed matter.
- **Audience:** General users doing lightweight analysis.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need users to read time using a continuous color ramp rather than discrete ticks.
- **Reason:** This rule relies on discrete segmentation; if discrete ticks are undesirable, this encoding strategy does not match the intended reading method [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Segment ticks add marks and can consume visual bandwidth along the path.
- **The Risk:** Dense ticking can become hard to parse visually if the trajectory is displayed very small (a general risk implied by the need to compare time encodings by performance) [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Remove the tick structure and assume users can infer time from the path geometry alone.
- **Why it fails:** In the collated designs, “no explicit time” variants rank worse for the time-related task than explicit time encodings [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Tick spacing does not visibly change where speed changes, or tick progression does not clearly communicate time.
- **The Test:** Ask a user to locate 25%, 50%, and 75% elapsed time and compare against the intended points; also ask for min/max speed and see if answers align with tight/wide tick spacing [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add or adjust tick placement so segment-length meaning is visible and consistent along the path.
- **Best Fix:** Use segment-length ticks as the primary time scaffold, and only add a second channel (e.g., color value/saturation) if users still misread speed extrema [@perinAssessingGraphicalPerception2018; @zengReviewCollationGraphical2023].

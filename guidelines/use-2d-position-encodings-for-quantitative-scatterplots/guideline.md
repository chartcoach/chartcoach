---
id: use-2d-position-encodings-for-quantitative-scatterplots
title: Encode Two Quantitative Variables with X/Y Position in a Scatterplot
bibliography: references.bib
description: Use a point mark with linear x/y position to represent two quantitative
  fields in a scatterplot.
labels:
- chart:scatter
- task:retrieve-value
- visual:position
- impact:clarity
- data:quantitative
- audience:general
- source:collated
---

## The Rule <!-- role: advice -->

Encode two quantitative variables using x-position and y-position on linear scales with point marks (i.e., a standard 2D scatterplot).

## The Logic <!-- role: reason -->

Using position on orthogonal axes provides a direct spatial mapping for two quantitative fields, forming the baseline scatterplot design discussed as the core reference design in the collated knowledge.

- **The Principle:** Two-variable quantitative spatialization via orthogonal position
- **The Evidence:** The collated schema records a scatterplot design with quantitative fields mapped to `positionX` and `positionY` using `linear` scales and `point` marks [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Working with scatterplots across common analysis intents (e.g., correlation, clustering, filtering, retrieving values, distribution/anomaly characterization).
- **Data Type:** Two quantitative fields (bivariate quantitative data).
- **Audience:** General audiences using standard visualization tools that generate basic scatterplots.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not visualizing two quantitative fields.
- **Reason:** This guideline is specifically scoped to the recorded design: two quantitative variables mapped to x/y position; it does not claim suitability for nominal/ordinal axes or alternative encodings [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limits you to two quantitative dimensions as primary axes in a single view.
- **The Risk:** If your analysis requires other dimensions or alternative representations, the basic encoding may be insufficient—but this guideline does not provide evidence-based alternatives [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Putting a quantitative field on x/y but using a non-linear or non-quantitative scale without a clear reason.
- **Why it fails:** It deviates from the recorded baseline design (linear x/y mapping for quantitative fields), making the visualization no longer match the evidence captured in the collation [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart is not a point-based x/y plot (e.g., one axis is not continuous/linear).
- **The Test:** Verify the specification: both axes use quantitative fields on `positionX`/`positionY` with `linear` scales and `point` marks [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Map the two quantitative fields directly to x and y and set both scales to linear.
- **Best Fix:** Rebuild as a standard point scatterplot with `positionX`/`positionY` linear encodings for the two quantitative fields [@zengReviewCollationGraphical2023; @sarikayaScatterplotsTasksData2018].

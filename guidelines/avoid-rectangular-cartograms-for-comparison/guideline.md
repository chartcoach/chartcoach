---
id: avoid-rectangular-cartograms-for-comparison
title: Avoid Rectangular Cartograms for Area Comparison
bibliography: references.bib
description: Rectangular cartograms yield the lowest accuracy for sorting and comparing
  data values.
labels:
- chart:cartogram
- chart:rectangular-cartogram
- task:compare
- task:sort
- visual:area
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not use rectangular cartograms if the primary task involves sorting regions by value or comparing the size of different areas.

## The Logic <!-- role: reason -->
Human perception struggles to accurately compare the areas of rectangles when they have varying aspect ratios (e.g., a tall, thin rectangle vs. a square one).
*   **The Principle:** Area Perception Bias.
*   **The Evidence:** Experiments collated in [@zeng_review_2023] from [@nusrat_evaluating_2018] show that rectangular cartograms (E-2) consistently ranked last in accuracy for `sort` (comparison) and `find top-k` tasks compared to contiguous, non-contiguous, and Dorling variations.

## Where to Apply <!-- role: context -->
*   **User Goal:** Ranking countries or states by a metric (e.g., GDP, population).
*   **Data Type:** Quantitative data mapped to area.
*   **Audience:** General audiences who need to make quick, accurate judgments of size.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization is a stylized schematic (like a transit map) where topology is more important than precise value comparison.
*   **Reason:** Rectangular cartograms excel at preserving adjacency relationships, even if size comparison suffers [@nusrat_evaluating_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to "pack" shapes neatly into a grid-like structure.
*   **The Risk:** The visualization may look less "orderly" or "clean" than a rectangular layout.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding labels to rectangles to compensate for poor readability.
*   **Why it fails:** While labels provide values, the visual encoding (area) remains misleading or difficult to process, creating a Stroop-like interference.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using rectangles of vastly different aspect ratios to represent values?
*   **The Test:** Pick two rectangles of similar area but different shapes. Can you instantly tell which is larger?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a Dorling (circle) cartogram for easier area comparison.
*   **Best Fix:** Use a contiguous cartogram if shape preservation is required alongside comparison.

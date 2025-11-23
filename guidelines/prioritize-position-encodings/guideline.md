---
id: prioritize-position-encodings
title: Prioritize Position Encodings for Quantitative Data
bibliography: references.bib
description: Use position on a common scale as the primary encoding for quantitative
  data to maximize accuracy.
labels:
- chart:general
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
Encode the most important quantitative data using position along a common scale (e.g., standard bar charts, scatterplots). Prefer this over length, angle, area, or color saturation.

## The Logic <!-- role: reason -->
Human visual perception extracts quantitative information with varying degrees of accuracy depending on the elementary task required.
*   **The Principle:** Hierarchy of Graphical Perception. Theoretical and experimental evidence establishes a distinct ranking of perceptual tasks.
*   **The Evidence:** The collation by [@zeng_review_2023] of the seminal work by [@cleveland_graphical_1984] confirms that "Position along a common scale" (Rank 1) is the most accurate method for extracting values. This outperforms "Length" (Rank 3), "Angle" (Rank 5/6), "Area" (Rank 6), and "Color Saturation" (Rank 7).

## Where to Apply <!-- role: context -->
*   **User Goal:** When the viewer needs to make precise comparisons or rank values accurately.
*   **Data Type:** Quantitative variables (interval or ratio data).
*   **Audience:** Any audience requiring accurate data interpretation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Constraints on aspect ratio or available space prevent a shared axis (e.g., small multiples with different scales, though this introduces risk).
*   **Reason:** Sometimes layout constraints force the use of "Position on non-aligned scales," which is the second-best option in the hierarchy [@cleveland_graphical_1984].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual variety or "infographic" aesthetics often rely on area (bubbles) or angle (donuts), which must be sacrificed for accuracy.
*   **The Risk:** Using lower-ranked encodings (like area or saturation) for primary data leads to significantly higher rates of error in user judgment [@cleveland_graphical_1984].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using bubble charts (Area) or heatmaps (Color Saturation) for precise comparison tasks.
*   **Why it fails:** Users cannot accurately judge linear differences via area or color intensity; the error rates are significantly higher than position judgments.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the data mapped to the size of a circle, the angle of a wedge, or the shade of a color?
*   **The Test:** Ask yourself: "Do I have to estimate the area or color to know the value?" If yes, convert to a position-based chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels to area/color charts to provide the exact numbers (mitigating the perceptual error).
*   **Best Fix:** Change the chart type to a bar chart, dot plot, or scatterplot where data is mapped to x or y coordinates.

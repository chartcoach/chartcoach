---
id: identify-extremum-size
title: Use Size Encodings for Finding Extremum Values
bibliography: references.bib
description: Map quantitative data to size when users need to identify minimum and
  maximum values accurately.
labels:
- chart:bubble
- chart:scatter
- task:find-extremum
- visual:area
- visual:size
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Encode quantitative data using size (area/radius) when the primary task is to accurately identify the minimum or maximum values in a set.

## The Logic <!-- role: reason -->
When users scan a collection of items to find the smallest or largest outliers, size provides the most accurate signal among common glyph channels.
*   **The Principle:** Discriminability of Extremes
*   **The Evidence:** According to [@zeng_review_2023], which collates results from [@chung_how_2016], Size (area-circle) ranked 1st in accuracy for "find-extremum" tasks, outperforming Shape, Texture, Value, Orientation, and Hue.

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding the "best" or "worst" performers, or identifying outliers (min/max).
*   **Data Type:** Quantitative data mapped to point marks (glyphs).
*   **Audience:** Users performing exploratory analysis or anomaly detection.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify the extremum *quickly* rather than accurately.
*   **Reason:** While Size was the most accurate, the study found that Color Value (Saturation) was significantly faster for identifying extremums (Rank 1 in time vs. Rank 5 for Size) [@chung_how_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Size encodings suffer from occlusion if marks overlap, and human perception of area is non-linear (often requiring correction).
*   **The Risk:** Large bubbles may obscure other data points; small bubbles may become invisible.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using orientation (tilt) to show magnitude for min/max tasks.
*   **Why it fails:** Orientation ranked poorly (5th) for extremum accuracy in the underlying experiment [@chung_how_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using color or tilt to highlight the largest item?
*   **The Test:** Ask a user to point to the highest value. If they hesitate or have to read a legend, the channel is not distinct enough.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Map the variable to the radius/area of the mark.
*   **Best Fix:** Ensure the size range is large enough to make the difference between the largest and second-largest values perceptibly distinct.

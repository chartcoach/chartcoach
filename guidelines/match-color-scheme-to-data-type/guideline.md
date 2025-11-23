---
id: match-color-scheme-to-data-type
title: Match Color Scheme to Data Type
bibliography: references.bib
description: Determine whether to use gradients or distinctive hues based on whether
  the data is continuous or categorical.
labels:
- visual:color
- data:categorical
- data:continuous
- impact:clarity
---

## The Rule <!-- role: advice -->
Use color gradients for continuous data and distinctive colors (hues) for categorical data.

## The Logic <!-- role: reason -->
The choice of color must align with the structure of the data to communicate correctly.
*   **The Principle:** Visual Correspondence.
*   **The Evidence:** According to [@muth_colorguide_2018], color gradients communicate that a value is "a bit higher or lower than the color next to me" (progression). In contrast, distinctive hues communicate that a category is independent: "I’m by myself and have nothing do to with all these other colors here!"

## Where to Apply <!-- role: context -->
*   **User Goal:** Selecting the foundational palette for a visualization.
*   **Data Type:** 
    *   **Continuous:** Data progressing from low to high (e.g., unemployment rates).
    *   **Categorical:** Data with distinct groups (e.g., political parties).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-cardinality categorical data where distinct hues run out.
*   **Reason:** The text implies distinctive colors are for distinct categories, but limits are often reached where distinction becomes impossible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot mix these metaphors easily without confusing the reader about the relationship between data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a gradient for categorical items (implies ranking where there is none).
*   **The Wrong Fix:** Using distinct hues for continuous data (implies separation rather than progression).

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the color change imply a change in magnitude (light to dark) or a change in identity (blue to red)?
*   **The Test:** Ask if the data points can be ranked. If yes, use a gradient. If no, use distinct hues.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the palette type in your visualization tool (e.g., from sequential to qualitative).

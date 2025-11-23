---
id: use-shades-to-emphasize-order
title: Use Shades to Emphasize Underlying Order
bibliography: references.bib
description: Double-encode values using shades to make ranked categorical charts readable.
labels:
- visual:color
- visual:brightness
- chart:treemap
- chart:bar
- task:rank
---

## The Rule <!-- role: advice -->
Use a quantitative color scale (shades) for categorical data if you want to emphasize an underlying number, rank, or count associated with those categories.

## The Logic <!-- role: reason -->
Categories often mask underlying numbers, such as the count of sub-categories, a rank (1st, 2nd, 3rd), or a value already encoded by size. By matching the color intensity to this underlying value, you improve readability and reduce visual chaos ("confetti"). For example, a treemap is easier to read if the box color intensity matches the box size, rather than assigning random hues to every category [@muth_quantitative_vs_qualitative_2021].

## Where to Apply <!-- role: context -->
*   **Chart Types:** Treemaps, symbol maps, and scatterplots.
*   **Data Type:** Categorical data that is sorted or sized by a quantitative variable.
*   **User Goal:** Quick scanning of high-value vs. low-value items.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Encoding a *new* variable with color that is not already encoded by position or size.
*   **Reason:** While possible, "using color to encode a new variable makes most charts incredibly hard to read" because the user has to do too much mental math [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->
*   **The Risk:** If the underlying order isn't obvious (e.g., grouped bars), users may not understand why one bar is darker than another without explicit explanation or double-encoding.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Coloring a treemap with 50 different hues for 50 different industries.
*   **Why it fails:** It creates a "confetti" effect that is overwhelming and hard to read.

## How to Check <!-- role: check -->
*   **The Test:** Does the color intensity (lightness/darkness) correlate with the size or position of the element?
*   **Visual Sign:** In a scatterplot, do the dots get darker as they move right or up? If yes, you are successfully using shades to emphasize order.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Change the color scale from categorical (hues) to sequential (shades of one color) that aligns with the sorting or sizing variable.

---
id: ensure-perceptible-gradient-steps
title: Ensure Perceptible Gradient Steps
bibliography: references.bib
description: Avoid subtle UI gradients in data visualization to ensure readers can
  distinguish between data values.
labels:
- visual:color
- chart:choropleth
- chart:heatmap
- impact:readability
---

## The Rule <!-- role: advice -->
Ensure the differences between color steps in a gradient are large enough to be clearly differentiated.

## The Logic <!-- role: reason -->
Beautiful, subtle gradients designed for user interfaces often fail in data visualization because the steps blend together.
*   **The Principle:** Perceptual Differentiation.
*   **The Evidence:** [@muth_colorguide_2018] states that the main concern with gradients is ensuring the reader can "clearly differentiate between a light green and a …lighter green." Tools that create subtle UI gradients are explicitly noted as "not sufficient for the job."

## Where to Apply <!-- role: context -->
*   **User Goal:** visualizing continuous data where specific value ranges matter.
*   **Data Type:** Continuous data mapped to color (e.g., maps, heatmaps).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Purely aesthetic backgrounds.
*   **Reason:** If the gradient does not encode data, differentiation is not required.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the "smooth" or "sleek" aesthetic of subtle UI design in favor of higher contrast, stepped colors.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using standard UI design gradient tools.
*   **Why it fails:** These tools prioritize aesthetics over distinct visual steps [@muth_colorguide_2018].

## How to Check <!-- role: check -->
*   **The Test:** Use a tool like the *Chroma.js Color Palette Helper* to visualize the actual steps and ensure they are distinct.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use data-specific tools like *ColorBrewer* or *CartoColor* that optimize for perceptibility steps [@muth_colorguide_2018].

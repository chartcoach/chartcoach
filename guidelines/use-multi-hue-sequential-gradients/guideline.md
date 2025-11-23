---
id: use-multi-hue-sequential-gradients
title: Use Multi-Hue Sequential Gradients
bibliography: references.bib
description: Use multiple hues in sequential color scales to improve contrast and
  readability.
labels:
- visual:color
- data:quantitative
- impact:clarity
- chart:choropleth
- chart:heatmap
---

## The Rule <!-- role: advice -->
Use multiple hues (e.g., light yellow to dark blue) rather than a single hue (e.g., light blue to dark blue) when designing sequential color scales for ordered data.

## The Logic <!-- role: reason -->
While single-hue gradients are functional, adding a second or third hue significantly increases the color contrast between different segments of the gradient. According to @muth_which_color_scale_2021, this added contrast makes it much easier for readers to distinguish between values along the scale.

## Where to Apply <!-- role: context -->
*   **User Goal:** Visualizing continuous or ranked data where values go from low to high.
*   **Data Type:** Ordered quantitative data (e.g., income, temperature, age).
*   **Audience:** General audiences requiring clear differentiation between value steps.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict branding constraints.
*   **Reason:** If a style guide strictly mandates a monochromatic palette.
*   **Scenario:** Over-complication.
*   **Reason:** If the color shift creates a "false category" effect where users perceive the hue change as a change in data type rather than magnitude.

## The Price <!-- role: costs -->
*   **The Risk:** If the hues are not ordered by lightness properly (e.g., a rainbow scale), the visualization may mislead readers about the magnitude of the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a single hue and only varying opacity/transparency.
*   **Why it fails:** This often results in poor contrast at the lighter end of the scale, making low values hard to see against the background.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do adjacent steps in the legend look distinct or do they blur together?
*   **The Test:** Convert the chart to grayscale. If the multi-hue scale is designed correctly, the lightness values should still progress linearly from light to dark.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a second hue to the lighter end of your gradient (e.g., transition from yellow to blue instead of white to blue).
*   **Best Fix:** Use established tools like ColorBrewer or Datawrapper’s built-in gradients to select a scientifically validated multi-hue sequential palette.

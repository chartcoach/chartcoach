---
id: create-direct-color-key
title: Create a Direct Color Key with Annotations
bibliography: references.bib
description: Replace standard legends with direct text annotations to explain color
  coding and emphasize data differences.
labels:
- chart:area
- visual:color
- visual:text
- impact:clarity
- task:identify
---

## The Rule <!-- role: advice -->
Do not use a separate legend box to explain your chart colors. Instead, use text annotations placed directly on or near the data elements to create a "direct color key" that explains what the areas represent.

## The Logic <!-- role: reason -->
By placing the explanation of the data (the text) directly next to the visualization of the data (the color), you reduce the cognitive load required to understand the chart.
*   **The Principle:** Proximity and Direct Labeling.
*   **The Evidence:** @mintzer_simple_data_2024 argues that text annotations should define what the chart's areas represent, simultaneously "emphasizing the difference between them" without forcing the eye to travel back and forth to a legend.

## Where to Apply <!-- role: context -->
*   **User Goal:** When you want to emphasize the difference between two categories or values.
*   **Data Type:** Simple datasets with clear, distinct categories (e.g., "Reported" vs. "Solved" cases).
*   **Chart Type:** Area charts, line charts, or bar charts where distinct colored areas need definition.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density charts with too many categories.
*   **Reason:** If there are too many categories (e.g., 10+ lines on a chart), direct labels may overlap or clutter the visualization, making a legend necessary for legibility.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "clean" look of a chart with no text overlay, and you must manually position text rather than relying on automatic legend generation.
*   **The Risk:** If the text is poorly placed, it may obscure the data trends.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a default legend box located far from the data (e.g., at the top or bottom).
*   **Why it fails:** This separates the definition from the data, forcing the reader to scan back and forth to understand what they are looking at.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for a box containing colored squares and text at the periphery of your chart.
*   **The Test:** If you delete the legend, can you still understand what the colors mean based on the text inside the chart area?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the legend box as close as possible to the data it describes.
*   **Best Fix:** Delete the legend entirely. Add text boxes directly onto the colored areas (e.g., "Over 29,000 cases..." on the grey area, "Only 4-5% solved" on the blue area) matching the text position to the relevant color block.

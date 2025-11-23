---
id: match-key-style-to-data-style
title: Match Key Styling to Data Forms
bibliography: references.bib
description: Ensure the shapes, strokes, and outlines in the color key exactly mimic
  the data elements in the chart.
labels:
- visual:shape
- visual:color
- impact:consistency
- chart:map
- chart:line
---

## The Rule <!-- role: advice -->
Design the elements in your color key to physically resemble the data elements in the visualization, including shape, stroke, and outline.

## The Logic <!-- role: reason -->
If data points differ by form (e.g., dashed vs. solid lines, circles vs. squares) or have specific styling (e.g., white outlines), the key must reflect this. This helps readers match the key to the chart instantly. Furthermore, colors appear differently depending on their stroke; including the outline in the key ensures accurate color matching, particularly for bright colors [@muth_color_keys_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate recognition of symbols and colors.
*   **Data Type:** Locator maps, line charts with different line styles, or scatter plots with outlines.
*   **Audience:** All users, especially those with vision deficiencies who rely on form over color.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Heatmaps or simple bar charts without borders.
*   **Reason:** If the data is purely a block of color without strokes or form variation, a simple square in the key is sufficient.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. Creating custom key symbols (like a dashed line icon) takes more technical effort than standard square swatches.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using standard square color swatches for a line chart.
*   **Why it fails:** The reader has to mentally translate "Square Blue" to "Dashed Blue Line."

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart uses circles with black outlines, but the key shows squares with no outlines.
*   **The Test:** Look at the brightest color in your chart. Does it look slightly different in the key because the key lacks the contrasting outline?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a border to key swatches if the chart elements have borders.
*   **Best Fix:** Use specific icons (e.g., a line segment icon for line charts, a circle for bubble charts) that mirror the data's CSS styling.

---
id: supplement-color-encoding
title: Supplement Color with Additional Visual Encodings
bibliography: references.bib
description: Do not rely on color alone to convey meaning; use shapes, textures, or
  patterns to ensure accessibility.
labels:
- chart:bar
- chart:line
- chart:scatter
- visual:color
- visual:shape
- visual:texture
- impact:accessibility
- impact:inclusion
- data:categorical
---

## The Rule <!-- role: advice -->

Do not use color as the sole method of conveying information, indicating an action, or distinguishing a visual element. Always pair color with a redundant visual channel such as text labels, shapes, textures, sizes, or dash patterns.

## The Logic <!-- role: reason -->

Relying on color alone creates barriers for users who cannot perceive color differences, such as those with color vision deficiencies (CVD) or those viewing content on monochrome displays. By using redundant encoding, you ensure the information is perceivable through multiple senses or visual channels.

*   **The Principle:** Redundant Encoding (Perceivability).
*   **The Evidence:** The Chartability framework identifies "Content is only visual" and "Color alone used to communicate meaning" as critical failure points in visualization accessibility [@elavsky_how_2022]. Guidelines from the W3C emphasize that designers must use shapes, patterns, or text labels in addition to color so that content remains understandable without color perception [@w3c_understanding_use].

## Where to Apply <!-- role: context -->

This rule applies to any data visualization where distinct categories or statuses are represented.

*   **User Goal:** Distinguishing between different categories (e.g., "Sales" vs. "Profit") or identifying status changes (e.g., "Active" vs. "Inactive").
*   **Data Type:** Primarily categorical data in bar charts, scatter plots, and line charts.
*   **Audience:** All users, specifically ensuring inclusion for the significant population living with visual impairments or CVD [@elavsky_how_2022].

## When to Break It <!-- role: exceptions -->

*   **Scenario:** High-density sequential or ordinal data scales (e.g., heatmaps).
*   **Reason:** The source notes that this standard is difficult to apply to color schemes that scale based on numerical data. There is currently little research exploring effective strategies for applying textures to continuous scales without overwhelming the user [@elavsky_how_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** Visual simplicity. Adding textures (hatching) or varied shapes increases the visual noise (ink-to-data ratio) of the chart.
*   **The Risk:** Implementation difficulty. Many standard visualization libraries do not support data-driven textures or patterns out of the box, requiring custom development or "hacking" the tools [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Relying solely on a "colorblind-safe" palette.
*   **Why it fails:** While helpful, a safe palette does not satisfy the requirement of *redundant* encoding. If the user is viewing in grayscale or has a specific type of CVD not covered by the palette, the meaning is lost.
*   **The Wrong Fix:** Using subtle opacity changes as the only alternative.
*   **Why it fails:** Low contrast can make these changes imperceptible [@w3c_understanding_use].

## How to Check <!-- role: check -->

*   **Visual Sign:** If you print the chart in black and white, do the bars or lines look identical?
*   **The Test:** Convert the visualization to grayscale. Can you still distinguish the different categories or lines without referencing the original color key? Use tools like the Chartability workbook or browser extensions to simulate these views [@elavsky_how_2022].

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add direct text labels to the data points so users do not need to rely on a color legend.
*   **Best Fix:** Implement distinct textures (for filled areas), dash patterns (for lines), or geometric shapes (for scatter points) mapped to the same categories as the colors [@observablehq_no_use].

---
id: text-outlines-on-backgrounds
title: Use Text Outlines on Busy Backgrounds
bibliography: references.bib
description: Apply a stroke (outline) around text that sits on top of gridlines or
  other elements.
labels:
- visual:contrast
- visual:typography
- impact:legibility
---

## The Rule <!-- role: advice -->
If your text sits on other elements—even just a subtle gridline—use a text outline. This is a stroke around your letters, usually in the background color of your chart.

## The Logic <!-- role: reason -->
Text overlapping with lines or data shapes becomes difficult to decipher because the shapes interfere with the letterforms. An outline creates a "halo" or buffer zone that separates the text from the background, ensuring legibility without needing to move the text away from the data it describes [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading labels clearly.
*   **Data Type:** Maps, dense line charts, or charts with gridlines.
*   **Audience:** All users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Text on a solid, high-contrast background (e.g., white text on a dark bar).
*   **Reason:** An outline is redundant and might degrade the sharpness of the font if the contrast is already sufficient.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It can slightly thicken the appearance of the font if not done carefully.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making the text bold or changing the color to something neon.
*   **Why it fails:** It doesn't solve the intersection problem; the gridline still cuts through the letter.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does a gridline or data line strike through a word?
*   **The Test:** Can you clearly see the shape of every letter, or do some blend into the lines behind them?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Enable "text outline" or "text stroke" in your design tool.
*   **Best Fix:** Set the outline color to match the chart's background color (e.g., white outline on a white background).

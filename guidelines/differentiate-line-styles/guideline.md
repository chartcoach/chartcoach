---
id: differentiate-line-styles
title: Differentiate Lines with Width and Dashes
bibliography: references.bib
description: Use dotted lines, dashes, and varying widths to distinguish overlapping
  lines.
labels:
- chart:line
- visual:texture
- visual:size
- impact:accessibility
---

## The Rule <!-- role: advice -->
When plotting multiple lines, especially where they overlap, apply different line widths (thick vs. thin) and dash styles (solid vs. dotted) to distinguish them.

## The Logic <!-- role: reason -->
In line charts, colors often cross or run parallel. If colors look similar to a colorblind reader, the lines merge into a single entity. Varying the stroke style separates them visually without relying on hue [@muth_colorblindness_2020].
*   **The Principle:** Texture and Size differentiation.
*   **The Evidence:** In the Bitcoin vs. Gold example in [@muth_colorblindness_2020], dotting one line makes the crossover point clear, preventing confusion where the lines intersect.

## Where to Apply <!-- role: context -->
*   **User Goal:** Tracking individual trends in a multi-line chart.
*   **Data Type:** Time series data.
*   **Audience:** General financial or analytical readers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** "Spaghetti charts" with 10+ lines.
*   **Reason:** Adding dashes to 10 lines creates chaos. (The better fix there is to highlight one line and gray out the rest).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness. Dotted lines can create visual vibration (Moire effects).
*   **The Risk:** A dotted line might be interpreted as "projected" or "uncertain" data in some contexts, rather than just a different category.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Only changing color for intersecting lines.
*   **Why it fails:** Where lines intersect, colorblind users cannot tell which line continues where if the contrast is low.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do lines clearly separate at intersection points in grayscale?
*   **The Test:** Trace a single line with your eye. If you get lost at an intersection, the line style needs to change.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Make one line dashed.
*   **Best Fix:** Make the most important line thick and solid; make comparison lines thinner or dotted.

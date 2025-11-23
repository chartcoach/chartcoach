---
id: leverage-elongation-for-color
title: Use Elongated Marks to Improve Color Discrimination
bibliography: references.bib
description: Elongated shapes like bars and lines allow for more subtle color differences
  than symmetric shapes like points.
labels:
- visual:shape
- visual:color
- chart:bar
- chart:line
- impact:accessibility
- data:nominal
---

## The Rule <!-- role: advice -->
Prefer elongated mark shapes (such as bars or thick lines) over symmetric shapes (circles or squares) when you need to encode a large number of color categories or subtle color gradients.

## The Logic <!-- role: reason -->
The geometry of a mark affects color perception. Extending a mark in one dimension (elongation) significantly increases color discriminability compared to a symmetric mark of the same thickness.
*   **The Principle:** Geometric Influence on Color JND (Just Noticeable Difference).
*   **The Evidence:** Szafir demonstrates that colors on elongated marks (bars and lines) are significantly more discriminable than on points of equal thickness [@szafir_modeling_2018]. This finding is highlighted in reviews of graphical perception as a way to maximize the effectiveness of visual encodings [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Maximizing the number of discriminable colors in a single view.
*   **Data Type:** Nominal data with many categories, or continuous data mapped to a multi-step color ramp.
*   **Chart Types:** Bar charts, Gantt charts, or line charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Spatial Distribution Analysis.
*   **Reason:** If the primary task is to show spatial correlation (XY position), elongation distorts the position signal. You must use points (scatterplots), even if it reduces color capacity [@zeng_review_2023].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Layout flexibility.
*   **The Risk:** Elongated marks (like bars) generally require more screen space per data point than points, reducing the overall density of data that can be displayed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the thickness of a short line or small bar to match a dot's area without increasing length.
*   **Why it fails:** Szafir found that gains from elongation are asymptotic; a length-to-thickness ratio of about 2:1 provides most of the benefit. Simply making a square mark larger is less efficient than making it longer [@szafir_modeling_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Users struggle to match the legend to the chart in a dense scatterplot, but succeed in a bar chart using the same palette.
*   **The Test:** Calculate the aspect ratio of the marks. If the ratio is 1:1 (circles/squares) and color confusion is high, the shape is the bottleneck.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the length of the marks (if using bars) to at least twice their thickness.
*   **Best Fix:** Switch the visualization type from a scatterplot to a bar chart or parallel coordinates plot if the data density and task allow, to take advantage of elongation.

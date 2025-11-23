---
id: position-for-point-comparison
title: Prioritize Position Encodings for Point Comparisons
bibliography: references.bib
description: Use position-based charts over color maps when users need to compare
  specific maxima, minima, or ranges.
labels:
- chart:line-chart
- chart:heatmap
- task:compare
- task:locate
- visual:position
- visual:color
- data:timeseries
---

## The Rule <!-- role: advice -->
When the user's task involves identifying specific data points (maxima, minima) or comparing the range between specific points, use position-based encodings (like line charts or stock charts) rather than color-based encodings (like heatmaps or colorfields).

## The Logic <!-- role: reason -->
Position encodings offer higher perceptual fidelity for extracting exact values than color.
*   **The Principle:** Perceptual Fidelity.
*   **The Evidence:** Experiments by [@albers_task-driven_2014] showed that position encodings (line graphs, box plots) significantly outperformed color encodings (standard and woven colorfields) for tasks requiring the identification of months with the highest sales, lowest sales, or largest range.

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding exact extremes (max/min) or calculating differences between specific points (range).
*   **Data Type:** Time series data where discrete values matter.
*   **Audience:** Users who need precision rather than a general overview.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user task is purely about identifying broad averages or "ensemble" properties rather than specific points.
*   **Reason:** For summary tasks (like finding the highest average), color encodings can sometimes outperform standard line charts by allowing the eye to summarize the field [@albers_task-driven_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Position encodings (like line charts) can become cluttered and suffer from overplotting if the data density is extremely high.
*   **The Risk:** Viewers may struggle to see aggregate trends (like average or spread) in a noisy line chart compared to a colorfield.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a heatmap (colorfield) to save space while asking users to find the "highest value day."
*   **Why it fails:** Users cannot accurately discriminate subtle differences in color value to find precise maxima/minima.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a color ramp to represent quantitative magnitude for a task asking "Which is highest?"
*   **The Test:** Ask yourself if the viewer needs to know the exact value or just the general "hot" area. If it's the exact value, color is likely insufficient.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch from a heatmap/colorfield to a standard line chart or modified stock chart.
*   **Best Fix:** If density is high, use a "Composite Graph" that layers a line graph (for precision) over a bar chart or other aggregate representation.

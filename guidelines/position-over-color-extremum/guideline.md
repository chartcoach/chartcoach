---
id: position-over-color-extremum
title: Prefer Position Over Color for Finding Extremes
bibliography: references.bib
description: Position-based charts vastly outperform color-based charts for identifying
  maximum and minimum values.
labels:
- chart:line
- chart:heatmap
- task:find-extremum
- task:determine-range
- visual:position
- visual:color-saturation
- impact:accuracy
---

## The Rule <!-- role: advice -->
Use position-based encodings (like lines, bars, or box plots) rather than color-based encodings (like heatmaps) when users need to identify minimum or maximum values.

## The Logic <!-- role: reason -->
The human visual system resolves spatial position with much higher precision than color saturation.
*   **The Evidence:** According to the dataset in [@zeng_review_2023], position-based designs (Composite Graph E-4, Modified Stock Chart E-2, Box Plot E-3) consistently ranked at the top for "find-extremum" and "determine-range" tasks.
*   **The Contrast:** Color-based designs (Colorfield E-5, Color Stock Chart E-6, Event Striping E-7) consistently ranked at the bottom. For example, in finding extremums, the position-based Composite Graph (E-4) was significantly better than the Colorfield (E-5) [@albers_task-driven_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining the range of data, finding the highest peak, or finding the lowest valley.
*   **Data Type:** Quantitative data mapped to a time series.
*   **Audience:** Users requiring precise value comparisons.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the dataset is extremely dense (pixel-level density) and screen real estate is severely limited.
*   **Reason:** Position encodings require vertical space to show magnitude. Colorfields (heatmaps) can be compressed into single-pixel rows (dense pixel displays), allowing for the display of vastly more data, provided precise value extraction is not required.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical screen real estate. Position encodings need y-axis height to be readable.
*   **The Risk:** Overplotting if multiple series are compared in the same space.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a heatmap (Colorfield) for precise value lookup to save space.
*   **Why it fails:** Users cannot accurately distinguish between "dark blue" and "slightly darker blue" to determine which represents the true mathematical maximum.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using color saturation to represent the primary magnitude of the data?
*   **The Test:** Convert the image to grayscale. If the peaks and valleys disappear or become indistinguishable, the chart fails this rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels to the highest and lowest values on the heatmap.
*   **Best Fix:** Switch the visualization mark from `area-rect` or `point` with color encoding to `line` or `bar` with `positionY` encoding.

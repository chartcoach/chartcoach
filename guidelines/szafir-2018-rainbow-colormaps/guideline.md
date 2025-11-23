---
id: szafir-2018-rainbow-colormaps
title: Replace Rainbow Colormaps with Sequential or Diverging Scales
bibliography: references.bib
description: Avoid rainbow colormaps for continuous data to prevent false patterns
  and support colorblind users.
labels:
- visual:color
- impact:accessibility
- impact:accuracy
- data:continuous
- bias:perception
---

## The Rule <!-- role: advice -->
Use sequential or diverging colormaps for ordered or continuous data. Avoid the "rainbow" (red-yellow-green-blue) spectrum.

## The Logic <!-- role: reason -->
Rainbow colormaps are not perceptually uniform. The transitions between hues create artificial "bands" (e.g., distinct stripes of yellow or red) where the data actually varies smoothly. This leads users to see boundaries that don't exist. Furthermore, rainbow maps are often illegible to colorblind individuals (approx. 1 in 12 men).
*   **The Principle:** Perceptual Uniformity.
*   **The Evidence:** [@szafir_good_2018] cites Harvard research showing that switching from rainbow to perceptual colormaps increased cardiologists' diagnosis accuracy from 50% to 81%.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying patterns in continuous data (e.g., heatmaps, scalar fields).
*   **Data Type:** Continuous or ordered numerical data.
*   **Audience:** General and expert audiences, specifically including colorblind users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Categorical Data.
*   **Reason:** If the data represents distinct, unordered categories (e.g., "apples" vs. "oranges"), distinct hues from across the spectrum are appropriate to help distinguish the groups [@szafir_good_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high contrast and "bright" engaging imagery associated with full-spectrum visualizations.
*   **The Risk:** Users accustomed to standard tools (like older versions of MatLab) may initially feel they are seeing "less" variation because the artificial bands are gone.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Just "learning to read" the rainbow map.
*   **Why it fails:** Studies prove that even experts who use rainbow maps daily are subject to significant perceptual errors and biases [@szafir_good_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the legend resemble a rainbow? Are there bright yellow stripes next to dark reds or greens?
*   **The Test:** Convert the image to grayscale. If the rainbow map is used, different hues may map to the same shade of gray, making the data unreadable.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a single-hue sequence (e.g., light blue to dark blue).
*   **Best Fix:** Determine if the data has a meaningful midpoint (e.g., zero). If yes, use a **Diverging** map (two colors meeting at a neutral center). If no, use a **Sequential** map (light to dark) [@szafir_good_2018].

---
id: avoid-extreme-donut-thinness
title: Avoid Extremely Thin Donut Rings
bibliography: references.bib
description: Donut charts with extremely large inner radii (thin rings) degrade value
  retrieval accuracy.
labels:
- chart:donut
- visual:arc-length
- visual:area
- task:retrieve-value
- impact:legibility
---

## The Rule <!-- role: advice -->
Maintain a moderate ring thickness for donut charts; avoid extremely large inner radii that result in very thin rings.

## The Logic <!-- role: reason -->
While donut charts are generally effective, their performance degrades when the ring becomes too thin. Zeng & Battle [@zeng_review_2023] report that in Skau & Kosara's second experiment [@skau_arcs_2016], extremely thin donuts (e.g., 97% inner radius, effectively just an arc) ranked lower than thicker donuts (e.g., 20%, 40%, 60% inner radius) and standard pie charts. Thicker rings preserve the **area** cue, which supports the **arc length** cue for accurate perception.

*   **The Principle:** Perceptual robustness of combined cues (Area + Arc).
*   **The Evidence:** [@skau_arcs_2016], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise reading of values.
*   **Data Type:** Quantitative proportions.
*   **Audience:** General users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Progress bars or dashboard indicators (Guages).
*   **Reason:** In UI elements where the goal is a rough status check (e.g., "loading..."), a thin arc is acceptable because precise value retrieval is secondary to binary status or rough progress.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Central whitespace. A thicker ring reduces the amount of empty space in the center available for text or icons.
*   **The Risk:** The chart takes up more visual weight.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Maximizing the inner radius to make the chart look sleek or to fit a large number inside the donut.
*   **Why it fails:** It removes the area cue almost entirely, forcing the user to judge arc length in isolation, which is slightly harder to process accurately.

## How to Check <!-- role: check -->
*   **Visual Sign:** The donut looks more like a thin stroke or a line drawing than a shape.
*   **The Test:** Is the ring thickness less than ~10-15% of the total radius? If so, it may be too thin for accurate data reading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Decrease the inner radius property in your visualization tool.
*   **Best Fix:** Aim for a donut ring that is thick enough to clearly display a distinct color area, not just a colored line.

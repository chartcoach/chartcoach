---
id: continuous-color-scales-for-nuance
title: Choose Continuous Color Scales for Nuance
bibliography: references.bib
description: Use continuous color scales to allow detailed comparison between neighboring
  regions, favoring nuance over quick bucketing.
labels:
- chart:map
- visual:color
- impact:detail
- task:compare
---

## The Rule <!-- role: advice -->
Consider using a continuous color scale (gradient) instead of discrete steps (buckets). If you use discrete steps, use them only for quick readability of ranges.

## The Logic <!-- role: reason -->
Discrete steps lump values into broad buckets (e.g., 0-10%), sacrificing nuance. A continuous scale allows readers to compare neighboring regions that might fall into the same "bucket" in a discrete version but actually have different values. It prevents the loss of detail [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Subtle comparison of neighbors or seeing the full fidelity of the data.
*   **Data Type:** Quantitative data with smooth variations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Quick Readability Required.
*   **Reason:** Discrete steps (classes) are better if you want the reader to immediately identify which range a region falls into without ambiguity [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Continuous scales make it harder to say "This region is definitely between 10-20%."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using discrete steps with arbitrary "stops."
*   **Why it fails:** The map's appearance changes dramatically based on where you draw the lines between buckets (the modifiable areal unit problem).

## How to Check <!-- role: check -->
*   **The Test:** Are neighboring regions the exact same color despite having different values?
*   **Visual Sign:** A "blocky" look vs. a smooth variation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the scale type to continuous.
*   **Best Fix:** Use a continuous scale for the visual, and enable tooltips so readers can still access the exact values [@muth_choroplethmaps_2018].

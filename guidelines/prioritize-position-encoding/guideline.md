---
id: prioritize-position-encoding
title: Prioritize Position and Length for Precision
bibliography: references.bib
description: Use position and length encodings for quantitative data to ensure the
  highest perceptual accuracy.
labels:
- visual:position
- visual:length
- visual:area
- impact:accuracy
- task:compare
---

## The Rule <!-- role: advice -->
Encode your most important quantitative data using position or length. Avoid using angle, rotation, or area for data that requires precise reading or comparison.

## The Logic <!-- role: reason -->
Human perceptual mechanisms decode visual variables with varying degrees of accuracy.
*   **The Principle:** Perceptual Accuracy Ranking.
*   **The Evidence:** Citing laboratory studies by Cleveland and McGill and crowdsourced studies by Heer and Bostock, [@borner_data_2019] confirms that "position encoding has the highest accuracy followed by length... angle and rotation, and then, area."

## Where to Apply <!-- role: context -->
*   **User Goal:** When the user needs to read specific values, find maximums, or compare averages accurately.
*   **Data Type:** Quantitative (Ratio or Interval) data.
*   **Audience:** General audiences, as this hierarchy holds true across standard user studies.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the specific insight need is identifying clusters rather than reading precise values.
*   **Reason:** Some graphic variable combinations (like position + color hue) are specifically optimized for tasks like "Clustering" or "Outlier identification" rather than value estimation [@borner_data_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Position and length (e.g., bar charts, scatterplots) often require more spatial footprint than compact area-based encodings (like pie charts or bubble charts).
*   **The Risk:** Visualizations may look less "novel" or "artistic" compared to complex area or angle encodings.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using bubble charts (area) or tree maps (area) for precise data comparison.
*   **Why it fails:** [@borner_data_2019] explicitly notes that rectangular and circular area encodings yield the lowest accuracy, "explaining why visualizations, such as bubble charts and tree maps, are harder to read."

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart relies on the size of circles or squares to convey value differences.
*   **The Test:** Look at two values that are close (e.g., 10% difference). Can you instantly tell which is larger without reading a label? If not, the encoding is likely area or angle.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add explicit data labels to the area/angle elements to supplement the weak visual signal.
*   **Best Fix:** Convert the visualization type from area-based (pie, bubble) to position/length-based (bar chart, dot plot).

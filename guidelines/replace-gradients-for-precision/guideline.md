---
id: replace-gradients-for-precision
title: Replace Color Gradients with Position for Precise Values
bibliography: references.bib
description: Use position or length encodings instead of color gradients when exact
  values matter.
labels:
- chart:choropleth
- chart:bar
- visual:color
- visual:position
- impact:clarity
- task:compare
---

## The Rule <!-- role: advice -->
If your readers need to decipher exact values or see specific differences between data points, do not use gradient colors (such as in a choropleth map). Instead, encode the most important values using bars, position (like a dot plot), or area.

## The Logic <!-- role: reason -->
While gradient colors are effective for showing broad patterns, they are poor at communicating precise numerical data. According to [@muth_colors_2018], it is "hard to decipher the actual values from them and to see differences between the values." Position and length allow readers to decipher values significantly faster than color intensity.

## Where to Apply <!-- role: context -->
*   **User Goal:** The reader needs to compare specific numbers or rank items accurately.
*   **Data Type:** Quantitative data currently visualized via color saturation or hue (e.g., heatmaps, choropleth maps).
*   **Audience:** Readers looking for specific insights rather than general geographic patterns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary goal is to show a macro-level geographic pattern or trend.
*   **Reason:** If the specific values are secondary to the overall spatial distribution, a choropleth map using gradients is appropriate [@muth_colors_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the geographic context provided by a map.
*   **The Risk:** The visualization may become less visually arresting or "beautiful" compared to a colorful map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a detailed color legend with many increments.
*   **Why it fails:** Readers still have to look back and forth repeatedly to match the specific shade to the legend, increasing cognitive load.

## How to Check <!-- role: check -->
*   **Visual Sign:** A map or heatmap where the primary data is encoded only by color.
*   **The Test:** Ask someone to read the exact value of a specific region without hovering over it. If they struggle or guess incorrectly, the encoding is insufficient.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels with the actual values directly onto the colored areas.
*   **Best Fix:** Switch the chart type to a bar chart or dot plot to represent the values, using color only for categorical separation if needed.

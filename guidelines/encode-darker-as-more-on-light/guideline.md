---
id: encode-darker-as-more-on-light
title: Map Larger Values to Darker Colors on Light Backgrounds
bibliography: references.bib
description: Use darker colors to represent higher quantities when visualizing data
  on a standard white or light background.
labels:
- chart:heatmap
- chart:choropleth
- visual:color
- visual:opacity
- task:identify
- data:quantitative
- impact:intuitiveness
---

## The Rule <!-- role: advice -->
When designing colormap visualizations on a white or light background, map larger numeric values to darker, more saturated colors and lower values to lighter colors.

## The Logic <!-- role: reason -->
Users possess an innate "dark-is-more" bias, instinctively associating darker colors with greater density or quantity. On light backgrounds, this bias is reinforced by an "opaque-is-more" bias, where darker colors appear to have higher opacity (more "ink") against the white canvas. Experiments collated by **Zeng and Battle** [@zeng_review_2023] show that participants react significantly faster to charts where dark equals more. **Schloss et al.** [@schloss_mapping_2019] demonstrated that for gray scales on white backgrounds, the "dark-more" encoding (Design E-14) significantly outperformed "light-more" encoding (Design E-13) in aggregation tasks.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification of high-value regions (e.g., "Where are the most sales?").
*   **Data Type:** Quantitative or ordinal data presented via color saturation (e.g., Heatmaps, Choropleth maps).
*   **Audience:** General audiences relying on intuitive color associations.
*   **Environment:** Standard document formats, white-background slides, and default web interfaces.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dark Backgrounds.
*   **Reason:** On dark backgrounds, lighter colors often appear more "opaque" or "glowing," triggering a conflicting "opaque-is-more" bias that may invert this rule [@schloss_mapping_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use "light" to represent "high intensity" (e.g., a glowing effect), which is common in scientific imaging.
*   **The Risk:** If the low values are too light, they may disappear entirely against the white background, making the data look sparse.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Light-is-more" mapping on a white background to simulate a "glow."
*   **Why it fails:** This contradicts the user's natural "dark-is-more" intuition on paper/screens, increasing the time required to interpret the legend [@schloss_mapping_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the most important/dense areas of the chart look "faded" or "washed out"?
*   **The Test:** Remove the legend. Ask a user to point to the "highest" value. If they point to the dark areas, your mapping is intuitive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Invert the color scale so the darkest hue corresponds to the maximum value.
*   **Best Fix:** Use a sequential, single-hue colormap (like Greys or Blues) where the gradient moves from white/light-gray (low) to dark/saturated (high).

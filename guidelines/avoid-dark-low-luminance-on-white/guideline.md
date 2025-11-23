---
id: avoid-dark-low-luminance-on-white
title: Avoid Dark Low-Luminance Colors on White Backgrounds
bibliography: references.bib
description: Prevent discrimination errors by avoiding colormaps that rely heavily
  on dark, low-luminance regions against white backgrounds.
labels:
- chart:heatmap
- visual:color-saturation
- visual:luminance
- task:retrieve-value
- impact:legibility
- context:white-background
---

## The Rule <!-- role: advice -->
Avoid using colormaps that extend deep into very dark, low-luminance regions (such as pure Greys or the darkest parts of Magma) when presenting data on a standard white background.

## The Logic <!-- role: reason -->
The human visual system struggles to discriminate differences between very dark colors when they are placed against a high-contrast white background. This leads to significantly higher error rates in data retrieval tasks for values mapped to the "dark" end of the scale.
*   **The Principle:** Simultaneous Contrast and Luminance Discrimination
*   **The Evidence:** Experiments showed that the "Greys" colormap (E-1) performed poorly, and the dark regions of "Magma" (E-6) showed degraded accuracy, specifically because dark regions against a white background afford much worse discrimination than predicted by color space models [@liu_somewhere_2018]. This limitation is noted in the collation of graphical perception knowledge [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate identification of values at the extremes of a scale.
*   **Data Type:** Quantitative data mapped to a sequential color scale.
*   **Audience:** Users viewing visualizations on standard computer monitors or paper (typically white backgrounds).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dark Mode Interfaces
*   **Reason:** If the background is dark, light-colored data points become the difficult-to-discriminate regions, and dark colors may actually have lower contrast against the background (though they might simply disappear). The specific issue here is the *contrast* impeding discrimination.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the full dynamic range of luminance (0–100), effectively truncating the "black" end of the scale.
*   **The Risk:** The visualization may look "washed out" if the darkest color is too light to provide good figure-ground separation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a black background without adjusting the scale.
*   **Why it fails:** This just inverts the problem; very light colors might then become hard to discriminate against the black background due to irradiation or bloom effects.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the highest (or lowest) value regions look like amorphous black/dark blobs?
*   **The Test:** Check the luminance values of the darkest color. If it approaches pure black (#000000) and sits on pure white (#FFFFFF), discriminability is likely compromised.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Truncate the colormap so it does not reach absolute black.
*   **Best Fix:** Use a colormap like "Viridis" or "Plasma" (E-7), which avoids the extreme low-luminance issues found in "Greys" or "Magma" while maintaining high contrast [@liu_somewhere_2018].

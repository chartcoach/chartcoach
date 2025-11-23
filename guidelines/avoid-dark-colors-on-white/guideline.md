---
id: avoid-dark-colors-on-white
title: Avoid Deeply Saturated Dark Colors on White Backgrounds
bibliography: references.bib
description: Performance degrades significantly in the dark regions of colormaps when
  presented on white backgrounds.
labels:
- visual:color
- visual:contrast
- impact:legibility
- context:background
---

## The Rule <!-- role: advice -->
Avoid using colormaps that extend into very dark, low-luminance regions (like the bottom end of *Magma* or *Greys*) when displaying data on a white background.

## The Logic <!-- role: reason -->
High contrast between dark data points and a white background impedes color discrimination. The perceived difference between dark colors is compressed when the eye adapts to the surrounding high luminance.
*   **The Principle:** Simultaneous Contrast / Crisis of Resolution.
*   **The Evidence:** Error rates increased dramatically in the dark regions of *Greys*, *Magma*, and *Plasma*. These errors were much higher than predicted by standard perceptual color models (like CIELAB or CAM02-UCS), suggesting the white background actively degraded discrimination [@liu_somewhere_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between low-value data points.
*   **Data Type:** Quantitative data mapped to a sequential scale.
*   **Audience:** Viewers using standard document or web interfaces (which typically default to white backgrounds).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using a dark background (Dark Mode).
*   **Reason:** The authors hypothesize that this specific degradation is due to the high-luminance white background. Using a dark background might mitigate the contrast issue (though this specific inversion was not tested, the warning is specific to white backgrounds) [@liu_somewhere_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the full dynamic range of luminance (from 0 to 100), which theoretically reduces the number of available distinguishable steps.
*   **The Risk:** Truncating the colormap might make the lowest values appear "washed out" or middle-gray rather than truly "empty" or "zero."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Trusting the "perceptual uniformity" of a standard colormap blindly.
*   **Why it fails:** Standard models (like CAM02-UCS) do not fully account for the impact of background contrast on discrimination in extremely dark regions [@liu_somewhere_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the darkest parts of your heatmap look like a solid black/dark blob where details disappear?
*   **The Test:** Look at the darkest 10-20% of the scale. Can you see boundaries between adjacent values, or do they merge into black?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Truncate the colormap so it doesn't go all the way to black (e.g., stop at 15-20% luminance).
*   **Best Fix:** Use a colormap designed with a higher minimum luminance if the presentation background must be white.

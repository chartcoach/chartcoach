---
id: prioritize-diverging-spectral-for-gradient-magnitude
title: Prioritize Diverging or Spectral Colormaps for Gradient Comparison
bibliography: references.bib
description: Use diverging or spectral colormaps over monotonic luminance scales when
  the user needs to judge gradient magnitude or data texture.
labels:
- chart:heatmap
- chart:scalar-field
- visual:color
- task:aggregate
- task:compare
- impact:clarity
- data:quantitative
- data:spatial
---

## The Rule <!-- role: advice -->
When visualizing scalar fields (e.g., heatmaps, terrain models) where the primary task involves comparing **gradient magnitudes** (steepness, roughness, or rate of change), use diverging colormaps (like Cool-Warm) or spectral colormaps (like Rainbow) instead of monotonic luminance ramps (like Viridis).

## The Logic <!-- role: reason -->
While perceptually uniform colormaps are generally preferred for reading exact values, they can hide structural details.
*   **The Principle:** **Beneficial Discretization.** The distinct color bands found in spectral and diverging maps—often considered artifacts—act as visual proxies. These "edges" in the color ramp help the eye estimate the density and frequency of value changes.
*   **The Evidence:** Experimental results collated by [@zeng_review_2023] from specific trials in [@reda_evaluating_2019] show that participants had significantly lower Just Noticeable Differences (JND) when judging gradient steepness using Cool-Warm and Rainbow scales compared to the Viridis scale.

## Where to Apply <!-- role: context -->
This advice applies to dense 2D data where the "texture" of the data is more important than individual values.
*   **User Goal:** Identifying regions of high turbulence, roughness, or rapid change (aggregate tasks).
*   **Data Type:** Continuous quantitative data mapped over a 2D spatial field (scalar fields).
*   **Audience:** Analysts looking for structural anomalies or patterns in simulation or sensor data.

## When to Break It <!-- role: exceptions -->
Do not apply this rule if the user needs to compare specific data values or if the audience includes colorblind users (specifically regarding Rainbow maps).
*   **Scenario:** **Value Estimation Tasks.**
*   **Reason:** Rainbow and some diverging maps lack perceptual ordering and uniformity, making it harder to estimate relative values (e.g., "Is green higher than yellow?").
*   **Scenario:** **Color Vision Deficiency.**
*   **Reason:** Spectral maps (Rainbow) are often indistinguishable for users with CVD. (Note: Cool-Warm is often designed to be CVD-safe and remains a strong candidate).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose perceptual uniformity. The "bands" that help see gradients may look like false boundaries in the data where none exist.
*   **The Risk:** Users might misinterpret a color shift as a sharp data edge rather than a smooth transition.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Universally applying "Viridis" (or similar monotonic luminance scales) for all heatmap tasks.
*   **Why it fails:** While Viridis is mathematically uniform, it smooths out the visual signal, making it significantly harder for users to detect subtle changes in gradient or texture [@reda_evaluating_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look "blurry" or "smooth" even in areas you know are high-frequency or noisy?
*   **The Test:** If you switch from Viridis to Cool-Warm, do you suddenly see more "texture" or "bumps" in the data field? If yes, the diverging map is likely better for structural analysis.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the color scale from a single-hue or monotonic multi-hue (e.g., Blues, Viridis) to a diverging scale (e.g., Cool-Warm, Blue-Red).
*   **Best Fix:** Use a diverging scale that is also colorblind-safe (like Cool-Warm) to gain the gradient-perception benefits of banding without the accessibility downsides of Rainbow.

---
id: prefer-sequential-for-magnitude
title: Use Sequential Color Scales for Magnitude
bibliography: references.bib
description: Use sequential color schemes over rainbow schemes for quantitative data
  to ensure intuitive ordering and accurate pattern recognition.
labels:
- chart:choropleth
- chart:isarithmic-map
- visual:color
- task:sort
- task:find-extremum
- impact:intuitiveness
- data:quantitative
---

## The Rule <!-- role: advice -->
Use sequential (single-hue or multi-hue ordered) color scales to represent quantitative magnitude. Avoid using rainbow color schemes when the user needs to perceive order or compare magnitudes.

## The Logic <!-- role: reason -->
Rainbow color schemes lack an intuitive perceptual order. Research shows little to no agreement among users on how to order rainbow hues (e.g., determining if red represents a higher value than green) [@golbiowska_rainbow_2022]. In contrast, sequential schemes leverage a subconscious "dark is more" bias, allowing users to intuitively associate darker shades with higher magnitudes. As noted in the collation by Zeng et al. [@zeng_review_2023], sequential scales significantly outperform rainbow scales in accuracy for finding extremums and determining ranges.

*   **The Principle:** Perceptual Ordering / Dark-is-more Bias
*   **The Evidence:** [@golbiowska_rainbow_2022], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying minimum and maximum values, understanding general patterns, or comparing magnitudes (e.g., "Is region A higher than region B?").
*   **Data Type:** Quantitative data on maps (Choropleth, Isarithmic) or heatmaps.
*   **Audience:** General audiences who rely on intuitive visual cues rather than memorizing complex legends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The task is strictly identifying or locating specific values using a lookup legend, without the need to assess gradients or trends.
*   **Reason:** Rainbow colors can be competitive or even faster for specific value extraction due to high distinctness between hues [@golbiowska_rainbow_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high contrast between specific values that distinct hues provide.
*   **The Risk:** Users may find it slightly slower to match a specific shade to a legend compared to matching a distinct hue (like "bright red").

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow scale but adding a legend to "explain" the order.
*   **Why it fails:** Users still struggle to internalize the order, leading to slower cognitive processing and higher error rates in tasks like finding the maximum value [@golbiowska_rainbow_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look like a full spectral rainbow (blue, cyan, green, yellow, red)?
*   **The Test:** Remove the legend. Can a user still tell which regions have the highest values? If not, the scale is not intuitive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the scale to a single-hue gradient (e.g., light blue to dark blue).
*   **Best Fix:** Use a perceptually uniform sequential multi-hue scale (e.g., Viridis or Magma) that preserves the "dark is more" ordering while maintaining some hue variation.

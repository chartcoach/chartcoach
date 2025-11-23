---
id: prioritize-pure-luminance-saturation-scales
title: Prioritize Pure Luminance or Saturation Scales
bibliography: references.bib
description: Use single-channel variation in luminance or saturation to guarantee
  intrinsic perceptual order.
labels:
- visual:color-luminance
- visual:color-saturation
- task:compare
- data:quantitative
- data:ordinal
---

## The Rule <!-- role: advice -->
For data requiring strict perceptual ordering, favor colormaps that vary only in luminance (grayscale) or only in saturation over complex multi-attribute scales.

## The Logic <!-- role: reason -->
Mathematically, pure luminance maps and pure saturation maps represent "shortest paths" in color metric spaces.
*   **The Principle:** Shortest Path Metrics
*   **The Evidence:** Bujack et al. prove that because grayscale and saturation maps lie on shortest paths in the color space, they mathematically suffice for both local and global intrinsic order (Theorems 2 and 3) [@bujack_ordering_2018]. This provides a theoretical guarantee of order often missing in complex scales, a finding categorized under "Theory" in the review by Zeng and Battle [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate estimation of magnitude or sequence without ambiguity.
*   **Data Type:** Quantitative (T-3) or Ordinal (T-4) data.
*   **Audience:** Scientific or technical contexts where accuracy supersedes aesthetics.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-frequency data requiring high discriminability.
*   **Reason:** Single-channel maps (especially saturation) often have fewer Just Noticeable Differences (JNDs) than multi-hue maps, making it harder to see fine details.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic appeal and discriminability. Pure saturation maps can look "washed out," and pure luminance maps lack color contrast.
*   **The Risk:** Users may find the visualization boring or struggle to distinguish small local differences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding hue variation randomly to "spice up" a luminance ramp without checking perceptual distances.
*   **Why it fails:** This can introduce "wiggles" in the path through color space, violating intrinsic order [@bujack_ordering_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the colormap look like a straight gradient from black-to-white or white-to-color?
*   **The Test:** Convert the visualization to grayscale. If the ordering is preserved perfectly and linearly, it relies on luminance.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a standard single-hue sequential scale (e.g., "Blues" or "Grays").
*   **Best Fix:** Use a scientifically designed colormap like Viridis (which combines luminance ordering with hue variation) if higher discriminability is needed, though a pure luminance scale remains the theoretical baseline for order.

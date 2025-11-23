---
id: restrict-hue-scales-for-order
title: Restrict Hue Scales to Half the Spectrum
bibliography: references.bib
description: Limit hue-based colormaps to less than 180 degrees of the color wheel
  to maintain perceptual order.
labels:
- chart:heatmap
- chart:choropleth
- visual:color-hue
- task:rank
- data:quantitative
- data:ordinal
---

## The Rule <!-- role: advice -->
When using color hue to represent ordered data (ordinal or quantitative), limit the range of the colormap to less than half of the color circle (partial hue map). Do not use the full color spectrum.

## The Logic <!-- role: reason -->
Full hue maps (like the rainbow) are periodic, meaning the end connects back to the beginning, which destroys global intrinsic order.
*   **The Principle:** Intrinsic Order & Periodicity
*   **The Evidence:** Bujack et al. demonstrate mathematically that a hue map covering every hue cannot satisfy global intrinsic order because $\gamma(0) = \gamma(1)$ (periodicity) implies the start and end are identical, violating distance requirements for distinct values [@bujack_ordering_2018]. However, they prove that if a hue map spans no more than half the circle, it satisfies intrinsic order in Euclidean color spaces [@bujack_ordering_2018]. This distinction is highlighted in the collation by Zeng and Battle [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Perceiving rank, magnitude, or sequence in data.
*   **Data Type:** Quantitative or Ordinal data mapped to Color Hue (as classified in designs T-1 and T-2).
*   **Audience:** General audiences who rely on intuitive perceptual cues rather than legend lookups.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Cyclic Data
*   **Reason:** If the data itself is periodic (e.g., time of day, angle, phase), a full hue circle is appropriate because the data topology matches the visual topology.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose discriminability capacity by discarding half the available color space.
*   **The Risk:** Reduced contrast between adjacent values compared to a full-spectrum map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a full rainbow map for linear data.
*   **Why it fails:** Users cannot intuitively tell if "Blue" is greater than "Red" without constantly checking a legend, and the periodicity confuses the "min" and "max" relationship [@bujack_ordering_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the colormap contain both Red and a Red-Purple/Violet at opposite ends?
*   **The Test:** Check if the start and end colors are perceptually closer to each other than they are to the middle colors.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Crop the colormap range to use only a segment (e.g., Blue to Green, or Yellow to Red).
*   **Best Fix:** Switch to a multi-hue ramp that is monotonic in luminance (e.g., Viridis or Magma) rather than a pure hue cycle.

---
id: verify-intrinsic-order-beyond-monotonicity
title: Verify Intrinsic Order Beyond Monotonicity
bibliography: references.bib
description: Do not assume a colormap is perceptually ordered merely because one attribute
  increases monotonically.
labels:
- visual:color
- design:creation
- task:design-colormap
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not assume a colormap is ordered simply because it is monotonic in one attribute (like luminance). Validate that perceptual distances between colors align with data distances.

## The Logic <!-- role: reason -->
Monotonicity is a mathematical property of a single dimension, but color perception is multi-dimensional.
*   **The Principle:** Triangle Inequality & Intrinsic Order
*   **The Evidence:** Bujack et al. provide a counter-example proving that monotonicity in any single attribute (hue, saturation, or luminance) is **not sufficient** to guarantee intrinsic order (Theorem 6) [@bujack_ordering_2018]. A path can increase in luminance while curving wildly in color space, making equidistant data points appear perceptually non-uniform. This challenges older heuristics cited in visualization literature reviews [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Designing or selecting custom colormaps.
*   **Data Type:** Continuous quantitative data.
*   **Audience:** Tool builders and visualization designers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Legend-Based Tasks
*   **Reason:** If the user always references a legend (legend-based order), simple monotonicity is sufficient (Theorem 1 in [@bujack_ordering_2018]), and intrinsic perceptual uniformity is less critical.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Design freedom. Many aesthetically pleasing colormaps (like spiral maps) might fail strict intrinsic order tests.
*   **The Risk:** "Mathematically correct" maps might look less vibrant.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Ensuring a colormap goes from Dark to Light and assuming it is perfect.
*   **Why it fails:** It ignores hue/saturation shifts that might create perceptual artifacts (e.g., the Mach band effect or false boundaries).

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there "bands" of color that look wider or narrower than others despite representing the same data range?
*   **The Test:** Compute the $\Delta E$ (perceptual difference) between equidistant points along the colormap. They should be roughly equal and satisfy the triangle inequality.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use established, perceptually uniform colormaps (e.g., cividis, mako) rather than rolling your own.
*   **Best Fix:** Use algorithmically generated colormaps optimized for path linearity in perceptually uniform color spaces (e.g., CIELAB or CAM02-UCS).

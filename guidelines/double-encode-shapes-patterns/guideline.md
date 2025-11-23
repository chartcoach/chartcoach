---
id: double-encode-shapes-patterns
title: Double Encode with Shapes and Patterns
bibliography: references.bib
description: Use symbols, shapes, and patterns alongside color to communicate data
  redundantly.
labels:
- visual:shape
- visual:texture
- impact:accessibility
- chart:scatter
- chart:map
---

## The Rule <!-- role: advice -->
Do not rely on color alone. Double-encode data by adding geometric shapes (triangles, crosses), symbols (checks, xs), or patterns (stripes) to distinguish categories.

## The Logic <!-- role: reason -->
Simulators are imperfect, and vision varies by individual. The only "bulletproof" solution is encoding data with a second visual variable that does not rely on hue [@muth_colorblindness_2020].
*   **The Principle:** Redundant Encoding.
*   **The Evidence:** [@muth_colorblindness_2020] highlights that relying purely on simulators isn't enough because "everyone is different." Shapes and patterns function regardless of color perception.

## Where to Apply <!-- role: context -->
*   **User Goal:** Differentiating points in a scatterplot or areas in a map.
*   **Data Type:** Discrete categories.
*   **Audience:** All audiences, especially strict accessibility compliance contexts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density scatterplots (thousands of points).
*   **Reason:** Different shapes (stars, crosses) look like "confetti" or noise when overlapped significantly [@muth_colorblindness_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. Adding patterns and shapes adds noise.
*   **The Risk:** Patterns can alter perceived color lightness (e.g., thin white lines make a green area look brighter) [@muth_colorblindness_2020]. Glyphs/shapes are also a "slower read" than color.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 10 different complex shapes.
*   **Why it fails:** It creates visual clutter. Limit shapes to 3 or 4 distinct types.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you tell the difference between two data points if you remove the color entirely?
*   **The Test:** Convert the image to black and white. If the categories are indistinguishable, you need shapes or patterns.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a checkmark icon next to "Good" values and a cross next to "Bad" values in tables.
*   **Best Fix:** Use different shapes (triangle, circle, square) for different categories in scatterplots, or hatch patterns in maps.

---
id: clamp-lightness-for-contrast
title: Clamp Lightness for Background Contrast
bibliography: references.bib
description: Restrict lightness values to ensure visibility on standard white or black
  backgrounds.
labels:
- visual:color
- impact:accessibility
- impact:visibility
- visual:background
---

## The Rule <!-- role: advice -->
Restrict the lightness ($L^*$) of your palette colors to a range between 25 and 85 (in CIELAB space) for standard visualization backgrounds.

## The Logic <!-- role: reason -->
To ensure marks are visible against both black and white backgrounds (common in visualization tools), colors must not be too dark or too light. [@gramazio_colorgorical_2017] enforced a lightness clamp ($L \in [25, 85]$) to guarantee that every selected color possessed sufficient contrast against $L=0$ (black) and $L=100$ (white) backgrounds, preventing data from vanishing into the canvas.

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring data visibility and legibility.
*   **Data Type:** Any graphical marks (points, bars, lines).
*   **Audience:** Users viewing charts on variable monitor settings or themes (dark/light mode).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Fixed, high-contrast background designs.
*   **Reason:** If you can guarantee the background is always dark charcoal (e.g., a specialized dashboard), you can use very light colors ($L > 85$). If the background is strictly white, you can use darker colors ($L < 25$).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Dynamic Range.
*   **The Risk:** You lose the ability to use deep blacks or near-white pastels as data encoding colors.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using full-range randomly generated RGB colors.
*   **Why it fails:** Random sampling often picks extremely bright yellows (invisible on white) or deep blues (invisible on black).

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you see the yellow points clearly on a white background? Can you see the navy blue points on a black background?
*   **The Test:** Convert colors to CIELAB and check if $L^*$ is $< 25$ or $> 85$.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Darken yellows/cyans and lighten blues/purples.
*   **Best Fix:** Set programmatic bounds in your color generation tool to reject colors outside the $[25, 85]$ $L^*$ range.

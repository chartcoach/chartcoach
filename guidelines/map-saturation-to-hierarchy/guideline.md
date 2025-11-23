---
id: map-saturation-to-hierarchy
title: Map Saturation Levels to Importance Levels
bibliography: references.bib
description: Use gradients of saturation to create multi-level visual hierarchies
  (most important, important, least important).
labels:
- visual:saturation
- visual:color
- task:rank
- impact:hierarchy
- complexity:advanced
---

## The Rule <!-- role: advice -->
When you need more than a binary distinction (important vs. unimportant), assign the most saturated, darkest colors to the primary category, lighter/less saturated colors to secondary categories, and gray to the least important categories.

## The Logic <!-- role: reason -->
Readers' eyes follow a predictable path based on contrast and intensity. As explained in [@muth_emphasize_color_2023], the eye goes first to the highest contrast/saturation, then to the slightly less saturated colors, and finally to the grays. This allows you to create a "1st level, 2nd level, 3rd level" reading order directly through color choice.

## Where to Apply <!-- role: context -->
*   **User Goal:** Nuanced storytelling where context (e.g., a rival country) is important, but not *the most* important element.
*   **Data Type:** Complex datasets with multiple actors or categories that have varying relevance to the story (e.g., The U.S. vs. China vs. Rest of World).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dark backgrounds.
*   **Reason:** On a dark background, "darker" colors do not equate to higher contrast. In that context, you might need high brightness/lightness rather than deep saturation to create emphasis [@muth_emphasize_color_2023].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Legibility of the lower-tier categories.
*   **The Risk:** Elements with very low saturation (0%) and high lightness (light gray) are seen last and may be overlooked entirely.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "pure black" to emphasize everything.
*   **Why it fails:** While black is high contrast on white, a "crazy-saturated" color like neon green or bright red often grabs attention faster than black because of its chromatic intensity [@muth_emphasize_color_2023].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the secondary category fighting for attention with the primary category?
*   **The Test:** Determine the intended reading order (e.g., A -> B -> C). Look at the chart. If you look at B before A, the saturation levels are likely too close.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the opacity of the secondary categories to step them down visually.
*   **Best Fix:** Define distinct "levels" in your palette:
    1.  **Primary:** High saturation, high contrast (e.g., Dark Pink).
    2.  **Secondary:** Medium saturation/lightness (e.g., Teal).
    3.  **Tertiary:** Low saturation gray (e.g., Dark Gray).
    4.  **Background:** Lowest saturation/contrast (e.g., Light Gray).

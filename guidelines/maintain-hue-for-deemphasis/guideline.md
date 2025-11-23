---
id: maintain-hue-for-deemphasis
title: Maintain Hue When De-emphasizing Related Data
bibliography: references.bib
description: Use desaturation, not a new hue, to reduce the visual prominence of secondary
  data within the same category.
labels:
- visual:color
- visual:saturation
- impact:clarity
- data:categorical
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When you want to de-emphasize specific data points without relegating them completely to the background, use a less saturated version of the *same* hue used for the highlighted data. Do not switch to a different hue.

## The Logic <!-- role: reason -->
In data visualization, a change of hue typically signals a change in category (e.g., Apples vs. Oranges). According to [@muth_emphasize_color_2023], using a new hue (like dark blue) for deemphasized data while using a bright hue (like light blue) for highlighted data can confuse the reader into thinking the data belongs to a separate group. Maintaining the hue but reducing saturation communicates "this is the same type of data, just less important."

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing a relationship between a highlighted subset and the immediate context (e.g., labeled vs. unlabeled countries).
*   **Data Type:** Charts where data points belong to the same fundamental group but have different states (e.g., selected vs. unselected, current year vs. previous years).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data points actually belong to fundamentally different categories.
*   **Reason:** If the distinction is categorical (e.g., Democrat vs. Republican) rather than hierarchical (Winner vs. Losers), distinct hues are necessary to prevent false association.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You have a limited range of contrast. A light, desaturated version of a color may be hard to see against a white background.
*   **The Risk:** If the desaturation is too subtle, the hierarchy won't be visible. If it is too extreme, the lighter color may disappear completely.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Picking a "random" dull color (like a muddy brown) to contrast with a bright red.
*   **Why it fails:** Readers may interpret the muddy brown as a specific, separate category rather than just "less important red data."

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the highlighted and non-highlighted elements look like they belong to different families?
*   **The Test:** Ask a viewer, "Are these two bars related?" If the hue shift makes them say "No," you should likely align the hues.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the opacity of the non-highlighted color (e.g., 80% opacity makes red look softer/lighter) [@muth_emphasize_color_2023].
*   **Best Fix:** Manually select a color that has the same hue value (H in HSV) but lower saturation (S) and higher brightness (B/L) to ensure it remains visible but recedes visually.

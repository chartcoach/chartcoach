---
id: match-color-scheme-to-data
title: Match Color Schemes to Data Types
bibliography: references.bib
description: Choose sequential, diverging, or qualitative color schemes based on whether
  the data is continuous, centered, or categorical.
labels:
- chart:map
- visual:color
- data:categorical
- data:quantitative
- impact:readability
---

## The Rule <!-- role: advice -->
Select the color scheme that matches the structure of your data:
1.  **Sequential** (e.g., light to dark blue) for data progressing from low to high.
2.  **Diverging** (e.g., red-white-blue) for data with a meaningful center point or extremes.
3.  **Qualitative** (e.g., distinct hues) for categorical data.

## The Logic <!-- role: reason -->
Color communicates hierarchy.
*   **Sequential** schemes drive attention to the highest values (usually the darkest).
*   **Diverging** schemes drive attention to both extremes of the scale (e.g., opposing political parties or positive/negative growth).
*   **Qualitative** schemes distinguish categories without implying rank [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating the nature of the data distribution instantly.
*   **Data Type:**
    *   Sequential: Unemployment rates, population density.
    *   Diverging: Election results (margins), temperature anomalies.
    *   Qualitative: Dominant industry, most popular brand.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None explicitly mentioned. Misusing the scheme miscommunicates the data structure.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Diverging scales require a clear, meaningful midpoint (like 0% change or 50% vote share); without it, the divergence is misleading.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential palette (one color gradient) for data that has positive and negative values.
*   **Why it fails:** It implies that negative values are simply "less" of the positive values, rather than an opposing metric.

## How to Check <!-- role: check -->
*   **The Test:** Does the data have a "zero" or "average" point where values go in opposite directions? If yes, use Diverging. Is it just "more is more"? Use Sequential.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Update the palette to match the data. Ensure sequential and diverging schemes use a lightness gradient (light color = low/middle value, dark color = high/extreme value) [@muth_choroplethmaps_2018].

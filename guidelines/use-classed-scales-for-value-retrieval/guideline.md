---
id: use-classed-scales-for-value-retrieval
title: Use Classed Scales for Value Retrieval
bibliography: references.bib
description: Prioritize classed scales when readers need to estimate specific numerical
  values or ranges from the visualization.
labels:
- visual:color
- impact:readability
- task:lookup
- audience:general
- media:print
---

## The Rule <!-- role: advice -->
If your readers need to read specific values or confidently place a region within a numerical range (e.g., "between 6% and 7%"), use a classed color scale.

## The Logic <!-- role: reason -->
Classed maps have a distinct, statistically significant advantage in "value-estimation tasks" [@muth_classed_vs_unclassed_2021]. It is cognitively easier for a reader to match a region's color to a distinct block in a legend than to estimate the position of a specific hue along a continuous gradient.

## Where to Apply <!-- role: context -->
*   **Media:** Static maps (PDF reports, print media) where interactive tooltips are not available.
*   **User Goal:** When the reader needs to know "How much?" rather than just "More or Less?"

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Interactive web maps.
*   **Reason:** If a user can hover over a region to see the exact number in a tooltip, the need for visual value estimation is negated, and you can opt for the nuance of an unclassed scale instead.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision. You can only communicate a range, not the exact number.
*   **The Risk:** As the number of classes increases, the colors become harder to distinguish, and the advantage in readability diminishes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using an unclassed scale with a highly detailed legend (e.g., markings every 1%).
*   **Why it fails:** Even with a detailed legend, readers struggle to match the exact shade on the map to the shade on the legend bar.

## How to Check <!-- role: check -->
*   **The Test:** Cover the numbers on the map (if any). Can you match a region's color to the legend and confidently state the value range? If you are unsure, the scale is likely unclassed or has too many classes.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Group the data into 4–6 distinct classes.
*   **Best Fix:** Ensure the colors chosen for the classes are distinct enough to be easily matched to the legend.

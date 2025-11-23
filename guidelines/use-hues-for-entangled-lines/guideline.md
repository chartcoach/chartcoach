---
id: use-hues-for-entangled-lines
title: Use Hues for Entangled Line Charts
bibliography: references.bib
description: Prioritize hues over shades in spaghetti charts to help distinctness.
labels:
- chart:line
- visual:color
- task:track
- complexity:high
---

## The Rule <!-- role: advice -->
Use qualitative colors (hues) rather than shades for entangled line charts ("spaghetti charts"), even if the lines have a clear ranking or order.

## The Logic <!-- role: reason -->
While shades convey order, they make it nearly impossible to distinguish intersecting lines in a dense chart. Hues allow the eye to follow a specific line (e.g., "the green line") across the entire x-axis much better than trying to track "the slightly-darker-blue line." The goal in this specific context is to optimize for distinguishing the entities, not emphasizing their rank [@muth_quantitative_vs_qualitative_2021].

## Where to Apply <!-- role: context -->
*   **Chart Type:** Line charts with multiple intersecting lines.
*   **Data:** Time-series data where lines frequently cross or overlap.
*   **User Goal:** Following the path of a single entity (e.g., a country) across time.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The lines never cross (e.g., a bump chart with clear spacing or strictly ordered data that stays ordered).
*   **Reason:** If the lines don't tangle, shades can safely double-encode the rank without sacrificing distinctness.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate visual cue of ranking. A reader cannot look at the "pink" line and immediately know it is ranked 2nd without checking the legend or starting point.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential blue scale for 5 different countries in a line chart to show their GDP rank.
*   **Why it fails:** When the lines cross, the reader loses track of which blue line is which.

## How to Check <!-- role: check -->
*   **The Test:** Pick a line on the left side. Can you follow it to the right side in under 2 seconds without using your finger?
*   **Visual Sign:** If you get lost in a "blob" of similar colors, the shades are failing.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Switch to a qualitative palette (distinct hues) to maximize contrast between intersecting lines.

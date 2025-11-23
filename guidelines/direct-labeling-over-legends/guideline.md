---
id: direct-labeling-over-legends
title: Label Data Directly to Replace Legends
bibliography: references.bib
description: Place labels near data points to minimize working memory load caused
  by looking back and forth.
labels:
- chart:pie
- chart:line
- visual:text
- impact:cognitive-load
- task:identify
---

## The Rule <!-- role: advice -->

Place text labels directly next to the data elements they describe. Avoid using separate legends that force the viewer to look back and forth between a key and the graph.

## The Logic <!-- role: reason -->

Visual processing in the natural world rarely requires substantial short-term memory; we usually look directly at what we need to identify. Legends force viewers to hold a visual feature (like a color or shape) in working memory while shifting their gaze to the legend and back. This "glancing around" is effortful and prone to error [@zacks_designing_2020].

*   **The Principle:** Spatial Contiguity / Minimizing Working Memory Demands
*   **The Evidence:** The visual system assumes related information is spatially close (like a tomato on a vine). Separating them violates this expectation and taxes memory [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** Rapidly identifying categories or specific data streams (e.g., identifying which line represents "France" in a multi-line chart).
*   **Data Type:** Categorical data encoded with color or shape (e.g., line charts, pie charts, scatterplots).
*   **Audience:** Any viewer, particularly those needing to make quick decisions without cognitive strain.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Extremely high-density data or limited space.
*   **Reason:** If direct labels would overlap significantly or clutter the view to the point of illegibility, a legend may be a necessary compromise, though it remains suboptimal.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Direct labeling consumes chart real estate that might otherwise be used for data plotting.
*   **The Risk:** Poorly placed direct labels can create visual clutter or "chart junk" if not managed carefully.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using a separate color lookup table (legend) far removed from the data (e.g., on the side or bottom).
*   **Why it fails:** It forces "sluggish integration" where the user must repeatedly saccade between the data and the legend, burdening short-term memory [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the chart have a box on the periphery listing colors/shapes and their meanings?
*   **The Test:** Track your eye movements. Do you have to look away from the data to understand what a specific bar or line represents?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Move the legend as close as physically possible to the data clusters.
*   **Best Fix:** Remove the legend entirely and place the text label directly adjacent to or on top of the corresponding data element (e.g., at the end of a line or inside a pie slice).

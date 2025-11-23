---
id: prioritize-cs-for-engagement
title: Use Connected Scatterplots for Engagement
bibliography: references.bib
description: Choose connected scatterplots over dual-axis line charts when the primary
  goal is to attract viewer attention.
labels:
- chart:connected-scatterplot
- task:explore
- visual:shape
- impact:engagement
- audience:general-public
---

## The Rule <!-- role: advice -->
Select the connected scatterplot format when your primary goal is to capture reader attention and encourage dwell time, rather than solely for rapid data extraction.

## The Logic <!-- role: reason -->
The novelty and "puzzle-like" nature of the connected scatterplot draws viewers in.
*   **The Principle:** Visual Novelty and Challenge.
*   **The Evidence:** Eye-tracking studies showed that participants prioritized viewing connected scatterplots over dual-axis line charts and spent more time examining them in the first half of the session [@haroz_connected_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Casual exploration or "hooking" a reader into a story.
*   **Data Type:** Paired time series with interesting shapes (loops or sharp turns).
*   **Audience:** News readers or web users scanning for interesting content.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dashboard or monitoring contexts.
*   **Reason:** If the user needs to extract precise values quickly or monitor status at a glance, the cognitive load of the "puzzle" is a hindrance, not a benefit.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Familiarity and immediate clarity.
*   **The Risk:** Some users may find the chart "loopy" or difficult to parse initially without guidance.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing dull data into this format.
*   **Why it fails:** If the data does not produce interesting shapes (loops/L-shapes), the novelty wears off without offering narrative insight [@haroz_connected_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like a random scribble, or does it have distinct geometric features?
*   **The Test:** Check if the "shape" of the line tells a story (e.g., "spiraling out of control" or "a sudden U-turn").

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add annotations pointing out the "shapes" (loops) to justify the format.
*   **Best Fix:** If engagement is not the priority, revert to a Dual-Axis Line Chart or Small Multiples.

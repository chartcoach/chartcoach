---
id: reinforce-colors-in-tooltips
title: Reinforce Category Colors in Tooltips
bibliography: references.bib
description: Include visual color indicators (text, shapes, or backgrounds) inside
  tooltips.
labels:
- visual:interaction
- visual:color
- impact:usability
- task:exploration
---

## The Rule <!-- role: advice -->
When designing tooltips (pop-ups), visually repeat the category color inside the tooltip. This can be done by coloring the category name, adding a colored shape (square/circle), or using a colored background/border.

## The Logic <!-- role: reason -->
Tooltips often overlap the main legend, blocking it from view. Furthermore, tooltips appear right where the user is looking (at the data point), removing the need to look away to identify the category [@muth_remind_colors_2023].
*   **The Principle:** Proximity and Redundancy
*   **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Investigating specific data points via hover or tap.
*   **Data Type:** Interactive charts (maps, scatterplots, multi-line charts).
*   **Audience:** Interactive users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Monochromatic charts.
*   **Reason:** If color encodes value (gradient) rather than category, listing the "color" in the tooltip is less useful than listing the specific numeric value.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Tooltip complexity. Requires more HTML/CSS styling than a plain text tooltip.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the value in the tooltip without the category name or color.
*   **Why it fails:** The user might know "Value is 50" but forgets which line belongs to "Company A" or "Company B."

## How to Check <!-- role: check -->
*   **Visual Sign:** Hover over a data point until the tooltip covers the main legend. Can you still identify which category the point belongs to?
*   **The Test:** If the legend is obscured and the tooltip is black text on white, the context is lost.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a colored unicode character (like a square ⬛ or circle ●) matching the data color before the category name in the tooltip text.
*   **Best Fix:** Style the category label in the tooltip to match the data color, or add a colored stripe/background to the tooltip container.

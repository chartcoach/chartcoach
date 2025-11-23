---
id: set-gridline-alpha-to-point-two
title: Set Gridline Opacity to 20 Percent
bibliography: references.bib
description: A specific opacity recommendation for gridlines to ensure they are visible
  without becoming intrusive.
labels:
- chart:scatter
- chart:line
- visual:gridlines
- visual:contrast
- impact:clarity
---

## The Rule <!-- role: advice -->
Set the alpha (transparency) value of black gridlines to approximately 0.2 (20% opacity) on white backgrounds.

## The Logic <!-- role: reason -->
Gridlines must be visible enough to aid estimation but subtle enough not to interfere with the data (the "fence" effect). Crowdsourced experiments corroborate laboratory findings that an alpha of 0.2 bounds the range of acceptable contrast, providing a "safe" default that balances perceptibility with unobtrusiveness [@heer_crowdsourcing_2010].
*   **The Principle:** Alpha Contrast Layering
*   **The Evidence:** Experiment 2 in [@heer_crowdsourcing_2010] replicated Stone & Bartram's results, confirming alpha = 0.2 as an optimal baseline across diverse monitor settings.

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading values from a plot using reference lines.
*   **Data Type:** Scatter plots, line charts, or bar charts requiring background grids.
*   **Audience:** Users on standard web displays (LCDs, varying gammas).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High Density Plots.
*   **Reason:** The study found a significant effect of plot density; denser plots may require slightly darker gridlines to remain visible [@heer_crowdsourcing_2010].
*   **Scenario:** High-Resolution/High-Bit-Depth Displays.
*   **Reason:** Users on high-quality displays tended to select lighter alphas due to better contrast resolution [@heer_crowdsourcing_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Gridlines may be faint on very poor quality projectors or washed-out monitors (though the study suggests 0.2 covers most web users).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using fully opaque black lines or fully invisible lines.
*   **Why it fails:** Opaque lines create visual clutter and "imprison" the data; invisible lines remove the reference utility.

## How to Check <!-- role: check -->
*   **Visual Sign:** Gridlines competing with data points for attention.
*   **The Test:** Take a screenshot and check the color value of the grid pixels; they should differ from the background by about 20% of the luminance range.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change gridline stroke color to `rgba(0,0,0,0.2)` or a light gray equivalent `#cccccc`.

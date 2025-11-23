---
id: distinguish-meaningful-elements
title: Ensure Meaningful Elements Are Distinct and Unobscured
bibliography: references.bib
description: Prevent visual occlusion and provide visual separation between adjacent
  data marks to ensure elements are perceivable.
labels:
- impact:accessibility
- impact:clarity
- visual:layout
- visual:geometry
- chart:stacked-bar
- chart:pie
- chart:scatter
---

## The Rule <!-- role: advice -->
Ensure primary chart elements are not obscured by other elements. Place at least 1px of distinct separation (whitespace or contrasting border) between adjacent elements, such as segments in stacked bars or pie charts, and ensure no text is overlapped by graphical marks.

## The Logic <!-- role: reason -->
This guideline ensures that content is "Perceivable," allowing users to identify content using sight, sound, or touch [@elavsky_how_2022]. While related to contrast, distinguishability focuses on the higher-level ability to perceive one object as separate from another.

*   **The Principle:** Distinguishability. This relies on Gestalt techniques to ensure users can separate foreground from background and distinct items from one another [@w3c_understanding_distinguishable].
*   **The Evidence:** Evaluation heuristics emphasize that mere color difference is often insufficient for separation; explicit boundaries are necessary for users to perceive distinct "things" [@elavsky_how_2022]. Techniques like adding whitespace between overlapping marks or adjacent segments reduce the cognitive load required to distinguish data points [@observablehq_contrast_and].

## Where to Apply <!-- role: context -->
This advice applies to high-density visualizations or charts where data marks share boundaries.

*   **User Goal:** Discriminating between specific values or categories.
*   **Data Type:** Categorical data in stacked layouts (stacked bars, area charts, pie charts) or dense quantitative data (scatterplots).
*   **Audience:** All users, particularly those with low vision or cognitive disabilities who rely on clear visual separation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When individual distinctness is irrelevant to the insight.
*   **Reason:** As noted in the Chartability heuristics, occlusion or lack of separation is "only a failure if discriminability or separability is required to understand the chart" [@elavsky_how_2022]. For example, in a massive scatterplot rendering a general density trend, distinguishing every single pixel-sized point may not be the goal.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Adding borders or padding reduces the available pixel area for the data ink itself, which may slightly reduce the precision of the visualization in very tight spaces.
*   **The Risk:** In extremely dense scatterplots, adding borders to every point without increasing canvas size may result in the borders dominating the visual field, obscuring the color encoding of the data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on color hue to separate adjacent stacked segments.
*   **Why it fails:** Without a separating line or whitespace, colors with similar luminosity may bleed together for users with color vision deficiencies or low contrast sensitivity [@observablehq_contrast_and].
*   **The Wrong Fix:** Placing text labels directly over complex data marks without a background.
*   **Why it fails:** The text becomes obscured or "overlapped," violating the requirement that text (any) must not be obscured by other elements [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for "touching" elements in pie charts or stacked bars that have no gap or border between them. Look for labels that cross data lines or points without a halo or background.
*   **The Test:** Verify there is at least 1px of whitespace (or distinct border color) between adjacent geometrical elements [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a stroke (border) to your data marks that matches the background color (e.g., a white stroke on a white background) to create the illusion of gaps.
*   **Best Fix:** Adjust the layout code to render explicit padding between elements and implement collision detection or background fills for text labels to prevent overlapping [@observablehq_contrast_and].

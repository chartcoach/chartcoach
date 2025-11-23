---
id: ensure-visual-distinctiveness
title: Ensure Visual Distinctiveness
bibliography: references.bib
description: Avoid generic templates to ensure the visualization is recognizable and
  memorable.
labels:
- style:design
- impact:memorability
- source:government
- visual:style
---

## The Rule <!-- role: advice -->
Design visualizations to be visually distinct rather than relying on repetitive, standard templates.

## The Logic <!-- role: reason -->
Research by [@borkin_beyond_2016] indicates that visualizations that are memorable "at-a-glance" (1 second exposure) are also the most memorable after prolonged exposure (10 seconds). Visualizations from sources that use repetitive templates and similar aesthetics (e.g., government reports in the study) were the least memorable and often confused with one another. Distinct visual elements allow the user to encode the image effectively for later retrieval.

## Where to Apply <!-- role: context -->
*   **User Goal:** Preventing their chart from blending in with others (e.g., in a slide deck or report).
*   **Data Type:** Series of similar datasets (e.g., multiple bar charts in a row).
*   **Audience:** Viewers seeing multiple charts in a session.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparing small multiples.
*   **Reason:** When the goal is direct comparison across a grid (small multiples), varying the design between charts destroys the ability to compare patterns. Uniformity is required there.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Consistency and efficiency in production.
*   **The Risk:** "Over-designing" where the style distracts from the substance if not balanced with clear data encoding.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the default Excel/Tableau color palette and font settings for every chart in a report.
*   **Why it fails:** It makes all charts look identical, leading to lower recognition rates.
*   **The Wrong Fix:** Changing colors randomly without meaning.
*   **Why it fails:** Distinctiveness should ideally be tied to the data or topic, not random stylistic changes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does this chart look exactly like the previous 10 charts I've seen?
*   **The Test:** Place the chart in a grid with other charts from the same report. If you squint, can you tell which one covers which topic?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the layout or color scheme to be specific to the dataset's topic.
*   **Best Fix:** Introduce unique composition or specific visual elements (like relevant icons or unique grouping) that define the chart's identity.

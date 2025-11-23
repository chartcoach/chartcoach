---
id: use-small-multiples-for-accuracy
title: Use Small Multiples for High-Accuracy Tasks
bibliography: references.bib
description: Small multiples reduce clutter and error rates compared to animation
  or overlaid traces.
labels:
- chart:small-multiples
- chart:scatter-plot
- task:compare
- impact:accuracy
- impact:clarity
- visual:layout
---

## The Rule <!-- role: advice -->
To minimize errors and avoid clutter in trend visualization, arrange data as small multiples (side-by-side panels) rather than overlaying all trends in a single view.

## The Logic <!-- role: reason -->
Overlaying many trend lines results in "spaghetti plots" where lines occlude one another, hiding reversals and anomalies. Small multiples isolate each trend, preventing occlusion.
*   **The Principle:** **De-cluttering**. By spatially separating the data, the user can examine complex patterns (like loops or reversals) without visual interference from neighboring data points.
*   **The Evidence:** [@robertson_effectiveness_2008] found that Small Multiples were significantly more accurate than Animation (p<.001) and reduced the visual clutter reported by users in overlaid "Traces" views.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precision tasks where the user must accurately identify specific movements, such as a country's GDP trajectory reversing direction.
*   **Data Type:** Large datasets (e.g., 80+ items) where overlaid lines would cause severe occlusion.
*   **Audience:** Users who need to verify facts or spot subtle counter-trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is very small (e.g., < 20 items).
*   **Reason:** With very few items, the clutter of an overlaid view (Traces) is manageable, and the user may prefer seeing all items in one coordinate system for easier direct comparison of position [@robertson_effectiveness_2008].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate and resolution. Each chart becomes very small, making it harder to read precise axis values.
*   **The Risk:** Comparison between two specific entities requires moving the eye back and forth between panels (serial scanning), which can be slower than comparing two lines drawn right next to each other.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping everything on one chart and using transparency to manage clutter.
*   **Why it fails:** While helpful, transparency (as used in the "Traces" view) still results in lower accuracy and higher perceived clutter than Small Multiples for large datasets [@robertson_effectiveness_2008].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there dense "knots" of ink/pixels where multiple lines cross, making it impossible to follow one line from start to finish?
*   **The Test:** Pick a single data entity in the middle of the cluster. Can you trace its entire path with your finger without crossing another line? If not, use small multiples.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a filter to reduce the number of displayed lines on the main chart.
*   **Best Fix:** Break the single chart into a grid of smaller charts, typically sorted alphabetically or grouped by category (e.g., continent) as done in the study.

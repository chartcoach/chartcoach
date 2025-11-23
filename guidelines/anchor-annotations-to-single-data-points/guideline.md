---
id: anchor-annotations-to-single-data-points
title: Anchor Annotations to Single Data Points
bibliography: references.bib
description: Connect text annotations to specific time points or values rather than
  general regions to align with professional narrative visualization conventions.
labels:
- chart:line
- visual:position
- task:annotate
- impact:clarity
- data:temporal
- audience:general
---

## The Rule <!-- role: advice -->
Attach text annotations directly to a single specific data point (datum) rather than to a general region or the entire view.

## The Logic <!-- role: reason -->
Professional designers overwhelmingly favor high-precision anchoring in narrative visualizations. In a survey of 136 professional visualizations (from sources like the *New York Times*), 74.3% of annotations were anchored to a single datum. This specific linking helps users immediately identify the exact moment or value associated with the textual context.
*   **The Principle:** Specificity in Narrative Visualization
*   **The Evidence:** [@hullman_contextifier_2013]

## Where to Apply <!-- role: context -->
*   **User Goal:** Providing historical context or explaining specific events in a narrative.
*   **Data Type:** Time-series data, specifically stock price or volume timelines.
*   **Chart Type:** Line graphs (where 100% of examples represented a temporal dimension).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Describing a trend or a generalized era.
*   **Reason:** If the insight applies to a duration rather than an event, anchoring to a "Group or Region" (found in 50% of surveyed charts) is appropriate.
*   **Scenario:** Providing a global summary.
*   **Reason:** "Entire Visual View" anchors (35.3%) are used for introductory summaries or broad takeaways.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual clutter. High-precision anchors often require lines or arrows pointing to the data, which adds ink to the chart.
*   **The Risk:** False precision. If the event described (e.g., "Quarter 4 uncertainty") is diffuse, pinning it to a single day may be misleading.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Floating text near the line without a connector.
*   **Why it fails:** It creates ambiguity about whether the text refers to a specific peak, a trough, or the general trend in that area.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the text block have a visual tether (line, arrow, or close proximity) to a single $x,y$ coordinate?
*   **The Test:** Can you point to the exact day or value the text refers to? If you have to wave your hand at a general area, the anchor is too loose.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Draw a line or arrow from the text box to the specific data point (e.g., the closing price on a specific date).
*   **Best Fix:** Implement an interactive hover state where the annotation snaps to the nearest single datum, highlighting the specific value.

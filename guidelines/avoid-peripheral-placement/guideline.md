---
id: avoid-peripheral-placement
title: Avoid Placing Critical Data at Edges
bibliography: references.bib
description: Avoid placing critical information at the very edges or borders of the
  visual field, as human fixation rarely occurs there.
labels:
- visual:layout
- impact:accessibility
- task:scan
- visual:position
---

## The Rule <!-- role: advice -->
Do not position critical data points, alerts, or legends at the extreme borders of the image or screen. Provide a margin.

## The Logic <!-- role: reason -->
Human eye fixations are rarely found near the edges of test images. @borji_quantitative_2013 notes that "non-trivial off-center fixations" are the most difficult to predict and capture. Furthermore, computational models of attention often struggle with "border effects," and human behavior shows a distinct drop-off in attention at the periphery compared to the center and para-central regions.

*   **The Principle:** Edge Effects / Center-Bias
*   **The Evidence:** @borji_quantitative_2013

## Where to Apply <!-- role: context -->
*   **User Goal:** Scanning a full interface or dashboard.
*   **Data Type:** Full-screen visualizations or dense dashboards.
*   **Audience:** All users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Utility navigation bars or fixed status bars.
*   **Reason:** Users learn to look at edges for "tools" (menus), but they do not naturally look there for "content."

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. You must leave "dead zones" or whitespace around the margins.
*   **The Risk:** If you push data to the edge to maximize density, it may be ignored entirely ("banner blindness" or peripheral neglect).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing the legend or a critical key at the very bottom-right or top-right pixel edge.
*   **Why it fails:** @borji_quantitative_2013 highlights the difficulty of predicting attention at edges; users are unlikely to fixate there unless explicitly driven by a task.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is text or data touching the outer frame of the visualization?
*   **The Test:** Apply a "safe zone" overlay (like in broadcast video). Is anything critical outside the inner 90% of the rectangle?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add padding/margin around the entire visualization container.
*   **Best Fix:** Move peripheral elements into the flow of the document (e.g., direct labeling instead of a peripheral legend).

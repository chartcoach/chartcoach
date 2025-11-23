---
id: prioritize-temporal-transitions
title: Prioritize Temporal Transitions Over Granularity
bibliography: references.bib
description: When multiple sequencing options exist, users prefer chronological steps
  over changes in granularity or variable dimensions.
labels:
- data:temporal
- task:sequencing
- impact:preference
- visual:transition
- audience:general
---

## The Rule <!-- role: advice -->
When you have a choice of how to transition from the current visualization to the next, prioritize **Temporal** changes (moving forward or backward in time) over **Dimension** or **Measure** changes. Avoid **Granularity** changes (drilling down/up) if a temporal or comparative option is available.

## The Logic <!-- role: reason -->
Users demonstrate a hierarchy of preference for transition types when costs are equal.
*   **The Principle:** Transition Type Preference.
*   **The Evidence:** In controlled studies, [@hullman_deeper_2013] found a distinct preference order: Temporal transitions were preferred over all others. Dimension and Measure walks (changing the specific variable shown) were preferred over Granularity changes (zooming in/out). The hierarchy is: Temporal > (Dimension | Measure) > Granularity.

## Where to Apply <!-- role: context -->
This applies when designing the "next step" in an automated or guided data presentation.
*   **User Goal:** Smoothly following a data narrative.
*   **Data Type:** Datasets containing time series, hierarchical categories, and multiple measures.
*   **Audience:** General audiences using linear presentation tools.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "Overview, Zoom, Filter" mantra.
*   **Reason:** While users *prefer* temporal steps in strictly linear narratives, exploratory analysis often demands starting with an overview (Granularity transition). However, within a narrative flow, the preference remains Temporal [@hullman_deeper_2013].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may delay showing detailed breakdowns (Granularity) until the temporal trends are established.
*   **The Risk:** If the specific detail is the most critical insight, burying it behind a temporal sequence might delay the "aha" moment.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Immediately drilling down from a country view to a state view (Granularity) when a temporal trend at the country level is available and relevant.
*   **Why it fails:** Users rate granularity transitions as the least preferred connector between visualization states compared to time or variable changes [@hullman_deeper_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at your storyboard edges.
*   **The Test:** Label every transition arrow: "Time", "Topic", or "Zoom". If you see "Zoom" occurring before "Time" variations are exhausted, consider reordering.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder the slides. Show the evolution of the dataset over time first, then switch dimensions or drill down.
*   **Best Fix:** Design the sequence to exhaust temporal comparisons (e.g., 1990 vs 2000) before introducing granularity changes (e.g., 2000 Total vs 2000 Sub-region).

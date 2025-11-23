---
id: minimize-visual-distance
title: Minimize Distance Between Related Elements
bibliography: references.bib
description: Place graphical elements and their associated data or comparators in
  close proximity to reduce cognitive load.
labels:
- impact:cognitive-load
- visual:layout
- task:compare
- chart:general
---

## The Rule <!-- role: advice -->
Reduce the spatial distance between a visual element (like a data point) and its target (like a label, legend, or comparison point).

## The Logic <!-- role: reason -->
Visual interpretation is serial and incremental, not holistic. The brain must hold information in working memory while scanning from one point to another.
*   **The Principle:** Graph Difficulty Principle / Working Memory Limits.
*   **The Evidence:** [@borner_data_2019] cites Kosslyn et al., demonstrating that "the time required to read a visual image increases systematically with the distance between initial focus point and the target."

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid reading or comparison of values.
*   **Data Type:** Any visualization requiring the user to look up values (e.g., mapping colors to a legend).
*   **Audience:** All users, as this relies on fundamental cognitive constraints.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Small multiples or faceted views where global comparisons are secondary.
*   **Reason:** Sometimes separation is necessary to prevent over-plotting, even if it increases eye-scan travel time.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Layouts may become more cluttered if labels are directly integrated (direct labeling) rather than tucked away in a side legend.
*   **The Risk:** The visualization may feel "crowded" if not managed with whitespace.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing a legend in the far corner of a large monitor or printout.
*   **Why it fails:** It forces the user to rely on "temporal storage and retrieval of an object's location in memory," which increases effort and potential for error [@borner_data_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Long leader lines connecting labels to data, or legends located outside the immediate focal area of the chart.
*   **The Test:** Track your eye movement. If you have to move your eyes back and forth more than once to understand a single data point, the distance is too great.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the legend closer to the chart area.
*   **Best Fix:** Use direct labeling (place the text label directly next to the data line or bar) to eliminate the distance entirely.

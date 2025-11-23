---
id: overlay-slope-charts
title: Superimpose Series in Slope Charts
bibliography: references.bib
description: Overlay data series in a single slope chart rather than separating them
  or animating them.
labels:
- chart:slope
- task:compare
- visual:position
- impact:precision
---

## The Rule <!-- role: advice -->
When comparing two data series using slope charts, overlay the series in the same space (superposition) rather than using small multiples or animation.

## The Logic <!-- role: reason -->
Overlaying values minimizes eye movements and memory load. For slope charts specifically, this static superposition allows for higher precision than animation because the motion of a line (often simple vertical translation) provides a weaker signal than the motion of a bar growing or shrinking [@ondov_face_2019].

*   **The Principle:** Superposition / Reduced Saccades
*   **The Evidence:** In the experiments, overlaid slope charts outperformed all other arrangements, including animated, mirrored, and adjacent small multiples, for identifying the maximum delta [@ondov_face_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise identification of changes in slope or value between two datasets.
*   **Data Type:** Paired numerical data suitable for slope charts (e.g., Time A vs Time B).
*   **Audience:** Users needing to perform analytical comparisons of change rates.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High data density / Clutter.
*   **Reason:** While not explicitly tested for clutter limits in this paper, the authors acknowledge that overlaying many series can lead to occlusion. The study used controlled datasets with limited points [@ondov_face_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Separability. It can be harder to view one series in isolation when they are drawn on top of each other.
*   **The Risk:** Occlusion. If data points overlap perfectly, one series may hide the other.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Animating the slope chart to show the change.
*   **Why it fails:** Animation did not accrue performance benefits for slope charts in the detection of value changes [@ondov_face_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there two separate charts side-by-side?
*   **The Test:** Can you see the relationship between Series A and Series B without moving your eyes?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the second series onto the same axes as the first series, using a distinct color or line style (e.g., gray for context).
*   **Best Fix:** Use a single overlaid chart design where both series are visible simultaneously, distinguishing them by color or opacity.

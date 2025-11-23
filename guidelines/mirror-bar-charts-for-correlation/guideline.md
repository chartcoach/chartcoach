---
id: mirror-bar-charts-for-correlation
title: Mirror Bar Charts to Estimate Correlation
bibliography: references.bib
description: Use mirrored axes for bar charts when the user needs to judge correlation.
labels:
- chart:bar
- task:correlate
- visual:position
- visual:orientation
- impact:pattern-recognition
- data:quantitative
---

## The Rule <!-- role: advice -->
Arrange comparative bar charts with mirrored axes (back-to-back) rather than standard side-by-side or stacked arrangements when the goal is judging correlation.

## The Logic <!-- role: reason -->
Mirrored arrangements harness the human visual system's sensitivity to symmetry. When comparing two bar chart series to determine if they are correlated, a mirrored layout significantly outperforms standard adjacent or stacked layouts.
*   **The Principle:** Bilateral Symmetry Processing
*   **The Evidence:** Data collated by [@zeng_review_2023] from [@ondov_face_2019] ranks mirrored bar charts (E-3) as the most effective design for correlation tasks, outperforming overlaid (E-4) and adjacent (E-2) designs.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the correlation or similarity between two sets of values.
*   **Data Type:** Quantitative data presented as Bar Charts.
*   **Audience:** Users needing to assess the relationship between two categorical distributions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary task is identifying specific magnitude differences (finding the "biggest mover") rather than correlation.
*   **Reason:** For finding specific value differences, overlaid designs (E-4) generally perform better than mirrored designs [@ondov_face_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Conventional readability. Users are less familiar with mirrored axes compared to standard side-by-side bar charts.
*   **The Risk:** Initial confusion regarding the axis direction for the mirrored series.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** stacking charts vertically (E-1) to check for correlation.
*   **Why it fails:** Vertical stacking was ranked lowest for correlation tasks in the experimental results [@ondov_face_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the bars originate from a shared central spine, or do they look like two separate charts placed next to each other?
*   **The Test:** Check if the baseline is shared and central (Mirrored) vs. separate baselines (Adjacent).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Flip the orientation of one bar chart so they share a central y-axis (or x-axis).
*   **Best Fix:** Implement a "Diverging Bar Chart" or "Population Pyramid" style layout where the bars grow outwards from a central line.

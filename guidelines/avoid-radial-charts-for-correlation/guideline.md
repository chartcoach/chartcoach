---
id: avoid-radial-charts-for-correlation
title: Avoid Radial and Stacked Charts for Correlation
bibliography: references.bib
description: Radial and stacked visualizations perform poorly for correlation tasks
  compared to Cartesian point or line charts.
labels:
- chart:radar
- chart:donut
- chart:stacked-area
- task:correlate
- visual:area
- visual:angle
---

## The Rule <!-- role: advice -->
Do not use radar charts, donut charts, or stacked area charts when the primary task is judging correlation.

## The Logic <!-- role: reason -->
The collation of graphical perception knowledge by [@zeng_review_2023] indicates that these chart types generally yield lower rankings in correlation tasks. The experimental results from [@harrison_ranking_2014] show that designs utilizing area and angle in radial layouts (e.g., E-35, E-53) or stacked layouts (e.g., E-33, E-39) consistently rank lower in performance (higher error rates and JNDs) compared to standard scatterplots or line charts. Coordinate transforms (like wrapping a bar chart into a donut) distort the perceptual baseline required to judge covariance.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the similarity or relationship between two variables.
*   **Data Type:** Quantitative data suitable for correlation analysis.
*   **Audience:** Any user, as these distortions affect basic perceptual processing.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The task is "Retrieve Value" or "Part-to-whole" comparison rather than "Correlate."
*   **Reason:** While bad for correlation, stacked or radial charts may be acceptable for simple value lookup or proportion judgments (though often still inferior to bar charts).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual variety. Radial charts are often chosen for aesthetic reasons.
*   **The Risk:** Users will fail to notice significant correlations or will perceive correlations where none exist due to the distortion of the visual forms.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Radar chart to show the "shape" of data profile similarity.
*   **Why it fails:** The perceptual judgment of correlation on radial axes is far less precise than on Cartesian axes [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the axes arranged in a circle (Radar/Donut) or stacked on top of each other (Stacked Area)?
*   **The Test:** Ask a user to estimate the correlation coefficient (r) between two variables shown in the chart. Compare their accuracy to a scatterplot.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Unroll radial charts into linear charts (line or bar).
*   **Best Fix:** Use Small Multiples of scatterplots or standard line charts to show relationships.

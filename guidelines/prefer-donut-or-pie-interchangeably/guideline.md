---
id: prefer-donut-or-pie-interchangeably
title: Use Donut Charts Interchangeably with Pie Charts
bibliography: references.bib
description: Donut charts perform as well as pie charts because the central angle
  is not the primary visual cue.
labels:
- chart:donut
- chart:pie
- visual:area
- visual:arc-length
- task:retrieve-value
- impact:flexibility
---

## The Rule <!-- role: advice -->
Use donut charts and pie charts interchangeably for part-to-whole comparisons; do not avoid donut charts based on the assumption that the missing central angle reduces accuracy.

## The Logic <!-- role: reason -->
For decades, it was assumed that the central angle was the primary visual cue for reading pie charts. However, evidence collated by Zeng & Battle [@zeng_review_2023] from experiments by Skau & Kosara [@skau_arcs_2016] refutes this. Their study demonstrated that "Baseline Donut" charts performed just as well as "Baseline Pie" charts in value retrieval tasks. This indicates that users rely primarily on **arc length** and **area**, not the central angle (which is absent in a donut chart), to judge proportions.

*   **The Principle:** Visual Encoding Redundancy.
*   **The Evidence:** [@skau_arcs_2016], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing proportions or retrieving specific percentage values from a whole.
*   **Data Type:** Quantitative part-to-whole data (percentages summing to 100%).
*   **Audience:** General audiences familiar with radial charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using an extremely thin ring.
*   **Reason:** If the donut becomes too thin (a very large inner radius), it essentially becomes an arc-length chart, which can slightly degrade performance compared to thicker donuts or filled pies.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the center pixel area.
*   **The Risk:** While accuracy is maintained, some traditionalists may still view donut charts as "chart junk" despite the empirical evidence to the contrary.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing the use of a standard filled pie chart when a donut chart would be aesthetically better or allow for a label in the center.
*   **Why it fails:** It restricts design flexibility without offering a tangible benefit in human perception accuracy.

## How to Check <!-- role: check -->
*   **Visual Sign:** A standard pie chart is used where a donut chart might save space or allow for central labeling.
*   **The Test:** Check if the center of the chart is required for data encoding. If not, a donut is a valid alternative.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the pie chart to a donut chart if you need to place a total value or label in the center.
*   **Best Fix:** Choose the variation (pie or donut) that best fits the layout constraints, knowing that readability is equivalent for standard thicknesses.

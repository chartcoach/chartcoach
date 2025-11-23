---
id: numerosity-avoid-connections
title: Disconnect Points to Estimate Quantity
bibliography: references.bib
description: Avoid connecting data points with lines if the user's primary task is
  to estimate the total number of items.
labels:
- chart:line-chart
- chart:scatterplot
- task:aggregate
- visual:connection
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not visually connect data points with lines if the primary goal is for the user to estimate the numerosity (count) of the data points.

## The Logic <!-- role: reason -->
Visual connections (lines) trigger a grouping mechanism where connected items are perceived as a single object or unit. This "objecthood" causes viewers to underestimate the number of original constituent parts (the individual data points) because the visual system prioritizes the whole over the parts.
*   **The Principle:** Connectedness and Numerosity Underestimation
*   **The Evidence:** [@szafir_four_2016] as collated in [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the density or total count of items (e.g., "How many events occurred?").
*   **Data Type:** Discrete events or network data where the node count is significant.
*   **Audience:** Users performing summary tasks related to volume or frequency.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to track trends, rates of change, or sequences over time.
*   **Reason:** Lines are superior for showing continuity and trends (structure estimation), which often outweighs the need for precise counting of the nodes [@szafir_four_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** By removing connections, you make it significantly harder to see the sequence or flow between points.
*   **The Risk:** The visualization becomes a scatterplot, potentially obscuring the relationship between consecutive data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding markers (dots) on top of a heavy line to help with counting.
*   **Why it fails:** While markers help, the strong visual connection of the line still biases the perceptual system toward seeing a single shape rather than a collection of discrete units.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there lines linking the data points?
*   **The Test:** Ask a user to quickly estimate the number of points in a section. Compare their estimate to the actual count; connections usually lead to lower estimates.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the lines and leave only the point markers (convert line chart to scatterplot/dot plot).
*   **Best Fix:** If sequence is needed but count is also important, use a "dot plot" style or ensure the markers are visually dominant over very faint connecting lines.

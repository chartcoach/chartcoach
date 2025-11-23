---
id: avoid-aggregation-for-object-centric-tasks
title: Avoid Aggregation for Object-Centric Tasks
bibliography: references.bib
description: Do not use binning or density plots when the user needs to identify,
  verify, or locate individual data points.
labels:
- chart:scatterplot
- task:retrieve-value
- task:filter
- visual:mark
- impact:detail
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not use grouping strategies (such as binning, contours, or density estimation) if the user needs to perform object-centric tasks like retrieving values, locating specific points, or verifying object details.

## The Logic <!-- role: reason -->
Scatterplot designs face a fundamental trade-off between aggregate-level legibility and object-level fidelity.
*   **The Principle:** Mark Fidelity. Grouping strategies abstract individual marks into larger visual shapes (like hex-bins or contour lines). This process "sacrifices the fidelity of item detail" to expose distributions.
*   **The Evidence:** [@sarikaya_scatterplots_2018] explicitly classifies tasks like "Identify object," "Locate object," and "Verify object" as unsupported (marked with an ✘ or requiring amenities) by design choices that utilize point grouping. [@zeng_review_2023] supports this by highlighting that tasks like `retrieve value` require designs that preserve individual encoding data.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user asks questions like "What is the value of item X?" or "Where is the outlier labeled Y?"
*   **Data Type:** Datasets where individual data points carry specific semantic meaning (e.g., a specific country in a GDP plot).
*   **Audience:** Users performing detailed auditing or lookup operations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The specific object-centric task is solely to find an outlier that is spatially distinct.
*   **Reason:** Some aggregation techniques (like Splatterplots) explicitly restore and style individual marks that fall outside the grouped region [@sarikaya_scatterplots_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Scalability. By refusing to aggregate, you risk visual clutter and overplotting if the dataset is large.
*   **The Risk:** The visualization may become illegible for distribution tasks (seeing the "shape" of the data) because of the noise from individual points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a heatmap or contour plot for a "Find the data point" task.
*   **Why it fails:** The user cannot click or hover over a specific data point because it has been mathematically merged into a region.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart use bins, hexes, or smooth gradients instead of distinct circles/points?
*   **The Test:** Try to point to a single row of data from your original spreadsheet on the chart. If you cannot distinguish it from its neighbors, you have broken this rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the mark type back to "point" or "circle."
*   **Best Fix:** Use a hybrid approach: display the full scatterplot for low-density data, or implement a "lens" interaction that reveals individual points within a dense area upon hover [@sarikaya_scatterplots_2018].

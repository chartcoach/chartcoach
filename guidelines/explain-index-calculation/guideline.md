---
id: explain-index-calculation
title: Annotate Index Relationships Verbally
bibliography: references.bib
description: Add a text annotation explaining the calculation logic of indexed values
  to assist general audiences.
labels:
- chart:line
- visual:annotation
- impact:comprehension
- data:index
- audience:novice
---

## The Rule <!-- role: advice -->
Include a direct verbal explanation on the chart that translates the axis values into a sentence describing their relationship to the baseline.

## The Logic <!-- role: reason -->
Indices are "tricky to understand" for general audiences because they represent a mathematical difference rather than a raw count.
*   **The Principle:** Explanatory Annotation. Providing a "read-key" helps users decode the abstraction of the y-axis.
*   **The Evidence:** To ensure readers understand how an index works, Mintzer-Sweeney advises giving "a verbal explanation of how values relate to that baseline," such as annotating a tick mark with text like "-5% from 2023" [@mintzer_y_axis_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing relative change or performance against a benchmark.
*   **Data Type:** Relative data (percentages, index points) where the y-axis does not represent absolute counts.
*   **Audience:** Readers who are not data specialists or economists.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly technical or financial dashboards.
*   **Reason:** Expert audiences (e.g., traders) understand basis points or index values without needing tutorial text.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Chart density. It adds extra text elements to the visualization.
*   **The Risk:** Can clutter the chart if not placed carefully near the axis or a relevant data point.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Putting the explanation in a footer or methodology section.
*   **Why it fails:** Readers need the context *while* scanning the lines, not after finishing the article.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there only numbers (e.g., -5, -10) on the axis?
*   **The Test:** Can a reader describe the unit of measurement ("percent difference from year X") immediately without reading the subtitle?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text box near a major gridline saying "X% lower than [Baseline]."
*   **Best Fix:** Incorporate the explanation into the axis gridline labels themselves (e.g., label the tick "-5% from 2023").

---
id: prioritize-familiar-chart-types
title: Prioritize Familiar Chart Types
bibliography: references.bib
description: Use standard chart types like bar and line charts to ensure broader audience
  comprehension and reduce cognitive load.
labels:
- chart:bar
- chart:line
- impact:clarity
- impact:accessibility
- audience:novice
- complexity:low
---

## The Rule <!-- role: advice -->

Use familiar, standard chart types—such as bar charts, line charts, or maps—that your audience can instantly recognize. Avoid novel, complex, or "artful" visualizations when a basic format serves the data.

## The Logic <!-- role: reason -->

The chosen chart type fundamentally shapes how an audience interprets data. Familiarity acts as a heuristic that aids decoding; if viewers recognize the format, they can focus on the content rather than deciphering the method.

*   **The Principle:** Visual Recognition and Cognitive Load.
*   **The Evidence:** Workshop insights indicate that recognizing a chart type helps viewers understand it; participants often prefer several simple charts over a single complex one [@knoll_gulf_2025]. Empirical testing shows that for comparing one-dimensional data, familiar bar charts are perceived as easier to interpret than bubble charts [@prantl_studying_forthcoming]. Practitioners report that audiences actively request simpler depictions over artful designs [@schuster_who_2023].

## Where to Apply <!-- role: context -->

*   **User Goal:** When the primary objective is accurate interpretation and quick comparison of values.
*   **Audience:** Lay viewers, the general public, or any group where data literacy levels vary.
*   **Data Type:** Standard categorical (bar), temporal (line), or geospatial (map) data.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Exploratory analysis for domain experts using high-dimensional data.
*   **Reason:** Basic charts may be unable to show multivariate correlations or clusters effectively without oversimplifying the data.
*   **Scenario:** When the chart type itself (e.g., a scatterplot) is considered "unfamiliar" or disliked by a specific stakeholder group, even if standard elsewhere [@schuster_who_2023].

## The Price <!-- role: costs -->

*   **The Sacrifice:** You lose the "wow" factor of novel design and potentially the spatial efficiency of encoding multiple dimensions into one complex graphic.
*   **The Risk:** Using multiple simple charts to replace one complex visualization takes up more screen real estate.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Prioritizing "artful" or unique designs to make the visualization look sophisticated.
*   **Why it fails:** Practitioners note that while these designs look impressive, they often result in lower understanding and requests for simpler versions [@schuster_who_2023].
*   **The Wrong Fix:** Using bubble charts for simple comparisons.
*   **Why it fails:** They are harder to interpret than standard bar charts for one-dimensional data [@prantl_studying_forthcoming].

## How to Check <!-- role: check -->

*   **Visual Sign:** If the chart requires a paragraph of text explaining *how to read it* (not just what it says), it is likely too complex.
*   **The Test:** Show the chart to a non-expert. If they cannot name the chart type (e.g., "It's a bar chart") within 2 seconds, it fails the familiarity test.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Convert exotic formats (like bubble charts or radial charts) into standard bar or line charts.
*   **Best Fix:** If the data is too complex for one chart, break it down into "small multiples"—a series of simple charts—rather than one multi-dimensional visualization [@knoll_gulf_2025].

---
id: prioritize-unique-chart-types
title: Prioritize Unique Visualization Types
bibliography: references.bib
description: Common chart types like bar and line graphs are easily forgotten; unique
  types like diagrams and trees are memorable.
labels:
- chart:diagram
- chart:network
- chart:bar
- impact:memorability
- impact:distinctiveness
---

## The Rule <!-- role: advice -->
Choose unique or novel visualization types (such as diagrams, tree networks, or grid matrices) over standard bar charts or line graphs when memorability is the objective.

## The Logic <!-- role: reason -->
Common graphs (bar charts, line charts) share a uniform visual structure and limited variability, causing them to interfere with one another in human memory. A viewer has seen thousands of bar charts; they all look alike. Unique types (like diagrams, heatmaps, or trees) have specific visual structures that act as unique exemplars, making them significantly easier to recall.

*   **The Principle:** Schema Interference / Conceptual Distinctiveness
*   **The Evidence:** [@borkin_what_2013] (Section 7.1, Fig 7)

## Where to Apply <!-- role: context -->
*   **User Goal:** Ensuring a specific dataset stands out in the viewer's mind later.
*   **Data Type:** Hierarchical data, process flows, or multivariate matrices.
*   **Audience:** Audiences suffering from "chart fatigue" (e.g., reading a report full of bar charts).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the audience needs to read values precisely and quickly without learning a new visual language.
*   **Reason:** Standard charts (bars/lines) are "common" because they are highly effective and standardized for data comparison. Novelty can slow down comprehension.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Familiarity. The user has to learn how to read the chart.
*   **The Risk:** High false-alarm rates. Users might remember *seeing* a unique chart but might not remember the *content* accurately if the encoding is too complex.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing simple comparison data into a complex network graph just to be "unique."
*   **Why it fails:** If the data doesn't fit the structure, the visualization becomes memorable but misleading or useless.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look like something "taught in primary school" (e.g., a standard bar chart)?
*   **The Test:** If the chart type is a "Bar," "Line," or "Point" plot, it falls into the lowest memorability tier found in the study.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Annotate the standard chart heavily to give it unique visual characteristics.
*   **Best Fix:** Re-evaluate if the data can be represented as a diagram, a circular layout, or a tree structure to leverage visual novelty.

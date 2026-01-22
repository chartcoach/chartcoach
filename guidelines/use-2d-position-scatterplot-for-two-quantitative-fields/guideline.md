---
id: use-2d-position-scatterplot-for-two-quantitative-fields
title: Use a point scatterplot with X/Y position for two quantitative variables
bibliography: references.bib
description: Encode two quantitative fields as point positions on orthogonal axes
  to support common scatterplot analysis tasks.
labels:
- chart:scatter
- task:retrieve-value
- task:filter
- task:sort
- task:cluster
- task:correlate
- task:aggregate
- task:characterize-distribution
- task:find-anomalies
- visual:position
- data:quantitative
- audience:general
- complexity:basic
---

## Use X/Y position encodings for two quantitative fields in a scatterplot <!-- role: advice -->

Use a point scatterplot that maps one quantitative variable to horizontal position and the other quantitative variable to vertical position. Use linear scales on both axes unless you have a specific reason to transform the scale.

## Why position-based scatterplots support many analysis tasks <!-- role: reason -->

Using position on two orthogonal axes provides a direct spatial representation of two quantitative variables, enabling readers to visually inspect patterns in point placement for multiple task types.

**Mechanism:** Mapping values to X and Y position creates a 2D spatialization that supports both object-level judgments (about individual points) and aggregate-level judgments (about overall structure) within the same view.

**Evidence:** A scatterplot design specified as points with quantitative fields encoded on positionX and positionY (linear scales) is treated as a broadly applicable design baseline connected to multiple analysis tasks (e.g., retrieve value, filter, sort, cluster, correlate, aggregate, characterize distribution, find anomalies) in a structured collation for visualization recommendation use cases [@sarikayaScatterplotsTasksData2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline constrains only the core encoding/mark choice (point + X/Y position for two quantitative fields) and does not prescribe additional design decisions.

## When this applies to your visualization scenario <!-- role: context -->

- **User Goal:** Understand how two numeric variables relate and how data points are arranged in 2D space.
- **Task:** Retrieve values, filter points, sort/compare values, cluster, correlate, aggregate, characterize distribution, or find anomalies.
- **Data:** Two quantitative attributes; one row per observation (points).
- **Chart Setting:** Static 2D view; standard display; minimal required interaction.
- **Audience:** General audiences who can read x/y axes.
- **Success Criterion:** Readers can perform the intended task(s) using the spatial arrangement of points.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** You do not have two quantitative fields to plot on orthogonal axes. **Why:** The design definition for this guideline depends on mapping two quantitative variables to positionX and positionY.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You commit two axes to quantitative fields, reducing flexibility for other encodings. **Risk:** If the task depends on information not represented by these two fields, readers may infer patterns that are not relevant to their goal. **Mitigation:** Ensure the chosen two quantitative fields match the user’s task and decision need.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a scatterplot when one or both fields are not quantitative. **Why it fails:** The intended interpretation of x/y position as a continuous quantitative mapping no longer holds for this rule’s scope.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask what the axes represent or cannot interpret the point positions as numeric values. **Quick Check:** Confirm both axes map to quantitative variables and both scales are linear. **Stronger Test:** Ask a reader to complete one target task (e.g., identify correlation or find anomalies) using only the plotted positions.

## What to do instead <!-- role: fix -->

- Use a chart design that matches your actual data types if one axis is not quantitative.
- Re-select fields so that exactly two quantitative variables are mapped to x/y position.
- Add a separate view tailored to tasks not supported by the chosen two variables.
- Reframe the analysis goal to one of the tasks supported by the x/y position scatterplot.

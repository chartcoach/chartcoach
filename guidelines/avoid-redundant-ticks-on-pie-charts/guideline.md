---
id: avoid-redundant-ticks-on-pie-charts
title: Rely on Natural Anchors for Pie Charts Rather than Added Ticks
bibliography: references.bib
description: Adding explicit tick marks to pie charts does not improve estimation
  accuracy and adds unnecessary clutter.
labels:
- chart:pie-chart
- visual:clutter
- task:estimate-value
- impact:simplicity
- impact:efficiency
- data:proportions
---

## The Rule <!-- role: advice -->
Do not add tick marks or grid lines to pie charts to indicate specific percentages (e.g., at 25% or 50% intervals).

## The Logic <!-- role: reason -->
Pie charts already possess "natural anchors" at cardinal directions (0°, 90°, 180°, 270°) which correspond to 0%, 25%, 50%, and 75%. Adding explicit visual marks to represent these values yields no statistically significant improvement in estimation accuracy because users already intuit these positions.
*   **The Principle:** Gestalt Closure / Natural Mapping
*   **The Evidence:** As summarized by Zeng and Battle [@zeng_review_2023], experimental data from Redmond [@redmond_visual_2019] showed no significant difference in performance between baseline pie charts (E-1) and pie charts with added quartile ticks (E-5).

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating segment size in a circular layout.
*   **Data Type:** Part-to-whole data.
*   **Audience:** General users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Interactive tooltips.
*   **Reason:** While *static* ticks don't help, on-demand readout of exact values is a standard usability feature for precision, distinct from estimation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "scientific" aesthetic that grids might convey.
*   **The Risk:** Users might *feel* the chart is less precise, even if their actual performance remains the same.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Drawing lines through the pie chart to divide it into quadrants.
*   **Why it fails:** It adds ink and cognitive load without improving the user's ability to estimate the area or angle [@redmond_visual_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there ticks, dashes, or lines on the perimeter of the pie chart intended to show scale?
*   **The Test:** Remove them. If the chart remains equally readable, they were redundant.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the tick marks.
*   **Best Fix:** Rely on the shape itself and provide direct data labels (e.g., "33%") if precise reading is required.

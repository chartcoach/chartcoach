---
id: use-pie-charts-for-anchor-percentages
title: Use Pie Charts for Anchor Percentages
bibliography: references.bib
description: Pie charts are most effective when displaying easily recognizable fractions
  like quarters or halves.
labels:
- chart:pie
- visual:shape
- task:part-to-whole
- data:categorical
- impact:readability
---

## The Rule <!-- role: advice -->
Use pie charts specifically when your data contains values close to 25%, 50%, or 75%.

## The Logic <!-- role: reason -->
Readers can spot these specific percentages (quarters and halves) more easily in a circular format than they can in a linear stacked bar or column chart. The circular shape provides intuitive visual anchors for these specific proportions [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing how a total is divided into shares.
*   **Data Type:** Categorical data where specific slices represent roughly 1/4, 1/2, or 3/4 of the total.
*   **Audience:** General audience looking for quick part-to-whole recognition.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The values are arbitrary (e.g., 33%, 12%, 55%) and do not align with these visual anchors.
*   **Reason:** Without these recognizable anchors, the advantage over other chart types diminishes.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to easily compare the lengths of the segments, which is easier in bar charts.
*   **The Risk:** If values deviate significantly from these anchors, precision is lost.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a stacked bar chart for a 50/50 split.
*   **Why it fails:** It may be slightly slower to recognize "half" in a bar compared to a semi-circle [@muth_pie_charts_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart clearly show a right angle (25% or 75%) or a straight line through the middle (50%)?
*   **The Test:** Glance at the chart. Can you instantly identify the fraction without reading the label?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Keep the pie chart if the data supports these anchors.
*   **Best Fix:** If the data does not contain these specific percentages, consider a bar or column chart instead.

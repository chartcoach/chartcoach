---
id: use-tables-for-value-retrieval
title: Use Tables for Precise Value Retrieval
bibliography: references.bib
description: Tables are significantly more accurate and faster than charts when the
  user needs to read specific values.
labels:
- chart:table
- task:retrieve-value
- visual:text
- impact:precision
- data:quantitative
---

## The Rule <!-- role: advice -->
If the user needs to read, look up, or report exact values, use a **Table**. Do not force users to decode visual marks (bars, points, angles) for precise data entry.

## The Logic <!-- role: reason -->
While visualization is powerful for patterns, symbolic representation (text) is superior for precision. The data collated by Zeng and Battle [@zeng_review_2023] confirms this distinction.
*   **The Principle:** Direct Lookup. Reading a number requires linguistic processing, whereas reading a chart requires decoding a visual abstraction (mapping position to axis), which introduces error.
*   **The Evidence:** In the referenced study, Tables (E-13, E-14, E-15) ranked #1 for both **Accuracy** and **Time** for the "Retrieve Value" task, significantly outperforming all graphical representations including Bar and Scatterplots [@saket_task-based_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Looking up a phone number, a price, or a specific sensor reading.
*   **Data Type:** Any data type where exact precision is required.
*   **Audience:** Operations managers, accountants, or users performing data entry.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to see the value *in context* of the whole (e.g., "Is this high or low?").
*   **Reason:** Tables fail to show relative standing or distribution without additional visual cues.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to see trends, clusters, or correlations quickly.
*   **The Risk:** Users may miss the "big picture" or anomalies because they are focused on individual cells.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding tooltips to a chart to "fix" retrieval issues.
*   **Why it fails:** While helpful, hovering over specific data points (especially in scatterplots) is slower (Fitts's Law) than scanning a sorted list or table for a specific label [@saket_task-based_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the user holding a ruler up to the screen to read the axis?
*   **The Test:** Ask the user to read out 5 specific values. Measure the time.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add value labels directly to the chart marks.
*   **Best Fix:** Provide a companion Table view alongside the visualization.

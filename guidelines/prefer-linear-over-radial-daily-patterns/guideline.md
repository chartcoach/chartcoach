---
id: prefer-linear-over-radial-daily-patterns
title: Use Linear Bar Charts Instead of Radial Charts for Daily Patterns
bibliography: references.bib
description: Linear layouts outperform radial layouts for analyzing daily time-series
  data in terms of accuracy, speed, and user preference.
labels:
- chart:bar
- chart:radial
- task:retrieve-value
- task:filter
- visual:position
- visual:length
- impact:accuracy
- impact:speed
- data:temporal
- data:quantitative
---

## The Rule <!-- role: advice -->
Visualize daily quantitative patterns using linear bar charts rather than radial (rose) charts.

## The Logic <!-- role: reason -->
Linear layouts are perceptually superior to radial layouts for reading and comparing values.
*   **The Principle:** Linear layouts allow for easier length and position comparisons compared to the angular and orientation changes required by radial charts.
*   **The Evidence:** In a comparison of radial and linear charts for daily patterns (such as traffic accidents), linear designs consistently outperformed radial designs in accuracy and completion time across filtering, value retrieval, and sorting tasks [@waldner_comparison_2020]. This finding is supported by broader reviews of graphical perception indicating the inefficiency of radial layouts for these tasks [@zeng_review_2023].

## Where to Apply <!-- role: context -->
Use this guidance when visualizing time-series data that spans a daily cycle (24 hours).
*   **User Goal:** Reading specific values, finding extremes, or comparing time slots (e.g., AM vs. PM).
*   **Data Type:** Quantitative data aggregated by hour (e.g., 24 bins).
*   **Audience:** General audiences who need to interpret data quickly and accurately.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is purely decorative or metaphorical (referencing a clock face) and precise data retrieval is not required.
*   **Reason:** While radial charts are less accurate, they may be used for aesthetic variety if performance cost is acceptable, though users in the study actually preferred the linear layout [@waldner_comparison_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "clock metaphor" visual association where the circle represents the 24-hour cycle.
*   **The Risk:** The visualization may look less novel or "infographic-style" compared to a rose chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a radial chart to emphasize the "cyclical" nature of the day.
*   **Why it fails:** The study explicitly tested this "clock metaphor" hypothesis and found it did not aid interpretation; users were slower and less accurate with the radial layout [@waldner_comparison_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the data wrapped in a circle (polar coordinates) where height extends outward from a center?
*   **The Test:** Ask a user to quickly identify the exact value of a specific hour. If they struggle or tilt their head, the radial layout is likely hindering performance.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Unwrap the chart into a standard Cartesian coordinate system (flat x-axis).
*   **Best Fix:** Use a single, continuous 24-hour linear bar chart.

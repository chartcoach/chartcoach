---
id: use-circular-slices-for-speed
title: Use Circular Slice Designs For Faster Comparisons
bibliography: references.bib
description: Circular slice designs are faster to read than stacked bars or standard
  pie charts.
labels:
- chart:radial
- chart:bar
- task:sort
- impact:speed
- visual:area
- data:quantitative
---

## The Rule <!-- role: advice -->
Utilize circular slice designs (area-based circular charts) when the speed of task completion is the highest priority.

## The Logic <!-- role: reason -->
Specific circular configurations allow for faster processing of part-to-whole relationships than linear bars or standard angle-based pies.
*   **The Evidence:** Experimental results from @kosara_impact_2019, extracted by @zeng_review_2023, show that Circular Slice designs (E-2) and Straight-Line Circular designs (E-3) were significantly faster (Time metric) than Stacked Bars (E-4) and Standard Pies (E-1).

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification of rankings within a whole.
*   **Data Type:** Part-to-whole data where speed is critical (e.g., dashboards, real-time monitoring).
*   **Audience:** Users needing "at a glance" information.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the visualization tool only supports standard library charts.
*   **Reason:** The "Circular Slice" (E-2) and "Straight-Line Circular" (E-3) are specific experimental designs that may not be standard in all tools.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may be using a non-standard chart type that requires brief user acclimation.
*   **The Risk:** If implemented poorly (not matching the E-2/E-3 specifications), you may lose the speed advantage.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Stacked Bar Chart for speed.
*   **Why it fails:** While Stacked Bars (E-4) are accurate, @kosara_impact_2019 found them to be significantly slower than the circular slice variants.

## How to Check <!-- role: check -->
*   **Visual Sign:** Users are taking too long to read a Stacked Bar or Pie Chart in a time-sensitive context.
*   **The Test:** Measure the time it takes for a user to sort the segments of the chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Simplify the data distribution to make the existing chart faster to read.
*   **Best Fix:** Implement a Circular Slice (area-based) design as described in the experimental setup of @kosara_impact_2019.

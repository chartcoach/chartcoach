---
id: avoid-angle-only-encodings
title: Avoid Angle-Only Encodings
bibliography: references.bib
description: Radial charts that rely solely on angle (without arc or area) significantly
  reduce accuracy.
labels:
- chart:pie
- visual:angle
- visual:orientation
- task:retrieve-value
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not use "angle-only" visualizations—such as two lines meeting at a vertex without a connecting arc or filled area—to represent quantitative proportions.

## The Logic <!-- role: reason -->
The human visual system struggles to estimate proportions based on angle alone when area and arc length are removed. In the systematic review by Zeng & Battle [@zeng_review_2023], they highlight findings from Skau & Kosara [@skau_arcs_2016] showing that "Angle Pie" and "Angle Donut" designs (essentially "V" shapes or floating line segments) performed significantly worse than standard pies, donuts, or even area-only charts. The rankings showed these angle-only designs consistently at the bottom for accuracy in retrieving values.

*   **The Principle:** Cue Summation (or lack thereof).
*   **The Evidence:** [@skau_arcs_2016], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately estimating the percentage of a slice.
*   **Data Type:** Part-to-whole quantitative data.
*   **Audience:** Any user needing to read data values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Geometry or Navigation tasks.
*   **Reason:** If the data represents actual physical angles (e.g., a compass heading or geometric proof), angle-only lines are appropriate because the task is reading degrees, not area proportions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Minimalist aesthetics. "Angle-only" charts are often used in high-design or minimalist contexts to reduce "ink."
*   **The Risk:** By adding the arc or fill, the chart becomes visually "heavier."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "clean" or "minimal" radial charts that consist only of the radius lines to separate sections, leaving the perimeter open.
*   **Why it fails:** This forces the user to rely solely on the angle difference between the lines, which is the least accurate method for judging radial data.

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart looks like a clock face with hands but no rim, or a pie chart with the outer circle removed.
*   **The Test:** Can you see the curve of the circle perimeter? If not, you are likely using an angle-only encoding.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Draw the perimeter line (the arc) connecting the radius lines.
*   **Best Fix:** Fill the segment with color to enable area perception, which supports arc length in accurate value retrieval.

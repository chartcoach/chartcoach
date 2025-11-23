---
id: use-points-for-means
title: Depict Means with Points, Not Bars
bibliography: references.bib
description: Bar graphs cause viewers to misinterpret the likelihood of data points
  due to visual containment bias.
labels:
- chart:bar
- chart:dot-plot
- task:summarize
- visual:shape
- impact:accuracy
- data:statistical
- audience:general
---

## The Rule <!-- role: advice -->
When visualizing means or averages of a distribution, use points (such as dot plots or box plots) instead of bar charts.

## The Logic <!-- role: reason -->
Bar charts create a cognitive distortion known as the "within-the-bar bias." Because the brain perceives the bar as a closed visual object, viewers incorrectly judge data points falling *inside* the bar as being more likely to belong to the distribution than points falling *outside* the bar, even when those points are equidistant from the mean [@newman_bar_2012]. This bias occurs because object perception principles (specifically closure) constrain attention and memory, making the bar seem like a "container" for the data.

## Where to Apply <!-- role: context -->
Apply this rule when communicating statistical information where the distribution of data around a central tendency is relevant.
*   **User Goal:** Reasoning about likelihood, probability, or variance around an average.
*   **Data Type:** Means with standard deviations or confidence intervals (e.g., test scores, temperature averages, safety ratings).
*   **Audience:** Both novice and expert audiences (the bias persists even among scientific readers).

## When to Break It <!-- role: exceptions -->
You should use bar charts when the data itself is inherently asymmetric or represents a concrete quantity rather than a statistical abstraction.
*   **Scenario:** Visualizing Counts or Absolute Quantities.
*   **Reason:** If the data represents a sum, a count, or a measure of extremity (magnitude from zero), the "fill" of the bar accurately represents the accumulation of value [@newman_bar_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high visual weight and immediate "impact" of a solid bar, which can be easier to spot from a distance.
*   **The Risk:** Lay audiences may be less familiar with dot plots or box plots, requiring slightly more cognitive effort to identify the category location initially.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding error bars to the bar chart.
*   **Why it fails:** Research shows that the "within-the-bar bias" persists equally strongly even when error bars are present; the solid bar dominates the interpretation [@newman_bar_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for a solid geometric shape connecting the data value to a zero-axis.
*   **The Test:** Ask, "Is it equally possible for a valid data point to exist 'below' the top edge of this shape as 'above' it?" If the answer is yes (e.g., a mean), but the graphic only fills the space below, the chart is biasing the user.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace the rectangular bar with a single data point (dot) located at the mean value.
*   **Best Fix:** Use a box plot, violin plot, or a point with bidirectional error bars to represent the distribution symmetrically.

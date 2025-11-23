---
id: avoid-bar-charts-for-inference
title: Avoid Bar Charts for Visualizing Mean and Error
bibliography: references.bib
description: Bar charts introduce 'within-the-bar' bias, causing viewers to misinterpret
  values inside the bar as more likely than those outside.
labels:
- chart:bar
- chart:error-bar
- task:inference
- visual:shape
- impact:accuracy
- audience:general
- bias:cognitive
---

## The Rule <!-- role: advice -->
Do not use bar charts with error bars to represent sample means and inferential uncertainty (such as confidence intervals). Instead, use glyphs that are symmetric around the mean, such as dot plots, violin plots, or gradient plots.

## The Logic <!-- role: reason -->
Bar charts suffer from "within-the-bar bias." Because a bar is a solid, continuous visual object that originates from a baseline, it creates a false metaphor of "containment."
*   **The Principle:** Within-the-Bar Bias.
*   **The Evidence:** Experiments show that viewers perceive values visually contained within the bar as significantly more likely than equidistant values outside the bar, even when the statistical likelihood is identical [@correll_error_2014]. This bias persists even when users are performing inferential tasks rather than simple magnitude comparisons.

## Where to Apply <!-- role: context -->
This advice applies to visualizations intended for statistical inference and comparison.
*   **User Goal:** Predicting outcomes, comparing group means, or assessing the likelihood of specific values.
*   **Data Type:** Sample means with associated uncertainty (Standard Error, Confidence Intervals).
*   **Audience:** General audiences and lay users who may rely on visual heuristics over statistical training.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparison of Ratios or Magnitudes from Zero.
*   **Reason:** If the task is strictly to compare the absolute magnitude or ratio of values (e.g., "A is twice as large as B") rather than the distribution or error, the bar chart's length encoding is superior for precision [@correll_error_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Familiarity. Bar charts are ubiquitous; alternative encodings like violin or gradient plots may initially confuse users unfamiliar with the format.
*   **The Risk:** Users may struggle to read the precise value of the mean if the center point is not clearly marked in the alternative encoding.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a bar chart but adding text labels for error.
*   **Why it fails:** Even if the error is stated, the visual weight of the bar dominates the user's probabilistic reasoning [@correll_error_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your chart have a solid bar extending from zero to the mean, topped with a whisker?
*   **The Test:** Ask a user, "Is a value slightly below the top of the bar more likely than a value slightly above the error bar?" If they strongly favor the "inside" value despite equal statistical distance, the chart is biasing them.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the bar chart to a dot plot with error bars (removing the bar fill).
*   **Best Fix:** Use a Gradient Plot (using transparency to show uncertainty) or a Violin Plot (using width) to ensure visual symmetry and avoid the containment metaphor [@correll_error_2014].

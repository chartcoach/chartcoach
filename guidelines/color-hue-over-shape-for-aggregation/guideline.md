---
id: color-hue-over-shape-for-aggregation
title: Prioritize Color Hue Over Shape for Scatterplot Averages
bibliography: references.bib
description: Use color hue instead of shape to distinguish classes in scatterplots
  when users need to compare means.
labels:
- chart:scatterplot
- task:aggregate
- task:compare
- visual:color
- visual:shape
- impact:accuracy
- data:categorical
---

## The Rule <!-- role: advice -->
Use color hue rather than shape marks to distinguish between categories in a multiclass scatterplot when the user needs to estimate or compare average values.

## The Logic <!-- role: reason -->
The human visual system aggregates information more efficiently when categories are defined by strong visual cues like color hue.
*   **The Principle:** Feature-based Attention. Stronger cues allow the visual system to "select" a set of points and extract statistics (like mean position) more effectively than weaker cues.
*   **The Evidence:** In a review of graphical perception, experiments showed that color hue encodings significantly outperformed shape encodings (and even shape encodings with color conflicts) for aggregate tasks in scatterplots [@zeng_review_2023]. Specifically, original experiments indicated that participants performed better with color (E-1) compared to shape (E-10, E-11) when judging which class had a higher average value [@gleicher_perception_2013].

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to identify the "center of mass" or average position of different groups within a scatterplot.
*   **Data Type:** Multiclass scatterplots (Quantitative X, Quantitative Y, Nominal Category).
*   **Audience:** General users performing visual analysis or summary tasks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data contains more categories than distinct color hues can support (e.g., >10 categories).
*   **Reason:** Color discriminability drops significantly with too many hues, making shape potentially necessary as a secondary channel, despite its lower aggregation efficiency.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use color for a fourth variable (e.g., a continuous heat map value).
*   **The Risk:** Color blindness issues must be managed by selecting an accessible palette, whereas shape is generally color-blind safe.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using different shapes (e.g., circles vs. triangles) to differentiate groups without color.
*   **Why it fails:** Shape is a "weaker" cue for the visual system's aggregation mechanism, leading to lower accuracy in estimating means [@gleicher_perception_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** The scatterplot uses only black outlines of different shapes (triangles, squares, circles) to denote groups.
*   **The Test:** Glance at the chart for 2 seconds. Can you instantly tell which group has a higher average Y-value? If not, the encoding is likely too weak.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Assign distinct colors (e.g., orange and purple) to the existing shape categories.
*   **Best Fix:** Standardize the mark shape (e.g., to filled circles) and use a categorical color palette to distinguish the groups.

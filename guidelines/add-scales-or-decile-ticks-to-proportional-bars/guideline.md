---
id: add-scales-or-decile-ticks-to-proportional-bars
title: Add Scales or Decile Ticks to Part-to-Whole Bar Charts
bibliography: references.bib
description: Simple bar charts fail at proportion estimation; adding scales or decile
  ticks significantly improves accuracy.
labels:
- chart:bar-chart
- visual:guides
- visual:ticks
- task:estimate-value
- impact:accuracy
- data:quantitative
- data:proportions
---

## The Rule <!-- role: advice -->
Never present a bar chart for part-to-whole comparisons in isolation. You must overlay decile ticks (every 10%) or provide a full quantitative scale.

## The Logic <!-- role: reason -->
A plain bar chart lacks internal reference points, making estimation of length difficult. Providing external visual anchors drastically reduces error. Experiments show a hierarchy of effectiveness where a full scale performs best, followed closely by decile ticks, both of which are significantly better than quartile ticks or no cues at all.
*   **The Principle:** Reference Framing
*   **The Evidence:** In the collation of graphical perception knowledge [@zeng_review_2023], results from Redmond [@redmond_visual_2019] show that bar charts with scales (E-6) and decile ticks (E-4) significantly outperformed baseline bars (E-1) and bars with only quartile ticks (E-3).

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate reading of percentage values from a bar visualization.
*   **Data Type:** Proportions or percentages (0-100%).
*   **Audience:** Dashboards and reports where accuracy is prioritized over minimalism.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When using Sparklines or micro-visualizations.
*   **Reason:** At very small sizes, decile ticks may cause visual clutter that obscures the data itself.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increased "chart junk" or ink density.
*   **The Risk:** The chart becomes visually heavier and requires more processing time than a clean bar, though the accuracy payoff is substantial.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding only quartile ticks (markers at 25%, 50%, 75%).
*   **Why it fails:** Evidence suggests quartile ticks on bars do not provide a statistically significant improvement over having no cues at all [@redmond_visual_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the bar chart look like a simple rectangle with no surrounding numbers or grid lines?
*   **The Test:** Can you precisely identify where 70% falls on the bar without guessing?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay vertical tick marks at every 10% interval inside the bar.
*   **Best Fix:** Place a standard quantitative axis (0-100) below or above the bar.

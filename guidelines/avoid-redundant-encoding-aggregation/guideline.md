---
id: avoid-redundant-encoding-aggregation
title: Avoid Redundant Encodings for Mean Estimation
bibliography: references.bib
description: Redundant encodings (color + shape) do not improve mean estimation in
  scatterplots.
labels:
- chart:scatterplot
- task:aggregate
- visual:redundancy
- impact:simplicity
- data:categorical
---

## The Rule <!-- role: advice -->
Do not add redundant visual encodings (such as combining shape and color for the same category) if your only goal is to improve the perception of average values in a scatterplot.

## The Logic <!-- role: reason -->
While common wisdom suggests redundancy aids discrimination, empirical studies on visual aggregation show it yields no significant performance benefit for estimating means. The visual system selects features serially; having two features pointing to the same set does not accelerate the "calculation" of the average position.
*   **The Principle:** Selective Attention. The visual system likely selects one feature to form an abstract map for aggregation; a second redundant feature does not enhance this specific process.
*   **The Evidence:** Analysis of experimental designs (E-1 vs E-5) found no significant difference in rank or accuracy when comparing a single color encoding against a redundant color-plus-shape encoding for aggregation tasks [@zeng_review_2023]. The original study explicitly states that combining cues redundantly does not improve performance [@gleicher_perception_2013].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly comparing the average positions of two or more groups.
*   **Data Type:** Multiclass scatterplots.
*   **Audience:** Situations where visual clutter needs to be minimized.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The chart must be accessible to color-blind users or printed in black and white.
*   **Reason:** Redundancy here is for *accessibility* and *legibility*, not for enhancing the cognitive task of aggregation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** By removing redundancy, you strictly rely on the user's ability to perceive the primary channel (usually color).
*   **The Risk:** Users with vision deficiencies may struggle if the primary channel is not accessible.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding unique shapes to colored dots thinking it will make the "trends" or "averages" pop out more.
*   **Why it fails:** It increases visual complexity (entropy) without statistically improving the accuracy of the specific task of comparing means [@gleicher_perception_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** A legend that says "Group A: Red Circle, Group B: Blue Square."
*   **The Test:** Ask if the shape conveys any *new* information. If not, and accessibility isn't the driver, it is unnecessary noise.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the shape variation and use circles for all data points.
*   **Best Fix:** Rely on a high-contrast, accessible color palette as the sole differentiator for categories.

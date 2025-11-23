---
id: stack-bar-charts-for-means-and-ranges
title: Vertically Stack Bar Charts to Compare Means and Ranges
bibliography: references.bib
description: When users need to identify the largest average or widest range between
  data sets, vertical stacking outperforms superposition or side-by-side layouts.
labels:
- chart:bar
- task:compare
- visual:position
- impact:precision
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When designing for the comparison of summary statistics (specifically the **Mean** or **Range**) between two sets of data, arrange the bar charts in a **vertical stack** (one above the other). Do not superimpose them or place them side-by-side.

## The Logic <!-- role: reason -->
Visual comparison does not rely on mathematical calculation but on "perceptual proxies"—simplified visual features that correlate with the data.
*   **The Principle:** **Global Visual Features.** For "set-level" tasks like estimating the average or range, viewers rely on global features such as the "ensemble length" (average length) or the centroid of the chart's area.
*   **The Evidence:** Experiments show that vertically stacked charts offer the highest precision for determining which set has the "Biggest Mean" or "Biggest Range." This arrangement allows viewers to "slice downward" to extract and compare these global shapes/lengths, whereas other arrangements (like superposition) clutter the global shape [@jardine_perceptual_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to determine which group has a higher average value or a wider spread (range) of values.
*   **Data Type:** Sets of quantitative values represented as bar charts (e.g., comparing test scores across two classrooms).
*   **Audience:** Users performing analytical comparisons where precision matters.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify **point-by-point differences** (e.g., "Which specific item changed the most?").
*   **Reason:** For item-level comparisons ("Biggest Delta"), previous research indicates that **superposed** (overlaid) or animated charts are superior because they minimize eye movements and highlight local differences, which are irrelevant for mean/range tasks [@jardine_perceptual_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical space. Stacked small multiples consume more vertical screen real estate than superposed charts.
*   **The Risk:** If the charts are too far apart, the "slicing" strategy may degrade, though standard small-multiple spacing is generally effective.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Superimposing (overlaying) the two bar charts to "save space" or "show everything at once."
*   **Why it fails:** Superposition encourages "focal" processing (looking at the difference between neighboring bars) rather than "global" processing. This destroys the perceptual proxy (the clear shape/hull of the dataset) needed to estimate the mean or range [@jardine_perceptual_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the bars of one series overlapping or sharing the exact same axis space as the bars of the other series?
*   **The Test:** Ask, "Can I clearly see the 'center of gravity' (centroid) of each individual distribution without visual interference from the other?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the charts to separate rows, aligning them to the same X-axis (Small Multiples).
*   **Best Fix:** Ensure the Y-axes are synchronized (shared scales) and place the charts immediately adjacent vertically to facilitate the "downward slicing" eye movement.

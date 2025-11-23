---
id: visualize-deltas-directly
title: Plot Differences Directly to Minimize Comparisons
bibliography: references.bib
description: Instead of asking viewers to mentally calculate differences between bars
  or lines, visualize the difference itself.
labels:
- chart:bar
- task:compare
- visual:position
- impact:speed
- data:relational
---

## The Rule <!-- role: advice -->

When the user's task is to compare values (e.g., "Is A larger than B?", "Which pair is decreasing?"), calculate and plot the difference (the delta) directly rather than plotting the raw values and asking the user to compare them.

## The Logic <!-- role: reason -->

While the visual system can extract summary statistics from groups quickly, specific pair-wise comparisons are serial operations—we can essentially only do one at a time. Performing dozens of comparisons (e.g., comparing every bar to its neighbor) takes seconds to minutes. Furthermore, visual illusions can distort the perceived difference between vertically offset curves [@zacks_designing_2020].

*   **The Principle:** Limitations of Serial Visual Comparison
*   **The Evidence:** Comparing one bar's length to another takes a split second; doing this for a whole dataset is slow and effortful. Turning the difference into a visual object makes the task immediate [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** Identifying changes, growth, decline, or ranking differences between two states (e.g., "Which category dropped the most?").
*   **Data Type:** Paired data sets (e.g., Before/After, Year 1/Year 2).
*   **Audience:** Decision-makers looking for "actionable" changes rather than raw totals.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When the absolute magnitude is more important than the relative change.
*   **Reason:** If the user needs to know the total capacity (e.g., "Do we have enough budget?") rather than the variance, plotting only the difference hides the necessary context.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You lose the context of the original raw values (e.g., a 5% drop looks the same whether the total is 100 or 1,000,000).
*   **The Risk:** Viewers may lose a sense of scale or proportion regarding the overall dataset.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Plotting two parallel lines or adjacent bars and expecting the user to accurately judge the changing gap between them.
*   **Why it fails:** Visual illusions (like the thickness of parallel curves) cause viewers to misjudge the vertical distance between lines, and comparing bar heights is a slow serial process [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Are you asking the user to look at "Bar A" and "Bar B" and mentally subtract one from the other?
*   **The Test:** Count how many unique pairwise comparisons are possible in your chart (e.g., 7 bars = 21 pairs). If the user needs to check many of these, the design is inefficient.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add explicit annotations labeling the difference (e.g., "+15%") between bars.
*   **Best Fix:** Create a new chart that plots the difference itself (e.g., a diverging bar chart showing growth/decline relative to a baseline) as the primary visual object.

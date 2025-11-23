---
id: group-bars-dont-stack
title: Group Bars Instead of Stacking Them
bibliography: references.bib
description: Stacked bars force inaccurate length judgments; grouped bars allow accurate
  position judgments.
labels:
- chart:bar
- chart:stacked-bar
- task:compare
- visual:length
- impact:clarity
---

## The Rule <!-- role: advice -->
Place bars side-by-side (grouped) rather than stacking them on top of each other when comparison of individual values is required.

## The Logic <!-- role: reason -->
Stacked bars force users to judge the *length* of the upper segments without a common baseline, whereas grouped bars allow users to judge *position* from a common baseline (usually zero).
*   **The Principle:** Perceptual Hierarchy (Position > Length).
*   **The Evidence:** Experiments by [@cleveland_graphical_1984], collated by [@zeng_review_2023], show that standard bar charts (E-1, position) significantly outperform stacked variations (E-4, E-5) where users must judge length or position without alignment. Specifically, Design E-1 (aligned) was significantly better than E-4 (top of stack) and E-5 (middle of stack).

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the values of specific sub-categories across different primary categories.
*   **Data Type:** Multidimensional quantitative data (e.g., Sales by Region by Year).
*   **Audience:** Users needing to compare the internal components of the totals.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary goal is to compare the *total* cumulative value of the stacks, and the sub-segments are of secondary interest.
*   **Reason:** Stacking provides a common baseline for the *total* height (position judgment), making the total easy to compare, even if internal segments become hard to read.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Grouped bars take up more horizontal space than stacked bars.
*   **The Risk:** If you stack bars, users will struggle to accurately compare the sizes of any segment that is not at the very bottom (which shares the zero baseline) [@cleveland_graphical_1984].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding gridlines behind a stacked bar to "help" read values.
*   **Why it fails:** The segments still do not start at the same point, requiring mental subtraction to determine the value (length), which is error-prone.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the bars sitting on top of other bars?
*   **The Test:** Pick a color segment in the middle of the stack. Try to compare its size to a segment of the same color in the next stack. Is it easy? (Likely not).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the most important category is at the bottom of the stack (where it is aligned to the axis).
*   **Best Fix:** Unstack the bars into a grouped bar chart or use a "small multiples" display (panel chart) to give each category its own common baseline.

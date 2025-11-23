---
id: format-axis-symbolically
title: Format Axis Values to Match Direction
bibliography: references.bib
description: Use negative signs and percentage symbols on axis labels to reinforce
  that values are below a record high.
labels:
- chart:line
- visual:formatting
- impact:clarity
- data:negative
- visual:axis
---

## The Rule <!-- role: advice -->
When displaying data that falls below a baseline (a "record high"), format the y-axis labels and tooltips as negative percentages (e.g., "-11%") rather than absolute positive numbers (e.g., "11").

## The Logic <!-- role: reason -->
Using absolute numbers (positive integers) to represent a gap below a peak is counter-intuitive and fails to communicate the concept of a "deficit" or "drop."
*   **The Principle:** Symbolic Consistency. Mathematical symbols (negative signs, percentage signs) act as cognitive cues that reinforce the directionality of the data.
*   **The Evidence:** Mintzer-Sweeney notes that to make it clear values have "never been higher," one should keep "repeating these concepts in symbolic terms, putting the whole y-axis and every tooltip value in terms of a negative percentage... instead of just plain 11" [@mintzer_y_axis_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Emphasizing that current values are a peak, and historical values were lower.
*   **Data Type:** "Distance from peak" or "drawdown" data.
*   **Audience:** Any audience, as this aligns mathematical notation with the visual representation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Magnitude comparisons where direction is irrelevant.
*   **Reason:** If you are only comparing the *size* of the gap regardless of direction (absolute deviation), negative signs might be distracting.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. It adds characters to every axis label.
*   **The Risk:** Small font sizes might make the negative sign hard to see, potentially leading to reading the value as positive.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Inverting the axis so "lower" looks "higher" without changing symbols.
*   **Why it fails:** This breaks standard chart conventions (up = more) and causes significant confusion.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the y-axis show positive numbers (5, 10, 15) but the lines are hanging below a zero line at the top?
*   **The Test:** Does the axis read like a countdown or a count-up? For "distance from peak," it should read as negative numbers approaching zero.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually edit axis ticks to include a "-" sign.
*   **Best Fix:** Adjust the underlying data to be actual negative values relative to the baseline so the charting tool generates the correct axis automatically.

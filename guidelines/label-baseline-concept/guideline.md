---
id: label-baseline-concept
title: Label the Zero Baseline Descriptively
bibliography: references.bib
description: Replace the numeric zero on a y-axis with a text label defining the benchmark
  to clarify abstract comparisons.
labels:
- chart:line
- visual:text
- impact:clarity
- task:compare
- data:index
- audience:general
---

## The Rule <!-- role: advice -->
When visualizing data relative to a benchmark (an index), replace the numeric "0" on the axis with a descriptive text label indicating what that baseline represents.

## The Logic <!-- role: reason -->
Abstract indices can confuse readers, particularly when the metric is easily confused with its inverse (e.g., employment rate vs. unemployment rate).
*   **The Principle:** Semantic Labeling. Explicitly naming the baseline anchors the reader's mental model to the specific variable being measured, preventing misinterpretation of the trend's direction.
*   **The Evidence:** Mintzer-Sweeney argues that to help readers distinguish concepts like employment and unemployment, one should "label the zero baseline in words, not just in numbers" (e.g., "Employment as of Q3 2023") [@mintzer_y_axis_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing historical data against a specific point in time (a record high, a specific year).
*   **Data Type:** Indexed time-series data where $y=0$ is a specific date or event.
*   **Audience:** Mainstream audiences who may not intuitively grasp indexed charts or "difference from baseline" calculations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standard absolute value charts.
*   **Reason:** If the y-axis represents a raw count starting at absolute zero (not a relative index), a text label might imply a benchmark that doesn't exist.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical axis space. A text label takes up more width or height than a simple "0".
*   **The Risk:** If the label is too long, it may overlap with data lines near the baseline.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on the chart title to explain the baseline.
*   **Why it fails:** Readers look at the axis to determine values; if the axis is ambiguous, they may misinterpret the lines before reading the title.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the y-axis end in a simple "0"?
*   **The Test:** Ask a viewer, "What does the straight line at the bottom represent?" If they have to look at the title to guess, the axis is under-labeled.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text annotation directly on top of the zero line.
*   **Best Fix:** Utilize custom axis tick labeling features to replace the value "0" with a string like "Employment as of [Date]."

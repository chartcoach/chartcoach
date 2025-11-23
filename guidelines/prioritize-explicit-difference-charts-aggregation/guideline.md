---
id: prioritize-explicit-difference-charts-aggregation
title: Use Explicit Difference Charts for Aggregation Tasks
bibliography: references.bib
description: Use explicit difference charts (diverging bars) instead of grouped bars
  when users need to aggregate changes or determine ranges.
labels:
- chart:difference-chart
- chart:bar
- task:aggregate
- task:determine-range
- visual:position
- impact:speed
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
If the user's primary task is to aggregate changes (e.g., estimate total growth/loss) or determine the range of differences, use an explicit Difference Chart (plotting only the delta) rather than Grouped Bar charts or Overlays.

## The Logic <!-- role: reason -->
Calculating an aggregate value from multiple grouped bars requires the user to perform mental arithmetic (subtraction then addition) for every category. An explicit difference chart pre-calculates the delta, turning the task into a simpler summation of visible bars.
*   **The Evidence:** Zeng et al. [@zeng_review_2023] highlight that in the study by Srinivasan et al. [@srinivasan_whats_2018], the Difference Chart (Design E-2) ranked 1st for `aggregate` tasks and performed significantly better than Grouped Bars (E-1) and Overlays (E-3) with a large effect size (Eta-squared > 0.5).

## Where to Apply <!-- role: context -->
*   **User Goal:** Summarizing overall performance or volatility (e.g., "What is the total variance?" or "What is the range of changes?").
*   **Data Type:** Quantitative comparison between two states (e.g., Budget vs. Actual).
*   **Audience:** Analysts or managers looking for the "net result" rather than absolute values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify specific absolute values (e.g., "Which month had the highest total sales?").
*   **Reason:** The Explicit Difference Chart (E-2) removes absolute values entirely. In `find-extremum` tasks, this design forces users to rely on interaction or secondary tables, making it ineffective for retrieving absolute magnitudes [@srinivasan_whats_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Context. You lose the visibility of the baseline values (the "source" and "target" magnitudes).
*   **The Risk:** A large percentage change might look identical to a small percentage change if the absolute scales differ significantly, potentially misleading the user about the significance of the delta relative to the total.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Single Bar with Difference Overlay" (Design E-4) to save space while hoping to support aggregation.
*   **Why it fails:** While better than standard bars, Design E-4 was statistically outperformed by the pure Difference Chart (E-2) in aggregation tasks [@srinivasan_whats_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you displaying two bars for every category?
*   **The Test:** Ask the user, "Roughly what is the total increase across all categories?" If they try to do math for each pair individually, the design is failing the aggregation task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a summary line or text annotation stating the total aggregate difference.
*   **Best Fix:** Switch the visualization to a Difference Chart (diverging bar chart) where the zero-line is central, and bars represent only the change [@srinivasan_whats_2018].

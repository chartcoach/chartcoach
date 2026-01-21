---
id: use-position-encodings-for-point-extrema-and-range-comparisons
title: Use Position Encodings for Point Extrema and Range Comparisons
bibliography: references.bib
description: Choose position-based time series displays when users must identify monthly
  maxima, minima, or ranges.
labels:
- chart:line
- chart:box
- task:locate
- task:compare
- task:rank
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- source:albers-2014
---

## The Rule <!-- role: advice -->

Use position-based encodings (e.g., line graphs or position-based summaries) when the task is to find which time block contains the highest/lowest point or the largest min–max range.

## The Logic <!-- role: reason -->

Position provides higher perceptual fidelity for extracting and comparing specific values than color-based encodings, which makes it more reliable for point-level judgments (like extrema) and paired point comparisons (like range).

- **The Principle:** High-fidelity value reading from spatial position supports point comparisons.
- **The Evidence:** In maxima, minima, and range tasks, position encodings generally outperformed color encodings in accuracy across the study’s comparisons [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which month contains the max, min, or largest range (max–min).
- **Data Type:** Time series segmented into discrete comparison blocks (e.g., months).
- **Audience:** General audiences performing forced-choice comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is summary comparison (e.g., comparing averages or spread) rather than locating specific points.
- **Reason:** The paper shows some summary tasks are better served by designs supporting visual/statistical aggregation rather than point extraction [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate support for some summary statistics (e.g., mean, spread) unless additional encodings are added.
- **The Risk:** If the display emphasizes raw variation without task-aligned summaries, viewers may struggle with summary tasks [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to a colorfield/heatmap for extrema tasks to “reduce clutter.”
- **Why it fails:** Color has lower fidelity for pinpointing exact highs/lows, reducing accuracy on point comparisons [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or scan broadly to find a single highest/lowest day.
- **The Test:** Ask a few users to answer “Which month had the highest day?”—if accuracy drops relative to other tasks, the encoding likely isn’t supporting point extraction [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the primary value encoding from color to vertical position for the series.
- **Best Fix:** Use a position-based design that also discretely emphasizes extrema per block if needed (e.g., add explicit min/max markers or range bars aligned to months) [@albersTaskdrivenEvaluationAggregation2014a].

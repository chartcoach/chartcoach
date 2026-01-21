---
id: use-colorfields-to-compare-average-over-time-windows
title: Use Colorfields to Compare Averages Over Time Windows
bibliography: references.bib
description: When users must find the time window with the highest average in dense
  time series, prefer a colorfield encoding over a line graph.
labels:
- chart:colorfield
- chart:line
- task:compare
- task:select
- visual:color
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- task:aggregate-judgment
- source:correll-chi-2012
---

## The Rule <!-- role: advice -->

Use a colorfield (value→color over time) instead of a line graph when the task is to choose which time window has the highest average.

## The Logic <!-- role: reason -->

Colorfields better support rapid summary judgments because the visual system can efficiently pool/average retinal features like color over regions, reducing the need for explicit mental computation of averages. In the authors’ study, participants were significantly more accurate with colorfields than with line graphs on a “pick the month with the highest average” task [@correllComparingAveragesTime2012a].

- **The Principle:** Perceptual averaging of color supports efficient aggregate judgments.
- **The Evidence:** Colorfields outperformed line graphs with a strong main effect of display type (ANOVA: F(1,1921)=143, p\<.0001) [@correllComparingAveragesTime2012a].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which segment/bin (e.g., month) has the maximum average value, not the maximum peak.
- **Data Type:** Dense 1D time series subdivided into known, discrete windows (e.g., 12 months × 30 days).
- **Audience:** General viewers without specialized statistical tools, needing fast “big picture” assessment [@correllComparingAveragesTime2012a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users need precise point values, slopes, or detailed local shape/trend interpretation.
- **Reason:** The paper motivates colorfields for aggregate judgments and notes line graphs’ established utility for identifying details; the color approach is chosen despite color being less precise than position for values [@correllComparingAveragesTime2012a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced precision for reading individual data points compared to position encodings.
- **The Risk:** Viewers may struggle to retrieve exact values if the task shifts from aggregate comparison to detailed lookup [@correllComparingAveragesTime2012a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a line graph for an average-over-window task and expecting users to “mentally average” the line’s heights.
- **Why it fails:** The paper argues shape/height in line graphs does not benefit from the same efficient perceptual averaging as color, leading to lower accuracy for this aggregate task [@correllComparingAveragesTime2012a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must trace the line and repeatedly estimate “area under the curve” for each window.
- **The Test:** Time-box a quick judgment (as in the study) and see whether accuracy drops sharply as windows become closer in average (small d) [@correllComparingAveragesTime2012a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a colorfield view alongside the line graph specifically for the average-comparison step.
- **Best Fix:** Replace the line graph with a colorfield for this task so window-level averages can be judged by perceived overall color [@correllComparingAveragesTime2012a].

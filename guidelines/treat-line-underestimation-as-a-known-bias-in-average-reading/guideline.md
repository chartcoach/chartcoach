---
id: treat-line-underestimation-as-a-known-bias-in-average-reading
title: Assume Line Averages Will Be Underestimated
bibliography: references.bib
description: Viewers tend to report average line positions lower than the true average
  after brief viewing.
labels:
- chart:line
- task:average
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:underestimation
---

## The Rule <!-- role: advice -->

When designing around average-level judgments, assume a line’s average height will be perceived/recalled as lower than it truly is.

## The Logic <!-- role: reason -->

Across experiments, average position reports for lines showed systematic negative error (underestimation) even when the line was uniform (not noisy), indicating a consistent directional bias rather than a strategy based on outliers.

- **The Principle:** Directional bias in remembered average position for lines
- **The Evidence:** Participants underestimated average line position in single-line conditions, and the effect persisted for uniform lines and in multi-series contexts [@xiongBiasedAveragePosition2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Reading/recalling a line’s typical level (mean) after a quick glance (e.g., dashboard scanning).
- **Data Type:** Single-series line charts or line series within multi-series charts.
- **Audience:** General audiences; the bias was observed in participant samples without specialized training.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users are not estimating an average from memory (e.g., they read a labeled value or a displayed mean).
- **Reason:** The paper’s evidence is about average estimates across a short delay, not explicit numeric read-offs.

## The Price <!-- role: costs -->

- **The Sacrifice:** Treating this as a design constraint may push you toward additional annotations or alternative encodings.
- **The Risk:** Over-correcting (adding too much scaffolding) could clutter the display.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trying to “fix” underestimation by smoothing the line or removing noise.
- **Why it fails:** Underestimation occurred for both noisy and uniform lines, so noise removal alone does not eliminate the bias [@xiongBiasedAveragePosition2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ indicated “average” line level lands below the actual average.
- **The Test:** Briefly show the line, then ask users to place a horizontal probe at the perceived average; compute signed error (estimate − true mean) [@xiongBiasedAveragePosition2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide the mean explicitly (e.g., a marked average reference) so users don’t rely on memory-based averaging (motivated by the presence of bias) [@xiongBiasedAveragePosition2020a].
- **Best Fix:** If average estimation is central, consider switching to bars or otherwise restructuring the view to reduce reliance on recalled average position [@xiongBiasedAveragePosition2020a].

---
id: avoid-overlaying-multiple-series-when-average-estimation-matters
title: Avoid Plotting Two Series Together When Average Estimation Matters
bibliography: references.bib
description: "When two series share a display, each series\u2019 perceived average\
  \ position is pulled toward the other."
labels:
- chart:line
- chart:bar
- task:average
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:perceptual-pull
---

## The Rule <!-- role: advice -->

Do not place two data series in the same plot if users must accurately estimate each series’ average position.

## The Logic <!-- role: reason -->

When two series appear together, estimates of each series’ average position shift toward the other series—an effect the paper calls “perceptual pull.” This can amplify or reduce existing biases (line underestimation, bar overestimation) depending on arrangement.

- **The Principle:** Perceptual pull (context-driven attraction between positional summaries)
- **The Evidence:** In two-series displays (line–line, bar–bar, and line–bar), average position estimates for the target series were pulled toward the non-target series, changing the error distribution relative to single-series controls [@xiongBiasedAveragePosition2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Accurately estimate the average level of each series (and/or compare the averages) after brief viewing.
- **Data Type:** Two quantitative series plotted in the same vertical frame (shared y-scale).
- **Audience:** Any audience; the effect was robust across tested series types.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is to emphasize convergence/relationship rather than precise average values, and small systematic shifts are acceptable.
- **Reason:** The rule targets precision of average estimates; if precision is not the goal, the cost of separating series may outweigh the benefit.

## The Price <!-- role: costs -->

- **The Sacrifice:** Using separate charts increases space and can make direct point-by-point comparison harder.
- **The Risk:** Small multiples may reduce immediate perception of interaction between series.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping two series in one chart and assuming viewers can “mentally isolate” them with attention.
- **Why it fails:** The paper shows the non-target series still biases the target’s perceived average via perceptual pull even when viewers are cued to the target [@xiongBiasedAveragePosition2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** In combined plots, reported averages “drift” toward the other series compared with the same series shown alone.
- **The Test:** A/B test single-series vs combined-series displays with the same target series and measure systematic shifts in average estimates [@xiongBiasedAveragePosition2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Split the display into two panels (one per series) when the task is average estimation [@xiongBiasedAveragePosition2020a].
- **Best Fix:** Use separate charts (small multiples) for average judgments, and reserve combined plots for tasks that benefit from co-location (the paper’s findings motivate avoiding co-location for average accuracy) [@xiongBiasedAveragePosition2020a].

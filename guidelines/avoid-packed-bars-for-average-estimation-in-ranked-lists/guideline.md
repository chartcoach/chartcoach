---
id: avoid-packed-bars-for-average-estimation-in-ranked-lists
title: Avoid packed bars for average estimation in ranked lists
bibliography: references.bib
description: Packed bars produce the worst accuracy for estimating the average value
  across a ranked list.
labels:
- chart:bar
- task:aggregate
- impact:accuracy
- data:quantitative
- audience:novice
- domain:ranked-list
- complexity:advanced
---

## Avoid packed bars for average estimation <!-- role: advice -->

Do not use packed bars when the task is to estimate the average across all items in a ranked list. Use an alternative ranked-list design for this summary judgment task.

## Why packed bars hurt average estimation accuracy <!-- role: reason -->

Estimating an average relies on visually integrating many values, which is sensitive to layout irregularity and perceptual grouping. Packed bars use a packing layout with varying baselines, which can make it harder to mentally combine values into a reliable overall average.

**Mechanism:** Irregular placement and non-uniform baselines interfere with forming a stable “center” impression across the full set of values.

**Evidence:** For the average (aggregate) accuracy ranking, packed bars were the worst-performing design, and reminders of significance pairs show it was significantly worse than scrolled bar charts, Zvinca plots, wrapped bars, piled bars, and treemaps [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance is specific to average estimation, not single-item ranking or two-item comparisons.

## When this applies <!-- role: context -->

- **User Goal:** Estimate the average value of the entire list.
- **Task:** Aggregate / mean estimation over all items.
- **Data:** Ranked list with many items and one quantitative value per item.
- **Chart Setting:** Any setting where packed bars are considered for space efficiency.
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Lower error in mean estimates.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** The task is not average estimation (e.g., you are not asking viewers to judge a global mean). **Why:** The evidence here only covers the mean/aggregate task outcome.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding packed bars may reduce space efficiency for showing all items at once. **Risk:** Switching away from packed bars can reintroduce scrolling or reduce the number of items visible simultaneously. **Mitigation:** Use alternative compact designs that performed better for mean estimation, and confirm performance with your intended tasks.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming “more items visible at once” automatically improves summary judgments like averages. **Why it fails:** Despite packing more bars into a space, packed bars performed worst for mean estimation accuracy.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ mean estimates vary widely or skew systematically high/low. **Quick Check:** Compare mean-estimation error using packed bars vs a scrolled bar chart for the same dataset. **Stronger Test:** Run a short task-based evaluation focused on mean estimation accuracy.

## What to do instead <!-- role: fix -->

- Replace packed bars with a scrolled bar chart when mean estimation accuracy matters.
- Replace packed bars with a Zvinca plot when you want a compact display and strong mean-estimation accuracy.
- Offer a separate “summary task” view instead of reusing the packed-bars view for everything.
- If you keep packed bars for other reasons, avoid using it as the default for tasks that require estimating an overall average.

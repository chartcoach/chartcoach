---
id: use-zvinca-or-scrolled-bars-for-ranked-list-average-estimation-accuracy
title: Use scrolled bar charts or Zvinca plots for average estimation in ranked lists
bibliography: references.bib
description: For estimating the overall average of a ranked list, scrolled bar charts
  and Zvinca plots are the most accurate among the tested designs.
labels:
- chart:bar
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- domain:ranked-list
---

## Use scrolled bar charts or Zvinca plots for average estimation <!-- role: advice -->

When viewers must estimate the average value across all items in a ranked list, use either a scrolled bar chart or a Zvinca plot. Prefer these over wrapped bars, piled bars, treemaps, and packed bars when accuracy is the priority.

## Why scrolled bars and Zvinca plots help average estimation <!-- role: reason -->

Average estimation is a summary judgment over many marks, so designs that support fast ensemble perception and reduce clutter can improve accuracy. In the measured results, the best-performing designs for this summary task were scrolled bar charts and Zvinca plots.

**Mechanism:** Clear baselines and/or minimal marks can support better ensemble judgments of central tendency across many items.

**Evidence:** For the average (aggregate) accuracy result, scrolled bar charts and Zvinca plots were grouped as the most accurate and both significantly outperformed wrapped bars, piled bars, treemaps, and packed bars in the reported significance pairs [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance does not claim these are always fastest; it is accuracy-focused.

## When this applies <!-- role: context -->

- **User Goal:** Estimate a single “typical” value across the entire ranked list.
- **Task:** Aggregate / average estimation over all items.
- **Data:** Many items, one quantitative value per item, already sorted as a ranked list.
- **Chart Setting:** Ranked-list visualization where the full list can be accessed (including via scrolling if needed).
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Lower error in average estimation.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Scrolling cost is unacceptable in your setting. **Why:** Scrolled bar charts were the slowest condition for the aggregate (mean) time result.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Scrolled bar charts can cost time due to navigation, and Zvinca plots may reduce familiarity compared to bars. **Risk:** If users cannot comfortably scan the entire list, they may estimate based on a subset. **Mitigation:** Make the full distribution easy to traverse (e.g., stable ordering and smooth navigation) and verify comprehension with a small pilot.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using packed bars for average estimation because they pack more items into view. **Why it fails:** Packed bars were the least accurate for the aggregate accuracy result.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ average estimates are consistently far from the true mean. **Quick Check:** Ask internal users to estimate the mean from your chart and compute absolute error; if high, test a Zvinca plot or a scrolled bar chart view. **Stronger Test:** A/B test mean-estimation accuracy across candidate ranked-list designs.

## What to do instead <!-- role: fix -->

- Use a scrolled bar chart for mean estimation when viewers benefit from familiar bar-length encoding.
- Use a Zvinca plot when you want a compact display that still supports accurate mean estimation.
- If you must use a compact bar variant, validate mean-estimation accuracy against these two baselines before shipping.
- Provide a task-specific “summary view” optimized for mean estimation rather than forcing the same ranked-list view for all tasks.

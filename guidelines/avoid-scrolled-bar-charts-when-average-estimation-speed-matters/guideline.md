---
id: avoid-scrolled-bar-charts-when-average-estimation-speed-matters
title: Avoid scrolled bar charts when average estimation speed is the priority
bibliography: references.bib
description: For estimating the average across a ranked list, scrolled bar charts
  are the slowest option among the tested designs.
labels:
- chart:bar
- task:aggregate
- impact:speed
- data:quantitative
- audience:novice
- domain:ranked-list
---

## Avoid scrolled bar charts when average estimation speed is the priority <!-- role: advice -->

When viewers need to estimate the average across a ranked list quickly, avoid scrolled bar charts. Prefer a faster design such as a Zvinca plot.

## Why scrolling slows down average estimation <!-- role: reason -->

Average estimation requires scanning across the full set of items. When the list is not fully visible and requires interaction to reveal more items, viewers spend time navigating rather than estimating.

**Mechanism:** Interaction and viewport changes add time and can disrupt the continuous visual integration needed for an overall average judgment.

**Evidence:** For the aggregate (mean) time result, the scrolled bar chart condition was ranked slowest, and multiple other designs (including Zvinca plots) were significantly faster in the reported significance pairs [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance is about speed; scrolled bar charts were among the most accurate for the same task.

## When this applies <!-- role: context -->

- **User Goal:** Produce a quick mean/average estimate across all items.
- **Task:** Aggregate / mean estimation.
- **Data:** Long ranked list with one quantitative value per item.
- **Chart Setting:** Any interface where full-list scanning requires scrolling interaction.
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Lower completion time.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Accuracy is more important than speed for mean estimation. **Why:** Scrolled bar charts were grouped among the most accurate designs for aggregate accuracy.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up some familiarity or certain bar-based affordances by switching away from scrolled bars. **Risk:** A faster design might change error patterns even if it saves time. **Mitigation:** Evaluate both time and accuracy for your expected list sizes before choosing the default.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a scrolled bar chart as the default ranked-list view for every task. **Why it fails:** For mean estimation, the scrolling interaction cost can dominate completion time.

## Quick tests <!-- role: check -->

**Failure Sign:** Mean-estimation tasks take noticeably longer than similar summary tasks in your UI. **Quick Check:** Time users estimating the average with and without scrolling requirements. **Stronger Test:** A/B test scrolled bars vs a Zvinca plot on mean-estimation completion time.

## What to do instead <!-- role: fix -->

- Use a Zvinca plot when mean estimation must be fast.
- Provide an overview-first view (non-scrolling) for mean estimation tasks, even if the detailed view is scrollable.
- Add task-specific shortcuts that reduce navigation time (e.g., jump controls) if scrolling cannot be removed.
- Offer a separate ranked-list visualization optimized for summary judgments rather than reusing the scroll-based view.

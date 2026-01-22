---
id: keep-timelines-synchronized-across-rows-to-support-comparison-of-uncertain-arrivals
title: Synchronize time axes across rows when comparing multiple uncertain arrival
  predictions
bibliography: references.bib
description: Enable across-item comparison by using a shared time scale rather than
  per-row rescaled timelines that change distribution appearance.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- platform:mobile
---

## Use a shared time scale across all rows <!-- role: advice -->

When showing multiple predicted arrivals as separate rows, keep all rows on the same time axis. Do not rescale each row’s axis to its own distribution range.

## Shared scales prevent misleading similarity across items <!-- role: reason -->

Per-row rescaling changes the apparent shape and height of distribution marks, making different uncertainty levels look comparable when they are not and making cross-row comparisons difficult.

**Mechanism:** A synchronized axis preserves positional meaning across items, so users can compare predicted arrival times and uncertainty extents directly between rows.

**Evidence:** Relative timelines (per-row ranges) were considered and rejected because they make it difficult to compare buses across rows; synchronized timelines were adopted to facilitate comparison between predicted buses [@kayWhenIshMy2016].

**Notes:** This is especially relevant when uncertainty encodings change height/shape with variance.

## Multi-item prediction lists in mobile transit contexts <!-- role: context -->

- **User Goal:** Choose among upcoming options (e.g., which bus to aim for, how risky it is to wait).
- **Task:** Compare predicted times and uncertainty across items.
- **Data:** Multiple predictive distributions for future arrival times.
- **Chart Setting:** List of rows, each with a distribution mark on a timeline.
- **Audience:** Everyday riders scanning multiple options.
- **Success Criterion:** Accurate relative judgments across items without scale confusion.

## When not to do this <!-- role: exceptions -->

**Break it when:** Items span extremely different time horizons such that a single shared scale makes most rows unreadably compressed. **Why:** The comparison benefit can be outweighed by illegibility.

## Tradeoffs of synchronized axes <!-- role: costs -->

**Sacrifice:** Some rows may look sparse or compressed if predictions are far apart in time. **Risk:** Very long shared horizons can reduce detail for near-term decisions. **Mitigation:** Limit the shared horizon to a decision-relevant window.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Auto-scaling each row to “fit” its distribution. **Why it fails:** It removes a stable positional reference and can make different variances appear similar.

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot tell which of two buses is more likely to arrive earlier when shown in different rows. **Quick Check:** Compare two rows with different uncertainty; if their marks look similarly “wide” despite different absolute time ranges, scaling is likely inconsistent. **Stronger Test:** Run a comparison task (choose the earlier/safer option) and measure error rates.

## What to do instead <!-- role: fix -->

- Use a single shared time window across all rows in the view.
- If you must change the window, change it for the entire view at once (not per row).
- If the horizon is too wide, split into separate views (e.g., “next 30 minutes” vs. later).

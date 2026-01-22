---
id: use-scrolled-bars-or-treemaps-to-improve-rank-task-speed
title: Avoid wrapped bars when single-item rank speed is the priority
bibliography: references.bib
description: For single-item rank tasks, wrapped bars are slower than several alternatives,
  so prefer faster designs when time dominates.
labels:
- chart:bar
- task:rank
- impact:speed
- data:quantitative
- audience:novice
- domain:ranked-list
---

## Avoid wrapped bars when single-item rank speed is the priority <!-- role: advice -->

When the main goal is to answer a single-item rank question quickly, avoid wrapped bars and prefer a faster ranked-list design such as treemaps, packed bars, piled bars, or Zvinca plots.

## Why wrapped bars can be slower for single-item rank tasks <!-- role: reason -->

Speed on rank lookup depends on how quickly viewers can locate the marked item and map it to a rank response. In the measured time results, wrapped bars did not deliver the fastest performance for the single-item rank task compared with several other layouts.

**Mechanism:** Reflowing into columns can increase the scanning and orientation work needed to locate the marked bar and interpret its position, which can increase completion time even if accuracy remains good.

**Evidence:** For the single-item ranking task time result (“sort-1”), treemaps, packed bars, piled bars, and Zvinca plots were grouped among the fastest conditions, while wrapped bars were grouped with scrolled bar charts as slower conditions [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about time, not accuracy.

## When this applies <!-- role: context -->

- **User Goal:** Get a quick rank lookup rather than a precise, error-minimized answer.
- **Task:** Sort / rank a single highlighted item.
- **Data:** Long ranked list with a single quantitative value per item.
- **Chart Setting:** Time-constrained setting (e.g., rapid review, repeated lookups).
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Lower completion time.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Accuracy is the dominant requirement for rank lookup. **Why:** Wrapped bars were the most accurate for the single-item rank accuracy result.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up some rank accuracy by prioritizing speed. **Risk:** Faster designs may lead to more mistakes in rank reporting, especially when values are visually similar. **Mitigation:** Validate accuracy on your expected list sizes and value distributions before committing.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating the fastest design as “best overall” for ranked lists. **Why it fails:** Time and accuracy diverged across designs in the reported results.

## Quick tests <!-- role: check -->

**Failure Sign:** Users take too long to answer “what rank is this item?” even when they are often correct. **Quick Check:** Time 10–20 rank lookups with your current chart and compare to a treemap/packed/piled/Zvinca prototype. **Stronger Test:** Run a small A/B test measuring completion time for single-item rank prompts.

## What to do instead <!-- role: fix -->

- Use treemaps, packed bars, piled bars, or Zvinca plots when rank lookup speed dominates.
- Offer a toggle between a speed-optimized view and an accuracy-optimized view (wrapped bars) depending on the task.
- If using scrolled bar charts, ensure the marked item is auto-scrolled into view to reduce navigation time.
- Reduce list size (filter, search, or paginate) to keep rank lookup fast regardless of layout.

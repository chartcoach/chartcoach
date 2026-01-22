---
id: prefer-wrapped-bars-for-single-item-rank-accuracy-in-ranked-lists
title: Prefer wrapped bars for single-item rank judgments in ranked lists
bibliography: references.bib
description: Wrapped bars yield the highest accuracy for judging the rank of a single
  item in a ranked list.
labels:
- chart:bar
- task:rank
- visual:length
- impact:accuracy
- data:quantitative
- audience:novice
- domain:ranked-list
---

## Prefer wrapped bars for single-item rank judgments <!-- role: advice -->

Use wrapped bars when viewers must identify the rank (position in the ordering) of a highlighted item within a long ranked list. Prefer wrapped bars over scrolled bar charts, treemaps, packed bars, piled bars, and Zvinca plots when accuracy is the priority.

## Why wrapped bars improve single-item rank accuracy <!-- role: reason -->

Single-item rank judgments benefit from layouts that preserve the ordered structure while keeping the full list visible without requiring navigation. Wrapped bars retain bar-length encoding while reflowing the list into multiple columns, supporting both rank-by-position cues and local length comparisons without scrolling.

**Mechanism:** Keeping the entire ranked list visible reduces search and memory burden, and a structured, columnar ordering supports rapid localization of the target item and its relative position.

**Evidence:** For the single-item ranking task (“sort-1”), wrapped bars were the most accurate and significantly outperformed treemaps, scrolled bar charts, packed bars, piled bars, and Zvinca plots in the reported pairwise significance results [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance is about accuracy, not speed.

## When to use wrapped bars for single-item rank judgments <!-- role: context -->

- **User Goal:** Find where a specific item sits in the overall ordering (e.g., “What rank is this item?”).
- **Task:** Sort / rank a single highlighted item.
- **Data:** A single quantitative value per item, many items in a list (long ranked list).
- **Chart Setting:** Ranked-list visualization where showing everything at once is feasible by reflowing into columns.
- **Audience:** General audiences or mixed experience.
- **Success Criterion:** Higher accuracy in rank identification.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** Completion time matters more than accuracy for this task. **Why:** Wrapped bars were not among the fastest conditions for the single-item rank task in the reported time ranking.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may not get the fastest completion times compared to other layouts. **Risk:** Users may need to compare across columns, which can add time even when accuracy is high. **Mitigation:** Treat wrapped bars as an accuracy-first choice and validate timing with a small task-based pilot if speed is critical.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing packed/piled/Zvinca variants for single-item rank judgments because they look more space-efficient. **Why it fails:** These variants were grouped among the least accurate designs for the single-item rank accuracy result.

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently misreport the item’s rank by a noticeable margin. **Quick Check:** Run a small internal test where people estimate the rank of a highlighted item; if errors cluster above what you consider acceptable, switch to wrapped bars. **Stronger Test:** A/B test wrapped bars vs your current ranked-list design on rank accuracy for the same list sizes.

## What to do instead <!-- role: fix -->

- Switch the ranked-list view to wrapped bars for tasks centered on “what rank is this item?”
- If you must keep a scrolled bar chart, add navigation support so the highlighted item is immediately brought into view.
- If your current design is treemap/packed/piled/Zvinca, provide a wrapped-bar alternative view specifically for rank lookup workflows.
- If you cannot reflow the layout, reduce the number of items shown (e.g., paginate or filter) so rank lookup stays reliable.

---
id: use-stacked-column-charts-to-compare-totals-and-one-key-part
title: Use stacked column charts only to compare totals and one key part
bibliography: references.bib
description: Stacked column charts are most effective when readers mainly need to
  compare overall totals and a single important segment across categories.
labels:
- chart:stacked-column
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Use stacked column charts only for totals plus one key segment <!-- role: advice -->

Use a stacked column chart only when the main comparisons are the overall totals and one especially important segment within those totals.

## Why stacked columns fit totals-and-one-segment comparisons <!-- role: reason -->

Stacked column charts preserve an easy baseline for the full height (the total) and for the bottom segment, but most other segments “float” and become hard to compare because they start at different heights.

**Mechanism:** Shared baselines make length comparisons easy; removing a shared baseline forces readers to estimate differences between misaligned segment endpoints.

**Evidence:** Comparing stacked segments that do not share a baseline is difficult, so stacked columns are a good fit only when the chart’s focus is the totals and a single segment that can be placed on a common baseline [@muth_stacked_columns_2018].

**Notes:** The key segment should be positioned where it benefits from a consistent baseline across columns.

## When your chart goal matches stacked columns <!-- role: context -->

- **User Goal:** Understand how totals differ across categories and how one key component contributes within each total.
- **Task:** Compare overall heights and compare one segment across columns.
- **Data:** Multiple categories (each a total) composed of parts that sum to that total.
- **Chart Setting:** Static or lightly interactive chart where quick scanning matters.
- **Audience:** General audiences who need fast, reliable comparisons.
- **Success Criterion:** Readers can accurately compare totals and the key segment without extensive legend lookups or calculation.

## When not to use stacked columns for this purpose <!-- role: exceptions -->

**Break it when:** The primary task is comparing several segments across categories (not just one). **Why:** Most segments won’t share a baseline, making cross-category segment comparisons unreliable [@muth_stacked_columns_2018].

## Tradeoffs of restricting stacked columns to this use case <!-- role: costs -->

**Sacrifice:** You may need to switch chart types to support multi-segment comparisons, which can take more space or require more layout work. **Risk:** Overusing stacked columns can hide meaningful differences among non-baselined segments. **Mitigation:** Be explicit about which segment is the “key” comparison and avoid implying precise comparison for the others.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Using stacked columns to invite readers to compare many segments across categories. **Why it fails:** Only the total and (typically) the bottom segment have a consistent baseline; other segments are hard to compare [@muth_stacked_columns_2018].

## Quick tests for whether stacked columns are the right tool <!-- role: check -->

**Failure Sign:** Readers must compare several mid-stack segments across columns to get the point. **Quick Check:** If you can’t name a single segment (plus the total) that carries the message, stacked columns are likely the wrong choice. **Stronger Test:** Ask a colleague to compare two non-bottom segments across two columns; if they hesitate or guess, the design is mismatched to the task [@muth_stacked_columns_2018].

## Better options when you need multi-segment comparisons <!-- role: fix -->

- Use split bars (one bar per segment) to give each segment a common baseline for comparison.
- Use small multiples so each segment can be compared on its own consistent scale.
- Switch to a table or a row-based display when category count is high and precise comparisons matter.
- If the total is not central, switch to a chart type that emphasizes the changing parts rather than stacked totals (for example, a line-based display of the key series).

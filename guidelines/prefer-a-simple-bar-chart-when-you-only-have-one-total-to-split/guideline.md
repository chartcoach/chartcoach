---
id: prefer-a-simple-bar-chart-when-you-only-have-one-total-to-split
title: Use a bar chart instead of stacked columns when splitting only one total
bibliography: references.bib
description: If you are only showing the parts of a single total, a bar chart is more
  space-efficient and easier to compare than a stacked column chart.
labels:
- chart:stacked-column
- task:part-to-whole
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Use a bar chart when you are splitting a single total into parts <!-- role: advice -->

If your data shows the parts of just one total, use a bar chart rather than a stacked column chart.

## Why stacked columns waste space for a single total <!-- role: reason -->

With only one total, a stacked column chart turns the composition into a single narrow column, leaving unused horizontal space and making it harder to compare segment sizes than a layout that directly allocates space to the parts.

**Mechanism:** Bar charts can devote more readable space to each part and support easier comparisons among parts than segments within a single stacked column.

**Evidence:** When showing parts of one total, bar charts use space better and make part-to-part comparison easier; if only one share of one total is the message, text may be sufficient [@muth_stacked_columns_2018].

**Notes:** This is about the “one total only” case; stacked columns can still be appropriate when you have multiple totals to compare.

## When this applies <!-- role: context -->

- **User Goal:** Understand composition within a single total.
- **Task:** Compare parts against each other within one group.
- **Data:** One group (one total) split into multiple parts.
- **Chart Setting:** Any medium where space efficiency and readability matter.
- **Audience:** General readers who need quick part comparison.
- **Success Criterion:** Parts are easy to compare without squinting at thin segments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You truly need to compare that one total against other totals in the same view. **Why:** The “single total” condition no longer holds, and stacked columns may be justified to compare totals plus composition [@muth_stacked_columns_2018].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You may lose the immediate “stacked-to-total” metaphor if you switch to separate bars. **Risk:** A bar chart can invite comparisons that aren’t your intent if ordering or labeling is unclear. **Mitigation:** Keep labeling explicit about what each bar represents.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Creating a stacked column chart with a single column to show one total’s parts. **Why it fails:** It wastes space and makes comparing the parts harder than necessary [@muth_stacked_columns_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The chart contains only one stacked column. **Quick Check:** If there is only one total, don’t stack it into a single column. **Stronger Test:** Ask whether the same message could be delivered as a sentence with one number; if yes, consider replacing the chart with text [@muth_stacked_columns_2018].

## What to do instead <!-- role: fix -->

- Use a bar chart to display each part with more readable space and clearer comparability.
- If the point is only one share of one total, write the value directly in text instead of charting it.
- Reduce or group minor parts (e.g., “Other”) before charting to keep the comparison focused.
- Add clear labels so readers can compare parts without relying on a legend.

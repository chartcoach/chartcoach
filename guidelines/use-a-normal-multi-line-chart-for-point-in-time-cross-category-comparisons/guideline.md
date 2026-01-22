---
id: use-a-normal-multi-line-chart-for-point-in-time-cross-category-comparisons
title: Use a normal multi-line chart to compare categories at the same point in time
bibliography: references.bib
description: Prefer a single shared plot when readers must judge which line is higher
  or lower at a specific date.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- complexity:beginner
---

## Use a normal multi-line chart to compare categories at the same point in time <!-- role: advice -->

Use a normal multi-line chart when readers need to compare categories against each other at specific dates. Keep the lines in one shared coordinate system so “higher vs. lower in year X” judgments are direct.

## A shared coordinate system enables direct vertical comparison <!-- role: reason -->

Point-in-time comparisons require a common quantitative frame: when all lines share the same axes, their vertical positions at a given x-value can be compared immediately. Splitting lines into separate panels removes this shared reference and forces memory-based or back-and-forth scanning, which undermines quick, accurate comparisons.

**Mechanism:** Shared axes turn cross-category comparison into a simple position judgment rather than a multi-step scan across panels.

**Evidence:** Small multiple line charts make it difficult to answer questions like which category was higher in a given year, while a normal line chart makes this comparison easy because the lines share one plot [@muth_small_multiple_line_charts_2024].

**Notes:** This guidance holds even if small multiples look cleaner; cleanliness alone does not guarantee the chart supports the intended comparison task.

## When cross-category comparison at time t is the main task <!-- role: context -->

- **User Goal:** Decide which category is higher/lower at a given date or compare gaps between categories over time.
- **Task:** Ranking at a specific time, estimating differences between categories, identifying overtakes.
- **Data:** Multiple temporal series where absolute comparability matters.
- **Chart Setting:** Space allows multiple lines with clear labeling; overlap is manageable or can be managed by filtering.
- **Audience:** Readers who benefit from quick ranking without scanning multiple panels.
- **Success Criterion:** Readers can correctly answer “which is highest in year X?” quickly.

## When to break this rule <!-- role: exceptions -->

**Break it when:** Lines overlap so much that readers can’t trace individual series even with careful design. **Why:** The shared plot becomes visually overwhelming and undermines comprehension of any one trend [@muth_small_multiple_line_charts_2024].

## Tradeoffs of keeping all lines together <!-- role: costs -->

**Sacrifice:** With many categories, readability can degrade due to overlap and the need for a legend or many labels. **Risk:** Over-plotting can hide important series behavior and discourage exploration. **Mitigation:** Consider showing fewer categories or switching to small multiples when trend readability is the priority [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Choosing small multiples while the written question is a point-in-time comparison. **Why it fails:** The chart type makes the intended judgment unnecessarily hard [@muth_small_multiple_line_charts_2024].
- **Mistake:** Adding too many lines to a normal line chart until it becomes a knot. **Why it fails:** Readers can no longer parse or compare reliably [@muth_small_multiple_line_charts_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers must scan across many panels to decide which category is higher in a specific year. **Quick Check:** If your headline or caption contains “higher/lower in YEAR,” a normal multi-line chart is likely the better default. **Stronger Test:** Give a reader the chart and ask “Which is higher in YEAR?”; if the answer is slow or wrong in small multiples, switch to a shared plot [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Use small multiple line charts when overlap makes the combined chart unreadable and the task is trend-per-category.
- Reduce the number of categories shown at once to keep overlap manageable.
- If you need both tasks, provide a combined chart for comparison and small multiples for per-category trend reading [@muth_small_multiple_line_charts_2024].
- If you must keep small multiples, repeat all series as faint background lines in each panel to reintroduce some comparability [@muth_small_multiple_line_charts_2024].

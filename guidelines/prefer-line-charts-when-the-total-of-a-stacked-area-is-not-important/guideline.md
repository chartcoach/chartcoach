---
id: prefer-line-charts-when-the-total-of-a-stacked-area-is-not-important
title: Use a line chart instead of an area chart when the total stack height is not
  important
bibliography: references.bib
description: If the overall total is not a key message, switch from stacked areas
  to lines for easier reading.
labels:
- chart:area
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:foundational
---

## Switch from stacked areas to lines when the total is not the point <!-- role: advice -->

Use a line chart instead of a stacked area chart when you do not need readers to interpret the overall total height.

## Stacked area structure adds a total cue that can distract <!-- role: reason -->

A stacked area chart visually emphasizes the combined height, which invites readers to interpret the sum even when it is irrelevant, increasing cognitive load compared with reading lines.

**Mechanism:** Lines isolate each series on a common baseline, while stacked areas embed most series on moving baselines that are harder to compare and that foreground the total silhouette.

**Evidence:** Area charts are recommended when the total is as important as the shares; if the total is not important, a line chart is recommended as easier for many readers to understand [@muth_area_charts_2018].

**Notes:** An exception is when values sum to exactly 100% at each time point, where an area chart can still be an intuitive “shares” display [@muth_area_charts_2018].

## When this switch applies <!-- role: context -->

- **User Goal:** See how multiple series change over time without emphasizing their sum.
- **Task:** Compare trends across series on a consistent baseline.
- **Data:** Time series with multiple components where the sum is not meaningful or not intended as a message.
- **Chart Setting:** Explanatory reporting where fast comprehension matters more than part-to-whole framing.
- **Audience:** Broad audiences who may misread stacked baselines.
- **Success Criterion:** Readers can correctly compare trend directions and relative levels across series.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Each time point represents a complete composition (adds to 100%). **Why:** A stacked area can be the most intuitively readable option for shares-over-time even if the total is fixed [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the immediate part-to-whole cue that stacked areas provide. **Risk:** With many lines, the chart can become visually busy and require stronger labeling. **Mitigation:** Limit the number of displayed series or group minor series before switching [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping a stacked area chart while writing text that only discusses individual series trends. **Why it fails:** The form highlights totals and moving baselines, which conflicts with the intended reading task [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The narrative never mentions the total, yet the chart visually shouts a total. **Quick Check:** Ask “Would the story change if the total were hidden?” If not, prefer lines. **Stronger Test:** Hide all but two series; if comparison becomes much clearer with lines, the stacked area was doing unnecessary work [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Replace the stacked area chart with a multi-line chart when comparing series trends is the primary goal [@muth_area_charts_2018].
- Show only the most relevant series instead of all shares if the point is a specific comparison [@muth_area_charts_2018].
- Group small categories into an “others” series before switching to reduce clutter [@muth_area_charts_2018].

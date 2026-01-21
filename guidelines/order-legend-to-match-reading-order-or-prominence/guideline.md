---
id: order-legend-to-match-reading-order-or-prominence
title: Sort Color-Key Items to Match the Chart
bibliography: references.bib
description: "Order legend items to reflect the chart\u2019s visual order, prominence,\
  \ or natural category order so readers don\u2019t hunt."
labels:
- chart:multiple
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Sort categorical color-key items to match the chart: follow the chart’s left-to-right/top-to-bottom order when elements are similarly sized; otherwise order by visual prominence (biggest share first); always preserve any natural order in the categories.

## The Logic <!-- role: reason -->

A mismatched order forces extra search. Aligning legend order with how readers encounter colors in the chart reduces scanning time and confusion. Muth recommends matching chart order, switching to “biggest first” when sizes differ, and deferring to natural category order when it exists [@muth_color_keys_2023].

- **The Principle:** Reduce search by aligning legend and visual sequence
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly mapping a seen color to its meaning
- **Data Type:** Categorical legends for charts where colors appear in a consistent spatial order or with strongly varying sizes (e.g., pies, bubble charts, categorical maps)
- **Audience:** General readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Categories have a well-known inherent order (e.g., left–center–right; good–ok–bad; chronological categories)
- **Reason:** Reordering to match appearance or size can conflict with semantic expectations; Muth advises keeping natural order in those cases [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose an “alphabetical” lookup convenience.
- **The Risk:** If the chart’s order is ambiguous (colors scattered), “match the chart” may be unclear and inconsistent [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Ordering legend items arbitrarily (or alphabetically) when the chart has an obvious reading order or dominance pattern
- **Why it fails:** Readers must hunt through the legend even though the chart itself provides a natural sequence [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** You can see a prominent color immediately in the chart but can’t find it quickly in the legend.
- **The Test:** Identify the first color you notice in the chart; if it isn’t near the beginning of the legend, ordering is likely wrong [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder legend items to mirror the chart’s spatial sequence.
- **Best Fix:** Choose the ordering rule explicitly: natural order > match reading order for equal-sized marks > descending prominence for unequal-sized marks, and apply it consistently [@muth_color_keys_2023].

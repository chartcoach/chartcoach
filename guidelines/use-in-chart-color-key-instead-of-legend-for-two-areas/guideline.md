---
id: use-in-chart-color-key-instead-of-legend-for-two-areas
title: Label the Two Areas with an In-Chart Color Key
bibliography: references.bib
description: Use on-chart text to explain what each colored area represents and highlight
  the contrast, instead of relying on a separate legend.
labels:
- chart:area
- task:identify
- visual:color
- impact:clarity
- data:temporal
- audience:general
- complexity:basic
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Use text annotations as a direct color key on the chart to explain what the two colored areas represent and emphasize the difference between them.

## The Logic <!-- role: reason -->

An in-chart key removes lookup effort (chart → legend → chart) and makes the meaning of each region immediately legible, supporting the “let that simplicity shine through” goal described in [@mintzer_simple_data_2024].

- **The Principle:** Reduce visual decoding steps by labeling in place
- **The Evidence:** [@mintzer_simple_data_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Instantly distinguish two quantities (e.g., solved vs. unsolved) and perceive their gap
- **Data Type:** Two-part/fill-based displays where regions are the story (stacked/filled areas with two categories)
- **Audience:** Skimmers and non-expert readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart contains many categories or too many segments to label cleanly.
- **Reason:** In-chart labeling would become cluttered and less readable than a legend [@mintzer_simple_data_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less room for the data display (labels take space).
- **The Risk:** Poor placement can overlap data or reduce contrast if labels sit on similar colors.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a detached legend while also adding lots of explanatory prose.
- **Why it fails:** The reader still must decode colors indirectly; extra prose doesn’t substitute for clear in-place mapping [@mintzer_simple_data_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** You need to search for a legend to know what each area means.
- **The Test:** Cover the legend (or imagine it removed). Can a reader still correctly name each colored area?

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add two short labels directly on/near each area (“Recorded thefts”, “Solved cases”).
- **Best Fix:** Position labels to both define the areas and underscore the imbalance (e.g., place the “Only 4–5% solved” note near the solved region) as modeled in [@mintzer_simple_data_2024].

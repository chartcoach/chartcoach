---
id: validate-categorical-color-hue-discriminability-for-colored-lines
title: Validate Categorical Color Hue Discriminability for Colored Lines
bibliography: references.bib
description: Ensure line colors remain distinguishable at the minimum line thickness
  when using color hue to separate series.
labels:
- chart:line
- task:cluster
- visual:color
- visual:position
- impact:clarity
- data:temporal
- data:categorical
- audience:general
- source:szafir2018
---

## The Rule <!-- role: advice -->

When encoding different series with color hue on line marks, validate that hues are distinguishable at the thinnest line stroke you will render.

## The Logic <!-- role: reason -->

- **The Principle:** Perceived color difference depends on mark geometry; line thickness influences how well viewers can discriminate colored line marks.
- **The Evidence:** This paper is collated as graphical perception evidence relevant to color-hue use for cluster-like separation across mark types [@zengReviewCollationGraphical2023]. Szafir measures color-difference perception for line marks and models how discriminability varies with line thickness in line-graph stimuli [@szafirModelingColorDifference2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster—visually separate multiple series/lines by color.
- **Data Type:** Ordinal/ordered x (e.g., time or sequence) with quantitative y, plus nominal series encoded with color hue (line chart design).
- **Audience:** General audiences on standard displays.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Lines are not differentiated by hue (e.g., only one line, or labeling/other encodings do all the separation work).
- **Reason:** The rule is only needed when hue-based discrimination between lines is required.

## The Price <!-- role: costs -->

- **The Sacrifice:** May require thicker strokes or fewer series to keep colors separable.
- **The Risk:** Thicker lines can increase overplotting/occlusion; reducing series can omit information.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing colors based on how they look in a legend or in thick sample strokes only.
- **Why it fails:** Line color discriminability depends on the stroke thickness actually used in the plot; thin strokes can reduce separability for some color choices [@szafirModelingColorDifference2018], motivating the need for mark-aware guidance as emphasized in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Two series that should be distinct look like the same colored line when strokes are thin or the chart is scaled down.
- **The Test:** Set stroke width to the minimum used in your responsive/embedded layout and verify you can still distinguish the nominal series by hue.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the minimum line thickness.
- **Best Fix:** Re-select or re-space the hues to remain distinguishable at the minimum stroke thickness, guided by mark-specific color-difference considerations from [@szafirModelingColorDifference2018] as assembled for recommendation use in [@zengReviewCollationGraphical2023].

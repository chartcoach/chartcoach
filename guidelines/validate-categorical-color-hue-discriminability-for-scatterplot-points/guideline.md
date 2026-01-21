---
id: validate-categorical-color-hue-discriminability-for-scatterplot-points
title: Validate Categorical Color Hue Discriminability for Scatterplot Points
bibliography: references.bib
description: Check that categorical colors remain distinguishable when used on point
  marks in scatterplots, accounting for mark size effects.
labels:
- chart:scatter
- task:cluster
- visual:color
- visual:position
- impact:clarity
- data:quantitative
- data:categorical
- audience:general
- source:szafir2018
---

## The Rule <!-- role: advice -->

When using color hue on scatterplot point marks, validate that your chosen colors are distinguishable at the smallest point size you will display.

## The Logic <!-- role: reason -->

- **The Principle:** Color discriminability depends on mark geometry (size/shape), so colors that are distinct in theory or on large patches may not be distinct on small plotted points.
- **The Evidence:** The collation of graphical perception findings highlights this study as evidence about color-hue perception in point marks used for clustering-style judgments [@zengReviewCollationGraphical2023]. Szafir measures color-difference perception for point marks in scatterplot-like stimuli and models how discriminability changes with mark size [@szafirModelingColorDifference2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster—distinguish groups/classes in a scatterplot using color.
- **Data Type:** Two quantitative fields mapped to x/y position, plus one nominal field mapped to color hue (scatterplot design).
- **Audience:** General audiences using typical (not necessarily calibrated) displays.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not relying on color hue to separate clusters (e.g., color is purely decorative or redundant).
- **Reason:** The rule is about ensuring the color channel supports cluster judgments; if clustering does not depend on color, the discriminability requirement is not relevant.

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra design/testing time (you must check the palette at the smallest rendered size).
- **The Risk:** If you tune colors for very small points, the palette may feel overly separated or less aesthetically subtle at larger sizes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a palette that looks distinct in a legend or in large swatches will stay distinct on tiny scatterplot points.
- **Why it fails:** Color difference perception changes with mark size and the visualization context; the same color pair can become harder to tell apart on small marks [@szafirModelingColorDifference2018], a concern surfaced in the collation for recommendation/design rules [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Neighboring categories (by hue) start to visually “merge” into the same-looking points, especially when points are small/dense.
- **The Test:** Temporarily set the point size to the minimum you expect and verify you can still reliably distinguish the nominal categories by hue.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase point size to improve discriminability of the existing color choices.
- **Best Fix:** Re-select or re-space the hues so they are distinguishable at the minimum point size you will display, informed by mark-specific color-difference considerations from [@szafirModelingColorDifference2018] as cataloged in [@zengReviewCollationGraphical2023].

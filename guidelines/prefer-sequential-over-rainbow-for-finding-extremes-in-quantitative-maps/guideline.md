---
id: prefer-sequential-over-rainbow-for-finding-extremes-in-quantitative-maps
title: Use Sequential Color Saturation (Not Rainbow Hue) to Find Extremes
bibliography: references.bib
description: For finding minima/maxima on quantitative maps, sequential (saturation-based)
  schemes outperform rainbow (hue-based) schemes in accuracy and time.
labels:
- chart:map
- task:find-extremum
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- color-scheme:sequential
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a sequential, saturation-based color scheme (SC) instead of a rainbow, hue-based scheme (RC) when the user must find minima or maxima on a quantitative map.

## The Logic <!-- role: reason -->

Sequential schemes provide a more consistently ordered perceptual cue for magnitude than rainbow hues, leading to better performance on extremum-finding.

- **The Principle:** Ordered perceptual cue supports extremum search
- **The Evidence:** In choropleth and isarithmic map conditions, SC designs (E-3, E-4) ranked above RC designs (E-2, E-1) for **find-extremum** in both **accuracy** and **time**, with significant differences reported [@golbiowskaRainbowDashIntuitiveness2022]. This guideline is recorded as part of a broader collation for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify the highest or lowest values on a map (find-extremum)
- **Data Type:** Quantitative values encoded into ordered classes (ordinal scale in the color encoding)
- **Audience:** General audiences performing map reading tasks

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is *not* finding extremes (e.g., a different task like filter or determine-range).
- **Reason:** This rule is only supported here for the **find-extremum** task; the extracted evidence does not claim the same ordering for other tasks [@golbiowskaRainbowDashIntuitiveness2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less categorical distinctiveness between adjacent classes than a strongly hue-varying rainbow.
- **The Risk:** If classes are too similar, users may feel the map is “monotone,” even if it supports extremum finding better.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a rainbow palette but “reordering” hues to imply magnitude.
- **Why it fails:** The evidence here supports switching to a sequential (saturation-based) encoding for better extremum performance, not merely reshuffling rainbow hues [@golbiowskaRainbowDashIntuitiveness2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or frequently misidentify the max/min colored region.
- **The Test:** Run a quick timed “find the maximum / minimum” check with a few users; compare error rate and time between RC and SC variants (mirroring the reported metrics) [@golbiowskaRainbowDashIntuitiveness2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the rainbow hue palette with a sequential palette mapped to ordered classes (color saturation on an ordinal scale).
- **Best Fix:** Keep the same map type and classing, but standardize on sequential saturation-based encoding for all extremum-finding views in your recommender or template library, as captured in the collation dataset [@zengReviewCollationGraphical2023; @golbiowskaRainbowDashIntuitiveness2022].

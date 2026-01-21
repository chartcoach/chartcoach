---
id: use-small-multiples-with-independent-y-axes-to-compare-shapes-not-magnitudes
title: Use Independent Y-Axes Only to Compare Trend Shapes
bibliography: references.bib
description: Use per-panel y-scales in small multiples to reveal similar-shaped trends
  when magnitudes differ widely.
labels:
- chart:line
- task:compare
- visual:scale
- impact:insight
- data:temporal
- audience:general
- chart:small-multiples
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use independent y-axis scales in small multiple line charts only when you want readers to compare the shapes of trends across categories with vastly different magnitudes.

## The Logic <!-- role: reason -->

Different y-scales can give each line similar visual height, making upward/downward patterns visible even when absolute values differ so much that some trends disappear in a shared-scale chart [@muth_small_multiple_line_charts_2024].

- **The Principle:** Normalize visual range to reveal hidden patterns
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Notice direction and volatility (how quickly/much a series rises or falls) rather than compare absolute values
- **Data Type:** Multiple time series with large differences in magnitude
- **Audience:** General readers who would otherwise miss smaller-amplitude but meaningful changes

## When to Break It <!-- role: exceptions -->

- **Scenario:** Readers need to compare absolute levels between categories.
- **Reason:** Independent scales can mislead by making unequal magnitudes look equally large [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loses direct magnitude comparability between panels.
- **The Risk:** Readers may assume a shared scale and draw false conclusions if scale differences aren’t noticed [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using independent y-axes without clearly signaling that scales differ.
- **Why it fails:** Readers may overlook per-panel axes and misinterpret relative sizes of change [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Panels look like they show equally large swings, but y-axis labels differ across panels.
- **The Test:** Remove attention from the axes: if the chart could be misread as shared-scale at a glance, the scale differences are not obvious enough [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear note in the chart description warning that y-axis scalings differ.
- **Best Fix:** Avoid independent scales when possible; if used, make the difference obvious (e.g., explicit description and visual cues like atypical gridlines) [@muth_small_multiple_line_charts_2024].

---
id: stack-horizontal-bar-charts-vertically-for-precise-range-width-comparisons
title: Stack Bar-Chart Small Multiples Vertically for Range Comparisons
bibliography: references.bib
description: "For comparing which group has the wider range (min\u2013max), use vertically\
  \ stacked horizontal bar-chart small multiples rather than adjacent, mirrored, or\
  \ superposed arrangements."
labels:
- chart:bar
- task:determine-range
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- comparison:set-to-set
---

## The Rule <!-- role: advice -->

When you need to judge which of two groups has the **wider range** (min–max spread) using horizontal bar charts, place the two charts in a **vertically stacked** small-multiples layout.

## The Logic <!-- role: reason -->

Stacked layouts support more precise range-width comparisons than adjacent, mirrored, or superposed arrangements (lower JND threshold in the reported ranking). This guideline comes from the structured collation in [@zengReviewCollationGraphical2023] and is grounded in the MAXRANGE-style experimental evidence in [@jardinePerceptualProxiesVisual2020].

- **The Principle:** Arrangement changes perceptual precision for set-to-set comparisons of spread.
- **The Evidence:** [@jardinePerceptualProxiesVisual2020], as collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which set has a wider min–max range (determine-range).
- **Data Type:** Two groups of quantitative values shown as horizontal bars (small multiples).
- **Audience:** General audiences doing quick, perceptual comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking viewers to compare ranges, but to perform a different comparison task (e.g., a task where overlap or another arrangement is needed).
- **Reason:** The evidence here is task-specific; the same arrangement may not be best for other comparison tasks, as emphasized in [@jardinePerceptualProxiesVisual2020] and summarized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses more vertical space than adjacent layouts.
- **The Risk:** If space forces smaller charts, bars may become too small to read comfortably (despite stacked being the better arrangement among those tested).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Superposing the two groups in a single bar chart (e.g., differentiating the groups by another encoding).
- **Why it fails:** The reported arrangement ranking places superposed last for range comparisons relative to stacked, mirrored, and adjacent [@jardinePerceptualProxiesVisual2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers frequently confuse which group has the larger spread.
- **The Test:** Show the same data in stacked vs. your current arrangement and ask a few users to pick the wider-range group; if stacked yields more consistent answers, your arrangement is likely reducing precision (consistent with [@jardinePerceptualProxiesVisual2020] as collated in [@zengReviewCollationGraphical2023]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-layout the two panels into a vertical stack.
- **Best Fix:** Keep stacked panels aligned and simultaneously visible (no toggling), matching the higher-precision arrangement identified in [@jardinePerceptualProxiesVisual2020] and captured as guidance in [@zengReviewCollationGraphical2023].

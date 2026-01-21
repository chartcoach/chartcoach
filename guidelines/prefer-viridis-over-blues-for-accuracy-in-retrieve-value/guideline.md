---
id: prefer-viridis-over-blues-for-accuracy-in-retrieve-value
title: Prefer Viridis Over Blues for Accuracy in Retrieve-Value Tasks
bibliography: references.bib
description: For retrieve-value judgments using quantitative colormaps, viridis yields
  higher accuracy than blues.
labels:
- chart:color-scale
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- colormap:multi-hue
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use viridis instead of blues when accuracy matters for retrieve-value judgments using quantitative color.

## The Logic <!-- role: reason -->

- **The Principle:** Multi-hue sequential colormaps can provide better discriminability for relative distance judgments than single-hue ramps in this task setting.
- **The Evidence:** The collated experimental results show viridis (E-5) ranked above blues (E-2) for retrieve-value accuracy, with a significant pairwise difference (E-5 > E-2) reported in [@liuSomewhereRainbowEmpirical2018] and collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly choose which of two colored values is closer to a reference value (retrieve-value).
- **Data Type:** Quantitative values encoded by a continuous sequential colormap.
- **Audience:** General users where correctness is more important than speed.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dominant KPI is speed and minor accuracy loss is acceptable.
- **Reason:** The same study shows blues can be faster than viridis in timing rank order in at least one retrieve-value comparison set [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not get the fastest response times compared to blues.
- **The Risk:** If your evaluation only measures time, you might miss the accuracy benefit.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating all “sequential” colormaps as equivalent.
- **Why it fails:** The experiment reports meaningful differences in accuracy rankings between specific palettes (viridis vs blues vs jet) for the same task [@liuSomewhereRainbowEmpirical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently misjudge which option is closer when colors are similar.
- **The Test:** Run a small forced-choice triplet task (reference + two options) with your palette and compare error rate against viridis as a baseline [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap your sequential palette from blues to viridis.
- **Best Fix:** Make palette choice task-aware: default to viridis for retrieve-value accuracy, and only use alternative palettes when you have evidence they meet your metric goals [@zengReviewCollationGraphical2023; @liuSomewhereRainbowEmpirical2018].

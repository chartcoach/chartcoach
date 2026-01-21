---
id: avoid-truncating-y-axis-when-you-want-neutral-effect-size-judgments
title: Avoid Truncating the Y-Axis When You Need Neutral Effect-Size Judgments
bibliography: references.bib
description: Truncating a y-axis increases perceived effect severity; use a zero baseline
  when you want to avoid visually inflating the effect.
labels:
- chart:bar
- chart:line
- task:compare
- task:judge-effect-size
- visual:position
- visual:length
- impact:truthfulness
- impact:trust
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Avoid truncating the y-axis (i.e., do not start it above 0) when your goal is to keep viewers’ perceived effect size from being inflated.

## The Logic <!-- role: reason -->

Truncating the y-axis visually magnifies differences, which increases subjective judgments of how “severe” or “important” the differences look.

- **The Principle:** Visual magnification increases perceived severity of differences.
- **The Evidence:** In crowd-sourced experiments, higher y-axis start points (greater truncation) produced higher perceived severity, and this persisted across bar and line charts [@correllTruncatingYAxisThreat2020]. This finding is captured as design-relevant knowledge in the perception-collation dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging how big an effect is (subjective severity), without exaggeration.
- **Data Type:** Quantitative values plotted across ordinal positions (e.g., categories or ordered points).
- **Audience:** General audiences (including viewers who may not closely read axes).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want to increase the perceived severity of differences.
- **Reason:** Truncation predictably increases perceived severity, so it can be used deliberately to make differences feel larger [@correllTruncatingYAxisThreat2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Small differences may become visually harder to notice when you keep the y-axis untruncated.
- **The Risk:** Viewers may under-react to meaningful but small changes because the chart’s visual slope/height differences are less visually prominent.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Truncate the y-axis and assume that viewers will “correct” their perception by reading the labels.
- **Why it fails:** The subjective inflation persists even when viewers can accurately report values and even with truncation cues in the design [@correllTruncatingYAxisThreat2020], as summarized in the collation effort [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The plotted differences look dramatically larger after raising the axis minimum, even though the underlying values changed only slightly.
- **The Test:** Re-render the same chart with a 0 baseline and compare whether the “severity” impression changes substantially; if it does, truncation is likely driving the impression [@correllTruncatingYAxisThreat2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reset the y-axis minimum to 0.
- **Best Fix:** If you must preserve detail while avoiding inflated impressions, provide an additional non-truncated view alongside the truncated view so viewers can see both the detailed variation and the full context (the key issue is that truncation changes perceived severity) [@correllTruncatingYAxisThreat2020; @zengReviewCollationGraphical2023].

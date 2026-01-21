---
id: do-not-assume-line-charts-are-immune-to-y-axis-truncation-inflation
title: Do Not Assume Line Charts Are Immune to Y-Axis Truncation Inflation
bibliography: references.bib
description: Y-axis truncation increases perceived effect severity in line charts
  similarly to bar charts.
labels:
- chart:line
- chart:bar
- task:judge-effect-size
- visual:position
- visual:length
- impact:truthfulness
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Treat y-axis truncation as a perceived-severity inflation risk in line charts, not just in bar charts.

## The Logic <!-- role: reason -->

Changing the y-axis start point increases perceived severity, and this effect did not differ significantly between bar and line charts in the reported experiments.

- **The Principle:** Perceived effect size responds to the displayed value range (visual magnification) across chart types.
- **The Evidence:** No significant difference was found between bar vs. line charts in how truncation increased perceived severity; truncation level was the driver [@correllTruncatingYAxisThreat2020]. This cross-chart implication is part of the structured perception knowledge collated for recommendation use cases [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Making qualitative judgments of “how big” a change is.
- **Data Type:** Quantitative y-values over ordinal x positions (including short sequences like 2–3 points).
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not eliciting subjective severity judgments (i.e., perceived importance) and instead only care about another objective that tolerates or benefits from magnification.
- **Reason:** The evidence here is specifically about perceived severity inflation, not about every possible analytic task outcome [@correllTruncatingYAxisThreat2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** If you keep a 0 baseline in line charts, subtle changes may appear visually smaller.
- **The Risk:** Important small changes may be less visually salient.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switch a truncated bar chart to a truncated line chart and assume the perceived-exaggeration problem is solved.
- **Why it fails:** The experiments found truncation-driven perceived-severity increases in both chart types, with no significant difference between them [@correllTruncatingYAxisThreat2020], consistent with the collation framing [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The line appears much steeper after raising the y-axis minimum, and viewers describe the change as more “extreme.”
- **The Test:** Render the line chart with different y-axis start points (e.g., 0 vs. truncated) and see whether the impression of severity changes markedly; if it does, truncation is driving interpretation [@correllTruncatingYAxisThreat2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a 0 baseline if preventing inflated severity impressions is important.
- **Best Fix:** If truncation is needed to show variation, pair the truncated view with a full-range (non-truncated) context view to reduce over-reliance on the magnified slope impression [@correllTruncatingYAxisThreat2020; @zengReviewCollationGraphical2023].

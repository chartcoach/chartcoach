---
id: do-not-expect-broken-axis-or-gradient-to-debias-truncated-bar-charts
title: Do Not Rely on Broken-Axis or Gradient Cues to De-Bias Truncated Bar Charts
bibliography: references.bib
description: Broken-axis and gradient bar designs do not reliably reduce the perceived-severity
  inflation caused by truncating the y-axis.
labels:
- chart:bar
- task:judge-effect-size
- visual:length
- impact:truthfulness
- impact:trust
- data:quantitative
- audience:general
- custom:axis-truncation-cue
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If you truncate a bar chart’s y-axis, do not assume that adding a broken-axis treatment or a gradient “continuation” will prevent viewers from perceiving the effect as larger.

## The Logic <!-- role: reason -->

Even when truncation is visually indicated, viewers’ subjective severity judgments still track the visual magnification created by the truncated scale.

- **The Principle:** Explicit cues about truncation do not reliably override visual magnification in subjective judgments.
- **The Evidence:** Bar charts with truncation cues (broken-axis bars/axes; gradient continuation) showed no consistent reduction in perceived severity compared to standard truncated bars; perceived severity still increased with greater truncation [@correllTruncatingYAxisThreat2020]. This is represented as actionable knowledge in the collation work for visualization recommendation contexts [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting how large/severe differences are (qualitative effect-size judgment).
- **Data Type:** Quantitative values shown as bar lengths over ordinal x positions.
- **Audience:** General audiences, including those who may notice the cue but still be influenced by the magnified visual differences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your only goal is to signal that truncation occurred (regardless of whether severity impressions change).
- **Reason:** The cue may communicate truncation presence, but the evidence here addresses perceived-severity bias rather than cue comprehension [@correllTruncatingYAxisThreat2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual complexity (broken marks/axis glyphs or gradients) without achieving the intended de-biasing benefit.
- **The Risk:** Designers may gain false confidence that the chart is “safe” because truncation is indicated, even though perceived severity remains inflated.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add a broken-axis symbol (or break the bars) and conclude the chart is no longer misleading.
- **Why it fails:** Perceived severity did not significantly differ across these designs once truncation was present; truncation level still drove severity judgments [@correllTruncatingYAxisThreat2020], as surfaced in the graphical perception collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** With a truncated y-axis, viewers (or stakeholders) still describe differences as “dramatic” even when a break/gradient is obvious.
- **The Test:** Compare perceived-severity ratings (e.g., internal quick user check) across (1) truncated bar, (2) truncated+broken-axis cue, (3) truncated+gradient cue; if impressions remain similar, the cue is not mitigating the bias (consistent with reported findings) [@correllTruncatingYAxisThreat2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove truncation (return to a 0 baseline) rather than adding more truncation cues.
- **Best Fix:** If truncation is required for analytic reasons, provide an accompanying non-truncated context view so the audience can anchor judgments to the full scale, instead of relying on cue-only interventions [@correllTruncatingYAxisThreat2020; @zengReviewCollationGraphical2023].

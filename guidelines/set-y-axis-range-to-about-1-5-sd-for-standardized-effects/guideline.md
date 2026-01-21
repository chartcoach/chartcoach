---
id: set-y-axis-range-to-about-1-5-sd-for-standardized-effects
title: Set the Y-Axis Range to About 1.5 SD for Standardized Effects
bibliography: references.bib
description: "Use a y-axis span of roughly 1\u20132 standard deviations (aim ~1.5\
  \ SD) to improve readers\u2019 sensitivity to effect size and reduce bias."
labels:
- chart:bar
- chart:line
- task:judge-effect-size
- visual:scale
- impact:clarity
- impact:calibration
- data:continuous
- audience:novice
- domain:standardized-effects
- source:wittGraphConstruction2019
---

## The Rule <!-- role: advice -->

When communicating standardized effect sizes (SD-based), center the y-axis on the grand mean and use an overall y-axis range of about 1.5 SD (roughly 1–2 SD).

## The Logic <!-- role: reason -->

A y-axis that is too narrow makes effects look visually large; a y-axis that is too wide makes effects look visually small. A mid-range tied to SD improves visual–conceptual compatibility, so readers’ judgments track the true effect magnitude more closely (higher sensitivity) and with less systematic over/underestimation (lower bias) [@wittGraphConstruction2019].

- **The Principle:** Visual–conceptual size compatibility
- **The Evidence:** Across five experiments, SD-based standardized ranges yielded higher sensitivity and lower bias than “full range” (0–100) or “minimal range” axes [@wittGraphConstruction2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging whether an effect is small/medium/large (magnitude calibration), not merely seeing direction.
- **Data Type:** Outcomes where effect sizes are interpreted via SD units (e.g., Cohen’s d conventions).
- **Audience:** Non-expert or mixed audiences who rely on the visual impression to estimate effect size [@wittGraphConstruction2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** SD is unknown or not relevant to interpreting effect size.
- **Reason:** The SD-based scaling logic does not apply; the guideline is specifically for SD-standardized interpretation [@wittGraphConstruction2019].
- **Scenario:** The needed SD-based range would force nonsensical axis values (e.g., negative performance scores) or would exclude required information (e.g., error bars).
- **Reason:** The axis must remain meaningful and must contain the displayed uncertainty and data elements [@wittGraphConstruction2019].
- **Scenario:** You must enforce an identical scale across multiple figures for cross-figure comparability.
- **Reason:** Consistency across graphs can outweigh per-graph SD centering; you may need a shared scale [@wittGraphConstruction2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less space to show the full possible outcome range (e.g., 0–100), which can reduce “context of the scale.”
- **The Risk:** If effects are unusually large, a fixed ~1.5 SD window may need to be expanded, otherwise data/uncertainty may be cramped or clipped [@wittGraphConstruction2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always using the minimal y-axis range just beyond the data.
- **Why it fails:** It biases readers toward judging effects as bigger than they are [@wittGraphConstruction2019].
- **The Wrong Fix:** Always forcing the axis to show the full possible range (e.g., 0–100).
- **Why it fails:** It biases readers toward judging effects as smaller than they are [@wittGraphConstruction2019].
- **The Wrong Fix:** Picking an SD-based range but not centering on the grand mean.
- **Why it fails:** The goal is aligning the visual size around the data’s central tendency; off-centering undermines the intended compatibility [@wittGraphConstruction2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Effects that should be “big” look tiny (overly tall range) or effects that should be “small” look dramatic (overly short range).
- **The Test:** Compute the plotted y-span in SD units; if it is far below ~1 SD total or far above ~2 SD total for a standardized-effects context, expect miscalibration and bias [@wittGraphConstruction2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recalculate y-limits as (grand mean ± 0.75 SD) to create a ~1.5 SD total range [@wittGraphConstruction2019].
- **Best Fix:** Standardize axis-setting as a rule in your figure pipeline: center on the grand mean and target a 1–2 SD total range (aim ~1.5 SD), expanding only as needed to include uncertainty displays and avoid nonsensical values [@wittGraphConstruction2019].

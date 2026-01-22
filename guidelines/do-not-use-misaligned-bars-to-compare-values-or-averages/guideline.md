---
id: do-not-use-misaligned-bars-to-compare-values-or-averages
title: Do not use misaligned bars (stack-like parts) for comparing values or averages
bibliography: references.bib
description: Misaligned bars remove shared positional baselines, pushing viewers toward
  less precise extent-based judgments.
labels:
- chart:bar
- task:compare
- visual:extent
- impact:accuracy
- data:categorical
- audience:general
- layout:misaligned
---

## Avoid misaligned bar segments for magnitude comparisons <!-- role: advice -->

Do not use misaligned bars (bar segments with varying baselines, as in stacked-bar parts) when the task requires comparing magnitudes across items or groups. Use an encoding that keeps values aligned to a shared baseline or represented as positions.

## Why misalignment forces less precise extraction <!-- role: reason -->

When bar baselines differ, viewers cannot reliably compare bar-top positions across items and instead must compare lengths (extent), which is a less precise visual channel for magnitude discrimination. For multi-value comparisons, this extends to average judgments where viewers may rely on summed extents, which becomes unreliable when group sizes differ.

**Mechanism:** Misalignment disables direct position comparison and increases reliance on extent-based proxies (length/area) that are noisier for fine discrimination.

**Evidence:** In single-value comparisons, misaligned bars produced much worse discrimination thresholds than normal aligned bars and dot plots, indicating reduced precision when only extent is available [@yuanPerceptualProxiesExtracting2019]. In multi-value average comparisons, normal bars performed no better than misaligned bars, consistent with viewers defaulting to extent-based proxies even when aligned position is available [@yuanPerceptualProxiesExtracting2019].

**Notes:** This applies to situations where the viewer must compare the magnitude of parts across categories, not to cases where the goal is solely within-stack composition.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Compare magnitudes across categories or between groups.
- **Task:** Identify which value (or group mean) is larger.
- **Data:** Categorical groups with quantitative values; possibly multiple observations per group.
- **Chart Setting:** Stacked bars where a component is compared across bars, waterfall-like bars, or any bar display with variable baselines.
- **Audience:** General readers who will default to fast perceptual comparisons.
- **Success Criterion:** Accurate comparisons at small differences (high precision).

## When not to follow it <!-- role: exceptions -->

**Break it when:** The only intended comparison is within a single stacked bar (part-to-whole within one category) and cross-category magnitude comparisons are explicitly not required. **Why:** The misalignment cost is primarily about cross-item comparisons that need a common positional reference.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding misaligned segments can reduce compactness when showing part-to-whole structure across many categories.\
**Risk:** Re-encoding parts separately can make it harder to perceive total composition in a single glance.\
**Mitigation:** Preserve composition via annotations or separate totals while keeping comparable quantities aligned.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Asking viewers to compare a specific stacked segment across categories by eye. **Why it fails:** The segment lacks a shared baseline, pushing viewers into less precise length comparisons [@yuanPerceptualProxiesExtracting2019].
- **Mistake:** Assuming that because a bar chart “uses position,” viewers will use bar tops for multi-value summaries. **Why it fails:** For average comparisons across many bars, viewers often behave as if only extent is being used [@yuanPerceptualProxiesExtracting2019].

## Quick tests before you ship <!-- role: check -->

**Failure Sign:** People disagree on which segment/value is larger when differences are small, especially across different baseline offsets.\
**Quick Check:** Remove the baseline offsets (align bars) and see whether the intended comparison becomes immediately clearer.\
**Stronger Test:** Measure accuracy on forced-choice comparisons between two items using the current design versus an aligned-position alternative.

## What to do instead <!-- role: fix -->

- Re-encode comparable quantities with a shared baseline (aligned bars) or as points on a common axis.
- Provide a separate dot plot (or position-based marks) specifically for cross-category comparisons of the component.
- If a stacked form must remain, add explicit numeric labels for the compared component values.
- Split the display: one view for composition within categories and a second view for cross-category magnitude comparisons.

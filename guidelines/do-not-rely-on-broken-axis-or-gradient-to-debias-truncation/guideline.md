---
id: do-not-rely-on-broken-axis-or-gradient-to-debias-truncation
title: Do not rely on broken-axis or gradient-bar designs to remove truncation-driven
  severity inflation
bibliography: references.bib
description: Visual cues for axis truncation do not reliably reduce the subjective
  exaggeration caused by truncating the y-axis.
labels:
- chart:bar
- task:compare
- visual:length
- impact:trust
- data:ordered
- audience:general
- topic:axis-break
---

## Avoid assuming truncation cues will neutralize exaggeration <!-- role: advice -->

Do not assume that adding a broken-axis treatment or a gradient “continuation” on bars will make truncated y-axes perception-neutral. If you truncate the y-axis, expect perceived severity to remain inflated.

## Salient truncation indicators do not cancel the visual magnification <!-- role: reason -->

Even when truncation is visually indicated, the plot still compresses the y-range and magnifies visible differences in bar heights. Viewers’ severity judgments track that magnification more than the presence of a warning cue.

**Mechanism:** Truncation cues may increase awareness of truncation, but they do not change the underlying magnification created by a reduced y-range.

**Evidence:** Bar-chart variants that visually indicated truncation (broken axis/broken bars, and gradient continuation) showed no consistent reduction in perceived severity compared to standard truncated bars; perceived severity still increased with greater truncation [@correllTruncatingYAxisThreat2020]. This outcome is part of the collated evidence base intended for visualization recommendation rules and constraints [@zengReviewCollationGraphical2023].

**Notes:** The observed effect concerns qualitative severity judgments, not only numeric decoding accuracy.

## Where truncation-indicator designs are being considered <!-- role: context -->

- **User Goal:** Understand how large or important a difference or change is.
- **Task:** Judge trend magnitude or compare first vs last values in bar charts.
- **Data:** Ordered categories with quantitative values; scenarios where y-axis truncation is being used to enlarge visible differences.
- **Chart Setting:** Static bar charts where designers consider axis-break glyphs or gradient fills to signal truncation.
- **Audience:** Broad audiences, including those who may notice truncation but still be influenced by visual magnification.
- **Success Criterion:** Reduce bias in subjective judgments of effect size.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your sole goal is to signal that truncation exists, not to change how severe the change feels. **Why:** The evidence here is about debiasing perceived severity, not about awareness or disclosure.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up a familiar “fix” that appears to address honesty concerns. **Risk:** Adding these cues can increase visual complexity without achieving the intended reduction in subjective exaggeration. **Mitigation:** Validate the design against the specific judgment you care about (severity) rather than assuming disclosure implies neutrality.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding a broken-axis mark and treating the chart as “unbiased.” **Why it fails:** Perceived severity still rises with truncation even with broken-axis cues.
- **Mistake:** Using gradient “continuation” to imply the missing baseline makes comparisons fair. **Why it fails:** The subjective exaggeration remains driven by the truncated range.

## Quick tests <!-- role: check -->

**Failure Sign:** Despite truncation cues, viewers still rate differences as much larger when the y-axis start is higher. **Quick Check:** Compare severity ratings (internal review or quick survey) for the same data with and without truncation cues at the same truncation level. **Stronger Test:** A/B test perceived severity across (a) full-range bars and (b) truncated bars with truncation cues.

## What to do instead <!-- role: fix -->

- Use a non-truncated y-axis when unbiased subjective severity judgments are required.
- Provide an additional context view with a broader y-range alongside any focused view, so viewers can judge magnitude under both scales.
- Make the numeric change explicit in text near the graphic (e.g., state the change from first to last), so severity can be grounded in values.
- Reconsider whether the task should be framed as judging severity visually, or whether the workflow should ask for numeric comparisons directly.

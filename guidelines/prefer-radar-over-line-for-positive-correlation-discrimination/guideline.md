---
id: prefer-radar-over-line-for-positive-correlation-discrimination
title: Prefer radar over unsorted line charts for positive-correlation discrimination
  (if choosing within that family)
bibliography: references.bib
description: In the tested task, radar charts yielded better JND performance than
  standard line charts for positive correlations.
labels:
- chart:radar
- task:compare
- visual:angle
- impact:accuracy
- data:quantitative
- audience:practitioner
- direction:positive-correlation
---

## Choose radar over an unsorted line chart when comparing positive correlation and you must use a connected-path chart <!-- role: advice -->

If you must use a connected-path chart to support discrimination of positive correlation strength, prefer a radar chart over a standard unsorted line chart in the tested setting.

## Why a coordinate transform can improve discrimination in some line families <!-- role: reason -->

Coordinate transforms can change which features stand out during correlation judgment. In the study, the radar transform produced lower JNDs than the unsorted line chart for positive correlations, indicating that the radar representation offered more discriminable cues for correlation strength in that condition.

**Mechanism:** A transform that accentuates consistent shape differences across correlation levels can reduce the threshold for detecting changes in correlation.

**Evidence:** For positive correlations, radar charts performed significantly better than standard line charts in JND-based discrimination [@harrisonRankingVisualizationsCorrelation2014a]. The study also shows that coordinate transforms have mixed effects across families (for example, donut vs stacked bar did not differ for negative correlations), so benefits are conditional [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The radar-negative condition was excluded due to unreliable JNDs, so the supported conclusion is for radar-positive.

## When radar-over-line applies <!-- role: context -->

- **User Goal:** Compare positive correlation strength using a connected-path visualization.
- **Task:** Decide which of two displays is more positively correlated.
- **Data:** Two quantitative variables displayed as two series over a shared index/order.
- **Chart Setting:** Static panels where a radar chart is an acceptable form factor.
- **Audience:** Mixed expertise; relies on perceptual discriminability.
- **Success Criterion:** Lower JND than the unsorted line chart for the target r range.

## When not to use radar for this purpose <!-- role: exceptions -->

**Break it when:** You need to judge negative correlations with a radar chart in this style. **Why:** The radar-negative condition was unreliable in the study’s JND procedure.

## Tradeoffs of preferring radar here <!-- role: costs -->

**Sacrifice:** The benefit is established for a specific task and sign; it may not generalize to other tasks. **Risk:** A radar chart can still yield high JND compared to top-performing forms (for example, scatterplots) even if it beats an unsorted line chart. **Mitigation:** Use radar only when constrained to that family; otherwise pick a better-ranked form.

## Common mistakes with radar vs line choices <!-- role: mistakes -->

- **Mistake:** Assuming radar is always better than line because it won here. **Why it fails:** The paper shows coordinate transforms can have inconsistent impacts across chart families and signs.
- **Mistake:** Using radar for negative-correlation discrimination without validation. **Why it fails:** Negative radar performance was unreliable in the tested procedure.

## Quick checks for using radar in this role <!-- role: check -->

**Failure Sign:** Radar shapes look similarly spiky/noisy across different correlation levels, leading to disagreement in judgments. **Quick Check:** Compare predicted JND for radar-positive vs line-positive at your target r values. **Stronger Test:** Run a small forced-choice study comparing the two under your styling and data.

## What to do instead if radar is not acceptable <!-- role: fix -->

- Use an ordered line chart (sorted by X) for correlation discrimination when ordering is permissible.
- Switch to a scatterplot for the correlation comparison tasks.
- Use the Weber-model ranking from the paper to select a better-performing alternative for your sign and r range.
- Reduce the required discrimination precision by communicating coarse bins of correlation strength.

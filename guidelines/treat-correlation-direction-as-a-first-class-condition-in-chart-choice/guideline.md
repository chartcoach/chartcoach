---
id: treat-correlation-direction-as-a-first-class-condition-in-chart-choice
title: Choose correlation-judgment charts separately for positive and negative correlation
bibliography: references.bib
description: Correlation-judgment effectiveness can differ by correlation direction,
  so chart selection should be conditioned on sign.
labels:
- chart:multiple
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- correlation:signed
- complexity:advanced
---

## Condition chart choice on correlation sign for correlation-judgment tasks <!-- role: advice -->

When selecting a chart for correlation judgment, treat positive and negative correlations as different cases and choose the chart separately for each sign.

## Why correlation direction changes perceptual performance <!-- role: reason -->

Some chart forms produce different visual structures for positive versus negative correlations, which can change how precisely viewers can discriminate correlation differences.

**Mechanism:** If the visual pattern for negative correlation is not simply a mirrored version of the positive pattern, the perceptual cues used for correlation discrimination can change with sign, altering JND and therefore effectiveness.

**Evidence:** The extracted results for the correlate task show strong direction-dependent ranking differences: parallel coordinates rank well for negative correlation but poorly for positive correlation, while scatterplots show similarly strong ranks across both signs. [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023]

**Notes:** This is a selection rule about conditioning on sign, not a claim that every chart is asymmetric.

## Where this applies <!-- role: context -->

- **User Goal:** Judge correlation strength where direction may be positive or negative.
- **Task:** Correlate (discriminate correlation differences).
- **Data:** Two quantitative variables with signed correlations across cases or subsets.
- **Chart Setting:** Static recommendation or auto-selection that must generalize across datasets.
- **Audience:** General audiences.
- **Success Criterion:** Consistent discrimination precision across correlation directions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your dataset only contains correlations of one direction and you do not expect sign to vary. **Why:** Conditioning on sign adds complexity without benefit if sign is constant.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Sign-conditional chart choice increases implementation and communication complexity.\
**Risk:** Over-complicating the interface can confuse users if the sign condition is not transparent.\
**Mitigation:** Keep the selection logic internal to the system and present a consistent user workflow.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Using one “best chart for correlation” rule regardless of whether correlations are positive or negative. **Why it fails:** The extracted ranks show that effectiveness can shift substantially with correlation direction for some chart types.

## Quick checks <!-- role: check -->

**Failure Sign:** A chart works well for one sign of correlation but users struggle when the sign flips.\
**Quick Check:** Test the same correlation magnitude with both signs and see if discrimination performance stays similar.\
**Stronger Test:** Compare JND-like thresholds by sign for candidate charts and pick sign-robust options when needed.

## What to do instead <!-- role: fix -->

- Use a chart that shows strong performance across both signs for correlation judgment when you need one consistent default.
- If using a chart with known sign asymmetry, add sign-aware selection rules in your recommendation logic.
- Split the workflow: use one chart for positive cases and another for negative cases.
- Provide a small validation step (e.g., quick comparison task) when deploying a sign-dependent recommendation in a new context.

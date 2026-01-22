---
id: prefer-line-or-scatter-over-area-for-trend-estimation
title: Prefer line charts or scatterplots over area charts for trend estimation (correlate
  task)
bibliography: references.bib
description: For estimating trends in bivariate data, line charts and scatterplots
  support more accurate judgments than area charts.
labels:
- chart:line
- chart:scatter
- chart:area
- task:correlate
- visual:position
- visual:area
- impact:accuracy
- data:quantitative
- complexity:basic
---

## Choose line charts or scatterplots over area charts for trend estimation <!-- role: advice -->

Use a line chart or scatterplot (position encodings) instead of an area chart when people need to estimate a bivariate trend by eye.

## Why position-based charts outperform area for trend estimation <!-- role: reason -->

Trend estimation in bivariate views depends on how reliably viewers can judge the relationship between x and y. When values are encoded with position (as in line charts and scatterplots), viewers can estimate trends more accurately than when values are encoded with filled area, which can distort judgments for the same correlate-style task.

**Mechanism:** Position encodings preserve the perceived geometry of the data relationship, while filling area introduces a visual feature that changes what viewers treat as signal when estimating the trend.

**Evidence:** For a correlate task, accuracy rankings placed line (E-2) and scatter/points (E-1) together above area (E-3), and both line and scatter significantly outperformed area (E-2 > E-3; E-1 > E-3) using ANCOVA at α = 0.05 [@correllRegressionEyeEstimating2017; @zengReviewCollationGraphical2023].

**Notes:** The evidence supports a preference for either line or scatter over area, but does not separate line vs scatter (they are tied in rank).

## When this trend-estimation guidance applies <!-- role: context -->

- **User Goal:** Estimate the direction/strength of a relationship (a trend) between two variables from the visualization.
- **Task:** Correlate (trend estimation by eye).
- **Data:** Bivariate data with a quantitative y-variable; x presented as an ordered sequence (ordinal x).
- **Chart Setting:** Static 2D chart where the trend is inferred visually (not computed by the viewer from shown regression output).
- **Audience:** General visualization readers; no specialized training assumed.
- **Success Criterion:** Higher accuracy of trend estimates.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You are not asking viewers to estimate a trend/relationship from the chart (i.e., correlate is not the task). **Why:** This guideline is only supported by evidence for correlate accuracy, not for other tasks or outcomes.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up the “filled” aesthetic or emphasis that area charts provide. **Risk:** Overapplying this preference can eliminate area charts even when area is needed for other communicative goals not evaluated here. **Mitigation:** Treat this as a task-conditional choice: apply it when trend estimation accuracy is a primary requirement.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Switching to an area chart for a bivariate trend view because it “looks stronger” or “fills space nicely.” **Why it fails:** Area charts ranked lower in correlate accuracy than line and scatter in the tested conditions.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers’ trend estimates are consistently less accurate for the filled area version than for the line/point version. **Quick Check:** Create two variants (area vs line or points) and compare whether trend judgments match expected direction/magnitude more often in the position-based version. **Stronger Test:** Run a small task-focused accuracy check that mirrors the correlate/trend-estimation question.

## What to do instead <!-- role: fix -->

- Use a line chart (positionX–positionY with a line mark) for the bivariate trend view.
- Use a scatterplot (positionX–positionY with point marks) for the bivariate trend view.
- If an area chart is required for another reason, add a separate position-based view (line or scatter) dedicated to trend estimation.
- If you must keep a single view, remove the filled area and keep the line-only version.

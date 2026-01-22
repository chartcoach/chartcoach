---
id: avoid-optimizer-generated-scatterplots-for-anomaly-detection-when-accuracy-is-primary
title: Avoid optimizer-generated scatterplots for anomaly finding when accuracy must
  match MATLAB or R defaults
bibliography: references.bib
description: For anomaly finding, MATLAB and R scatterplot defaults can be more accurate
  than an optimizer-generated scatterplot in the reported comparison.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:advanced
---

## Prefer MATLAB/R-style defaults for anomaly-finding accuracy <!-- role: advice -->

Avoid an optimizer-generated scatterplot preset for anomaly finding when accuracy is the top requirement, and prefer MATLAB or R defaults instead.

## Why some presets can improve anomaly-finding accuracy <!-- role: reason -->

Anomaly finding can be more sensitive to design-parameter choices than correlation or clustering; certain defaults can make anomalies more detectable, leading to higher accuracy.

**Mechanism:** Parameter choices can change how distinct anomalous points appear relative to the rest of the point cloud, affecting detectability.

**Evidence:** For anomaly-finding accuracy, MATLAB and R designs were ranked above the optimizer-generated design, and several significant pairwise differences were reported between those baselines and the optimizer-generated design at the stated threshold [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

**Notes:** The evidence compares specific presets; it does not imply all optimizer-generated designs will underperform.

## When this anomaly-finding rule applies <!-- role: context -->

- **User Goal:** Correctly identify anomalies/outliers from a scatterplot.
- **Task:** Find anomalies.
- **Data:** Two quantitative attributes with potential outliers/anomalies.
- **Chart Setting:** Static scatterplot with point marks and linear position scales.
- **Audience:** People relying on presets (no manual tuning).
- **Success Criterion:** Higher anomaly-detection accuracy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Speed matters more than accuracy for anomaly finding. **Why:** The optimizer-generated design was faster than the compared baselines for this task even when its accuracy ranked lower.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose time efficiency if you prioritize the more accurate defaults. **Risk:** Using a more accurate preset can still miss anomalies if the anomalies are ill-defined for the viewer’s goal. **Mitigation:** Clarify what qualifies as an anomaly in the workflow and test with representative examples.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a single “optimized” preset across correlation, clustering, and anomaly finding. **Why it fails:** The anomaly-finding results show a different ranking pattern than correlation/cluster accuracy.

## Quick tests <!-- role: check -->

**Failure Sign:** Users miss obvious outliers or mislabel normal points as anomalies. **Quick Check:** Compare anomaly-finding accuracy on a small benchmark set using MATLAB/R defaults versus the optimizer preset. **Stronger Test:** Run a within-subjects test measuring hit rate and false alarms across presets.

## What to do instead <!-- role: fix -->

- Use MATLAB or R default-like presets for anomaly finding when correctness is the priority.
- Offer multiple presets and let users choose based on whether they value accuracy or speed for anomaly finding.
- Validate the chosen preset on your most common anomaly patterns before deploying it as the default.

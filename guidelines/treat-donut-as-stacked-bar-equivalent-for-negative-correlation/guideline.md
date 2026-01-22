---
id: treat-donut-as-stacked-bar-equivalent-for-negative-correlation
title: Treat donut charts as comparable to stacked bars for negative-correlation discrimination
  (when forced to use radial form)
bibliography: references.bib
description: For negative correlations, donut charts showed no significant JND difference
  from stacked bars in the tested discrimination task.
labels:
- chart:donut
- task:compare
- visual:angle
- impact:accuracy
- data:quantitative
- audience:practitioner
- direction:negative-correlation
---

## If you must use a donut for negative correlation, expect similar discrimination precision to stacked bars <!-- role: advice -->

When a radial stacked form is required for comparing negative correlations, a donut chart can be used with similar expected correlation-discrimination precision as a stacked bar chart in the tested setting.

## Why the donut transform did not change JND relative to stacked bars here <!-- role: reason -->

A coordinate transform does not necessarily change the underlying perceptual discriminability for a task; it can preserve or alter the cues viewers rely on. In this tested case, the donut transformation of a stacked bar did not produce a statistically detectable difference in correlation-discrimination thresholds for negative correlations.

**Mechanism:** If the cue used to judge correlation remains effectively the same after transformation, JND may remain similar.

**Evidence:** For negative correlations, donut charts and stacked bar charts were not significantly different in JND-based discrimination under the paper’s multiple-comparison testing [@harrisonRankingVisualizationsCorrelation2014a]. The positive donut condition was excluded due to unreliable (near-chance) performance, limiting the conclusion to negative correlations [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** This equivalence is specific to the discrimination task and the tested donut/stacked-bar implementations.

## When this donut-versus-stacked-bar equivalence applies <!-- role: context -->

- **User Goal:** Compare correlation strength but constrained to a radial, donut-like design.
- **Task:** Decide which of two displays is more negatively correlated.
- **Data:** Two quantitative series encoded as stacked components.
- **Chart Setting:** Static small multiples where correlation comparison is the focus.
- **Audience:** Mixed expertise.
- **Success Criterion:** Discrimination performance similar to stacked bars for negative correlations.

## When not to rely on donut equivalence <!-- role: exceptions -->

**Break it when:** You need to communicate positive correlations with a donut chart. **Why:** The paper excluded the positive donut condition due to unreliable discrimination performance.

## Tradeoffs of using donut charts here <!-- role: costs -->

**Sacrifice:** The evidence supports parity only for negative correlations and only for the tested task. **Risk:** Donut charts may still be a poor choice for other tasks not measured by JND discrimination. **Mitigation:** Restrict donut use to cases where the task is exactly correlation discrimination and the sign matches validated conditions.

## Common mistakes with donuts for correlation <!-- role: mistakes -->

- **Mistake:** Assuming the donut result generalizes to positive correlations. **Why it fails:** Positive donut performance was unreliable in the paper’s procedure.
- **Mistake:** Treating coordinate transforms as always improving or always degrading discrimination. **Why it fails:** The paper shows transforms can have mixed effects across chart families.

## Quick checks for using a donut chart for negative correlation comparison <!-- role: check -->

**Failure Sign:** Viewers cannot consistently choose the more correlated display using the donut view. **Quick Check:** Verify predicted JND for the donut-negative model is within an acceptable range for your r values. **Stronger Test:** Conduct a small forced-choice comparison between donut-negative and stacked-bar-negative in your design system.

## What to do instead if donut performance is unreliable in your setting <!-- role: fix -->

- Use stacked bars for the correlation-comparison task if radial form is not strictly required.
- Switch to scatterplots for correlation discrimination if you can show individual points.
- Separate the decorative radial summary from a companion chart used specifically for correlation comparison.
- Reduce the need for fine discrimination by communicating coarse categories of correlation strength.

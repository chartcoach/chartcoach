---
id: prefer-static-summaries-over-hops-for-mean-estimation-when-variance-is-high
title: Prefer Static Summaries Over HOPs for Mean Estimation When Variance Is High
bibliography: references.bib
description: When variance is high, viewers estimate the mean less accurately from
  HOPs than from error bars or violin plots.
labels:
- chart:uncertainty
- task:estimate
- visual:position
- impact:accuracy
- data:univariate
- audience:novice
- method:hops
---

## Prefer error bars or violin plots for high-variance mean estimates <!-- role: advice -->

When the task is to estimate the mean of a single variable and the distribution has high variance, use a static depiction that directly marks the mean (such as an error bar mean line or a violin plot with a visible center) instead of HOPs.

## Why high variance hurts mean inference in HOPs <!-- role: reason -->

Estimating a mean from HOPs requires integrating many temporally separated outcomes; higher variance increases frame-to-frame movement and increases the sampling error from viewing only a finite number of frames, making mean estimation harder.

**Mechanism:** High dispersion makes the animated mark jump over a large range, increasing integration difficulty and requiring more frames to reach the same precision as a static mean indicator.

**Evidence:** For high-variance univariate distributions, mean absolute error for mean estimates was significantly worse with HOPs than with error bars or violin plots. [@hullmanHypotheticalOutcomePlots2015]

**Notes:** For low-variance univariate distributions, mean estimation accuracy did not differ meaningfully between HOPs and static depictions in the reported analysis. [@hullmanHypotheticalOutcomePlots2015]

## When mean estimation is the primary task <!-- role: context -->

- **User Goal:** Read or estimate the average level of a single uncertain quantity.
- **Task:** Estimate the mean from a univariate uncertainty depiction.
- **Data:** Univariate distribution with relatively high variance (wide spread).
- **Chart Setting:** Any medium (static or interactive).
- **Audience:** General readers; limited statistical background.
- **Success Criterion:** Lower absolute error in mean estimates.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The primary question is comparative ordering across multiple variables rather than a single-variable mean. **Why:** HOPs substantially improved accuracy for ordering judgments even though they underperformed for high-variance mean estimation. [@hullmanHypotheticalOutcomePlots2015]

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Static summaries may not convey joint behavior across variables or correlation.\
**Risk:** Viewers can misinterpret what an interval means if the summary is ambiguous about coverage.\
**Mitigation:** Clearly label what the interval represents (for example, “covers 95% of values”) when using static intervals. [@hullmanHypotheticalOutcomePlots2015]

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using HOPs for a single high-variance variable and expecting viewers to accurately infer the mean from a short viewing. **Why it fails:** Mean estimates were significantly less accurate with HOPs under high variance. [@hullmanHypotheticalOutcomePlots2015]

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ mean estimates vary widely and cluster far from the true mean when variance is high.\
**Quick Check:** Ask a few users to estimate the mean after a brief viewing; if errors are consistently larger than with a static mean marker, the HOPs mean task is failing.\
**Stronger Test:** Compare mean absolute error for mean estimation between a HOPs version and a static mean-marked version using the same underlying distribution. [@hullmanHypotheticalOutcomePlots2015]

## What to do instead <!-- role: fix -->

- Use a static display that explicitly marks the mean (for example, a mean line) for univariate high-variance mean reading.
- If using HOPs anyway, increase the opportunity to view many frames so integration is possible.
- Keep the y-axis range fixed to make frame-to-frame integration less demanding.
- Pair HOPs with a static mean indicator when the mean must be read precisely. [@hullmanHypotheticalOutcomePlots2015]

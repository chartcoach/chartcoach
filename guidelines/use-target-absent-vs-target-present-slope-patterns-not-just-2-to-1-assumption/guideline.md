---
id: use-target-absent-vs-target-present-slope-patterns-not-just-2-to-1-assumption
title: Evaluate target-absent behavior using slope ratios and intercepts, not a strict
  2:1 slope rule
bibliography: references.bib
description: Target-absent slopes are not simply double target-present slopes; ratios
  average above 2 and regression has a positive intercept.
labels:
- chart:scatter
- task:diagnose
- visual:position
- impact:validity
- data:quantitative
- audience:expert
- domain:psychophysics
- metric:slope-ratio
---

## Check for >2 slope ratios and positive intercepts in absent vs present slopes <!-- role: advice -->

When interpreting target-absent versus target-present RT × set size slopes, examine both the slope ratio and the regression intercept rather than assuming a strict 2:1 relationship. Treat systematic ratios greater than 2 and a positive target-absent intercept as expected empirical patterns that models and interpretations must accommodate.

## Empirical absent/present relationships depart from simple serial predictions <!-- role: reason -->

A simple serial, self-terminating account predicts an approximately 2:1 target-absent to target-present slope ratio and a line through the origin. If the observed relationship instead shows ratios reliably above 2 and a positive y-intercept, then “2:1 implies serial” becomes an unreliable diagnostic and the termination/decision process must be more complex than the simple rule suggests.

**Mechanism:** Slope ratios and intercepts reflect how searches terminate when no target is found; if quitting criteria differ systematically from a self-terminating scan, absent trials can accumulate additional time beyond a pure doubling of item-by-item processing.

**Evidence:** Across a very large aggregated dataset, target-present and target-absent slopes were strongly correlated, but the regression line relating target-absent to target-present slope had an approximately 2.0 slope with a positive y-intercept, and the mean slope ratio was significantly greater than 2.0 (including after log-transforming ratios to address skew) [@wolfeWhatCan11998]. Hypothesis tests rejected the constraint “target-absent slope − (2 × target-present slope) = 0” for efficient-slope ranges, indicating systematic departures from the strict 2:1 rule [@wolfeWhatCan11998].

**Notes:** Ratio instability increases when target-present slopes approach zero, so ratio summaries should consider that sensitivity.

## When you are modeling or interpreting absent vs present RT patterns <!-- role: context -->

- **User Goal:** Infer search process or stopping rule from RT × set size functions.
- **Task:** Compare target-present and target-absent slopes; test “serial self-terminating” signatures.
- **Data:** Separate RT × set size functions for target-present and target-absent trials; computed slopes and intercepts.
- **Chart Setting:** Scatterplot of target-absent slope vs target-present slope; distribution of slope ratios.
- **Audience:** Researchers evaluating search models or diagnosing task efficiency.
- **Success Criterion:** Avoid over-accepting a simple serial account based on approximate 2:1 expectations.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The dataset cannot support stable slope estimates (e.g., too few set sizes or too few trials per set size to estimate slopes/intercepts). **Why:** Ratio and intercept diagnostics become too noisy to interpret.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You must compute and report additional quantities (ratios, intercepts) beyond a single slope. **Risk:** Ratios can be misleading when target-present slopes are near zero. **Mitigation:** Use regression-based summaries and/or analyze log(ratio) or exclude near-zero denominators when summarizing.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Treating an approximately 2:1 slope ratio as confirmation of a simple serial, self-terminating mechanism. **Why it fails:** Empirical ratios average above 2.0 and the absent-vs-present line shows a positive intercept, inconsistent with the simplest 2:1-through-origin prediction [@wolfeWhatCan11998].
- **Mistake:** Reporting only the regression slope and ignoring the intercept. **Why it fails:** The intercept encodes systematic extra time on target-absent trials that a through-origin assumption would hide [@wolfeWhatCan11998].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Your interpretation relies on “ratio ≈ 2” without checking whether the intercept is near zero or whether ratios skew upward in efficient searches. **Quick Check:** Fit a regression of target-absent slopes on target-present slopes and record both slope and intercept. **Stronger Test:** Plot the distribution of slope ratios (or log ratios) and test whether the mean differs from 2.0.

## Fix: What to do instead <!-- role: fix -->

- Report target-present slope, target-absent slope, their ratio, and the absent-on-present regression intercept.
- Use log-transformed slope ratios when summarizing across conditions to reduce skew sensitivity.
- Analyze subsets that exclude near-zero target-present slopes when computing mean ratios, and report the exclusion rule.
- Treat deviations from 2:1 as informative signals about stopping criteria and task structure, not as noise.

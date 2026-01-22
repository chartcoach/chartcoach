---
id: choose-and-enforce-the-statistics-you-want-to-hold-constant-via-a-pluggable-equivalence-test
title: Choose and enforce the statistics you want to hold constant via a pluggable
  equivalence test
bibliography: references.bib
description: Keep datasets identical on whatever measures matter by swapping the statistical
  checks used to accept or reject proposed perturbations.
labels:
- chart:scatter
- task:generate
- visual:position
- impact:integrity
- data:quantitative
- audience:expert
- custom:statistics
- complexity:advanced
---

## Gate accepted perturbations with the specific statistics you intend to preserve <!-- role: advice -->

Implement statistical equivalence as an explicit acceptance gate and swap in the exact statistics you want to preserve (parametric or non-parametric) rather than hard-coding a single summary set.

## Why a swappable “stats gate” controls what remains invariant <!-- role: reason -->

The method separates “how you search” (perturbations plus annealing) from “what you preserve” (the equivalence test), so you can keep different statistical properties fixed by changing only the gate while leaving the exploration mechanism unchanged.

**Mechanism:** The acceptance gate defines invariants; any proposed dataset that violates the chosen measures is rejected, so the optimization can change appearance only within the feasible region induced by those measures.

**Evidence:** The same iterative framework was demonstrated while holding standard summary statistics (means, standard deviations, Pearson correlation) fixed and also while holding non-parametric statistics (medians, interquartile ranges, Spearman rank correlation) fixed [@matejkaSameStatsDifferent2017]. The approach is described as agnostic to which statistical properties are maintained between datasets [@matejkaSameStatsDifferent2017].

**Notes:** Equality was operationalized as matching to a set number of decimal places in the examples [@matejkaSameStatsDifferent2017].

## When you need invariance on a particular statistical contract <!-- role: context -->

- **User Goal:** Produce alternative datasets that keep the “reported” or “required” statistics unchanged.
- **Task:** Maintain invariants while varying visual appearance.
- **Data:** Quantitative x/y samples (or 1D samples) where multiple statistics may be relevant.
- **Chart Setting:** Any workflow where downstream interpretation depends on a specific set of statistics.
- **Audience:** Analysts, educators, or tool builders who need control over which measures are held fixed.
- **Success Criterion:** The preserved statistics match the seed dataset under the chosen equivalence rule, while the plotted appearance changes.

## When not to use a simple decimal-place equivalence definition <!-- role: exceptions -->

**Break it when:** Your use case requires distribution-level similarity rather than matching a few rounded summary measures. **Why:** Matching a small set of rounded summaries can permit large differences in distributional structure and appearance [@matejkaSameStatsDifferent2017].

## Tradeoffs of customizing the preserved-statistics set <!-- role: costs -->

**Sacrifice:** Adding more constraints reduces the feasible space and can slow convergence. **Risk:** Preserving an ill-chosen set of measures can create outputs that satisfy the gate but miss your actual intent. **Mitigation:** Define the gate from the real requirement (for example, robust statistics or distributional tests) rather than convenience [@matejkaSameStatsDifferent2017].

## Common mistakes when choosing invariants <!-- role: mistakes -->

- **Mistake:** Preserving only mean, standard deviation, and correlation when the goal is to preserve distributional shape. **Why it fails:** Many different-looking datasets can share those summaries [@matejkaSameStatsDifferent2017].
- **Mistake:** Treating “matches to two decimals” as a meaningful equivalence without checking sensitivity. **Why it fails:** Small rounding tolerances can hide meaningful differences in the underlying values [@matejkaSameStatsDifferent2017].

## Quick tests for whether your invariants match your intent <!-- role: check -->

**Failure Sign:** Outputs satisfy the chosen gate but violate the qualitative property you hoped to preserve (or destroy one you hoped to change). **Quick Check:** Compute the gated statistics and at least one additional, non-gated diagnostic statistic to see if it drifts. **Stronger Test:** Plot multiple outputs side-by-side and verify that only the intended aspects vary while the intended invariants remain stable [@matejkaSameStatsDifferent2017].

## What to do instead when the wrong things stay fixed <!-- role: fix -->

- Replace the preserved-statistics gate with robust alternatives (for example, median and interquartile range) when outliers should not dominate.
- Add a distributional similarity test in the gate when you need the overall shape to remain similar.
- Reduce the number of preserved measures if the optimization cannot produce distinct appearances under the current constraints.
- Change the seed dataset if its statistics define an infeasible or unhelpful constraint region for your intended outputs [@matejkaSameStatsDifferent2017].

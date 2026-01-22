---
id: use-simulated-annealing-to-morph-a-seed-dataset-while-holding-summary-statistics-constant
title: Use simulated annealing to morph a seed dataset while holding chosen statistics
  constant
bibliography: references.bib
description: Iteratively perturb points from a seed dataset and accept changes via
  simulated annealing only when target statistics remain unchanged to a chosen precision.
labels:
- chart:scatter
- task:generate
- visual:position
- impact:integrity
- data:quantitative
- audience:expert
- complexity:advanced
- method:simulated-annealing
---

## Simulated-anneal point perturbations under a fixed-statistics constraint <!-- role: advice -->

Iteratively perturb one or more points in a seed dataset and accept proposed changes via simulated annealing only when the selected statistical properties remain unchanged to your specified precision.

## Why annealed perturbations preserve stats while enabling new shapes <!-- role: reason -->

The approach works because small random point moves can be tuned so that most proposed datasets remain statistically equivalent (to a chosen rounding precision), while simulated annealing allows occasional fitness-decreasing moves to escape local optima and reach visually distinct arrangements.

**Mechanism:** A constrained random walk explores many alternative point configurations; simulated annealing broadens exploration early and narrows it later, while a statistical-equivalence gate keeps the chosen summary measures fixed.

**Evidence:** An iterative perturb-and-accept procedure with simulated annealing produced multiple datasets with visibly different appearances while matching specified statistics (for example, mean, standard deviation, and correlation) to two decimal places [@matejkaSameStatsDifferent2017]. The same framework was shown to work with alternative statistics (for example, medians, interquartile ranges, and Spearman’s rank correlation) [@matejkaSameStatsDifferent2017].

**Notes:** The method is driven by a seed dataset; the seed’s computed statistics define the constraint the outputs must match.

## When you need many different-looking plots with the same statistics <!-- role: context -->

- **User Goal:** Create multiple datasets that look different in a plot while sharing the same reported statistics.
- **Task:** Generate or stress-test examples where summary statistics are held constant.
- **Data:** 1D or 2D quantitative samples represented as points (or a 1D distribution).
- **Chart Setting:** Static figures or datasets used for teaching, testing, or demonstration.
- **Audience:** People who may over-trust summary statistics without inspecting plots.
- **Success Criterion:** Output datasets remain equal on chosen statistics to a defined precision, but differ clearly in visual appearance.

## When not to rely on this approach <!-- role: exceptions -->

**Break it when:** You need exact equality of statistics (not equality to a rounding threshold) across datasets. **Why:** The acceptance gate described is based on equality to a chosen decimal precision rather than exact invariants [@matejkaSameStatsDifferent2017].

## Tradeoffs of constrained simulated annealing <!-- role: costs -->

**Sacrifice:** You trade compute time for exploration because many perturbations are proposed and filtered. **Risk:** The process can yield undesirable shapes when the seed distribution and target structure are far apart. **Mitigation:** Expect iteration and parameter tuning, including the annealing schedule and perturbation scale [@matejkaSameStatsDifferent2017].

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Only accepting fitness-improving perturbations. **Why it fails:** Greedy acceptance can trap the process in locally optimal configurations instead of reaching more globally optimal appearances [@matejkaSameStatsDifferent2017].

## Quick ways to validate success <!-- role: check -->

**Failure Sign:** The plot changes, but the dataset no longer matches the seed’s required statistics at the chosen precision. **Quick Check:** Recompute the constrained statistics after each accepted step and verify equality to the configured decimal places. **Stronger Test:** Run multiple independent annealing runs from the same seed to see whether you can reach distinct appearances while keeping the statistics fixed [@matejkaSameStatsDifferent2017].

## What to do instead when it stalls or drifts off-constraint <!-- role: fix -->

- Reduce the perturbation step size so that most proposed moves preserve the constrained statistics at your chosen precision.
- Add simulated-annealing acceptance (temperature-based acceptance of worse fitness) rather than using only greedy improvements.
- Increase iteration count or adjust the cooling schedule if the dataset stops changing appearance while still meeting constraints.
- Change the constrained statistics set (the ISERROROK gate) to match what you truly need to preserve [@matejkaSameStatsDifferent2017].

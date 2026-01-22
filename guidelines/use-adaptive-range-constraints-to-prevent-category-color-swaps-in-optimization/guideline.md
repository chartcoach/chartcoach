---
id: use-adaptive-range-constraints-to-prevent-category-color-swaps-in-optimization
title: Use adaptive range constraints to prevent category color swapping during categorical
  palette optimization
bibliography: references.bib
description: "Keep each category\u2019s color stable by limiting per-iteration change\
  \ so optimization evolves colors smoothly instead of swapping them."
labels:
- chart:general
- task:maintain-mapping
- visual:color
- impact:trust
- data:categorical
- audience:expert
- method:optimization
- method:constraints
---

## Prevent category color swapping with adaptive per-iteration constraints <!-- role: advice -->

When optimizing a categorical palette iteratively, use adaptive range constraints that limit how much each color component can change per iteration to avoid category colors swapping identities.

## Smooth evolution preserves category identity across iterations <!-- role: reason -->

Some optimization methods can improve distances by effectively reassigning colors (a swap), which breaks the original category-to-color mapping. Adaptive per-iteration limits constrain the search locally around the current palette so changes remain gradual, preserving identity while still improving separation.

**Mechanism:** Limiting step size reduces discontinuous jumps in the solution space that can replace one category’s color with another’s, maintaining stable semantic association.

**Evidence:** An adaptive range constraint (bounded percentage change per iteration) is used to alleviate color swapping in genetic-algorithm-based optimization, producing smoother evolution and preventing undesired reassignment effects [@fangCategoricalColormapOptimization2017; @zengReviewCollationGraphical2023].

**Notes:** This is particularly relevant when categories have fixed labels and users expect continuity.

## Context for avoiding color swaps <!-- role: context -->

- **User Goal:** Improve discriminability without changing category-to-color assignments.
- **Task:** Ongoing use of a fixed legend mapping across time or products.
- **Data:** Nominal categories where reassignment would be costly or dangerous.
- **Chart Setting:** Automated palette optimization workflows; iterative or search-based optimization (e.g., genetic algorithms).
- **Audience:** Operational users and experts who depend on stable mappings.
- **Success Criterion:** No category ends up with a dramatically different color family than it started with.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** You explicitly allow categories to be reassigned to new colors (e.g., redesigning a system from scratch). **Why:** Swap-prevention constraints can slow convergence and reduce the best achievable separation.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More iterations may be needed to reach a good solution, and the best attainable minimum distance may be lower. **Risk:** Too-small adaptive steps can stall improvement. **Mitigation:** Increase the allowed percentage change gradually until improvement resumes without swaps.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Letting an optimizer freely search the space when category-to-color identity must be preserved. **Why it fails:** The optimizer may “solve” the objective by effectively permuting colors across categories.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** After optimization, stakeholders report that two categories “traded colors” even if overall separation improved. **Quick Check:** Track per-category hue trajectories over iterations; sudden large jumps or crossings indicate swapping behavior. **Stronger Test:** Have a domain user match each optimized color to its original category name without the legend; frequent mismatches indicate identity loss.

## Fix: What to do instead <!-- role: fix -->

- Apply adaptive per-iteration bounds on hue, saturation, and luminance changes during optimization.
- Lock critical categories (fixed colors) and optimize only non-critical categories.
- Restart optimization from the original palette with stricter constraints if a swap is detected.
- Replace the optimization method with one that better respects local continuity under constraints.

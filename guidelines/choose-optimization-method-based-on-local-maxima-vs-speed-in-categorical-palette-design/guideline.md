---
id: choose-optimization-method-based-on-local-maxima-vs-speed-in-categorical-palette-design
title: "Choose genetic algorithms to escape local maxima, and Nelder\u2013Mead for\
  \ faster constrained categorical palette optimization"
bibliography: references.bib
description: Balance palette quality and compute cost by selecting an optimization
  algorithm suited to your constraint and robustness needs.
labels:
- chart:general
- task:optimize
- visual:color
- impact:efficiency
- data:categorical
- audience:expert
- method:optimization
---

## Select the optimization algorithm based on robustness versus speed <!-- role: advice -->

Use a genetic algorithm when you need to escape local maxima and improve the best-achievable minimum distance, and use Nelder–Mead simplex when you need faster convergence under constraints.

## Different optimizers trade off solution quality, speed, and stability <!-- role: reason -->

Color-distance landscapes can be non-convex, so some algorithms get trapped in local maxima and stop improving the minimum distance. More global search (e.g., genetic algorithms) can find better minima-separation solutions but often costs more computation and can deviate from the initial semantics unless constrained.

**Mechanism:** Global search explores more of the solution space (reducing local maxima trapping) while local search converges quickly but can stop early in non-convex landscapes.

**Evidence:** The optimization landscape for CIEDE2000-based distances is described as non-convex, motivating methods that handle local maxima; genetic algorithms tend to reach higher minimum-distance solutions while Nelder–Mead converges faster, with comparative results shown across constrained settings [@fangCategoricalColormapOptimization2017; @zengReviewCollationGraphical2023].

**Notes:** If semantic preservation matters, algorithm choice interacts with constraints; unconstrained global search can distort the mapping.

## Context for choosing an optimizer <!-- role: context -->

- **User Goal:** Produce a categorical palette with strong separability under time/compute constraints.
- **Task:** Optimize a palette (often repeatedly, e.g., in tooling).
- **Data:** Nominal categories mapped to color hue.
- **Chart Setting:** Automated or semi-automated palette generation; interactive tools where responsiveness matters versus offline design where quality is prioritized.
- **Audience:** Tool builders, visualization engineers, or advanced designers.
- **Success Criterion:** Adequate minimum perceptual distance achieved within acceptable compute time and within constraints.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot enforce constraints needed to preserve semantics during a genetic algorithm run. **Why:** The optimizer can deviate substantially from the intended category meanings.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Genetic algorithms typically cost more computation; Nelder–Mead can sacrifice solution quality by getting stuck. **Risk:** Choosing speed-first can leave problematic near-collisions unresolved; choosing robustness-first can produce semantically unacceptable palettes. **Mitigation:** Pair algorithm choice with appropriate constraints and stopping criteria.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a fast local optimizer and assuming the first converged result is globally good. **Why it fails:** Non-convex distance spaces can cause premature convergence at a local maximum.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** The minimum pairwise distance plateaus early while obvious close pairs remain. **Quick Check:** Run multiple restarts from different initializations; large variance suggests local maxima issues. **Stronger Test:** Compare achieved Dmin and runtime across candidate algorithms on the same constraints and palette size.

## Fix: What to do instead <!-- role: fix -->

- Switch to a genetic algorithm (or add restarts) when local maxima trapping is suspected.
- Use Nelder–Mead for interactive scenarios where response time is critical.
- Add semantic-preserving constraints (fixed colors, hue bounds, adaptive ranges) when using global search.
- Predefine a compute budget and accept the best-found palette by Dmin within that budget.

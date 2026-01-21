---
id: use-simulated-annealing-to-avoid-local-optima-when-shaping-datasets
title: Use Simulated Annealing to Accept Occasional Worse Moves
bibliography: references.bib
description: Avoid getting stuck while shaping datasets by probabilistically accepting
  worse steps early and cooling over time.
labels:
- chart:scatter
- task:optimize
- visual:position
- impact:robustness
- data:bivariate
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When optimizing a dataset’s visual fit to a target under statistical constraints, use simulated annealing so you sometimes accept worse fitness moves early and reduce that acceptance over time.

## The Logic <!-- role: reason -->

- **The Principle:** Probabilistic acceptance helps escape local optima; cooling gradually shifts from exploration to refinement.
- **The Evidence:** The method explicitly uses simulated annealing to avoid getting stuck by allowing non-improving moves based on a temperature schedule [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Reach a globally better-looking target shape rather than a locally “good enough” partial match.
- **Data Type:** Any iterative point-perturbation procedure with a fitness function (e.g., distance to a target curve/shape).
- **Audience:** Developers implementing “same stats, different graphs” generators.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need a minor visual change from the seed dataset.
- **Reason:** Greedy acceptance may be sufficient and simpler if the optimization landscape is easy.

## The Price <!-- role: costs -->

- **The Sacrifice:** More parameters (start/end temperature, cooling schedule) and potentially longer runtime.
- **The Risk:** Too much exploration can delay convergence or yield unstable intermediate shapes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Accept only improvements (pure hill-climbing).
- **Why it fails:** The paper notes this can get stuck in locally optimal solutions even when better global solutions exist [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The dataset stops improving visually long before it resembles the target, despite many iterations.
- **The Test:** Track fitness over iterations; long plateaus suggest local-optimum trapping [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the early temperature so occasional worse steps are accepted.
- **Best Fix:** Use a monotonic cooling schedule (the paper reports a quadratically-smoothed schedule working well in examples) and tune until fitness improves smoothly toward the target [@matejkaSameStatsDifferent2017].

---
id: optimize-for-target-crowding-not-staggered-predictability
title: Prioritize Reducing Target Crowding Over Predictable Stagger Order
bibliography: references.bib
description: When staggering is used, reducing close encounters between marks matters
  more than making the motion order predictable.
labels:
- chart:scatter
- task:track
- visual:position
- impact:accuracy
- data:multivariate
- audience:expert
- animation:pacing
- metric:crowding
---

## The Rule <!-- role: advice -->

If you use staggered motion at all, prioritize configurations that reduce target crowding, even if the motion order becomes less predictable.

## The Logic <!-- role: reason -->

The paper’s best-case experiment shows the only clearly observable accuracy gain occurs in the condition that most reduces crowding (their “smart” ordering with higher dwell), despite participants perceiving it as harder; this suggests that crowding reduction is the dominant lever for tracking performance compared to predictability of a simple spatial order [@chevalierNotsoStaggeringEffectStaggered2014].

- **The Principle:** Crowding (close spacing and near-crossings) drives target–distractor confusion in tracking.
- **The Evidence:** Smart ordering (chosen to minimize crowding) with higher dwell produced a measurable accuracy gain compared to baseline, while predictable spatial ordering did not show comparable improvement [@chevalierNotsoStaggeringEffectStaggered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Maintain correct correspondences for multiple moving points.
- **Data Type:** Dot-cloud transitions where near passes between points are common.
- **Audience:** Users doing accurate visual tracking (not just watching an animation).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You value perceived ease/comfort over objective tracking accuracy.
- **Reason:** Participants rated the best-performing (crowding-minimizing) stagger as most difficult, so a predictable order may be preferable for perceived smoothness even if it doesn’t improve tracking [@chevalierNotsoStaggeringEffectStaggered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Motion may feel less orderly and less predictable.
- **The Risk:** Viewers may report the animation as “harder” even if their accuracy improves [@chevalierNotsoStaggeringEffectStaggered2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always staggering top-to-bottom (or left-to-right) to make timing predictable.
- **Why it fails:** Predictability alone did not reliably translate into better tracking performance in the paper’s tests; crowding reduction was the more diagnostic factor [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Many close encounters still occur during the transition (targets get “mixed up” near distractors).
- **The Test:** Compare crowding-like events between alternative stagger orders (e.g., count near-neighbor minima over time) and verify with a small tracking test [@chevalierNotsoStaggeringEffectStaggered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Try an order that empirically reduces close approaches (e.g., reorder starts to reduce nearest-neighbor conflicts).
- **Best Fix:** Use an ordering strategy explicitly selected to reduce crowding (as in the paper’s “smart ordering” idea), then validate with tracking accuracy, not preference ratings [@chevalierNotsoStaggeringEffectStaggered2014].

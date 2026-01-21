---
id: use-discrete-outcome-distributions-to-improve-short-term-recall-of-uncertainty
title: Use Discrete Outcome Distributions to Improve Recall of Uncertainty
bibliography: references.bib
description: Prefer small-multiple discrete outcomes (e.g., 20 dots) over continuous
  density when the goal is remembering a distribution later.
labels:
- chart:distribution
- task:recall
- visual:mark
- impact:memorability
- data:uncertainty
- audience:novice
- custom:discrete-outcomes
---

## The Rule <!-- role: advice -->

When you want people to remember an uncertainty distribution from a single exposure, show it as a discrete set of outcomes (e.g., ~20 dots) rather than only as a continuous density curve.

## The Logic <!-- role: reason -->

Discrete outcomes can make the distribution’s shape easier to encode and reproduce from memory (people can recall the “shape” and placement of a small set of outcomes).

- **The Principle:** Discrete, countable outcomes support memory via shape encoding
- **The Evidence:** Discrete-outcome visualizations improved participants’ graphical recall accuracy of the shown sampling distribution compared to continuous visualizations [@hullmanImaginingReplicationsGraphical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Recalling the uncertainty in a reported effect after reading a study result.
- **Data Type:** A single univariate distribution representing uncertainty about an experimental effect.
- **Audience:** General readers / non-experts who may ignore or misremember uncertainty.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is accurate *estimation for a new study* (transfer), not recall.
- **Reason:** In the transfer task, discrete visualizations were associated with worse accuracy than continuous in this study [@hullmanImaginingReplicationsGraphical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower precision/continuity than a smooth density.
- **The Risk:** Some users may not understand what each discrete outcome represents, which can increase between-user variability [@hullmanImaginingReplicationsGraphical2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using too many discrete outcomes assuming it will be “more accurate.”
- **Why it fails:** In the paper’s interface evaluation, more outcomes did not reliably improve drawing accuracy, and added interaction time [@hullmanImaginingReplicationsGraphical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can recreate the rough shape but answer probability questions inconsistently.
- **The Test:** Pair a quick graphical recall check (redraw) with a few probability questions; if redraw is good but probability answers are poor, memorability may be superficial [@hullmanImaginingReplicationsGraphical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short annotation like “Each dot ≈ 5% of replications” when using 20 outcomes.
- **Best Fix:** If comprehension (not just recall) is needed, combine discrete outcomes with a prediction-and-feedback step to focus attention on meaning, not only shape [@hullmanImaginingReplicationsGraphical2018].

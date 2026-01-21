---
id: use-low-outcome-counts-in-discrete-distributions-to-reduce-drawing-time-without-losing-accuracy
title: Use Low Outcome Counts in Discrete Distributions
bibliography: references.bib
description: Keep discrete outcome counts small (e.g., ~20) to reduce interaction
  time, since more outcomes may not improve accuracy.
labels:
- chart:distribution
- task:elicit
- visual:mark
- impact:efficiency
- data:uncertainty
- audience:novice
- custom:discrete-outcomes
---

## The Rule <!-- role: advice -->

If you use discrete-outcome uncertainty displays for elicitation, keep the number of outcomes small (around 20) rather than scaling to 50–100+.

## The Logic <!-- role: reason -->

More discrete outcomes increase interaction cost (time) without reliably increasing how accurately people can reproduce a target distribution in the paper’s evaluation.

- **The Principle:** Diminishing returns of resolution under interaction cost
- **The Evidence:** In the interface evaluation, higher-outcome-count discrete interfaces took ~1.6× the time of 20-outcome versions and did not yield reliably better accuracy [@hullmanImaginingReplicationsGraphical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly sketching an uncertainty distribution rather than precisely specifying every nuance.
- **Data Type:** Univariate probability distributions elicited interactively.
- **Audience:** General users / MTurk-like populations / non-experts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need high-resolution probability mass for downstream quantitative modeling, and users are trained and motivated.
- **Reason:** The paper’s evidence is about novice usability and drawing accuracy/time tradeoffs; expert elicitation goals may differ [@hullmanImaginingReplicationsGraphical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less granularity in the expressed distribution.
- **The Risk:** Users may overfit to coarse bins (e.g., step-like shapes), limiting subtle differences.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing dot count to “make it more precise” while keeping the same interaction method.
- **Why it fails:** Time increases and accuracy may not improve; the extra effort can discourage careful shaping [@hullmanImaginingReplicationsGraphical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users spend long periods placing many outcomes with little improvement in the resulting shape.
- **The Test:** Run a quick pilot comparing 20 vs 50/100 outcomes; if completion time rises substantially without consistent accuracy gains, reduce outcomes.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Default to ~20 outcomes and only offer higher resolution behind an “advanced” toggle.
- **Best Fix:** Match outcome count to the cognitive goal: keep it low for communication/learning and only increase resolution when you can justify and support the added interaction cost [@hullmanImaginingReplicationsGraphical2018].

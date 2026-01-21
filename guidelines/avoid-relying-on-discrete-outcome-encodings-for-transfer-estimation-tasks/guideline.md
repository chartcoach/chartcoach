---
id: avoid-relying-on-discrete-outcome-encodings-for-transfer-estimation-tasks
title: Avoid Discrete Outcome Encodings for Transfer Estimation of Uncertainty
bibliography: references.bib
description: Use continuous uncertainty displays when users must estimate replication
  uncertainty for a new study, because discrete can reduce accuracy.
labels:
- chart:distribution
- task:predict
- visual:shape
- impact:accuracy
- data:uncertainty
- audience:novice
- custom:transfer-task
---

## The Rule <!-- role: advice -->

When users must estimate uncertainty for a *new* experiment (transfer), prefer a continuous distribution display over a discrete-outcome display.

## The Logic <!-- role: reason -->

In transfer estimation, discrete-outcome displays can worsen accuracy—likely because discrete marks reduce precision and can be misunderstood, producing higher error for some users.

- **The Principle:** Precision and interpretation demands dominate in transfer estimation
- **The Evidence:** In the graphical transfer task, discrete visualization format was associated with worse performance (higher divergence from the normative replication prediction distribution) [@hullmanImaginingReplicationsGraphical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Predicting what would happen if a different study were replicated many times.
- **Data Type:** Univariate uncertainty distributions constructed/estimated from summary statistics for a new domain.
- **Audience:** Non-experts estimating effect uncertainty beyond a single shown example.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is short-term recall of a shown distribution rather than accurate transfer estimation.
- **Reason:** Discrete-outcome visualizations improved graphical recall in the same study [@hullmanImaginingReplicationsGraphical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Continuous densities may be less memorable and less “countable” than discrete outcomes.
- **The Risk:** Users may still misinterpret what the curve means without additional scaffolding (the paper motivates prediction as a scaffold) [@hullmanImaginingReplicationsGraphical2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to discrete dots because they “feel intuitive” while asking users to make precise spread judgments.
- **Why it fails:** The study found discrete format can reduce accuracy on transfer tasks even if it helps recall [@hullmanImaginingReplicationsGraphical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ predicted distributions cluster around defaults (e.g., center of axis) or show bimodal errors.
- **The Test:** Compare users’ predicted means and spreads to a normative reference (e.g., divergence or moment error); large systematic under/over-spread suggests format isn’t supporting estimation [@hullmanImaginingReplicationsGraphical2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Offer a continuous mode (smooth curve/handles) for prediction tasks while keeping discrete for recall-oriented views.
- **Best Fix:** Combine continuous prediction with immediate feedback (show predicted vs true distribution for an example) to improve transfer accuracy [@hullmanImaginingReplicationsGraphical2018].

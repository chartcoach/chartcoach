---
id: elicit-uncertainty-by-asking-users-to-draw-a-replication-distribution
title: Elicit Uncertainty by Having Users Draw a Replication Distribution First
bibliography: references.bib
description: Have users sketch expected replication outcomes before revealing the
  actual uncertainty to improve later uncertainty estimation.
labels:
- chart:distribution
- task:estimate
- visual:interaction
- impact:learning
- data:uncertainty
- audience:novice
- custom:graphical-prediction
---

## The Rule <!-- role: advice -->

Ask users to graphically predict the distribution of effects they expect from many replications *before* showing the true sampling/replication distribution.

## The Logic <!-- role: reason -->

Making a prediction forces active reasoning and creates a clear “gap” between the user’s belief and the revealed distribution, which supports learning and improves later estimation in a new scenario.

- **The Principle:** Prediction-based active learning / learning from discrepancy
- **The Evidence:** In a controlled study, participants who completed graphical prediction produced more accurate distributions on a near-transfer task estimating replication uncertainty for a new experiment [@hullmanImaginingReplicationsGraphical2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating what would happen if a study were replicated; forming expectations about effect uncertainty for a new study.
- **Data Type:** Univariate effect-size uncertainty communicated as a probability distribution (sampling/replication prediction distribution).
- **Audience:** Non-experts / non-statisticians reading experimental results.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need users to quickly read a provided interval/value with no learning or transfer goal.
- **Reason:** Graphical prediction adds interaction steps and time, and the demonstrated benefit is specifically for later estimation (transfer), not necessarily for immediate recall in all formats [@hullmanImaginingReplicationsGraphical2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More time and interaction complexity than passive viewing.
- **The Risk:** Some users may respond variably; the paper reports increased variance in performance in prediction conditions in some analyses [@hullmanImaginingReplicationsGraphical2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Asking for a single-point guess (e.g., “What’s the mean?”) instead of a distribution.
- **Why it fails:** The paper’s intervention targets reasoning about the *distribution* of replication outcomes; point estimates don’t elicit uncertainty structure [@hullmanImaginingReplicationsGraphical2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ outputs collapse into a narrow spike or a single bin regardless of the described variability.
- **The Test:** Compare predicted spread to what the interface allows (e.g., do users use only 1–2 bins/handles despite being asked about “many replications”?).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit prompt text like “Draw the range of outcomes you expect across many replications, not just the most likely outcome.”
- **Best Fix:** Show the user’s predicted distribution overlaid with the revealed distribution immediately after prediction to make the discrepancy salient, as in the study flow [@hullmanImaginingReplicationsGraphical2018].

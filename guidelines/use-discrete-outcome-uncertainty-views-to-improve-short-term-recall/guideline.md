---
id: use-discrete-outcome-uncertainty-views-to-improve-short-term-recall
title: Use Discrete Outcome Uncertainty Views to Improve Short-Term Recall of a Sampling
  Distribution
bibliography: references.bib
description: "Displaying sampling uncertainty as a small set of discrete outcomes\
  \ improves users\u2019 graphical recall of the distribution."
labels:
- chart:distribution
- task:recall
- visual:marks
- impact:memorability
- data:uncertainty
- audience:novice
- representation:discrete-outcomes
---

## Prefer a small discrete-outcome display when you want users to remember uncertainty <!-- role: advice -->

When the goal is for users to recall a sampling distribution later, display uncertainty as a discrete set of outcomes rather than only as a smooth continuous density. Keep the number of outcomes small enough that the distribution shape is easy to encode and reproduce.

## Discrete outcomes can be remembered as a shape pattern <!-- role: reason -->

A discrete set of outcomes reduces a probability distribution into a limited collection of marks that can be encoded as a visual pattern. This can support later reconstruction of both location and shape when users are asked to reproduce the distribution from memory.

**Mechanism:** Discretization constrains and “chunks” the uncertainty into countable marks, making the distribution’s form easier to store and retrieve as a visual pattern.

**Evidence:** In a controlled study, participants who viewed the true sampling distribution in a discrete-outcome form had better graphical recall (lower divergence from the true sampling distribution) than those who viewed a continuous form [@hullmanImaginingReplicationsGraphical2018]. The same study observed many perfectly recalled distributions in discrete conditions, consistent with a memorability-by-shape effect [@hullmanImaginingReplicationsGraphical2018].

**Notes:** The recall advantage did not clearly carry over to text-only probability recall, suggesting the benefit may be strongest for visual reconstruction rather than modality translation.

## Where discrete-outcome recall benefits apply <!-- role: context -->

- **User Goal:** Remember the uncertainty around an observed effect after leaving the chart.
- **Task:** Recreate or recognize the approximate sampling distribution later (graphical recall).
- **Data:** Univariate uncertainty distribution for an effect estimate.
- **Chart Setting:** Reports, dashboards, or interactive articles where viewers may return later and need to remember uncertainty shape.
- **Audience:** Novices or mixed audiences without strong statistical training.
- **Success Criterion:** Lower error in reproducing the distribution’s center and spread from memory.

## When not to rely on discrete outcomes <!-- role: exceptions -->

**Break it when:** The primary goal is accurate estimation of uncertainty for a new study (transfer), not recalling the original distribution. **Why:** The same experiment found discrete displays did not improve transfer estimates and were associated with worse transfer accuracy in that task [@hullmanImaginingReplicationsGraphical2018].

## Tradeoffs of discrete-outcome uncertainty views <!-- role: costs -->

**Sacrifice:** Reduced precision and granularity compared to a continuous density representation. **Risk:** Some users may not understand what each outcome represents, producing high variability in reasoning tasks beyond recall. **Mitigation:** Ensure the display clearly signals that outcomes represent frequency/proportion of replications.

## Common discrete-outcome pitfalls <!-- role: mistakes -->

**Mistake:** Using a discrete display without clarifying that each mark corresponds to a share of replications. **Why it fails:** Users may treat marks as decorative texture, which can increase variability in interpretation.

**Mistake:** Expecting discrete displays to automatically improve transfer reasoning to new studies. **Why it fails:** The observed benefit was for graphical recall of the shown distribution, not for estimating a new replication distribution [@hullmanImaginingReplicationsGraphical2018].

## Quick checks for discrete recall effectiveness <!-- role: check -->

**Failure Sign:** Users cannot reproduce the distribution shape any better than with a continuous density. **Quick Check:** Ask a small sample of users to redraw the distribution after a brief delay and compare reconstruction error. **Stronger Test:** Measure divergence between recalled distributions and the true sampling distribution across discrete vs continuous encodings.

## What to do instead if discrete outcomes hurt your main task <!-- role: fix -->

- Use a continuous density display when the main task is predicting replication uncertainty for a new study rather than recalling the original.
- Pair the discrete-outcome view with an immediate comprehension check about what the marks represent before users proceed.
- Use the discrete-outcome view only for the “recallable summary” and provide a continuous view for precise reading or downstream estimation.
- If users struggle with meaning, switch to a continuous visualization while keeping the same interaction pattern for consistency.

---
id: pay-more-to-finish-faster-not-to-improve-quality-in-crowdsourced-vis-studies
title: Increase Per-HIT Reward to Accelerate Completion, Not to Increase Accuracy
bibliography: references.bib
description: "Higher payments speed up crowdsourced study completion but do not meaningfully\
  \ improve\u2014and may slightly reduce\u2014accuracy."
labels:
- chart:multiple
- task:collect
- visual:multiple
- impact:throughput
- data:quantitative
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

Use higher rewards when you need faster turnaround; do not assume higher pay yields better perceptual data quality.

## The Logic <!-- role: reason -->

Across experiments, Heer & Bostock found higher rewards (≥$0.04/HIT) significantly reduced elapsed time to completion (about 0.8 vs 1.9 days on average), while accuracy did not improve and in an overlapped condition was slightly worse at higher pay [@heerCrowdsourcingGraphicalPerception2010a]. Payment mainly changes throughput, not carefulness.

- **The Principle:** Incentives affect participation rate more than performance quality
- **The Evidence:** Significant reward effect on completion time; minimal/negative effect on accuracy in overlapped Experiment 3 conditions [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Finish a perception study quickly (e.g., iterative design testing)
- **Data Type:** Any MTurk-hosted visualization judgment task
- **Audience:** Researchers managing study timelines

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot ethically pay too little given task duration.
- **Reason:** Compensation should also reflect fairness; Heer & Bostock note their own pay misestimation [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher direct study cost.
- **The Risk:** Faster completions may slightly reduce care (small accuracy drop observed) [@heerCrowdsourcingGraphicalPerception2010a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Raising pay expecting it to “fix” noisy or misunderstood tasks.
- **Why it fails:** Confusion is better addressed with qualification and verifiable checks, not compensation [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Completion curves flatten at low pay and steepen at higher pay (as in their HIT completion plots).
- **The Test:** Run a small A/B pilot with two reward levels and compare time-to-fill vs error/outlier rates [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase reward to reach your required completion deadline.
- **Best Fix:** Pair adequate pay with qualification + verifiable checks so speed gains don’t compromise data validity [@heerCrowdsourcingGraphicalPerception2010a].

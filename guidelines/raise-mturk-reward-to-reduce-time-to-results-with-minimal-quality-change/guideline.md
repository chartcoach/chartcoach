---
id: raise-mturk-reward-to-reduce-time-to-results-with-minimal-quality-change
title: Raise crowdsourcing reward to reduce time-to-results with minimal quality change
bibliography: references.bib
description: Higher per-task rewards substantially sped completion while leaving result
  quality largely unchanged in tested studies.
labels:
- chart:research
- task:evaluate
- visual:general
- impact:efficiency
- data:quantitative
- audience:researcher
- custom:method-crowdsourcing
---

## Increase per-task payment when you need faster completion, not higher accuracy <!-- role: advice -->

If you need results sooner, raise the reward per task to increase completion speed. Do not expect higher pay to meaningfully improve response quality.

## Why reward affects throughput more than correctness <!-- role: reason -->

Higher rewards attract more workers and increase how quickly tasks are picked up, but accuracy is primarily constrained by task clarity and participant capability rather than marginal pay.

**Mechanism:** Payment shifts participation rate and task selection behavior more than it shifts carefulness on short, well-specified tasks.

**Evidence:** Across multiple experiments, higher-reward tasks completed faster (lower elapsed time to completion), while accuracy changed little and sometimes slightly worsened; overlapping conditions in two runs showed faster completion at higher reward with a small decrease in accuracy that did not change design implications [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** Naming and presentation errors can also affect completion rates, independent of reward.

## When this applies <!-- role: context -->

- **User Goal:** Complete a crowdsourced perception study on a deadline.
- **Task:** Microtasks with clear instructions and objective or near-objective outputs.
- **Data:** Many independent assignments needed across conditions.
- **Chart Setting:** Market-based crowdsourcing platforms.
- **Audience:** Remote workers choosing among available tasks.
- **Success Criterion:** Faster study completion without compromising validity.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your budget is fixed and the schedule is flexible. **Why:** Higher pay primarily buys speed, not better data.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Higher monetary cost per response. **Risk:** Overpaying can still fail to improve data if the task is confusing or technically brittle. **Mitigation:** Spend effort on qualification and verifiable checks before increasing pay.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using higher reward as a substitute for clear instructions and validation checks. **Why it fails:** Throughput increases, but the same confusion-driven errors remain.

## Quick tests <!-- role: check -->

**Failure Sign:** Tasks remain uncompleted for long periods despite being correctly set up. **Quick Check:** Increase reward for a small subset of tasks and compare completion slope. **Stronger Test:** Run an overlapped-condition A/B with two reward levels and compare both elapsed time and accuracy distributions.

## What to do instead <!-- role: fix -->

- Add or refine qualification tasks to prevent misunderstanding-driven noise.
- Improve task titles and descriptions to avoid unintended sequencing or discouraging participation.
- Batch related trials only if you can maintain attention and technical stability.
- Use staged pilots to validate the instrument before scaling assignments.

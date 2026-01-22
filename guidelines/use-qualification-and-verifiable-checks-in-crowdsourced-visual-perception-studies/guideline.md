---
id: use-qualification-and-verifiable-checks-in-crowdsourced-visual-perception-studies
title: Use a qualification task and verifiable checks in crowdsourced visualization
  perception studies
bibliography: references.bib
description: Qualification tasks and verifiable questions substantially reduced unusable
  responses in crowdsourced perception experiments.
labels:
- chart:research
- task:evaluate
- visual:general
- impact:validity
- data:quantitative
- audience:researcher
- custom:method-crowdsourcing
---

## Add a qualification step and verifiable questions to keep crowdsourced perception data usable <!-- role: advice -->

Before collecting responses, require a short qualification that ensures participants understand the task and can operate any interactive stimulus. Include at least one verifiable check within the task so clearly incorrect work can be identified.

## Why this increases data quality without filtering for ability <!-- role: reason -->

Crowdsourced participants often fail due to misunderstanding or tool incompatibility rather than perceptual limitations; qualification screens for comprehension and technical readiness, while verifiable checks discourage random answering.

**Mechanism:** Early comprehension gating reduces confusion-driven noise, and verifiable checks make “gaming” less attractive than simply doing the task.

**Evidence:** Omitting a qualification step in a pilot proportional-judgment study led to over 10% unusable responses, while the main studies using qualification plus verifiable questions had very low rejection/outlier rates (about 0.75% across experiments) and successfully replicated established perception results [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** Qualification was designed to confirm understanding, not to filter out participants with lower perceptual accuracy.

## When this applies <!-- role: context -->

- **User Goal:** Collect reliable perception judgments from a crowd platform.
- **Task:** Any visualization reading task where misunderstanding can produce invalid responses.
- **Data:** Experimental responses where outliers can contaminate estimates.
- **Chart Setting:** Crowdsourcing platforms with minimal experimental control.
- **Audience:** Remote participants with unknown attention and device constraints.
- **Success Criterion:** Low unusable-response rate and replicable effects.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The study cannot include any ground-truth or verifiable component. **Why:** You lose the ability to distinguish misunderstanding or random responses from legitimate variation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Extra participant time and additional study-building effort. **Risk:** An overly strict qualification can reduce recruitment speed. **Mitigation:** Keep qualification short and focused on comprehension and technical capability.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using qualification questions that test the same perceptual ability being measured. **Why it fails:** It can bias the sample by filtering out the very variability the study aims to measure.

## Quick tests <!-- role: check -->

**Failure Sign:** High rates of nonsensical answers or missing submissions. **Quick Check:** Run a small pilot without changing design variables and measure unusable response rate; if it exceeds a few percent, add or refine qualification and checks. **Stronger Test:** Track error distributions and verify that replicated effects match known baselines.

## What to do instead <!-- role: fix -->

- Convert a small number of practice trials into multiple-choice checks with obviously wrong distractors.
- Add a simple operational test for interactive tasks (e.g., set a control to minimum/maximum).
- Embed at least one sanity-check question with an objectively verifiable answer.
- Pilot with a small assignment count, then scale up after verifying response validity.

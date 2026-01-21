---
id: test-type1-vs-type2-with-time-pressure
title: Test Visualizations Under Time Pressure to Reveal Type-1 Biases
bibliography: references.bib
description: Evaluate designs with fast response limits to detect when automatic processing
  drives different decisions than deliberation.
labels:
- chart:general
- task:evaluate
- visual:encoding
- impact:validation
- data:general
- audience:general
- method:time-pressure
- mechanism:dual-process
---

## The Rule <!-- role: advice -->

When validating a visualization, test it both with fast decision time limits and with ample time.

## The Logic <!-- role: reason -->

The review frames visualization decision making as dual-process: time pressure encourages Type 1 (fast, automatic) responses, while more time allows Type 2 (working-memory-intensive) processing. Studies reviewed show visualization effects can appear under fast decisions and diminish when users have time to deliberate, so time conditions reveal different failure modes [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Real-world decisions that may be rushed (hazards, emergency response, quick screening)
- **Data Type:** Uncertainty/hazard maps and other high-stakes displays
- **Audience:** Non-experts and professionals operating under time constraints

## When to Break It <!-- role: exceptions -->

- **Scenario:** The real-world use case always involves slow, careful review (no time pressure)
- **Reason:** Then the fast-condition results may overstate problems unlikely in practice [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More evaluation effort and study complexity
- **The Risk:** Over-optimizing for speed could reduce performance for careful analytic tasks [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Only testing comprehension in untimed lab conditions
- **Why it fails:** You may miss Type 1 attention-and-bias effects that dominate in real time-pressured use [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Decisions change qualitatively between fast and slow conditions.
- **The Test:** Compare error patterns under short vs long time limits; divergent patterns indicate different processing routes are being triggered [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust salience and remove misleading cues that dominate in fast viewing.
- **Best Fix:** Iterate the design until it supports correct judgments under both fast (Type 1) and deliberate (Type 2) conditions appropriate to the use case [@padillaDecisionMakingVisualizations2018].

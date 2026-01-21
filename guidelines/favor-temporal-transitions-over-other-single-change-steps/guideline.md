---
id: favor-temporal-transitions-over-other-single-change-steps
title: Favor Temporal Transitions When Costs Are Equal
bibliography: references.bib
description: If multiple next slides are equally similar, prefer a time step (temporal
  transition) as the next move.
labels:
- task:sequence
- data:temporal
- impact:preference
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

If you have multiple candidate next visualizations with equal transformation cost (one-attribute change), choose a temporal transition over dimension, measure, or granularity transitions.

## The Logic <!-- role: reason -->

When cost was held constant, participants preferred temporal transitions over other implicit transition types, indicating time-based steps are especially acceptable as “next” moves in a linear narrative [@hullmanDeeperUnderstandingSequence2013].

- **The Principle:** Type weighting for transitions beyond cost
- **The Evidence:** In cost-constant trials, temporal transitions were preferred over granularity, dimension, and measure transitions (all p\<0.01) [@hullmanDeeperUnderstandingSequence2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose among equally “simple” next steps
- **Data Type:** Data with a recognized time variable (years, dates, periods)
- **Audience:** General audiences consuming linear slideshows/videos

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your story’s next point requires holding time constant to compare groups (dimension walk) or perspectives (measure walk).
- **Reason:** The paper’s finding is about average preference for next-step selection, not about the analytical necessity of a particular comparison [@hullmanDeeperUnderstandingSequence2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may delay introducing new variables or levels of detail.
- **The Risk:** Overuse can turn the narrative into a “timeline” even when time isn’t central.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching measures or drilling into detail even when a clear next time step exists.
- **Why it fails:** Users in the paper consistently preferred temporal transitions over those alternatives at equal cost [@hullmanDeeperUnderstandingSequence2013].

## How to Check <!-- role: check -->

- **Visual Sign:** The sequence feels like it “zig-zags” across topics despite having a natural time order.
- **The Test:** If two candidate next slides both differ on exactly one attribute, and one is a time step, pick the time step.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder slides to align adjacent steps by time.
- **Best Fix:** Add time as an explicit sequencing backbone, inserting non-temporal transitions only when needed for the narrative point [@hullmanDeeperUnderstandingSequence2013].

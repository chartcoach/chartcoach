---
id: avoid-animation-as-a-substitute-for-simultaneous-facet-visibility-in-analytic-tasks
title: Avoid animated substitution when users must analyze trends or compare multiple
  facets; keep facets concurrently visible
bibliography: references.bib
description: Do not rely on animation to swap facets over time for analytic tasks
  because it increases memory load and can reduce trend accuracy.
labels:
- task:compare
- task:analyze
- visual:time
- impact:accuracy
- data:temporal
- audience:novice
- complexity:intermediate
- domain:health
---

## Keep analytic comparisons concurrent instead of temporal <!-- role: advice -->

When users need analytic comparisons across facets or time, show the relevant facets at the same time rather than using animation that replaces one state with another.

## Why animated substitution harms analytic sensemaking <!-- role: reason -->

Animated views are temporal and substitutive, so information disappears and users must rely on short-term memory to compare states, which can overload cognition and degrade trend understanding as complexity grows.

**Mechanism:** When representations replace each other, comparisons become memory-based instead of perception-based, increasing cognitive load and error risk.

**Evidence:** Animated visualizations that substitute states require users to recall previous views and can overload short-term memory; with increasing data, this can lead to inaccurate understanding of trends [@olaSimpleChartsDesign2016]. Big health data tasks often require exploring multiple facets simultaneously, which is poorly served by substitutive animation [@olaSimpleChartsDesign2016].

**Notes:** Animation may still fit narrative communication, but this guideline targets analytic exploration.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Detect changes, compare trends, and relate multiple variables (e.g., causes vs risks across years and regions).
- **Task:** Trend analysis, hypothesis testing, multi-facet comparison.
- **Data:** Many time points and/or multiple facets that must be compared directly.
- **Chart Setting:** Exploratory analytic tools (not linear storytelling).
- **Audience:** Analysts and decision-makers who need accurate comparisons.
- **Success Criterion:** Users can compare states perceptually without remembering prior frames.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is narrative presentation of a single storyline with limited comparison demands. **Why:** Temporally staged views can support storytelling even if they are less suited to analytic comparison [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More screen space may be needed to show multiple facets concurrently. **Risk:** Showing everything at once can create clutter. **Mitigation:** Use integrated multifaceted structures and interaction to reveal detail without substituting away key context.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Animating between facets (or years) to “save space.” **Why it fails:** The user must remember prior states to compare, which undermines accurate trend judgments as complexity increases [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users pause, replay, or scrub repeatedly to compare moments. **Quick Check:** If answering a comparison requires watching at least two frames and remembering the first, it is substitutive. **Stronger Test:** Ask users to identify which of two entities changed more; if they need replays, the design is memory-bound.

## What to do instead <!-- role: fix -->

- Use static concurrent encodings that place time or facets in a shared frame (e.g., aligned small multiples or integrated structures).
- Distribute facets through space with explicit structural alignment when simultaneous viewing is required.
- Use interaction for filtering/highlighting while keeping comparison context visible.
- Encode temporal change with links or continuous forms when the task is to track change across time.

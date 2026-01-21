---
id: use-dual-task-to-measure-working-memory-demand
title: Use Dual-Task Testing to Measure Working-Memory Demand
bibliography: references.bib
description: Add a secondary task during evaluation to estimate whether a visualization
  requires Type-2 working memory resources.
labels:
- chart:general
- task:evaluate
- visual:encoding
- impact:validation
- data:general
- audience:general
- method:dual-task
- mechanism:type-2
---

## The Rule <!-- role: advice -->

When comparing visualization designs, use a dual-task experiment to detect whether accurate use depends on working memory.

## The Logic <!-- role: reason -->

The review argues Type 2 processing is defined by significant working memory demands, and proposes dual-task paradigms as a way to test whether visualization decisions require working memory: performance drops under a working-memory-loading secondary task indicate Type 2 dependence [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine whether a design supports intuitive (low-load) decisions vs effortful reasoning
- **Data Type:** Any visualization where you suspect mental transformations or complex inference steps
- **Audience:** Especially important when users differ in working memory capacity

## When to Break It <!-- role: exceptions -->

- **Scenario:** When you cannot run behavioral tests (e.g., fixed product constraints)
- **Reason:** Without experimentation, you cannot cleanly attribute performance to working memory demands as proposed [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex study design and participant time
- **The Risk:** Poorly chosen secondary tasks can confound results (e.g., loading the wrong modality) [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Inferring “it’s Type 2” solely because a task feels hard
- **Why it fails:** Difficulty can come from perceptual issues, salience traps, or schema mismatch; dual-task cost is a more direct indicator of working-memory reliance [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Accuracy and/or response time for the primary visualization task worsens when a demanding secondary task is added.
- **The Test:** Compare baseline vs dual-task performance; meaningful degradation suggests working-memory dependence [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove unnecessary transformations (simplify encoding, reduce mismatches).
- **Best Fix:** Redesign the visualization to increase cognitive fit so more of the decision can be made via perceptual (Type 1) processes rather than working-memory-heavy computation [@padillaDecisionMakingVisualizations2018].

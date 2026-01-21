---
id: expect-preference-to-drop-when-you-maximize-discriminability
title: Expect Preference to Drop When You Maximize Discriminability
bibliography: references.bib
description: Recognize and manage the predictable inverse relationship between discriminability
  scores and preference ratings.
labels:
- chart:categorical
- task:tradeoff
- visual:color
- impact:decision-making
- data:categorical
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When you increase discriminability (Perceptual Distance or Name Difference), plan for average aesthetic preference to decrease—then choose a deliberate compromise.

## The Logic <!-- role: reason -->

Across human-subject evaluations in the paper, higher discriminability scores correlated with better discrimination performance but lower preference ratings, while higher Pair Preference correlated with higher preference ratings but worse discrimination performance—demonstrating a consistent inverse relationship you must manage rather than ignore [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Inverse correlation between discriminability and preference
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide how to tune a palette for either performance (accuracy) or appeal (liking)
- **Data Type:** Categorical palettes, especially 3-, 5-, and 8-color sets tested in the paper
- **Audience:** Designers iterating on palette choices; teams negotiating design goals

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are using a palette already validated as both discriminable and preferable against benchmarks.
- **Reason:** Some palettes can sit on a favorable point of the tradeoff and don’t require further aggressive tuning [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** A single “best” palette rarely exists; you must decide priorities.
- **The Risk:** If you tune blindly for one metric, you may harm the other enough to reduce overall effectiveness [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating preference complaints as “purely subjective” and ignoring them after maximizing distance.
- **Why it fails:** The paper shows systematic, measurable preference effects tied to palette properties [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Palettes that are very contrasty and varied are described as harsh or unattractive; palettes that look cohesive cause category confusions.
- **The Test:** Compare a “low-error” tuned palette versus a “preferable” tuned palette and confirm the expected direction (errors vs ratings) holds for your use case [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce emphasis on the metric you over-optimized (e.g., dial back distance slightly if users dislike it).
- **Best Fix:** Generate multiple candidates at different weightings and select based on your task priority, acknowledging the tradeoff explicitly [@gramazioColorgoricalCreatingDiscriminable2017a].

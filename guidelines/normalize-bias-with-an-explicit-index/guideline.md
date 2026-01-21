---
id: normalize-bias-with-an-explicit-index
title: Normalize Bias Using a Bounded Index
bibliography: references.bib
description: Express curse-of-knowledge bias as a normalized ratio so magnitudes are
  comparable across items with different scales.
labels:
- chart:dot-plot
- task:compare
- visual:position
- impact:comparability
- data:categorical
- audience:expert
- domain:behavioral-economics
---

## The Rule <!-- role: advice -->

When comparing bias across multiple items with different numeric scales, convert outcomes to a normalized bias index defined relative to the unbiased and informed endpoints.

## The Logic <!-- role: reason -->

In the paper, different companies have different earnings scales, so raw deviations are not comparable. A normalized index (interpretable as w) measures bias as the fraction of the distance from E(X|I0) toward E(X|I1), enabling across-item comparison.

- **The Principle:** Scale-free bias measurement using a ratio of distances
- **The Evidence:** [@camererCurseKnowledgeEconomic1989]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing degree of bias across conditions, companies, tasks, or time
- **Data Type:** Multi-item outcomes where each item has its own natural scale (e.g., different firms, products, markets)
- **Audience:** Analysts reporting aggregate bias patterns

## When to Break It <!-- role: exceptions -->

- **Scenario:** The denominator (E(X|I1) − E(X|I0)) is near zero or unstable.
- **Reason:** The ratio becomes noisy or undefined, obscuring interpretation.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less intuitive than raw units (e.g., dollars or earnings per share).
- **The Risk:** Readers may forget what the index is anchored to unless you label endpoints.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Comparing raw “distance from unbiased” across items with different scales.
- **Why it fails:** Larger-scale items mechanically appear “more biased” even if the proportional bias is identical [@camererCurseKnowledgeEconomic1989].

## How to Check <!-- role: check -->

- **Visual Sign:** Items with larger numeric scales dominate the apparent variation in bias.
- **The Test:** Recompute bias in proportional terms; if the ranking changes substantially, raw units were misleading.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Plot the normalized index (w) for each item instead of raw deviations.
- **Best Fix:** Plot both: the normalized index for comparison and a separate view (or tooltip/table) with raw-unit values for interpretability.

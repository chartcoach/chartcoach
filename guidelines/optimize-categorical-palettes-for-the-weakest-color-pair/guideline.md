---
id: optimize-categorical-palettes-for-the-weakest-color-pair
title: Optimize categorical palettes for the weakest color pair using a minimum-pair
  criterion
bibliography: references.bib
description: Evaluate a categorical palette by its lowest-scoring color pair so the
  most confusable pair does not determine failure.
labels:
- chart:categorical
- task:validate
- visual:color
- impact:clarity
- data:categorical
- audience:expert
- complexity:intermediate
---

## Use the minimum pairwise score as the palette’s quality criterion <!-- role: advice -->

Evaluate and optimize a categorical palette using the minimum pairwise score across all color pairs (for discriminability and/or preference), so the palette is not limited by one confusable pair.

## Why the minimum-pair criterion matches failure behavior <!-- role: reason -->

In many categorical tasks, users fail when they encounter the single hardest pair to tell apart; using the minimum makes that “weakest link” explicit and prevents strong pairs from hiding a critical failure.

**Mechanism:** Taking the minimum across all palette pairs forces optimization pressure onto the most confusable (or least preferred) pairing, rather than letting averages conceal problematic pairs.

**Evidence:** The palette-generation procedure assigns each candidate color a score based on its minimum pairing with already-picked colors, reflecting the assumption that a palette is only as good as its lowest score [@gramazioColorgoricalCreatingDiscriminable2017a]. The discrimination task in the experiments specifically targeted the lowest and second-lowest perceptual-distance colors as target and distractor, tying behavioral difficulty to the weakest pair [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** This criterion can be applied to multiple scores (perceptual distance, name difference, pair preference).

## When this applies <!-- role: context -->

- **User Goal:** Prevent any pair of categories from becoming a consistent confusion source.
- **Task:** Accurate identification across all categories (not just most).
- **Data:** Categorical with multiple classes where any class may be queried.
- **Chart Setting:** Legends and repeated lookups between legend and marks.
- **Audience:** Users who may encounter any category as a focal target.
- **Success Criterion:** No “bad pair” that drives most errors.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Some categories are intentionally secondary and occasional confusion is acceptable for those pairs. **Why:** The minimum criterion will over-prioritize rare or low-importance pairs.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce overall aesthetic cohesion because you are forced to fix the hardest pair. **Risk:** The palette may become conservative, limiting available colors especially at higher palette sizes. **Mitigation:** Use importance weighting across pairs only if category importance is truly unequal.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Selecting palettes by average distance or “overall vibe.” **Why it fails:** A single low-distance pair can dominate confusion even if the rest are strong.
- **Mistake:** Checking only adjacent legend entries. **Why it fails:** The worst pair can be non-adjacent and still cause confusion.

## Quick tests <!-- role: check -->

**Failure Sign:** One specific pair of categories is repeatedly confused while others are fine. **Quick Check:** Inspect all pairwise differences and identify the minimum pair; if it is low, treat the palette as failing. **Stronger Test:** In a small user test, set target/distractor to the minimum-distance pair and confirm acceptably low error.

## What to do instead <!-- role: fix -->

- Compute all pairwise scores and redesign only the minimum-scoring pair first.
- Re-run palette generation with constraints that increase the minimum score (e.g., increase discriminability weight).
- Split categories across multiple encodings (e.g., position or shape) when the minimum pair cannot be improved within color constraints.
- Reduce the number of categories per view if minimum scores collapse as palette size increases.

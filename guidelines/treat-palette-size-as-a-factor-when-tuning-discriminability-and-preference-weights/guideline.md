---
id: treat-palette-size-as-a-factor-when-tuning-discriminability-and-preference-weights
title: Tune discriminability and preference settings separately for 3-, 5-, and 8-color
  categorical palettes
bibliography: references.bib
description: Adjust palette-generation settings by palette size because size modulates
  discrimination performance and preference behavior.
labels:
- chart:categorical
- task:optimize
- visual:color
- impact:clarity
- data:categorical
- audience:expert
- complexity:intermediate
---

## Adjust palette-generation settings based on the number of colors needed <!-- role: advice -->

Tune discriminability and preference settings separately for 3-, 5-, and 8-color palettes rather than assuming one setting works across palette sizes.

## Why palette size changes how well settings predict outcomes <!-- role: reason -->

As palette size grows, both the probability of a weak pair and the behavioral relationships between pair-based scores and outcomes can change, so the same weighting strategy can behave differently at different sizes.

**Mechanism:** Pairwise score models (distance, naming, preference) may generalize differently as the number of required pairings increases; size can also change task difficulty and observer strategy.

**Evidence:** Discrimination error increased with palette size in the experiments, and palette size interacted with palette set in benchmark comparisons [@gramazioColorgoricalCreatingDiscriminable2017a]. The paper reports that some relationships (e.g., response time correlations and preference behavior) differed across 3-, 5-, and 8-color conditions, suggesting size-dependent effectiveness of pair-based scoring approaches [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** The paper highlights unexpected results for some 5- and 8-color conditions, motivating size-aware tuning.

## When this applies <!-- role: context -->

- **User Goal:** Choose settings that reliably produce usable palettes.
- **Task:** Generate palettes for different category counts across views or products.
- **Data:** Categorical with varying cardinality requirements.
- **Chart Setting:** A system where palette size changes depending on filters or facets.
- **Audience:** Designers or engineers implementing palette generation.
- **Success Criterion:** Stable discriminability and preference at each intended palette size.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You only ever use one fixed palette size across all outputs. **Why:** There is no cross-size generalization need to manage.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More configuration and testing effort. **Risk:** Inconsistent “look” across views if settings diverge too much by size. **Mitigation:** Keep shared constraints (lightness clamp, avoidance regions) constant while tuning weights.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using the same slider/weight setting for all palette sizes. **Why it fails:** The experiments show size-dependent changes in error and in correlations with palette scores.
- **Mistake:** Validating a setting on 3 colors and deploying it for 8. **Why it fails:** The hardest-pair dynamics and predictiveness can shift as size increases.

## Quick tests <!-- role: check -->

**Failure Sign:** A setting that works for small category counts produces confusions at larger counts. **Quick Check:** Test the same setting at 3, 5, and 8 colors and compare the weakest pair and a simple error estimate. **Stronger Test:** Run a small discrimination and preference check at each intended size.

## What to do instead <!-- role: fix -->

- Maintain different preset configurations for common sizes (e.g., 3, 5, 8) aligned with your success criteria.
- Reduce category count per view when the 8-color setting cannot meet an error threshold.
- Use stricter discriminability emphasis at larger sizes where weak pairs are more likely.
- Generate multiple candidates per size and select the one maximizing the minimum criterion relevant to the use case.

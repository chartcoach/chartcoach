---
id: use-vsup-to-allocate-more-value-resolution-when-uncertainty-is-low
title: Use a Value-Suppressing Uncertainty Palette (VSUP) to allocate finer value
  resolution only when uncertainty is low
bibliography: references.bib
description: Budget more distinguishable value encodings to low-uncertainty data and
  progressively suppress value distinctions as uncertainty increases.
labels:
- chart:heatmap
- task:decide
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- uncertainty:explicit
- complexity:advanced
---

## Use VSUP quantization so value distinctions disappear as uncertainty rises <!-- role: advice -->

Use a Value-Suppressing Uncertainty Palette (VSUP) that maps high-uncertainty values to fewer (or a single) visual outputs and reserves more distinct outputs for low-uncertainty values. Ensure the mapping culminates in a common, maximally-uncertain appearance where value is no longer distinguishable.

## Why suppressing value under high uncertainty improves integration <!-- role: reason -->

VSUPs treat perceptual discriminability as a limited budget and spend it where comparisons are most warranted: when uncertainty is low. By intentionally aliasing values under high uncertainty, VSUPs reduce misleading fine-grained comparisons in noisy regions and improve discriminability where uncertainty encoding would otherwise interfere with value decoding.

**Mechanism:** Reducing the number of distinct value encodings at high uncertainty decreases the chance that viewers over-interpret small value differences when marks are already hard to discriminate due to the uncertainty channel.

**Evidence:** In a decision task requiring integration of value and uncertainty, VSUPs shifted choices away from very high-uncertainty regions compared to a standard bivariate map, indicating viewers weighted uncertainty more in their decisions [@correllValueSuppressingUncertaintyPalettes2018]. VSUPs also produced more cautious tradeoffs (accepting higher expected danger to avoid high uncertainty), showing a measurable impact on decision-making strategy [@correllValueSuppressingUncertaintyPalettes2018].

**Notes:** VSUPs are simultaneously a bivariate encoding and an intentional filtering/attenuation of uncertain values.

## When VSUP suppression fits the task <!-- role: context -->

- **User Goal:** Make decisions that appropriately downweight unreliable or noisy estimates.
- **Task:** Choose locations/items balancing expected value against uncertainty; avoid overconfident fine comparisons.
- **Data:** Quantitative value plus a quantitative uncertainty measure (e.g., standard error, margin-of-error ratio), often dense (maps/heatmaps).
- **Chart Setting:** Static bivariate color map where both variables must be read together.
- **Audience:** General audiences who may otherwise discount uncertainty.
- **Success Criterion:** Viewers behave more uncertainty-aware (avoid highly uncertain regions) while still enabling precise comparisons where uncertainty is low.

## When not to suppress value with uncertainty <!-- role: exceptions -->

- **Break it when:** Highly uncertain extreme values must remain distinguishable (e.g., “long tail risk” or black-swan planning). **Why:** VSUP aliasing intentionally removes value resolution in high-uncertainty regions, which can hide consequential extremes.

## Tradeoffs of VSUP suppression <!-- role: costs -->

**Sacrifice:** You lose the ability to distinguish fine value differences in high-uncertainty regions by design. **Risk:** Viewers may interpret suppression as “no data” or may miss patterns that only exist in highly uncertain areas. **Mitigation:** Treat VSUP use as a task-driven choice where downweighting uncertainty is desired.

## Common VSUP implementation failures <!-- role: mistakes -->

- **Mistake:** Using VSUP when the analysis requires increased discrimination among uncertain values. **Why it fails:** The palette intentionally collapses distinctions as uncertainty rises, working against the task.
- **Mistake:** Treating VSUP bin boundaries as statistical significance thresholds. **Why it fails:** Quantization can create sharp visual jumps near boundaries and does not provide guarantees equivalent to hypothesis testing.

## Quick checks for appropriate suppression <!-- role: check -->

**Failure Sign:** Viewers can still “read” fine value differences in the highest-uncertainty regions, or they make confident-seeming choices in those regions. **Quick Check:** Verify that the most uncertain uncertainty bin maps to a single appearance regardless of value. **Stronger Test:** Run a small decision pilot and confirm that choices shift away from the highest-uncertainty regions relative to a standard bivariate map.

## What to do instead of VSUP suppression <!-- role: fix -->

- Use a standard bivariate quantization that keeps value resolution constant across uncertainty when high-uncertainty value differences must remain visible.
- Use an explicit encoding that combines value and uncertainty into a single derived quantity when the task permits a single score rather than two-variable reasoning.
- Add interaction to reveal exact values and uncertainty on demand when suppression would remove needed detail.
- Reframe the task to separately analyze uncertainty patterns before making value comparisons if uncertainty structure itself is the primary analytic target.

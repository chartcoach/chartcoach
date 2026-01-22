---
id: predict-and-control-preference-with-pair-preference-model
title: Increase categorical palette liking by weighting pair preference (cool hues,
  lightness contrast, hue similarity)
bibliography: references.bib
description: Use a pair-preference objective to bias categorical palettes toward combinations
  people like on average.
labels:
- chart:categorical
- task:choose
- visual:color
- impact:appeal
- data:categorical
- audience:novice
- complexity:advanced
---

## Weight pair preference to increase average palette preference <!-- role: advice -->

When audience acceptance matters, weight a pair-preference objective that favors cooler colors, greater lightness contrast, and smaller hue differences between paired colors.

## Why pair-preference weighting increases liking <!-- role: reason -->

A preference objective steers palette selection toward color relationships that people tend to like, which can improve perceived quality even when discriminability objectives are also present.

**Mechanism:** The pair-preference model used in the paper increases predicted preference with color coolness and lightness contrast and decreases it with hue difference; upweighting it biases sampling toward those relationships.

**Evidence:** Preference ratings increased as Pair Preference palette scores increased, and increasing the relative weight on the Pair Preference slider predicted higher preference ratings in regression analyses [@gramazioColorgoricalCreatingDiscriminable2017a]. Upweighting Pair Preference also tended to worsen discrimination performance, demonstrating the tradeoff that must be managed when optimizing for liking [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** The model is pair-based, and the paper reports that palette size can affect how well pair-based predictions generalize.

## When this applies <!-- role: context -->

- **User Goal:** Produce a palette that viewers like while still being usable.
- **Task:** Choose among candidate palettes for a categorical visualization.
- **Data:** Categorical data where colors are arbitrary identifiers (not semantically fixed).
- **Chart Setting:** Presentational or public-facing visualizations where aesthetic judgment matters.
- **Audience:** General viewers; stakeholders sensitive to “professional look.”
- **Success Criterion:** Higher preference ratings without unacceptable increases in confusion.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Misidentifying categories has high cost (e.g., operational decisions). **Why:** Increasing pair preference can reduce discriminability and increase errors.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some discriminability is typically traded away for higher liking. **Risk:** Palettes may become too hue-similar, increasing confusion in legend lookups. **Mitigation:** Keep a nontrivial discriminability objective active while weighting preference.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Maximizing pair preference while ignoring discriminability outcomes. **Why it fails:** The experiments show error rates can rise as Pair Preference increases.
- **Mistake:** Assuming the same preference behavior across all palette sizes. **Why it fails:** The paper reports size-related differences and potential breakdowns in pair-based generalization.

## Quick tests <!-- role: check -->

**Failure Sign:** The palette is liked but users confuse two similarly hued categories. **Quick Check:** Look for pairs with very similar hue and verify they remain distinguishable in the intended mark size and context. **Stronger Test:** Collect both preference ratings and a simple discrimination error measure on representative stimuli.

## What to do instead <!-- role: fix -->

- Increase lightness contrast within similarly hued colors if you are prioritizing preference but need separation.
- Reduce the number of categories so you can keep hue similarity without severe confusions.
- Generate multiple palettes at different preference weights and select the one that meets an error threshold.
- If preference-driven palettes consistently cause errors, switch to a more discriminability-weighted setting and use other design elements to improve appearance (layout, spacing, annotation).

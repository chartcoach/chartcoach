---
id: prefer-discrete-bivariate-color-maps-over-continuous-for-value-uncertainty-identification
title: "Discretize Bivariate Color Maps for Value\u2013Uncertainty Reading"
bibliography: references.bib
description: Use discrete bins rather than continuous bivariate gradients to improve
  identification accuracy for combined value and uncertainty.
labels:
- chart:heatmap
- chart:choropleth
- task:identify
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- encoding:discrete
---

## The Rule <!-- role: advice -->

For bivariate color encodings of value and uncertainty, use a discrete (binned) palette rather than a continuous bivariate gradient when users must identify specific (value, uncertainty) combinations.

## The Logic <!-- role: reason -->

Continuous bivariate color ramps demand precise color estimation and matching in the presence of channel interference, increasing perceptual decoding error. In the paper’s identification experiment, discrete bivariate maps outperformed continuous ones (63% vs. 47% accuracy) [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Bound perceptual decoding error by limiting outputs to a small, distinguishable set.
- **The Evidence:** Significant effect of discretization on identification accuracy [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Use a bivariate legend to find/verify specific combinations of value and uncertainty in a grid/map.
- **Data Type:** Quantitative value + quantitative uncertainty encoded via color channels.
- **Audience:** Non-expert or mixed audiences performing basic read-off tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly need smooth, continuous appearance and accept lower accuracy in exact identification.
- **Reason:** Discretization introduces quantization; the paper frames this as a tradeoff (quantization vs perceptual error) [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fine-grained numeric fidelity (within-bin variation is hidden).
- **The Risk:** Bin boundaries can create apparent jumps; values near boundaries may look more different than they are [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a continuous bivariate gradient to “avoid quantization bias” in tasks requiring exact lookup.
- **Why it fails:** The perceptual error of estimating values from continuous bivariate color is high, reducing task accuracy [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend is a smooth 2D gradient and users struggle to match colors to exact target pairs.
- **The Test:** Run a quick internal test: ask someone to identify a target (value, uncertainty) cell using the legend; frequent mismatches indicate continuous encoding is too demanding.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Quantize the bivariate scale into a small grid of discrete outputs.
- **Best Fix:** Use a discrete scheme designed for uncertainty integration (e.g., VSUP) so binning aligns with uncertainty-driven discriminability limits [@correllValueSuppressingUncertaintyPalettes2018].

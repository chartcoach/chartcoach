---
id: prefer-discrete-bivariate-color-bins-over-continuous-for-value-uncertainty-identification
title: Use discrete binned bivariate color scales (not continuous) for value-plus-uncertainty
  identification
bibliography: references.bib
description: Quantize bivariate color maps into a small set of categories to reduce
  perceptual estimation error in decoding value and uncertainty.
labels:
- chart:heatmap
- task:identify
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- uncertainty:explicit
- encoding:discrete
---

## Use discrete binned outputs for bivariate value-and-uncertainty color maps <!-- role: advice -->

Use a discrete (quantized) set of bivariate colors when viewers must identify specific value–uncertainty combinations from a legend. Keep the number of categories small enough that the legend is learnable.

## Why binning beats continuous bivariate estimation <!-- role: reason -->

Continuous bivariate color requires precise color matching under perceptual noise and channel interference, which increases decoding error. Discrete bins bound the decoding problem to category recognition rather than fine-grained estimation.

**Mechanism:** Quantization trades unbounded perceptual estimation error for bounded categorization, improving reliability in legend-based lookup tasks.

**Evidence:** In a bivariate identification task, discrete bivariate maps substantially outperformed continuous bivariate maps in accuracy (63% vs. 47%) [@correllValueSuppressingUncertaintyPalettes2018]. This pattern held across discrete variants (including VSUP and standard quantization), indicating the key benefit was discretization for the identification task [@correllValueSuppressingUncertaintyPalettes2018].

**Notes:** This guideline targets identification/lookup performance rather than nuanced continuous reading.

## When discrete bivariate bins are most useful <!-- role: context -->

- **User Goal:** Look up or confirm value and uncertainty categories from a legend.
- **Task:** Identify regions matching a target value–uncertainty pair.
- **Data:** Continuous quantitative value and uncertainty that can be reasonably grouped into bins.
- **Chart Setting:** Bivariate color map with a legend; static presentation or quick scanning.
- **Audience:** General audiences or time-constrained readers.
- **Success Criterion:** Higher accuracy in legend-driven decoding.

## When not to discretize bivariate color <!-- role: exceptions -->

**Break it when:** The task requires reading fine continuous gradients rather than categorizing, and small quantitative differences must remain visible. **Why:** Binning introduces quantization error that can hide small changes.

## Tradeoffs of discretization <!-- role: costs -->

**Sacrifice:** You introduce quantization error and boundary artifacts. **Risk:** Values near bin boundaries may look more different than they are. **Mitigation:** Treat bins as categories for reading, not as precise numeric judgments.

## Common discretization mistakes <!-- role: mistakes -->

- **Mistake:** Using too many discrete bivariate categories. **Why it fails:** The legend becomes hard to learn and colors become less distinguishable.
- **Mistake:** Interpreting bin membership as exact numeric equality. **Why it fails:** The display encodes ranges, not precise values.

## Quick checks for discretized bivariate scales <!-- role: check -->

**Failure Sign:** Users hesitate and repeatedly compare legend swatches to the map for single-cell lookups. **Quick Check:** Ask a colleague to identify several target pairs using the legend; frequent near-misses indicate bins or colors are too fine. **Stronger Test:** Run a short identification study and compare accuracy against a continuous alternative.

## What to do instead of discrete bivariate bins <!-- role: fix -->

- Use explicit encoding that combines value and uncertainty into one displayed variable when a single score is sufficient.
- Add interaction that reveals exact numeric value and uncertainty on hover when continuous reading is needed.
- Reduce the problem to a smaller set of decision-relevant categories (e.g., acceptable vs. unacceptable uncertainty) if fine binning is not interpretable.
- Use separate analyses or views for continuous inspection after an initial discrete overview supports reliable lookup.

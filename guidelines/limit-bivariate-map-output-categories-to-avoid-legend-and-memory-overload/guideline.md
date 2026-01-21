---
id: limit-bivariate-map-output-categories-to-avoid-legend-and-memory-overload
title: Keep Bivariate Map Outputs to a Small, Memorable Set
bibliography: references.bib
description: Constrain the number of distinct bivariate outputs (e.g., colors) to
  keep legends usable and interpretation feasible.
labels:
- chart:heatmap
- chart:choropleth
- task:identify
- visual:color
- impact:usability
- impact:clarity
- data:quantitative
- audience:general
- design:legend
---

## The Rule <!-- role: advice -->

Constrain bivariate maps to a limited number of distinct output categories, and design your VSUP tree depth/branching to stay within that budget.

## The Logic <!-- role: reason -->

Bivariate maps are hard to interpret and their legends are hard to memorize; practical bivariate maps therefore often use a small grid of outputs. The paper cites work suggesting no more than 16 distinct outputs for bivariate maps, and uses this constraint to motivate tree depth choices (e.g., binary tree depth 4 → 15 outputs) [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Limit cognitive and perceptual load by bounding the legend’s complexity.
- **The Evidence:** The paper discusses practical limits on bivariate outputs and explicitly references the “no more than 16” guideline to bound VSUP tree depth [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Use a legend to decode bivariate encodings reliably.
- **Data Type:** Any bivariate map where value and uncertainty are co-encoded (especially via color).
- **Audience:** General audiences or any setting with quick, repeated lookup.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A specialized expert audience with time/training and tooling to interactively query exact values.
- **Reason:** The paper’s constraint is motivated by memorability and practical interpretability; interactive aids may change that tradeoff (though the paper centers on static charts) [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Precision: fewer outputs mean more quantization.
- **The Risk:** Over-binning can hide meaningful variation unless bins are chosen with care [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more and more bivariate bins to “show all the detail.”
- **Why it fails:** Legends become harder to learn and colors harder to distinguish, undermining the goal of accurate decoding [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend looks dense or requires careful, slow inspection to differentiate neighboring bins.
- **The Test:** Count the distinct outputs; if it exceeds a small matrix-scale set, your map likely exceeds practical interpretability in the paper’s framing [@correllValueSuppressingUncertaintyPalettes2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of bins in either value or uncertainty.
- **Best Fix:** Use VSUP budgeting: keep few outputs overall while allocating more of them to low-uncertainty regions and fewer to high-uncertainty regions [@correllValueSuppressingUncertaintyPalettes2018].

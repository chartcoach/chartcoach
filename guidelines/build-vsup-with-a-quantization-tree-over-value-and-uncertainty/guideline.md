---
id: build-vsup-with-a-quantization-tree-over-value-and-uncertainty
title: Quantize Value and Uncertainty with a VSUP Tree
bibliography: references.bib
description: Construct VSUPs using a quantization tree that branches by value as uncertainty
  decreases, with a single root for highest uncertainty.
labels:
- chart:heatmap
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- impact:legend-design
- data:quantitative
- audience:designer
- technique:vsup
---

## The Rule <!-- role: advice -->

Implement VSUPs using a quantization tree: quantize uncertainty into layers, and within each lower-uncertainty layer, split the value domain into more bins (children), with the highest-uncertainty layer mapping all values to one root output.

## The Logic <!-- role: reason -->

A tree structure makes the “value suppression” explicit and controllable: uncertainty determines how many value distinctions are allowed. This produces predictable aliasing at high uncertainty and increasing value resolution at low uncertainty, aligning available mark types with decision relevance and perceptual limits [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Controlled, hierarchical quantization to manage limited output categories.
- **The Evidence:** The paper defines VSUPs as a quantization tree with a root for high uncertainty and branching leaves as uncertainty decreases; their example tree (branching factor 2, depth 4) yields 15 outputs [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Read value and uncertainty together without requiring users to decode two independent legends.
- **Data Type:** Any bivariate mapping of (value, uncertainty) where the outputs must be limited (e.g., practical legend size).
- **Audience:** Visualization designers implementing uncertainty-aware color encodings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need continuous readout of both value and uncertainty without bin boundaries.
- **Reason:** VSUPs rely on discrete bins; boundaries can create discontinuities in appearance [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Smoothness/continuity in appearance; exact numeric decoding.
- **The Risk:** Values near bin boundaries can appear more different than their actual numeric difference because of quantization [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many bins to “recover precision.”
- **Why it fails:** Too many outputs reduces memorability and increases legend complexity; bivariate maps are practically constrained [@correllValueSuppressingUncertaintyPalettes2018].
- **The Wrong Fix:** Using non-explicit perceptual fading as a stand-in for hierarchical binning.
- **Why it fails:** You lose guarantees about which values alias together and how many distinguishable categories remain [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend shows a full grid of value categories at all uncertainty levels.
- **The Test:** Count distinct value categories available at high uncertainty vs. low uncertainty—if they’re equal, you don’t have a VSUP tree behavior.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Collapse the highest-uncertainty bins to a single output and progressively merge value categories as uncertainty rises.
- **Best Fix:** Define uncertainty “layers” and a branching factor for value splits per layer (tree depth/branching), then generate the palette from that tree [@correllValueSuppressingUncertaintyPalettes2018].

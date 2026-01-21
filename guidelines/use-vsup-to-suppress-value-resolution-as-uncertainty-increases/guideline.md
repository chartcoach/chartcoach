---
id: use-vsup-to-suppress-value-resolution-as-uncertainty-increases
title: Suppress Value Resolution as Uncertainty Increases
bibliography: references.bib
description: Use Value-Suppressing Uncertainty Palettes to intentionally alias values
  at high uncertainty and preserve discriminability at low uncertainty.
labels:
- chart:heatmap
- chart:choropleth
- chart:treemap
- task:decide
- task:compare
- visual:color
- visual:lightness
- visual:saturation
- impact:clarity
- impact:uncertainty-awareness
- data:spatial
- data:quantitative
- audience:general
- technique:vsup
---

## The Rule <!-- role: advice -->

Encode (value, uncertainty) with a Value-Suppressing Uncertainty Palette: as uncertainty increases, map more values to fewer (eventually one) visual outputs.

## The Logic <!-- role: reason -->

VSUPs assume a limited “budget” of perceptual discriminability and prioritize distinguishing reliable values over unreliable ones. They explicitly allocate more output categories to low-uncertainty regions and fewer to high-uncertainty regions, which both improves discrimination where it matters and discourages overconfident reading where it doesn’t [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Non-uniform allocation of perceptual categories (“budgeting”) to emphasize more decision-relevant regions.
- **The Evidence:** VSUPs increased separation among the closest colors compared to a standard bivariate map in their example, and shifted decision behavior away from very high-uncertainty regions in the prediction study [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Make uncertainty hard to ignore when comparing or choosing based on a map-like display.
- **Data Type:** Quantitative value with an associated quantitative uncertainty/quality measure.
- **Audience:** General audiences or mixed expertise, especially for decision-making under uncertainty.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must preserve distinctions among highly uncertain values (e.g., “black swan”/long-tail risk analysis).
- **Reason:** VSUPs intentionally collapse uncertain values, which can hide differences you explicitly need to see [@correllValueSuppressingUncertaintyPalettes2018].
- **Scenario:** Tasks that require *more* discriminability when uncertainty is high (e.g., filtering outliers driven by uncertainty).
- **Reason:** VSUPs reduce resolution precisely in high-uncertainty regions [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fidelity among high-uncertainty values (they may become indistinguishable).
- **The Risk:** Viewers may interpret suppressed areas as “not worth analyzing” even when uncertain areas still contain relevant signals [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a standard bivariate grid with uniform bins while also encoding uncertainty via channels that reduce discriminability (e.g., lightness/saturation), causing hard-to-parse interference.
- **Why it fails:** It spends the same number of categories on unreliable regions where viewers cannot reliably distinguish them anyway [@correllValueSuppressingUncertaintyPalettes2018].
- **The Wrong Fix:** Treating ad hoc “fading to transparent/gray” as a VSUP without explicit binning.
- **Why it fails:** The aliasing becomes accidental and provides no guarantees about discriminability or interpretability [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** High-uncertainty regions still show many distinct value colors, inviting fine-grained comparisons where uncertainty is high.
- **The Test:** Pick two cells/regions with very high uncertainty but different values—if they look clearly different, you are not suppressing value as uncertainty rises.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of value bins available at higher uncertainty levels (merge categories).
- **Best Fix:** Implement a VSUP quantization tree so uncertainty layers progressively branch into more value leaves only as uncertainty decreases [@correllValueSuppressingUncertaintyPalettes2018].

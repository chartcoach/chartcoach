---
id: assess-colormap-local-global-discriminative-power-with-speed
title: Assess Colormap Discriminative Power with Average Speed
bibliography: references.bib
description: "Evaluate a continuous colormap\u2019s ability to separate values by\
  \ measuring its average speed (locally or globally) in a perceptual color-difference\
  \ metric."
labels:
- chart:colormap
- task:evaluate
- visual:color
- impact:clarity
- data:quantitative
- audience:expert
- scope:continuous-colormap
---

## The Rule <!-- role: advice -->

Assess a continuous colormap’s discriminative power using average speed: use **average local speed** for local discriminative power, and **average global speed** for global discriminative power.

## The Logic <!-- role: reason -->

- **The Principle:** Discriminative power corresponds to how large perceived color differences are along the colormap, quantified as average speed derived from pairwise color distances in a perceptual metric.
- **The Evidence:** The theoretical framework defines local discriminative power via average local speed and global discriminative power via average global speed [@bujackGoodBadUgly2018], and this knowledge is collated for visualization recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing (discriminating) differences encoded by a continuous color scale.
- **Data Type:** Quantitative values mapped to a continuous colormap.
- **Audience:** Designers/engineers evaluating or selecting colormaps (e.g., for automated recommendation).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not using a continuous colormap (e.g., categorical/discrete palettes).
- **Reason:** The measures are defined for continuous colormaps and depend on continuous sampling along the map [@bujackGoodBadUgly2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires computing distances under a chosen color-difference metric and sampling the colormap.
- **The Risk:** Results depend on the metric choice and sampling resolution (the paper discusses using multiple ∆E metrics and discrete sampling) [@bujackGoodBadUgly2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Judging discriminative power only by inspecting the endpoints or by eyeballing “vividness.”
- **Why it fails:** Discriminative power is defined through measured perceived distances/speeds across the colormap, not just endpoints or aesthetics [@bujackGoodBadUgly2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The colormap appears to have sections where changes feel “slow” or “compressed” relative to others.
- **The Test:** Compute average local speed (neighbor-to-neighbor) and average global speed (all pairs) as defined by the framework; compare across candidate colormaps [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the colormap with an alternative whose computed average speed is higher under the same metric and sampling setup.
- **Best Fix:** Incorporate average-speed measures as an explicit selection criterion in your recommendation/evaluation pipeline for continuous colormaps [@zengReviewCollationGraphical2023; @bujackGoodBadUgly2018].

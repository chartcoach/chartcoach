---
id: encode-uncertainty-with-lightness-increase-and-saturation-decrease
title: Encode Uncertainty by Increasing Lightness and Decreasing Saturation
bibliography: references.bib
description: Map higher uncertainty to lighter, less saturated colors to make uncertainty
  visually apparent within a bivariate map.
labels:
- chart:heatmap
- chart:choropleth
- task:assess
- visual:lightness
- visual:saturation
- impact:uncertainty-awareness
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->

When encoding uncertainty in color, map higher uncertainty to higher lightness and lower saturation, and lower uncertainty to lower lightness and higher saturation.

## The Logic <!-- role: reason -->

The paper uses increasing luminance and decreasing saturation as an uncertainty encoding and recommends choosing uncertainty channels that both intuitively read as uncertainty and support multiple distinguishable levels. This supports interpreting uncertainty directly in the mark appearance and integrates uncertainty with value encodings like hue position [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Use an uncertainty channel that both communicates “less confidence” and can be graded across levels.
- **The Evidence:** The VSUP examples and experimental stimuli encode uncertainty via lightness/saturation; the paper recommends this pairing for uncertainty in their designs [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly see which regions are reliable vs unreliable while still reading values.
- **Data Type:** Bivariate displays where value is encoded by color position (e.g., a sequential or multi-hue ramp) and uncertainty is a second dimension.
- **Audience:** General audiences who may not have statistical training.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your value colormap already uses large lightness swings as the primary value cue.
- **Reason:** Lightness becomes ambiguous between “value” and “uncertainty,” which the paper warns can introduce interference [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Color vividness in uncertain regions (uncertain marks become muted).
- **The Risk:** If overused, large pale regions can dominate as “background fog,” potentially hiding meaningful but uncertain patterns [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding uncertainty with channels that unintentionally destroy value discriminability without a controlled scheme.
- **Why it fails:** You may end up with ad hoc aliasing and unclear perceptual properties; VSUPs make this explicit and controlled [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Highly uncertain areas look just as saturated/dark as certain areas.
- **The Test:** Sort a few sample marks by perceived certainty; if observers can’t reliably pick the “most uncertain” ones, the encoding isn’t working.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remap uncertainty so it monotonically increases lightness and decreases saturation.
- **Best Fix:** Combine this uncertainty encoding with a VSUP quantization so high uncertainty also reduces value resolution, matching perceptual limits [@correllValueSuppressingUncertaintyPalettes2018].

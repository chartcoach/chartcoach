---
id: choose-a-value-colormap-that-avoids-extreme-lightness-to-reduce-ambiguity-with-uncertainty
title: Use a Value Colormap That Avoids Very Light and Very Dark Colors
bibliography: references.bib
description: Pick a value colormap that minimizes lightness extremes so lightness
  can more cleanly encode uncertainty.
labels:
- chart:heatmap
- chart:choropleth
- task:compare
- visual:color
- visual:lightness
- impact:clarity
- data:quantitative
- audience:general
- design:colormap-selection
---

## The Rule <!-- role: advice -->

If uncertainty is encoded with lightness (and saturation), choose a value colormap that avoids very light and very dark endpoints to reduce ambiguity between value and uncertainty.

## The Logic <!-- role: reason -->

If the value colormap varies strongly in luminance, it interferes with an uncertainty encoding that also changes luminance, making it harder to interpret the bivariate mapping. The paper notes that many common sequential ramps interpolate in luminance and can introduce ambiguity; they frequently use Viridis because it avoids very light and very dark colors, reducing this ambiguity [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Reduce channel interference by minimizing overlap in what each channel “means.”
- **The Evidence:** The design consideration discussion explicitly motivates using ramps like Viridis to avoid luminance extremes when luminance/saturation encode uncertainty [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Read value while simultaneously judging uncertainty from lightness/saturation.
- **Data Type:** Any bivariate color design where uncertainty uses luminance.
- **Audience:** Broad audiences prone to misattributing lightness differences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not using luminance to encode uncertainty.
- **Reason:** The specific interference concern is tied to luminance being used for uncertainty in the paper’s designs [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some value colormaps with strong lightness range can make univariate value ordering more salient; avoiding extremes may reduce that cue.
- **The Risk:** If your chosen colormap has too subtle value differences, low-uncertainty value discrimination may still be limited without sufficient binning [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Pairing an already lightness-varying sequential ramp with an uncertainty-as-lightness encoding.
- **Why it fails:** Viewers cannot tell whether lightness changes come from value or uncertainty, increasing ambiguity [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Two marks with the same uncertainty but different values look “more/less certain” because of the value ramp’s lightness swings.
- **The Test:** Hold uncertainty constant and scan across values; if perceived certainty changes, the value ramp is interfering.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the value ramp with one that stays away from near-white and near-black.
- **Best Fix:** Rebuild the bivariate mapping (e.g., a VSUP) using a value ramp chosen to minimize luminance ambiguity with your uncertainty channel [@correllValueSuppressingUncertaintyPalettes2018].

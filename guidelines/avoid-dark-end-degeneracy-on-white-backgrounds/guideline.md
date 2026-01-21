---
id: avoid-dark-end-degeneracy-on-white-backgrounds
title: Avoid Very Dark Colormap Regions on White Backgrounds
bibliography: references.bib
description: Dark regions of some colormaps on white backgrounds can produce disproportionately
  high judgment error.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- context:background
---

## The Rule <!-- role: advice -->

On white backgrounds, avoid colormaps (or ranges within colormaps) where important distinctions occur in very low-luminance (near-black) regions.

## The Logic <!-- role: reason -->

- **The Principle:** Extremely dark patches against a high-luminance background can become hard to discriminate, beyond what perceptual distance models predict.
- **The Evidence:** The paper reports dramatic error spikes in low-luminance regions for greys and for the dark ends of magma (and to a lesser extent plasma), despite similar LAB/UCS distance estimates; they attribute this to the high contrast of a white background impairing discrimination of dark shades [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate relative comparison near the low end of the scale.
- **Data Type:** Quantitative scales where low values matter (e.g., detecting subtle differences near minimum).
- **Audience:** General audiences on typical white-page dashboards/reports.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Low-end values are unimportant and can be treated as “effectively zero,” so precision in the darkest region is not needed.
- **Reason:** The degradation matters most when users must discriminate within the dark region [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose dramatic contrast at the low end.
- **The Risk:** Compressing or shifting the dark range can reduce perceived dynamic range.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trusting LAB/UCS distance computations alone to validate dark-end readability on a white background.
- **Why it fails:** The study observed worse discrimination in dark regions than these models predicted [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Near-black swatches look “all the same,” and users guess on low-end comparisons.
- **The Test:** Specifically test triplets near the low end (e.g., around the first 10–20% of the scale); if error spikes there, your dark end is degenerating under your background conditions [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Avoid mapping critical low-end differences into the darkest portion of the palette (shift the data-to-color mapping away from near-black).
- **Best Fix:** Choose or redesign the colormap/range so that low-end distinctions occur at higher luminance when the background is white [@liuSomewhereRainbowEmpirical2018a].

---
id: encode-ordinal-uncertainty-with-lighter-value
title: Encode Ordinal Uncertainty With Lighter Value
bibliography: references.bib
description: Use lighter color value to indicate less certainty for point symbols.
labels:
- chart:map
- task:rank
- visual:color-value
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Map increasing uncertainty to lighter (higher) color value on the same hue: lighter = less certain.

## The Logic <!-- role: reason -->

Color value (lightness) was rated as a good abstract encoding for general ordinal uncertainty, but only with a specific directionality (“lighter = less certain”), demonstrating a consistent ordering cue when hue is held constant [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Ordinal encoding through perceived intensity ordering
- **The Evidence:** Experiment #1 Series #1 descriptive results and directionality finding [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly scanning and comparing certainty across many points
- **Data Type:** Discrete items with ordinal uncertainty; constant hue available
- **Audience:** Users interpreting symbol legends (as in the experiments)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The background is very light or contrast is low.
- **Reason:** Light symbols can become hard to see, undermining both the data display and the uncertainty cue [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visibility of high-uncertainty items (they become faint).
- **The Risk:** Users may miss uncertain points entirely when marks get too light.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to hue changes to imply uncertainty.
- **Why it fails:** Hue was rated unacceptable for general ordinal uncertainty encoding in this study’s Series #1 [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** High-uncertainty points are difficult to detect, not just “less certain.”
- **The Test:** View at typical zoom and ask users to locate the most uncertain points; if they can’t, contrast is too low.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Darken the lightest level slightly while preserving the ordinal order.
- **Best Fix:** Combine value with another acceptable cue (e.g., fuzziness) to preserve detectability while maintaining ordering [@maceachrenVisualSemioticsUncertainty2012].

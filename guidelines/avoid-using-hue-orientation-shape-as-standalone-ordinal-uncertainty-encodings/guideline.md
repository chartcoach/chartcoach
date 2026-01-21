---
id: avoid-using-hue-orientation-shape-as-standalone-ordinal-uncertainty-encodings
title: Avoid Using Hue, Orientation, or Shape As Standalone Ordinal Uncertainty Encodings
bibliography: references.bib
description: Do not encode ordered uncertainty levels using only hue, orientation,
  or shape changes in point symbols.
labels:
- chart:map
- task:rank
- visual:color-hue
- visual:orientation
- visual:shape
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Do not represent ordinal uncertainty levels using only changes in color hue, symbol orientation, or symbol shape.

## The Logic <!-- role: reason -->

In Experiment #1’s general uncertainty series, hue, orientation, and shape were rated unacceptable (mean/median/mode below the midpoint), indicating users do not naturally read these channels as ordered uncertainty without additional structure [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Weak inherent ordering (dominant perceptual order) for these channels in this task
- **The Evidence:** Experiment #1 Series #1 ratings for hue, orientation, and shape [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading an ordered certainty scale (least → most certain)
- **Data Type:** Discrete points with ordinal uncertainty
- **Audience:** Map readers performing fast comparisons

## When to Break It <!-- role: exceptions -->

- **Scenario:** Uncertainty is categorical (not ordinal) and you intentionally want distinct, unordered classes.
- **Reason:** The paper’s evidence addresses ordinal uncertainty signification; categorical uncertainty is a different encoding problem [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer channels remain for multivariate symbolization.
- **The Risk:** Designers may overuse value/fuzziness, reducing other differentiation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using three different shapes to mean “high/medium/low uncertainty.”
- **Why it fails:** Viewers may not infer an order from shapes, undermining “more vs less uncertain” judgments [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can’t tell which level is “in between” without reading text.
- **The Test:** Remove labels and ask users to sort the three symbols by certainty; if they can’t, the encoding is failing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the channel with value or fuzziness using the correct directionality.
- **Best Fix:** If hue/shape must be used for another variable, reserve an accepted channel (e.g., fuzziness) specifically for uncertainty [@maceachrenVisualSemioticsUncertainty2012].

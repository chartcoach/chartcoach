---
id: encode-ordinal-uncertainty-with-positional-jitter-from-center
title: Encode Ordinal Uncertainty With Positional Offset
bibliography: references.bib
description: Use increasing offset from a reference position to show decreasing certainty.
labels:
- chart:map
- task:judge
- visual:position
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Show increasing uncertainty by moving a point mark further from its reference position (greater offset = less certain).

## The Logic <!-- role: reason -->

Position (labeled “location” in the paper) was one of the most intuitive abstract encodings for general ordinal uncertainty, but only in the direction “further from center = less certain,” indicating that spatial displacement maps well to uncertainty magnitude when ordered correctly [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Direct metaphor of imprecision via displacement
- **The Evidence:** Experiment #1 Series #1 directionality results [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding which discrete locations are less reliable (especially spatial component uncertainty)
- **Data Type:** Point features with ordinal certainty classes
- **Audience:** Users comfortable interpreting map symbols

## When to Break It <!-- role: exceptions -->

- **Scenario:** The point’s exact location must remain accurate for operational reading (e.g., selecting a specific site).
- **Reason:** Displacement changes perceived location, potentially misleading about the feature’s position even if uncertainty is communicated [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Spatial accuracy of the displayed point position.
- **The Risk:** Users may treat the offset as “true location shifted,” not as an uncertainty cue.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Randomly jittering points without a visible reference or consistent ordering.
- **Why it fails:** Without a reference “center” and consistent directionality, users cannot reliably map offset to certainty [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users read displaced points as different places rather than “less certain.”
- **The Test:** Ask users to rank three symbols by certainty; if they don’t consistently pick “closest to center = most certain,” revise.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit reference anchor (e.g., target center) so offset is interpretable.
- **Best Fix:** Use an encoding that does not move the point (e.g., fuzziness/value) when positional fidelity is critical [@maceachrenVisualSemioticsUncertainty2012].

---
id: avoid-using-color-saturation-as-a-general-ordinal-uncertainty-cue
title: Avoid Using Color Saturation As a General Ordinal Uncertainty Cue
bibliography: references.bib
description: Do not rely on saturation alone to depict general ordinal uncertainty
  for point symbols.
labels:
- chart:map
- task:judge
- visual:color-saturation
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Do not use color saturation alone to encode general ordinal uncertainty for point symbols.

## The Logic <!-- role: reason -->

In Experiment #1’s general uncertainty testing of visual variables, saturation received low intuitiveness ratings (below the midpoint threshold used to mark acceptable encodings), despite prior assumptions in the literature; participants did not find saturation a logical standalone uncertainty cue in this setup [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Perceptual/cognitive mismatch between channel and intended meaning
- **The Evidence:** Experiment #1 Series #1 results for saturation [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding ordered certainty levels (high → low)
- **Data Type:** Ordinal uncertainty on discrete items
- **Audience:** Map/vis-literate users (as tested)

## When to Break It <!-- role: exceptions -->

- **Scenario:** Saturation is not the primary encoding and is only redundant to reinforce another accepted cue.
- **Reason:** The paper’s finding is about saturation as the main standalone sign-vehicle for general uncertainty, not about redundant encoding [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a potentially available channel for redundancy.
- **The Risk:** Overloading other channels (e.g., value/fuzziness) if saturation is avoided everywhere.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “washed out = uncertain” will be universally understood without testing.
- **Why it fails:** The empirical results showed this mapping was not judged intuitive in the tested general case [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users disagree on whether more saturated means more or less certain.
- **The Test:** Ask users to order a 3-step legend by certainty; inconsistent ordering indicates saturation is not working.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the primary cue to fuzziness or value.
- **Best Fix:** Use saturation only as a secondary reinforcement alongside an encoding that tested as good/acceptable (fuzziness, location, value, arrangement, size, transparency) [@maceachrenVisualSemioticsUncertainty2012].

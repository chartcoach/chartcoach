---
id: do-not-assume-keys-correct-uncertainty-misinterpretation
title: Do Not Rely on Legends Alone to Correct Uncertainty Misinterpretations
bibliography: references.bib
description: Keys and legends may not override default schemas and visual-spatial
  biases in uncertainty graphics.
labels:
- chart:uncertainty
- task:interpret
- visual:legend
- impact:comprehension
- data:uncertainty
- audience:novice
- bias:deterministic-construal
- mechanism:type-1
---

## The Rule <!-- role: advice -->

Assume users will still misinterpret uncertainty graphics even if you provide a legend; design the graphic to make the intended interpretation intuitive.

## The Logic <!-- role: reason -->

The review reports cases where viewers persisted in incorrect interpretations of uncertainty displays despite keys explaining the correct meaning, suggesting default schemas and visual-spatial biases can dominate over instruction text [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand ranges, intervals, probabilistic forecasts, or positional uncertainty
- **Data Type:** Error bars, forecast intervals, uncertainty overlays, ensemble summaries
- **Audience:** Public communication (weather, hazards, health)

## When to Break It <!-- role: exceptions -->

- **Scenario:** Controlled expert environments with standardized training and enforced conventions
- **Reason:** With stable training pipelines, explicit instruction may reliably shape interpretation [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design and testing effort; may require changing the encoding, not just annotating it
- **The Risk:** Alternative encodings may introduce new biases if not tested [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more explanatory text when users misinterpret the uncertainty
- **Why it fails:** Misinterpretations can be driven by automatic, early visual processing that text does not override [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users describe an interval as “the high and low forecast” rather than uncertainty around a distribution.
- **The Test:** Ask users what the graphic implies about values outside the interval/region; deterministic answers indicate persistent bias [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Simplify the uncertainty depiction to reduce boundary-like or discrete “endpoints” cues that encourage deterministic reading.
- **Best Fix:** Redesign uncertainty displays to reduce visual-spatial biases (especially containment and deterministic construal) and validate with user testing [@padillaDecisionMakingVisualizations2018].

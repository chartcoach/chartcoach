---
id: avoid-obscuring-with-noise-and-complex-mappings
title: Avoid Visual and Semantic Obscuring in Data-to-Visual Mappings
bibliography: references.bib
description: Do not introduce perceptual or semantic noise that makes values hard
  to decode or implies false causality.
labels:
- task:compare
- impact:clarity
- custom:rhetoric:mapping
- visual:position
- visual:color
- audience:general-public
---

## The Rule <!-- role: advice -->

Do not add mapping choices that obscure decoding—avoid unnecessary perceptual noise and avoid semantic mappings that imply relationships you can’t support.

## The Logic <!-- role: reason -->

Mapping rhetoric can obscure through perceptual noise (hard-to-judge sizing/position) or semantic noise (implying cause-and-effect or using complex constructs that are difficult to decode); these framing tactics can change interpretation without changing data.

- **The Principle:** Obscuring alters what is perceived and inferred
- **The Evidence:** [@hullmanVisualizationRhetoricFraming2011a]

## Where to Apply <!-- role: context -->

- **User Goal:** Decode values and compare groups without confusion
- **Data Type:** Multivariate stories where encoding choices are already complex
- **Audience:** Non-experts who rely on surface cues for inference

## When to Break It <!-- role: exceptions -->

- **Scenario:** When intentional ambiguity or “noise” is part of a clearly signposted rhetorical critique (e.g., satirical framing)
- **Reason:** The paper notes noise can be used rhetorically; if that’s the point, it must be understood as such [@hullmanVisualizationRhetoricFraming2011a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some stylistic flourish or metaphorical impact
- **The Risk:** Over-sanitizing may reduce engagement in narrative contexts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding complexity to look sophisticated (e.g., “busy” visuals or convoluted mappings)
- **Why it fails:** Complexity can function as obscuring, reducing interpretability while still feeling authoritative [@hullmanVisualizationRhetoricFraming2011a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can’t tell where values sit on an axis, or they infer causality from juxtaposition alone
- **The Test:** Ask a reader to extract a specific value or comparison; if they hesitate or disagree widely, obscuring is likely.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove non-essential mapping transformations and reduce competing visual elements.
- **Best Fix:** Re-encode the key variables using simpler, more directly decodable mappings and add text that limits unsupported causal readings.

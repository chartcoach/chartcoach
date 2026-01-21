---
id: avoid-motion-as-a-high-cardinality-quantitative-encoding
title: Avoid Using Motion to Encode Many Distinct Quantitative Values
bibliography: references.bib
description: Do not encode many quantitative levels with speed/direction because viewers
  can only discriminate a small number of motion differences.
labels:
- chart:scatter
- task:estimate
- visual:motion
- impact:accuracy
- data:multivariate
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not encode high-cardinality quantitative values using speed or direction; reserve motion for coarse patterns or a small number of distinguishable states.

## The Logic <!-- role: reason -->

People can distinguish only a handful of different speeds and motion directions and can track only a few moving points at once, limiting motion’s capacity for precise quantitative reading, as summarized in [@szafirGoodBadBiased2018].

- **The Principle:** Limited discrimination and tracking capacity for motion
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Read or compare quantitative values across many marks
- **Data Type:** Multivariate displays where motion encodes a variable (velocity/direction as value)
- **Audience:** Any audience; limitations apply broadly

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need to communicate a small number of qualitative motion states (e.g., “increasing vs decreasing”)
- **Reason:** Motion can still convey coarse patterns even when it fails for fine discrimination, consistent with [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Dynamic, attention-grabbing effects
- **The Risk:** Alternative encodings (position/size/color) may increase visual complexity

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more distinct speeds to “increase resolution”
- **Why it fails:** Viewers cannot reliably discriminate many velocity steps, per [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Many items appear to move “about the same,” making ranking/estimation impossible
- **The Test:** See whether viewers can correctly order more than a few moving marks by the encoded value—if not, motion is overloaded (as anticipated by [@szafirGoodBadBiased2018])

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of motion levels (bin values into a few classes)
- **Best Fix:** Re-encode the variable using channels better suited for quantitative comparison (e.g., position or color with an appropriate scale), while keeping motion only for highlighting change, aligning with the constraints described in [@szafirGoodBadBiased2018]

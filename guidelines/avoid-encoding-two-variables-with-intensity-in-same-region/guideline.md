---
id: avoid-encoding-two-variables-with-intensity-in-same-region
title: Do Not Overlay Intensity Fields for Multiple Variables
bibliography: references.bib
description: Avoid using intensity in a way that forces viewers to judge brightness
  under changing backgrounds.
labels:
- chart:map
- task:compare
- visual:intensity
- impact:accuracy
- data:spatial
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Do not encode a value with **intensity** in a region whose **background intensity varies**, especially when multiple variables share the same space.

## The Logic <!-- role: reason -->

- **The Principle:** Luminance contrast illusion biases perceived brightness.
- **The Evidence:** Identical intensities appear different when placed on lighter vs darker backgrounds, producing systematic misreadings in maps and layered intensity plots [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing magnitudes across regions (e.g., country vs country).
- **Data Type:** Spatial maps or layered fields where shading varies under marks.
- **Audience:** General viewers likely to trust “darker means more.”

## When to Break It <!-- role: exceptions -->

- **Scenario:** The intensity-coded marks sit on a uniform, constant background.
- **Reason:** The specific bias described arises from varying backgrounds altering perceived brightness [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need separate panels/layers instead of a single composite view.
- **The Risk:** Splitting variables can reduce immediate “all-in-one” context.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the overlay but tweaking colors until it “looks right.”
- **Why it fails:** The illusion is perceptual; subjective tuning won’t remove systematic bias for all viewers [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Two equal-valued marks look different depending on where they sit.
- **The Test:** Copy the same mark to two different background regions; if they appear unequal, the design is biased.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Place intensity marks on a constant neutral backdrop (e.g., a uniform halo behind marks).
- **Best Fix:** Separate variables into distinct views or switch key judgments to position/length encodings [@zacksDesigningGraphsDecisionMakers2020].

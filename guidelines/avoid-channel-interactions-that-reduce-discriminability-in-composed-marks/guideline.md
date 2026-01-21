---
id: avoid-channel-interactions-that-reduce-discriminability-in-composed-marks
title: Avoid Composing Encodings That Interfere with Each Other
bibliography: references.bib
description: Do not combine channels like size and shape in ways that make one channel
  hard to perceive (e.g., tiny shapes becoming indistinguishable).
labels:
- chart:any
- task:encode
- visual:shape
- impact:legibility
- data:multivariate
- audience:any
- composition:mark
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Do not compose two encodings on the same marks if the combination reduces perceptual discriminability (e.g., size changes make shapes hard to tell apart).

## The Logic <!-- role: reason -->

Composing channels can create side effects: one encoding can degrade perception of another; the paper explicitly notes that composing size with shape can make small shapes look identical, reducing effectiveness.

- **The Principle:** Check channel interactions in composite designs
- **The Evidence:** The paper’s size–shape interaction example shows discriminability loss as marks shrink [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly distinguish categories (shape) while also reading an additional variable (size)
- **Data Type:** Multivariate encodings using multiple retinal properties on the same marks
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** The rendering guarantees minimum size (or otherwise ensures discriminability) across all marks.
- **Reason:** The failure arises when composed encodings push marks into perceptually ambiguous ranges [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limits how many variables you can pack into one mark.
- **The Risk:** If you ignore this, viewers may misclassify categories because shapes (or other channels) become indistinguishable [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the composition but “hoping users will zoom in” (in a static design) or ignoring the smallest marks.
- **Why it fails:** The chart’s effectiveness depends on perceiving all marks; the ambiguous ones are still part of the message [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Small marks lose distinctive features; different shapes appear the same at a glance.
- **The Test:** Look at the smallest marks and attempt to identify their shape/category quickly; if you can’t, the composition is failing [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase minimum mark size or reduce the range of size variation.
- **Best Fix:** Reassign one variable to a different channel or separate the encodings into composed views that do not interfere (e.g., axis-based composition) [@mackinlayAutomatingDesignGraphical1986b].

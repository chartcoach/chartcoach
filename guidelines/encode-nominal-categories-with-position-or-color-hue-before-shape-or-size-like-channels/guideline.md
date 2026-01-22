---
id: encode-nominal-categories-with-position-or-color-hue-before-shape-or-size-like-channels
title: Encode nominal categories with position or color hue before texture, saturation,
  or shape
bibliography: references.bib
description: For nominal data, prefer position and then color hue (and texture) over
  saturation and shape to improve categorical discriminability.
labels:
- chart:general
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:basic
---

## Prefer position and color hue for nominal categories <!-- role: advice -->

Encode nominal categories using position when possible, and otherwise prefer color hue (and then texture) over saturation or shape.

## Why hue is prioritized for nominal categories <!-- role: reason -->

Nominal encodings work best when the channel supports clear category separation without implying order; hue provides categorical distinctness, while saturation and size-like cues can suggest ordering.

**Mechanism:** Channels that naturally support categorical differentiation reduce confusion between categories and reduce unintended ordered interpretations.

**Evidence:** A theoretical effectiveness ranking for nominal data orders position (X/Y) first, then color hue, then texture, followed by color saturation and shape, with length/angle/orientation/area ranked lower for nominal use in that ordering [@mackinlayAutomatingDesignGraphical1986a]. This ranking is recorded and collated into structured guidance for visualization recommendation workflows [@zengReviewCollationGraphical2023].

**Notes:** This guideline does not specify a particular palette; it only specifies which channel families to prioritize.

## When this applies for nominal encodings <!-- role: context -->

- **User Goal:** Distinguish categories (identity), not order them.
- **Task:** Identify, group, or compare categories.
- **Data:** Nominal (unordered) variables.
- **Chart Setting:** Static 2D charts using standard displays.
- **Audience:** General audiences.
- **Success Criterion:** Fast and accurate category identification.

## When not to follow the nominal channel ordering <!-- role: exceptions -->

**Break it when:** Color hue cannot be used due to output constraints (e.g., monochrome reproduction). **Why:** The preferred categorical channel is unavailable.

## Tradeoffs of prioritizing hue for nominal categories <!-- role: costs -->

**Sacrifice:** You may lose hue for other semantic purposes in the same view. **Risk:** Too many categories can exceed discriminable hue capacity. **Mitigation:** Reduce categories shown at once or split into multiple views.

## Common mistakes with nominal category encodings <!-- role: mistakes -->

**Mistake:** Using saturation levels to encode categories. **Why it fails:** Saturation can be perceived as ordered rather than purely categorical.

## Quick tests for nominal encoding quality <!-- role: check -->

**Failure Sign:** Viewers interpret categories as “more/less” because the encoding varies in intensity rather than identity. **Quick Check:** Ask whether a viewer could list the set of categories without inferring any ordering. **Stronger Test:** Time a simple “find all items of category X” task across encodings (hue vs saturation vs shape).

## What to do instead when hue is not viable <!-- role: fix -->

- Use texture to differentiate categories when color is constrained.
- Use position-based separation (e.g., grouping or faceting) to encode category identity.
- Use shape only after exhausting position, hue, and texture options.
- Reduce the number of categories visible at once to keep categorical differences clear.

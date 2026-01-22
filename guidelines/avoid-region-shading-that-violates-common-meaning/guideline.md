---
id: avoid-region-shading-that-violates-common-meaning
title: Do not use shaded regions to mean uncertainty when viewers will read them as
  object size
bibliography: references.bib
description: Prevent schema-driven misinterpretation by avoiding uncertainty displays
  that resemble expanding objects.
labels:
- chart:map
- task:interpret
- visual:area
- impact:misinterpretation
- data:uncertainty
- audience:novice
- risk:schema-mismatch
---

## Avoid uncertainty bands that look like an enlarging object <!-- role: advice -->

Do not depict uncertainty with a growing shaded region if the likely reading is that the object itself is growing in size. Use an uncertainty depiction whose visual meaning aligns with what viewers conventionally infer from shaded areas.

## Viewers map shaded area to object extent by default <!-- role: reason -->

When a shaded region surrounds a forecast path, viewers can apply a natural interpretation that the region represents the physical size of the phenomenon, not a probability distribution over locations. This schema mismatch creates predictable misunderstanding even when the display is technically accurate.

**Mechanism:** Prior knowledge about shaded regions and object boundaries drives an automatic mapping from area to “size,” overriding an intended mapping to “uncertainty.”

**Evidence:** A cone-like shaded forecast region is often misinterpreted as the storm expanding in size rather than uncertainty increasing, demonstrating a convention violation that changes viewers’ understanding [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** This risk increases when the visualization resembles a familiar object depiction rather than a statistical depiction.

## Apply to forecasts and probabilistic spatial displays <!-- role: context -->

- **User Goal:** Understand where something is likely to occur and how uncertain that prediction is.
- **Task:** Interpret uncertainty, not physical extent.
- **Data:** Paths, predictions, or spatial distributions with uncertainty over time.
- **Chart Setting:** Public-facing risk communication and operational decision support.
- **Audience:** Broad publics and non-experts with strong everyday object schemas.
- **Success Criterion:** Viewers correctly explain what the shaded region represents.

## When the audience is trained and explicitly instructed <!-- role: exceptions -->

**Break it when:** The audience has strong domain training and the uncertainty encoding is explicitly taught and reinforced in the workflow. **Why:** Learned schemas can override the default object-size interpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Alternative uncertainty depictions may be less visually compact or less familiar. **Risk:** Simplifying to avoid misinterpretation can omit nuance about distribution shape. **Mitigation:** Prioritize correct qualitative understanding over fine-grained probabilistic detail for public contexts.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming viewers will infer “uncertainty” from any widening shaded band without explicit support. **Why it fails:** Shaded regions are often read as the size or boundary of an object, leading to systematic misunderstanding [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers say the object is “getting bigger” when asked what the shading means. **Quick Check:** Ask a neutral question—“What does the shaded region represent?”—and listen for size-based explanations. **Stronger Test:** Run a brief comprehension test with 5–10 target users before deployment.

## What to do instead <!-- role: fix -->

- Choose an uncertainty representation that does not resemble an object boundary.
- Add a brief, adjacent annotation that states what the shaded region means in plain language.
- Separate the depiction of the phenomenon’s physical extent from the depiction of forecast uncertainty.
- Provide a simpler graphic focused on the decision question if uncertainty nuance cannot be communicated reliably.

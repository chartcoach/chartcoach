---
id: avoid-hue-or-shape-for-ordinal-uncertainty-in-point-symbols
title: Avoid hue, orientation, shape, and saturation to encode ordinal uncertainty
  in point symbols
bibliography: references.bib
description: Do not rely on hue, orientation, shape, or saturation alone to communicate
  ordered uncertainty levels for discrete point symbols.
labels:
- chart:map
- task:rank
- visual:color
- impact:clarity
- data:uncertainty
- audience:expert
- symbol:point
---

## Do not use hue, orientation, shape, or saturation alone for ordered uncertainty on point symbols <!-- role: advice -->

Avoid encoding increasing uncertainty purely by changing color hue, orientation, shape, or color saturation for a three-level ordinal uncertainty scale on point symbols.

## Why these channels fail for ordinal uncertainty mapping <!-- role: reason -->

These encodings do not reliably produce a perceived “more vs. less” order for uncertainty, so viewers find the mapping illogical and may not infer the intended direction.

**Mechanism:** When a channel does not naturally imply an ordered scale for the viewer, interpreting uncertainty becomes a learned code rather than an immediate perceptual judgment.

**Evidence:** In intuitiveness ratings of single-variable point-symbol encodings for general uncertainty, hue, orientation, shape, and saturation were rated below the midpoint and were deemed unacceptable for ordinal uncertainty signification; saturation was notably low despite being commonly suggested elsewhere [@maceachrenVisualSemioticsUncertainty2012].

**Notes:** This result concerns using the channel alone for uncertainty, not using it redundantly with a stronger uncertainty cue.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Identify which points are less certain at a glance.
- **Task:** Order or compare points by uncertainty level.
- **Data:** Ordinal uncertainty categories (e.g., high/medium/low certainty).
- **Chart Setting:** Point-symbol maps or point-based information displays.
- **Audience:** Readers expected to interpret without extensive training.
- **Success Criterion:** Correct ordering without requiring users to memorize a code.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users will be trained and repeatedly exposed to a fixed, documented encoding scheme. **Why:** A learned code can work in stable, controlled operational contexts even if it is not intuitive.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding hue/shape can reduce design freedom for multivariate symbols. **Risk:** You may run out of remaining channels when also encoding thematic attributes. **Mitigation:** Reserve a strong ordered channel (fuzziness/value/location) specifically for uncertainty.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using saturation to imply uncertainty because it “feels natural.” **Why it fails:** Participants did not find saturation logical for ordinal uncertainty in this setting.
- **Mistake:** Using different shapes to imply “more vs. less uncertain.” **Why it fails:** Shape differences are read as categorical, not ordered, in this task.

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask what the colors/shapes “mean” even after seeing the map. **Quick Check:** Remove the legend and see if viewers can still pick the least certain point correctly. **Stronger Test:** Run a timed ordering task and confirm accuracy is high without instruction.

## What to do instead <!-- role: fix -->

- Use fuzziness, value (lightness), or offset location to encode uncertainty order.
- Use hue or shape for nominal categories in the data, not for uncertainty order.
- If color must encode uncertainty, use value (light/dark) rather than hue shifts.
- Add a separate legend-first step when you must keep a non-intuitive encoding.

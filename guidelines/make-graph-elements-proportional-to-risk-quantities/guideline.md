---
id: make-graph-elements-proportional-to-risk-quantities
title: Make graphical elements proportional to the risk quantities being depicted
bibliography: references.bib
description: Ensure visual encodings preserve part-to-whole relationships so risk
  magnitude is not distorted.
labels:
- chart:bar
- task:compare
- task:estimate
- visual:position
- visual:length
- impact:accuracy
- data:probability
- audience:novice
- domain:risk-communication
---

## Use proportional visual encodings for risk magnitude and part-to-whole <!-- role: advice -->

Ensure that the size or length of marks in a risk graphic is proportional to the underlying risk quantities, including the part-to-whole relationship between affected people and the total at risk.

## Why proportional encoding supports accurate magnitude judgments <!-- role: reason -->

Risk graphics can change decisions by shifting attention and perceived magnitude. When the visual mapping is proportional to the quantities, viewers can more directly translate what they see into magnitude judgments without unintended exaggeration or compression.

**Mechanism:** Proportional encodings reduce interpretive distortion by aligning perceived magnitude with the actual numeric relationship, especially for part-to-whole judgments.

**Evidence:** Graphical displays that emphasize only the numerator (affected people) versus showing both numerator and denominator change risk-avoidant behavior, and proportional part-to-whole displays are recommended when the goal is accuracy in magnitude judgments. [@lipkusNumericVerbalVisual2007]

**Notes:** Proportional encoding does not guarantee precise numeric estimation relative to numbers-only, but it reduces distortions from mismapped visual cues.

## When proportional encoding is essential <!-- role: context -->

- **User Goal:** Judge how large a health risk is or how much it differs between options.
- **Task:** Compare magnitudes; understand part-to-whole.
- **Data:** Probabilities expressed as counts within a population (numerator/denominator).
- **Chart Setting:** Decision aids, medication side-effect communication, prevention benefit/harms materials.
- **Audience:** Patients and the public; mixed numeracy.
- **Success Criterion:** Perceived magnitude aligns with the intended numeric relationship.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The purpose is not magnitude judgment but a purely qualitative message (for example, “some risk exists”). **Why:** Strict proportionality may add complexity without supporting the intended outcome.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More space may be needed to show both affected and unaffected groups clearly. **Risk:** Viewers may still focus on the most salient region and miss the denominator. **Mitigation:** Pair the graphic with an explicit statement of the reference class (the total at risk).

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Drawing marks that look “more dramatic” than the numeric difference. **Why it fails:** Visual exaggeration changes perceived magnitude and can bias choices.

## Quick tests <!-- role: check -->

**Failure Sign:** A small numeric difference looks large (or vice versa) when eyeballing the display. **Quick Check:** Verify that doubling the risk would approximately double the visual measure used (e.g., length). **Stronger Test:** Ask users to rank risks by size and compare their ranking to the numeric ordering.

## What to do instead <!-- role: fix -->

- Use length/position encodings where the measured dimension corresponds directly to the risk quantity.
- Display both the affected and unaffected portion when communicating frequencies within a population.
- Add the numeric value (e.g., “5 out of 100”) next to the visual to anchor proportional interpretation.
- Simplify the display if proportional encoding requires overly complex graphics for the audience.

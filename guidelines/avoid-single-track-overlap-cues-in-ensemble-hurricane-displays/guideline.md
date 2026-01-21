---
id: avoid-single-track-overlap-cues-in-ensemble-hurricane-displays
title: Prevent Single Track Overlap From Driving Local Risk Judgments
bibliography: references.bib
description: "Ensure that a single ensemble member crossing a location does not dominate\
  \ viewers\u2019 damage/risk judgments in ensemble hurricane track displays."
labels:
- chart:ensemble
- task:assess-risk
- visual:position
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## The Rule <!-- role: advice -->

Design ensemble hurricane track displays so that a single track intersecting a location is not visually interpretable as meaningfully higher local risk than a nearby non-intersecting location.

## The Logic <!-- role: reason -->

- **The Principle:** Marks can be treated as deterministic “hits,” causing viewers to overweight an intersecting line (a “collocation effect”) even when lines are only samples from a distribution.
- **The Evidence:** Viewers rated substantially higher damage for locations overlapped by one ensemble track versus equally plausible nearby locations not overlapped, and this bias persisted even with mitigations [@padillaPowerfulInfluenceMarks2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating/triaging expected damage or risk for specific locations (towns, assets, facilities) from track uncertainty.
- **Data Type:** Ensemble track forecasts visualized as multiple polylines/paths.
- **Audience:** General public or other novice/non-expert viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The lines truly are discrete deterministic scenarios with equal weight and you explicitly want users to treat each line as a separate scenario.
- **Reason:** The “don’t overweight an intersecting line” rule conflicts with the intended meaning of the display.

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced salience of individual paths may make the display feel less concrete or less actionable for users seeking a single “answer.”
- **The Risk:** Over-correcting may cause users to ignore potentially useful information about distribution structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming users will naturally interpret lines as a probability distribution without accounting for overlap-driven judgments.
- **Why it fails:** Even when users perceive distributional uncertainty, they still overweight an intersecting line in damage judgments [@padillaPowerfulInfluenceMarks2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users consistently rate higher damage for a location that happens to lie on one path, compared to an equidistant location not on a path.
- **The Test:** Run an A/B task with “on-line” vs “off-line” target locations matched for distance to the distribution center; check for a systematic positive difference in damage ratings [@padillaPowerfulInfluenceMarks2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an interpretive cue (short instruction) that single lines are only a small subset and “any one line isn’t very meaningful” [@padillaPowerfulInfluenceMarks2020].
- **Best Fix:** Combine instructional mitigation with design changes that reduce the dominance of single-line overlap (e.g., increasing the number of displayed members within readable limits; see related guideline on ensemble count) [@padillaPowerfulInfluenceMarks2020].

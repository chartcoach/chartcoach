---
id: do-not-let-centerline-imply-maximum-intensity
title: Prevent the Centerline from Signaling Peak Damage
bibliography: references.bib
description: "Avoid making the center track look like the storm\u2019s most intense\
  \ region when that is not what the data encode."
labels:
- chart:map
- task:assess-risk
- visual:line
- impact:accuracy
- data:spatiotemporal
- audience:novice
- domain:hurricane
---

## The Rule <!-- role: advice -->

If the centerline is only a predicted track (not intensity), do not present it as a dominant visual anchor that encourages “maximum damage at the line” interpretations.

## The Logic <!-- role: reason -->

Non-experts use salient geometric features as meaning-bearing cues. In the study, removing the centerline (cone-only and fuzzy-cone) reduced damage judgments at the storm center compared to the cone-centerline condition, suggesting the centerline itself can drive beliefs that the “middle” is more intense/damaging [@ruginskiNonexpertInterpretationsHurricane2016].

- **The Principle:** Salience-driven anchoring on discrete marks (lines become “the thing”)
- **The Evidence:** [@ruginskiNonexpertInterpretationsHurricane2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate damage at locations relative to a forecast.
- **Data Type:** Track forecast where the line is not an intensity/impact boundary.
- **Audience:** Non-experts making quick judgments from the graphic.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The centerline truly encodes a physically meaningful feature users should anchor on (e.g., the best-estimate center position) and you explicitly want that anchoring.
- **Reason:** Then the visual prominence matches the intended decision rule.

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced ability to communicate a single “most likely” path at a glance.
- **The Risk:** Users may feel less oriented without a clear central reference.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the centerline highly prominent while hoping users will treat the cone as uncertainty.
- **Why it fails:** Users still anchor on the line and treat distance-to-line as a primary damage cue, as reflected in both ratings and think-aloud reports [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Check <!-- role: check -->

- **Visual Sign:** People explain judgments mainly as “closer to the line = more damage,” independent of other uncertainty cues.
- **The Test:** Run short think-alouds; frequent “distance to the line” justification indicates the line is acting as a misleading intensity cue [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce centerline dominance (thinner/lower-contrast line relative to uncertainty depiction).
- **Best Fix:** Use an uncertainty depiction that does not rely on a single dominant line (e.g., ensemble of tracks) so the forecast reads as a distribution, not a single “damage spine” [@ruginskiNonexpertInterpretationsHurricane2016].

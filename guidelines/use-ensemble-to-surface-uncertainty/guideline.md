---
id: use-ensemble-to-surface-uncertainty
title: Use Ensemble Tracks to Make Uncertainty Salient
bibliography: references.bib
description: "Show multiple plausible tracks to change non-experts\u2019 damage judgments\
  \ and reduce misleading cone-based inferences."
labels:
- chart:map
- task:assess-risk
- visual:position
- impact:interpretability
- data:spatiotemporal
- audience:novice
- domain:hurricane
---

## The Rule <!-- role: advice -->

When communicating track uncertainty to non-experts, use an ensemble visualization (multiple plausible tracks) rather than relying only on a single centerline plus cone.

## The Logic <!-- role: reason -->

Seeing many possible tracks prompts users to reason about **distribution/variability** instead of treating the display as a single deterministic path with an “impact area.” In the study, the ensemble condition produced different damage ratings over time (including reduced “damage increases over time” interpretations) and different stated heuristics (e.g., “counting” tracks) compared to the cone-centerline condition [@ruginskiNonexpertInterpretationsHurricane2016].

- **The Principle:** Instance-based reasoning (multiple samples cue uncertainty)
- **The Evidence:** [@ruginskiNonexpertInterpretationsHurricane2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Make an intuitive judgment of potential damage/risk at locations around a forecast track.
- **Data Type:** Forecast track with positional uncertainty that increases with lead time.
- **Audience:** General public / novices, especially when displays appear without a legend (typical media use case).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot show many lines due to extreme overplotting or limited resolution (e.g., very small mobile thumbnails).
- **Reason:** The ensemble may become an unreadable mass, undermining any uncertainty communication.

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual clutter than a single track/cone.
- **The Risk:** Users may adopt simplistic “count the lines that hit me” heuristics (observed in the study) that may not match the underlying probabilities [@ruginskiNonexpertInterpretationsHurricane2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a few ensemble lines but styling them so heavily that they look like equally-weighted “definite” paths.
- **Why it fails:** It can turn the ensemble into multiple deterministic-looking tracks, encouraging misleading counting or certainty.

## How to Check <!-- role: check -->

- **Visual Sign:** Users describe the forecast as “multiple possibilities” rather than “the storm will go along this line,” and they do not infer growth just from time progression.
- **The Test:** Ask users whether the display implies the storm is getting larger over time; ensemble should reduce that endorsement relative to cone displays [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase distinguishability of individual tracks (so they read as multiple instances rather than a single blob).
- **Best Fix:** Use an ensemble as the primary uncertainty depiction (or pair it with a clearly secondary centerline) to shift interpretation toward uncertainty rather than a widening “impact cone” [@ruginskiNonexpertInterpretationsHurricane2016].

---
id: avoid-cone-size-implies-storm-growth
title: Prevent Cone Widening from Implying Storm Growth
bibliography: references.bib
description: Do not let increasing uncertainty width be visually read as increasing
  storm size or damage over time.
labels:
- chart:map
- task:assess-risk
- visual:size
- impact:clarity
- data:spatiotemporal
- audience:novice
- domain:hurricane
---

## The Rule <!-- role: advice -->

Do not encode forecast uncertainty primarily as a widening cone over time if you need users to avoid interpreting it as the storm getting larger or more damaging.

## The Logic <!-- role: reason -->

People map salient **visual size changes** to **object size/intensity changes**, even when the graphic intends “uncertainty.” In the study, users rated higher damage at later timepoints in cone-style displays (consistent with “storm grows over time”), while ensemble displays reduced this “growth” interpretation.

- **The Principle:** Size-as-magnitude heuristic (visual size is read as physical magnitude)
- **The Evidence:** [@ruginskiNonexpertInterpretationsHurricane2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge how damage/risk changes across forecast time.
- **Data Type:** Spatiotemporal track forecast with increasing positional uncertainty over time.
- **Audience:** Non-experts viewing forecasts without detailed legends (e.g., mass media context).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly want to communicate that the hazard footprint itself expands over time (not just uncertainty).
- **Reason:** Then the size cue is aligned with the intended meaning.

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a familiar “cone” convention that some audiences recognize.
- **The Risk:** Alternative encodings may require explanation to preserve trust or interpretability.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the cone but adding more emphasis (darker fill, bolder outline).
- **Why it fails:** It can further strengthen the size/intensity inference that the study observed in cone-based displays [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers say/assume “the storm is bigger later” or “damage increases because the cone is wider.”
- **The Test:** Ask a few non-experts what changes from 24h to 48h; if they mention storm growth/intensity from widening alone, the encoding is failing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce reliance on width growth by de-emphasizing the cone boundary/area and avoiding cues that make the cone look like a physical footprint.
- **Best Fix:** Replace or complement the cone with an ensemble-style depiction of multiple plausible tracks to shift interpretation away from “growing storm” [@ruginskiNonexpertInterpretationsHurricane2016].

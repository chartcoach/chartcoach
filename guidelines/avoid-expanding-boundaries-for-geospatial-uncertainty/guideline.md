---
id: avoid-expanding-boundaries-for-geospatial-uncertainty
title: Avoid Expanding Boundaries to Encode Geospatial Uncertainty
bibliography: references.bib
description: Do not use widening cones or expanding outlines to represent forecast
  uncertainty when viewers may infer physical growth.
labels:
- chart:map
- chart:uncertainty
- task:interpret
- visual:shape
- impact:clarity
- data:geospatial
- audience:novice
- domain:weather
---

## The Rule <!-- role: advice -->

Do not encode increasing geospatial uncertainty with an expanding boundary (e.g., a widening cone outline) when the phenomenon could be misconstrued as changing physical size.

## The Logic <!-- role: reason -->

Expanding outlines are a salient feature that attracts attention and can be misread as literal size growth rather than uncertainty growth.

- **The Principle:** Salient shape/boundary cues can dominate interpretation
- **The Evidence:** Viewers of the hurricane cone were significantly more likely to judge the hurricane as getting larger over time and made larger size-change judgments than viewers of ensemble displays [@padillaEffectsEnsembleSummary2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding what changes over time (uncertainty vs physical attributes)
- **Data Type:** Geospatial forecast uncertainty over time (e.g., track predictions)
- **Audience:** General public / novice viewers

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are explicitly visualizing the physical boundary of an object that truly expands over time.
- **Reason:** In that case, the expanding boundary is the intended message, not a competing interpretation [@padillaEffectsEnsembleSummary2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loses a compact, familiar summary shape that is easy to recognize.
- **The Risk:** Some users may find ensembles harder to parse at a glance compared to a single summarized region [@padillaEffectsEnsembleSummary2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the expanding cone but adding a short note like “uncertainty increases.”
- **Why it fails:** The boundary remains visually dominant and can still be interpreted as size information despite text [@padillaEffectsEnsembleSummary2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Users talk about the storm “growing,” “getting bigger,” or “widening,” instead of “less certain.”
- **The Test:** Ask a novice what changes over time in one sentence; if they say “size,” the display is failing [@padillaEffectsEnsembleSummary2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce emphasis of the boundary (e.g., de-emphasize outline relative to other marks) and avoid cues that resemble physical extent.
- **Best Fix:** Replace the expanding-boundary summary with an ensemble track display when the goal is communicating path uncertainty without implying size growth [@padillaEffectsEnsembleSummary2017].

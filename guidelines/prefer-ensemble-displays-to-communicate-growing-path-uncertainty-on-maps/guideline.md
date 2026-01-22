---
id: prefer-ensemble-displays-to-communicate-growing-path-uncertainty-on-maps
title: Use ensemble track displays to communicate increasing path uncertainty over
  time on geospatial forecasts
bibliography: references.bib
description: Ensemble tracks can lead novices to better recognize increasing forecast
  uncertainty over time than cone-style summaries.
labels:
- chart:map
- task:interpret
- visual:position
- impact:clarity
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## Use ensemble tracks when the message is uncertainty growth, not object growth <!-- role: advice -->

Use an ensemble display (multiple forecast tracks) when you need novices to recognize that forecasters become less certain about the future path over time. Ensure the display supports reading uncertainty as a distribution of possible locations.

## Why ensembles cue distributional uncertainty <!-- role: reason -->

A set of multiple tracks makes the uncertainty structure visible as spatial spread rather than as a single enclosing object whose size changes. Viewers can attend to the relative dispersion of the tracks and interpret that dispersion as uncertainty about location, which aligns better with the intended meaning of ensemble forecasts.

**Mechanism:** Salient dispersion among many samples supports distribution-based interpretation (uncertainty as spread) instead of object-based interpretation (uncertainty as an expanding shape).

**Evidence:** Viewers were more likely to report that forecasters are less certain about the hurricane’s path as time passes when viewing an ensemble display compared to a cone-style summary [@padillaEffectsEnsembleSummary2017].

**Notes:** This guideline targets communicating uncertainty growth, not communicating impacts at a single point.

## When this applies to geospatial uncertainty communication <!-- role: context -->

- **User Goal:** Understand how forecast certainty changes with time.
- **Task:** Interpret uncertainty about future location from a visualization.
- **Data:** Ensemble geospatial trajectories (e.g., hurricane track members).
- **Chart Setting:** Static map display where multiple paths can be drawn without excessive crowding.
- **Audience:** Novice or general-public viewers.
- **Success Criterion:** Increase correct recognition that uncertainty increases with forecast horizon.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The ensemble is so dense that individual tracks merge into clutter that cannot be visually parsed. **Why:** Overplotting can reduce legibility and undermine the ability to use spread as an uncertainty cue.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Ensembles can be visually busy and may require more space. **Risk:** Individual tracks can become overly salient and be over-weighted for point decisions. **Mitigation:** Match the display choice to the user’s task (area/pattern judgments vs point-specific decisions).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Presenting an ensemble for a point-specific decision without considering that a single visible track can dominate attention. **Why it fails:** Viewers may treat one track as a decisive outcome rather than as one sample from a distribution.

## Quick tests <!-- role: check -->

**Failure Sign:** Users interpret the display as showing a single “most likely” path rather than a spread of possibilities. **Quick Check:** Ask users what the multiple lines represent; flag “this is where it will go” interpretations. **Stronger Test:** Compare uncertainty-growth comprehension questions across ensemble vs summary encodings in a pilot.

## What to do instead <!-- role: fix -->

- If clutter is the barrier, reduce the number of displayed members while preserving the visible spread pattern.
- Provide task-aligned prompts that ask about regions or overall spread rather than a single point on a single line.
- Add a short legend/annotation clarifying that lines are multiple plausible tracks and density/spread conveys uncertainty.
- If the task is inherently point-based, switch to a design that avoids making any single member appear decisive for that point.

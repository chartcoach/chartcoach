---
id: avoid-cone-boundaries-for-geospatial-uncertainty-when-size-can-be-inferred
title: Avoid summary uncertainty boundaries on maps when they could be misread as
  object size
bibliography: references.bib
description: On geospatial maps, boundary-based uncertainty summaries can be misinterpreted
  as indicating an object physically grows over time.
labels:
- chart:map
- task:interpret
- visual:boundary
- impact:clarity
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## Boundary summaries can be read as size changes on maps <!-- role: advice -->

Avoid using boundary-shaped summary uncertainty displays on geospatial maps when viewers might interpret the boundary’s widening as the object physically growing. Prefer a display that does not use an expanding enclosing outline as the primary visual cue.

## Why widening boundaries trigger size inferences <!-- role: reason -->

When uncertainty is encoded as an enclosing shape whose width increases over time, the most visually salient feature can become the changing area/diameter of that shape. In a geospatial setting, viewers can map that salient width change onto a physical-size change of the phenomenon, rather than interpreting it as increasing forecast uncertainty.

**Mechanism:** Bottom-up attention is captured by salient borders; in map contexts, viewers can mis-map a widening boundary to “the thing is getting bigger” instead of “uncertainty is increasing.”

**Evidence:** Novice viewers using a cone-style summary display judged hurricane size to increase more than viewers using an ensemble display and were more likely to report that the display showed the hurricane getting larger over time [@padillaEffectsEnsembleSummary2017].

**Notes:** This effect was observed even though the summary cone is not intended to encode storm size.

## When this applies to uncertainty displays <!-- role: context -->

- **User Goal:** Understand what an uncertainty display implies about a geospatial forecast over time.
- **Task:** Interpret implied size or change in magnitude from an uncertainty visualization.
- **Data:** Ensemble-based geospatial forecasts summarized into an expanding boundary region.
- **Chart Setting:** Static map-based display with an enclosing outline or region that widens with forecast horizon.
- **Audience:** Novice or general-public viewers.
- **Success Criterion:** Reduce systematic misinterpretation of uncertainty as physical size change.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The communication goal explicitly includes showing a physical extent that truly grows/shrinks and that extent is separately validated and explained. **Why:** In that case, the widening boundary is meant to be interpreted as size, not uncertainty.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the simplicity of a single iconic region for uncertainty. **Risk:** Switching away from a boundary summary can increase visual complexity. **Mitigation:** Keep the alternative display visually constrained and task-focused.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming viewers will automatically interpret a widening boundary as “more uncertainty later” rather than “bigger storm later.” **Why it fails:** Salient boundaries on maps can be mapped to physical extent, producing systematic size-growth inferences.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers say the phenomenon is “getting larger” when the data shown is only track/path uncertainty. **Quick Check:** Ask a few target users what changes over time in the graphic; flag “size grows” responses. **Stronger Test:** Compare size-change judgments across two encodings (boundary summary vs non-boundary alternative) in a small pilot.

## What to do instead <!-- role: fix -->

- Use an ensemble-based display that shows multiple plausible tracks rather than an expanding enclosing outline.
- Add explicit annotation stating that the display encodes path uncertainty and does not encode storm size.
- If a region summary must be used, visually de-emphasize the boundary relative to other task-relevant cues.
- Change the task framing to focus on uncertainty about location rather than physical size if size inference is not intended.

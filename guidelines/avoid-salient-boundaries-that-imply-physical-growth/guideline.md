---
id: avoid-salient-boundaries-that-imply-physical-growth
title: Avoid salient uncertainty boundaries that can be misread as the object's physical
  size
bibliography: references.bib
description: Highly salient uncertainty outlines can be mistaken for a changing physical
  extent rather than a probability envelope.
labels:
- chart:map
- task:forecast
- visual:edge
- impact:trust
- data:uncertainty
- audience:novice
- domain:weather
---

## Prevent uncertainty outlines from being interpreted as literal object boundaries <!-- role: advice -->

If an uncertainty visualization uses an outline, ensure it cannot be reasonably interpreted as the physical size or growth of the forecasted object. Prefer depictions that emphasize probability of paths/locations rather than a single bold perimeter.

## Salient outlines invite a concrete, object-like interpretation <!-- role: reason -->

Viewers may apply an object-boundary schema to a strong outline, construing it as the edge of a thing rather than as a statistical summary. This “deterministic construal” can cause misunderstandings about what is uncertain and what is changing.

**Mechanism:** A prominent edge triggers object-based perception and categorical interpretation, biasing the conceptual message toward physical extent rather than uncertainty distribution.

**Evidence:** Salient boundaries in hurricane forecast “cone” displays are linked to misinterpretations such as believing the storm is growing in size, whereas alternative depictions that remove the salient perimeter can improve probabilistic interpretation [@padillaDecisionMakingVisualizations2018]. Viewers also show deterministic construal errors for uncertainty shown with interval-like graphics, treating them as concrete high/low outcomes rather than uncertainty [@padillaDecisionMakingVisualizations2018].

**Notes:** This is especially problematic when the real object (e.g., a hurricane) does have a physical size, making the misread plausible.

## When this applies <!-- role: context -->

- **User Goal:** Understand forecast uncertainty to make protective or resource decisions.
- **Task:** Judge relative risk/impact across locations under uncertain future paths.
- **Data:** Spatial forecast uncertainty; ensemble predictions summarized into an envelope/region.
- **Chart Setting:** Public-facing forecast products and emergency communication.
- **Audience:** Non-expert decision makers under time pressure.
- **Success Criterion:** Viewers interpret the display as uncertainty about path/location, not size.

## Exceptions <!-- role: exceptions -->

**Break it when:** The visualization’s purpose is to show a literal spatial extent (e.g., a true boundary of impact) rather than uncertainty. **Why:** A boundary is then semantically correct.

## Costs <!-- role: costs -->

**Sacrifice:** Removing a bold outline can reduce immediate legibility of a single “zone.” **Risk:** Viewers may feel less confident without a clear perimeter. **Mitigation:** Use explicit labeling and clear legends to support interpretation without relying on a strong outline.

## Mistakes <!-- role: mistakes -->

- **Mistake:** Using a thick, high-contrast outline as the primary uncertainty encoding. **Why it fails:** It encourages reading the outline as a physical boundary.
- **Mistake:** Relying on a legend/key alone to correct the interpretation. **Why it fails:** The visual inference can dominate even when correct instructions are available.

## Check <!-- role: check -->

**Failure Sign:** People describe the forecast as “the storm gets bigger” when uncertainty increases. **Quick Check:** Ask what the outline represents; if the answer refers to size/extent rather than probability, the design is failing. **Stronger Test:** Compare interpretations between an outlined summary and a boundary-free/sampled depiction.

## Fix <!-- role: fix -->

- Replace a single outlined envelope with representative samples (e.g., multiple plausible paths) to convey distribution.
- De-emphasize the perimeter (lower contrast/thinner edge) and emphasize density/likelihood cues instead.
- Add direct annotation near the graphic stating what is uncertain (e.g., “possible paths”), not just a generic legend.
- Provide paired views (summary + samples) so viewers can cross-check the intended probabilistic meaning.

---
id: prefer-implicit-trajectory-ensembles-over-explicit-uncertainty-glyphs-when-storm-attributes-matter
title: Prefer implicit trajectory ensembles over explicit uncertainty glyphs when
  storm attributes must be interpreted
bibliography: references.bib
description: Use discrete forecast tracks to convey spatial uncertainty without visually
  confounding it with storm size or intensity.
labels:
- chart:trajectory
- task:judge-risk
- visual:position
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:tropical-cyclone
---

## Use implicit uncertainty via discrete tracks, not expanding areas, when size/intensity judgments are important <!-- role: advice -->

Use a discrete set of forecast tracks to convey uncertainty implicitly through their spatial spread, instead of encoding uncertainty as an expanding area or glyph size. Keep other storm attributes (such as size and intensity) separate from the uncertainty encoding.

## Implicit spread avoids conflating uncertainty with phenomenon magnitude <!-- role: reason -->

When uncertainty is encoded as a growing region, viewers can misread increasing uncertainty as the phenomenon itself growing (e.g., “the storm is getting bigger/stronger”). Showing multiple possible paths makes uncertainty a property of the distribution of positions, leaving visual channels free to depict storm attributes directly without competing meanings.

**Mechanism:** Discrete samples encourage viewers to infer probability/spread from dispersion, while continuous “area increases” invite a magnitude interpretation that competes with size/intensity.

**Evidence:** Viewers can misinterpret expanding uncertainty summaries (e.g., cone-like area growth) as storm growth, while ensemble-track displays reduce this confound and better support uncertainty interpretation in hurricane contexts [@liuVisualizingUncertainTropical2019]. The paper motivates implicit ensembles specifically to avoid size/intensity confusion and to make multivariate annotation feasible [@liuVisualizingUncertainTropical2019].

**Notes:** This guideline addresses the *visual encoding choice* (implicit tracks vs explicit area glyph), not the specific sampling algorithm.

## When this applies: forecasts where uncertainty and intensity/size are both decision-relevant <!-- role: context -->

- **User Goal:** Understand where the event might go while also judging likely strength/impact.
- **Task:** Risk/damage estimation at locations under uncertain future paths.
- **Data:** Path ensembles with uncertainty over space/time plus additional variables (e.g., intensity, size).
- **Chart Setting:** Map-based forecast display intended to be read quickly.
- **Audience:** Non-experts or mixed audiences prone to cue-confounds.
- **Success Criterion:** Uncertainty is perceived as spread, not as growth in the phenomenon’s magnitude.

## When not to follow it: cases where only a summary region is operationally required <!-- role: exceptions -->

**Break it when:** The display must be a single compact summary shape with no room for multiple tracks. **Why:** A track ensemble requires multiple marks and may not fit strict space or simplicity constraints.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the compactness of a single summary glyph and may need legend/annotation support. **Risk:** With too many tracks, overdrawing and clutter can obscure the distribution. **Mitigation:** Reduce clutter by sampling a representative subset rather than drawing the full ensemble.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using an expanding uncertainty region while also expecting viewers to infer storm size/intensity from that region. **Why it fails:** Viewers may conflate uncertainty growth with storm growth, corrupting risk judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** Users describe the storm as “getting bigger” just because the uncertainty region widens over time. **Quick Check:** Ask a novice what the widening means; if they mention storm size/strength, the encoding is confounded. **Stronger Test:** Replicate a location-based damage judgment task and check whether judgments change primarily with uncertainty spread rather than apparent “area growth.”

## What to do instead <!-- role: fix -->

- Draw a set of forecast tracks so uncertainty is read from their dispersion on the map.
- Annotate tracks with storm attributes (e.g., intensity color, size circles) rather than reusing the uncertainty channel.
- If clutter is high, show a representative subset of tracks rather than the full ensemble.
- If a single summary is mandatory, add explicit text or separate attribute encodings so the uncertainty shape is not misread as storm size.

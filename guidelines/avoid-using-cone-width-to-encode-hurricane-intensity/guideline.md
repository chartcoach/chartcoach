---
id: avoid-using-cone-width-to-encode-hurricane-intensity
title: Do not rely on widening forecast cones to imply increasing hurricane size or
  damage over time
bibliography: references.bib
description: Cone width is frequently misread as storm growth or increasing damage,
  so it should not be used as an implicit cue for intensity over time.
labels:
- chart:map
- task:judge
- visual:size
- impact:interpretability
- data:temporal
- audience:novice
- domain:weather
---

## Cone width should not act as an intensity cue <!-- role: advice -->

Do not let the widening of a hurricane forecast cone be the primary visual cue that changes over time when the intent is to communicate growing track uncertainty rather than increasing storm size or damage.

## Why cone width triggers a storm-growth interpretation <!-- role: reason -->

When uncertainty is encoded with a shape that expands over time, viewers can map the visual increase in area onto a semantic increase in the storm itself (size/intensity), even if the visualization is only meant to represent forecast error around the track. This creates a systematic mismatch between what the visual variable “size” naturally communicates and what the designer intends.

**Mechanism:** Increasing filled area/width is an intuitive cue for “more” (bigger/stronger), so viewers may interpret later, wider parts of the cone as more intense or more damaging rather than merely less certain.

**Evidence:** Damage ratings increased from the 24-hour to the 48-hour timepoint in cone-based conditions, consistent with interpreting the widening cone as increasing damage, while this pattern reversed for an ensemble display that does not widen as a cone over time [@ruginskiNonexpertInterpretationsHurricane2016]. Post-task responses also showed greater endorsement of “hurricane getting larger over time” and “damage getting greater over time” for cone-based displays than for the ensemble display [@ruginskiNonexpertInterpretationsHurricane2016].

**Notes:** This effect appeared even though participants were not given legends or detailed explanations, matching common “media-style” consumption.

## When you are encoding positional uncertainty over time <!-- role: context -->

- **User Goal:** Judge potential impact or damage at locations given a forecast track.
- **Task:** Make intuitive severity judgments across timepoints.
- **Data:** Spatiotemporal track forecasts with increasing positional uncertainty into the future.
- **Chart Setting:** Static map-like displays, often consumed quickly and without a legend.
- **Audience:** Non-expert viewers.
- **Success Criterion:** Viewers treat widening as uncertainty growth (not storm growth) and do not inflate later-time damage solely due to cone size.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is explicitly intended to communicate that the storm’s physical footprint or expected damage area increases over time. **Why:** In that case, mapping “more area” to “more impact” is aligned with the message rather than a misinterpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reducing reliance on a widening cone can remove a simple, familiar visual convention. **Risk:** Some viewers may then under-detect that forecast certainty decreases with lead time. **Mitigation:** Validate with quick comprehension checks that viewers still recognize uncertainty increases with time.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a widening cone and assuming viewers will interpret it as “less certainty later.” **Why it fails:** Many viewers also interpret wider cones as larger or more damaging storms over time [@ruginskiNonexpertInterpretationsHurricane2016].
- **Mistake:** Treating cone geometry as self-explanatory in legend-free contexts. **Why it fails:** Viewers default to perceptual heuristics (e.g., “bigger shape means bigger storm”) when statistical semantics are not explicit [@ruginskiNonexpertInterpretationsHurricane2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers’ damage judgments at the storm center increase at later forecast times even when only uncertainty (not intensity) should change. **Quick Check:** Ask a small sample what “gets larger” from early to late in the display; if they answer “the hurricane,” the encoding is likely being misread. **Stronger Test:** Replicate a damage-at-location judgment task and verify that timepoint does not systematically inflate damage ratings in a pure-uncertainty encoding [@ruginskiNonexpertInterpretationsHurricane2016].

## What to do instead <!-- role: fix -->

- Replace the cone-as-a-single-filled-region with an ensemble of multiple plausible tracks to avoid a single expanding footprint cue.
- Add a display variant that reduces or removes filled-area growth cues while still showing multiple possible paths across time.
- Collect quick qualitative “think-aloud” feedback to confirm viewers describe the change as uncertainty rather than storm growth.

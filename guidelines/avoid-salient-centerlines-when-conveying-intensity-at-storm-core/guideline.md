---
id: avoid-salient-centerlines-when-conveying-intensity-at-storm-core
title: Avoid adding a salient centerline if it increases perceived damage at the storm
  center
bibliography: references.bib
description: A prominent centerline can raise perceived intensity/damage at the storm
  core compared with cone-only variants.
labels:
- chart:map
- task:estimate
- visual:line
- impact:bias-reduction
- data:uncertainty
- audience:novice
- domain:weather
---

## Do not let the centerline act as an intensity cue <!-- role: advice -->

Avoid adding a visually dominant hurricane centerline when your intent is to depict track uncertainty without implying greater intensity at the middle of the displayed region.

## Why a centerline can inflate “peak damage” judgments <!-- role: reason -->

A centerline provides an explicit, high-contrast object that viewers can treat as the storm’s “true path” and as a cue for maximum impact. When that line is present, viewers can anchor severity judgments around it, potentially increasing perceived damage at the center compared with displays that only show the uncertainty region.

**Mechanism:** A salient line becomes an “object” that supports proximity-based heuristics (closer to the line means more severe), which can amplify perceived intensity at the center even when intensity is not encoded.

**Evidence:** At the 24-hour timepoint and at distance zero (the center), damage judgments were higher for cone-with-centerline than for cone-only and fuzzy-cone variants that removed the centerline [@ruginskiNonexpertInterpretationsHurricane2016]. Think-aloud reports in cone-centerline conditions frequently referenced distance and containment heuristics consistent with anchoring on these salient structures [@ruginskiNonexpertInterpretationsHurricane2016].

**Notes:** This is about perceived severity at the storm core, not about whether the track location is easier to identify.

## When the centerline is not the message <!-- role: context -->

- **User Goal:** Judge potential damage/impact at a location from a forecast that includes uncertainty.
- **Task:** Use the uncertainty information rather than treating a single line as “the storm.”
- **Data:** Track forecast with positional uncertainty.
- **Chart Setting:** Public-facing, legend-free or minimally explained graphics.
- **Audience:** Non-expert viewers prone to proximity-based heuristics.
- **Success Criterion:** Center-location judgments are not inflated merely because a line is present.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary purpose is to communicate a single official track for operational decisions and the audience expects a best-track line. **Why:** Removing the centerline may reduce task performance for “follow the track” use cases.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Removing or down-weighting the centerline can make “most likely path” extraction slower. **Risk:** Viewers may feel less confident without a single definitive trajectory cue. **Mitigation:** Confirm via user checks that viewers still understand there is a central tendency without over-weighting it as intensity.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Making the centerline the darkest, highest-contrast element in the figure while also expecting uncertainty to be the takeaway. **Why it fails:** Viewers anchor on the line and increase perceived severity near it [@ruginskiNonexpertInterpretationsHurricane2016].
- **Mistake:** Removing the centerline but keeping a hard boundary that still invites categorical inside/outside reasoning. **Why it fails:** Viewers may continue to rely on discrete region membership rather than uncertainty interpretation [@ruginskiNonexpertInterpretationsHurricane2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Peak damage ratings at the storm center are materially higher when a centerline is present than when it is absent, with all else held constant. **Quick Check:** Show paired variants (with vs. without centerline) and ask what visual cue drove the “most damage” judgment. **Stronger Test:** Run a location-based damage rating task and test whether the center (distance zero) intercept increases with centerlines [@ruginskiNonexpertInterpretationsHurricane2016].

## What to do instead <!-- role: fix -->

- Use a cone-only or other non-line-dominant depiction when the message is uncertainty rather than a single path.
- Validate whether viewers’ “maximum damage” judgments shift simply due to adding a line, and remove the line if it does.
- Use qualitative think-aloud checks to ensure participants describe uncertainty rather than treating the line as the storm itself.

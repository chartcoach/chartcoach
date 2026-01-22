---
id: prefer-perceptually-uniform-multihue-sequential-colormaps-for-continuous-scalars
title: Prefer perceptually-uniform multi-hue sequential colormaps for continuous scalar
  encoding
bibliography: references.bib
description: Use perceptually-uniform multi-hue sequential colormaps (e.g., viridis-like)
  to support faster and more accurate similarity judgments than rainbow or many single-hue
  ramps.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use perceptually-uniform multi-hue sequential colormaps for scalar fields <!-- role: advice -->

Use a perceptually-uniform multi-hue sequential colormap (one that ramps in both hue and luminance) when encoding a continuous quantitative variable. Prefer this over rainbow colormaps and over single-hue ramps when viewers must make many “which is closer” comparisons.

## Multi-hue + luminance ramps improve discriminability without losing order <!-- role: reason -->

Perceptually-uniform multi-hue sequential schemes provide multiple perceptual cues (hue changes plus luminance changes) while still supporting a consistent ordered reading, which can improve discrimination in relative distance judgments.

**Mechanism:** Adding hue variation alongside luminance increases perceptual separation between nearby values, helping viewers decide which sample is closer to a reference without relying on unstable hue boundaries.

**Evidence:** In triplet similarity judgments with legends present, the perceptually-uniform multi-hue sequential colormap viridis showed lower error and faster responses than a rainbow colormap (jet), and was among the best overall across tested colormaps [@liuSomewhereRainbowEmpirical2018a]. Across perceptually-uniform multi-hue sequential colormaps (viridis, plasma, magma), performance was broadly comparable and consistently low-error relative to other families studied [@liuSomewhereRainbowEmpirical2018a].

**Notes:** This guideline concerns ordinal similarity judgments (relative closeness), not precise numeric read-off.

## Where this colormap choice matters most <!-- role: context -->

- **User Goal:** Compare magnitudes by similarity (e.g., “which region/value is closer to this one?”).
- **Task:** Forced-choice or informal relative distance judgments along a continuous scale.
- **Data:** One continuous quantitative variable mapped to a sequential colormap.
- **Chart Setting:** Heatmaps, scalar fields, choropleth-like views, or any view relying on a continuous legend.
- **Audience:** Mixed expertise; include users with varied displays and environments.
- **Success Criterion:** Low comparison error and reasonable response time.

## When not to default to this choice <!-- role: exceptions -->

**Break it when:** The data are centered on a meaningful midpoint and the primary task is judging deviation on both sides of that midpoint. **Why:** This situation calls for a diverging design goal rather than a purely sequential one, and midpoint behavior can dominate judgments.

## Tradeoffs of multi-hue sequential schemes <!-- role: costs -->

**Sacrifice:** Multi-hue ramps can be slightly slower than the fastest single-hue conditions in some cases. **Risk:** Dark-end performance can still degrade in some multi-hue schemes depending on the specific palette and background. **Mitigation:** Evaluate the dark region performance against the intended background early.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Replacing rainbow with an arbitrary multi-hue ramp that is not designed for perceptual ordering/uniformity. **Why it fails:** Multi-hue alone does not guarantee ordered, low-error judgments; naive hue transitions can recreate the problems seen in rainbow-like designs.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** Users hesitate or disagree when comparing close values, or errors cluster near specific hue boundaries. **Quick Check:** Sample triplets with small value differences and see if “closer” choices feel ambiguous across the scale. **Stronger Test:** Run a small triplet-judgment pilot across representative spans and reference locations.

## If you can’t use a perceptually-uniform multi-hue sequential colormap <!-- role: fix -->

- Use a single-hue luminance-ramping colormap when comparisons are mostly coarse (large value spans).
- Reduce the need for fine comparisons by binning values more coarsely when the task tolerates it.
- Add interaction (hover value readout) when users must make precise decisions from color.
- Re-encode key comparisons using a higher-precision channel (e.g., position/length) if accuracy is critical.

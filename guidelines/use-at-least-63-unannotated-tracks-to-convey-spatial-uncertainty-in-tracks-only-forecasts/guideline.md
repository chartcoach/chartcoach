---
id: use-at-least-63-unannotated-tracks-to-convey-spatial-uncertainty-in-tracks-only-forecasts
title: Use at least 63 unannotated tracks to convey spatial uncertainty in tracks-only
  forecasts
bibliography: references.bib
description: "Tracks-only displays need high track counts to make viewers\u2019 damage\
  \ judgments reflect increasing uncertainty over time."
labels:
- chart:trajectory
- task:judge-risk
- visual:position
- impact:interpretability
- data:uncertainty
- audience:novice
- domain:tropical-cyclone
---

## If you show tracks without size/intensity annotations, draw enough tracks that spread changes with time become visible <!-- role: advice -->

When using an unannotated tracks-only forecast display, draw a high number of tracks (e.g., 63) so viewers’ judgments reflect broader uncertainty at later forecast times. Avoid relying on sparse tracks-only displays (e.g., 7 or 15) to communicate changes in uncertainty over time.

## Sparse track sets can hide uncertainty structure needed for risk judgments <!-- role: reason -->

If too few tracks are shown, viewers may focus on the implied central tendency and treat the display as more precise than it is, leading to similar damage–distance relationships across forecast horizons even when uncertainty grows. Higher track density can better reveal how spread increases with time, shifting attention away from only the central path when later forecasts are more uncertain.

**Mechanism:** More samples provide stronger visual evidence of dispersion, enabling viewers to adjust judgments based on uncertainty spread rather than extrapolating from a small set.

**Evidence:** In a damage-judgment study, tracks-only displays with 63 tracks showed a flatter damage–distance relationship at 48 hours than at 24 hours (consistent with increased uncertainty), while 7- and 15-track displays did not show this time-based slope change; confidence was also higher with 63 tracks than with 7 or 15 [@liuVisualizingUncertainTropical2019].

**Notes:** This guideline is specific to *tracks-only* displays; annotation changes the required number of tracks.

## When this applies: spaghetti-style uncertainty displays without multivariate cues <!-- role: context -->

- **User Goal:** Judge risk at locations relative to the forecast distribution.
- **Task:** Translate spatial spread into damage/impact estimates across time horizons.
- **Data:** Ensemble tracks over time where uncertainty increases with forecast lead time.
- **Chart Setting:** No size/intensity glyphs; tracks are visually uniform.
- **Audience:** Non-experts making quick risk judgments.
- **Success Criterion:** Users’ judgments become less centered (flatter vs distance) at later forecast times.

## When not to follow it: when many tracks will cause unacceptable clutter or prevent annotation <!-- role: exceptions -->

**Break it when:** Adding many tracks causes heavy overdraw that prevents reading key annotations or geographic context. **Why:** Clutter can defeat comprehension even if it increases sampling density.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More tracks increase visual clutter and reduce space for labels and annotations. **Risk:** Dense overlaps can make it hard to trace individual paths or see base-map features. **Mitigation:** Use representative sampling or add attribute annotations so fewer tracks are needed.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Showing 7–15 unannotated tracks and assuming viewers will infer uncertainty growth over time. **Why it fails:** Viewers’ damage–distance slopes may remain similar across time points, indicating uncertainty spread is not being incorporated.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ risk judgments vs distance look almost identical at early and later forecast horizons. **Quick Check:** Compare average damage–distance slopes at two time points; if they do not change with forecast horizon, uncertainty spread is not being read. **Stronger Test:** Run a small replicated damage judgment task and test for a distance-by-time interaction consistent with increased uncertainty at later times.

## What to do instead <!-- role: fix -->

- Increase the number of tracks in tracks-only displays until spread changes are visually salient (e.g., around 63 in the paper’s setting).
- Replace a full spaghetti plot with a representative subset plus attribute annotations to reduce the number of tracks required.
- Use a visualization that explicitly supports time-slice uncertainty reading (e.g., show positions at specific times) if the display must remain sparse.
- Add interaction to toggle between sparse overview and dense uncertainty view at selected horizons.

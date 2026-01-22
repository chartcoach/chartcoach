---
id: add-intensity-and-size-annotations-to-reduce-track-count-needed-for-uncertainty-interpretation
title: Add intensity color and size rings so fewer tracks still convey uncertainty
  and risk
bibliography: references.bib
description: Annotating tracks with storm intensity and size improves damage judgments
  and supports uncertainty perception with fewer tracks.
labels:
- chart:trajectory
- task:judge-risk
- visual:color
- impact:decision-support
- data:multivariate
- audience:novice
- domain:tropical-cyclone
---

## Encode intensity and size on tracks so viewers can calibrate damage judgments without needing a very dense spaghetti plot <!-- role: advice -->

Annotate forecast tracks with storm intensity using a discrete color scheme and with storm size using periodic size rings, so viewers incorporate both hazard attributes and spatial uncertainty in their risk judgments. Use these annotations to reduce reliance on very high track counts to convey uncertainty.

## Attribute annotations anchor risk judgments and make spread easier to interpret <!-- role: reason -->

When tracks are unannotated, viewers must infer risk from path geometry alone, which can underutilize uncertainty information unless many tracks are drawn. Adding intensity and size cues provides direct evidence of hazard magnitude at locations and times, improving calibration of damage estimates and increasing awareness of uncertainty spread even with fewer tracks.

**Mechanism:** Separate encodings for intensity and size give viewers concrete inputs for damage judgments; uncertainty can then be inferred from track dispersion rather than being conflated with magnitude or ignored.

**Evidence:** With 15 tracks, adding size and intensity annotations changed the damage–distance relationship in a way consistent with uncertainty interpretation, and storm size and intensity both explained significant variance in damage ratings beyond distance and time; the annotated 15-track display produced flatter damage–distance relationships than a 63-track unannotated display, indicating greater awareness of spatial spread [@liuVisualizingUncertainTropical2019].

**Notes:** The paper also notes an indication that more than 15 annotated tracks may further improve sensitivity to increasing spread with time.

## When this applies: multivariate storm forecasts where decisions depend on strength and footprint <!-- role: context -->

- **User Goal:** Estimate damage/impact based on both likelihood of impact and storm strength/size.
- **Task:** Compare risk at locations across time horizons.
- **Data:** Tracks with per-time intensity and size attributes.
- **Chart Setting:** Map with limited room; desire to avoid clutter while still showing uncertainty.
- **Audience:** Non-experts (or mixed expertise) needing interpretable cues.
- **Success Criterion:** Damage estimates increase with higher intensity/size and reflect greater uncertainty at longer lead times.

## When not to follow it: when the annotation values are unreliable or physically inconsistent <!-- role: exceptions -->

**Break it when:** The displayed size/intensity annotations can be misleading due to modeling/interpolation artifacts or known decoupling issues. **Why:** Incorrect annotations can miscalibrate risk judgments even if uncertainty is visible [@liuVisualizingUncertainTropical2019].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional legend/encoding complexity is required. **Risk:** Annotations can overlap and clutter the map, especially with many tracks or frequent glyph placement. **Mitigation:** Reduce annotation frequency and manage spacing across tracks.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding annotations at every time step along every track. **Why it fails:** Overdrawing and overlap can make both the tracks and annotations unreadable.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ damage judgments do not increase with higher displayed intensity/size, or users ignore the spread of tracks. **Quick Check:** Verify that annotated intensity and size values vary along tracks and are legible at a glance. **Stronger Test:** Run a small user study to confirm size and intensity predict damage ratings beyond distance/time.

## What to do instead <!-- role: fix -->

- Encode intensity as discrete categories using distinct colors applied along track segments.
- Encode size as periodic rings centered on track positions at coarser intervals to avoid overlap.
- Reduce track count when annotations are present to preserve legibility, then add tracks only until spread is adequately conveyed.
- Provide a clear legend for the intensity categories and clarify what the size rings represent.

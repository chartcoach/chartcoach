---
id: use-enough-tracks-or-annotations-so-users-perceive-increasing-uncertainty-over-time
title: Ensure Track Count or Annotation Is Sufficient to Reveal Uncertainty
bibliography: references.bib
description: If tracks are unannotated, use many; if annotated, fewer tracks can work
  but still must support time-based spread perception.
labels:
- chart:trajectory
- task:estimate
- visual:position
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

If you show tracks without annotations, draw enough tracks for viewers to perceive increased spatial spread at later forecast times; if you add size/intensity annotations, you can reduce track count but still validate that time-based spread is noticeable.

## The Logic <!-- role: reason -->

In the paper’s study, viewers only showed a time-sensitive damage–distance pattern consistent with increasing uncertainty when many unannotated tracks were shown (63). With fewer unannotated tracks (7 or 15), that time-based slope change did not emerge; adding annotations improved sensitivity to spatial spread even with fewer tracks (15) [@liuVisualizingUncertainTropical2019].

- **The Principle:** Sample density affects perceived uncertainty structure
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Calibrate risk across time horizons (e.g., 24h vs 48h) as uncertainty grows
- **Data Type:** Track ensembles where spread increases with forecast horizon
- **Audience:** Non-experts interpreting forecast risk

## When to Break It <!-- role: exceptions -->

- **Scenario:** The display must remain extremely uncluttered and cannot add tracks or annotations
- **Reason:** Then the visualization may be unable to communicate time-varying spread effectively, which is the tradeoff [@liuVisualizingUncertainTropical2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** More tracks increase clutter; more annotations add visual elements and design complexity
- **The Risk:** Too many tracks can cause overdrawing; too few can hide uncertainty growth over time [@liuVisualizingUncertainTropical2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assume a small number of unannotated representative tracks (e.g., 7–15) will still communicate uncertainty evolution
- **Why it fails:** The study found time-based sensitivity emerged clearly with a much denser unannotated display (63) [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** The late-forecast region does not look meaningfully “more spread” than early-forecast regions
- **The Test:** Compare 24h vs 48h (or early vs late) snapshots; if spread increase is not apparent at a glance, track count/annotation is insufficient [@liuVisualizingUncertainTropical2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the number of tracks in an unannotated view (the paper demonstrated 63 worked well)
- **Best Fix:** Add intensity/size annotations so fewer tracks can still convey risk-relevant uncertainty, then tune track count upward if time-based spread still isn’t perceived [@liuVisualizingUncertainTropical2019]

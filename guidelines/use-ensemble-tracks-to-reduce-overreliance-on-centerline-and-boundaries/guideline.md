---
id: use-ensemble-tracks-to-reduce-overreliance-on-centerline-and-boundaries
title: Use ensemble track displays to reduce centerline and boundary-driven damage
  judgments
bibliography: references.bib
description: Ensemble displays shift viewers away from treating a single centerline
  and cone edges as the main cues for impact.
labels:
- chart:map
- task:estimate
- visual:position
- impact:decision-quality
- data:uncertainty
- audience:novice
- domain:weather
---

## Prefer ensembles when people must judge impact beyond a single path <!-- role: advice -->

Use an ensemble visualization of multiple plausible hurricane tracks when non-experts must judge potential damage at locations, rather than relying on a single centerline plus a hard-bounded cone.

## Why ensembles change the heuristics people use <!-- role: reason -->

A single prominent track and crisp boundaries invite categorical and distance-to-line reasoning (e.g., “inside is safe/unsafe” and “closer to the line means more damage”). Showing many possible tracks instead makes uncertainty perceptually salient and encourages more distributed judgments that are less anchored to one “most likely” path.

**Mechanism:** Multiple realizations reduce the dominance of any one trajectory cue and make spatial dispersion visible, which can temper sharp distance-based drop-offs and inside/outside boundary thinking.

**Evidence:** Compared with cone-with-centerline displays, ensemble displays produced different timepoint effects (damage ratings decreased from 24 to 48 hours) and showed a more spatially distributed pattern of damage judgments at later lead times [@ruginskiNonexpertInterpretationsHurricane2016]. In think-aloud data, the “count” heuristic (counting how many tracks affect a location) occurred only with ensembles, while cone-with-centerline displays prompted more distance/containment and size-based reasoning [@ruginskiNonexpertInterpretationsHurricane2016].

**Notes:** These effects were observed in a legend-free, intuitive-judgment setting, where viewers relied heavily on visual heuristics.

## When you need users to reason about multiple plausible futures <!-- role: context -->

- **User Goal:** Decide how much damage/impact a location might face from a forecasted storm.
- **Task:** Integrate uncertainty into a severity judgment rather than only reading a “most likely” path.
- **Data:** Multiple plausible tracks or a distribution around a predicted path (positional uncertainty over time).
- **Chart Setting:** Static or minimally explained forecast graphics used in public-facing contexts.
- **Audience:** Non-experts with limited statistical training.
- **Success Criterion:** Judgments reflect uncertainty dispersion rather than a sharp centerline-or-boundary heuristic.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** The communication channel cannot visually support many tracks (e.g., extremely small display area or severe clutter constraints). **Why:** Overplotting can make the display unreadable and prevent any meaningful interpretation.
- **Break it when:** The task is explicitly to follow the official single best track for operational navigation (not uncertainty-aware impact judgment). **Why:** Multiple tracks can hinder rapid extraction of the single intended path.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Ensembles can be visually dense and may require more effort to interpret than a single cone. **Risk:** Viewers may switch to simplistic “count the lines” reasoning that does not match calibrated probability. **Mitigation:** Check whether viewers’ explanations reference uncertainty dispersion rather than purely line counts.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding an ensemble but making all tracks equally dark and prominent, creating a “hairball” that viewers can only count or ignore. **Why it fails:** The display becomes clutter-first rather than uncertainty-first, reducing interpretability in quick-glance contexts [@ruginskiNonexpertInterpretationsHurricane2016].
- **Mistake:** Keeping a dominant centerline as the most salient element within an ensemble-like view. **Why it fails:** Viewers revert to centerline anchoring and distance-to-line heuristics rather than integrating dispersion [@ruginskiNonexpertInterpretationsHurricane2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe their strategy primarily as “distance to the center line” or “inside the shaded region” rather than referencing multiple plausible paths. **Quick Check:** Run brief think-aloud trials and code whether “count/multiple tracks” is mentioned. **Stronger Test:** Compare distance–damage slopes over time; ensembles should reduce the steepness/anchoring patterns seen with cone-centerline displays at later timepoints [@ruginskiNonexpertInterpretationsHurricane2016].

## What to do instead <!-- role: fix -->

- Use an ensemble of multiple plausible tracks in place of a single hard-bounded cone when the goal is uncertainty-aware impact judgment.
- Reduce the salience of any single “official” track element if present, so dispersion remains the dominant cue.
- Validate with short think-aloud sessions that viewers do not default to centerline-only or inside/outside boundary heuristics.

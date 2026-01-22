---
id: avoid-ensemble-tracks-for-point-based-damage-choices-when-overlap-can-dominate
title: Avoid ensemble track displays for point-based choices when overlap with a single
  member can dominate judgments
bibliography: references.bib
description: When a decision is about a specific location, novices may overweight
  an ensemble member that visually passes through that point.
labels:
- chart:map
- task:decide
- visual:position
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## Don’t use raw ensemble lines for single-location decisions where a line can “hit” the point <!-- role: advice -->

Avoid using an ensemble display of individual tracks when the user’s task is to decide outcomes at a specific point location and a track can visually intersect that point. Use an alternative that does not make any single ensemble member appear like a decisive strike on the point.

## Why line-point intersection becomes an over-weighted cue <!-- role: reason -->

A line crossing a marked point is a highly salient geometric event that can be treated as categorical evidence (“it will hit here”), even though each line is only one sample from the ensemble. This can pull judgments away from a distributional strategy (e.g., using proximity to the centerline) toward overweighting the one intersecting member.

**Mechanism:** Salient colocation between a point of interest and an individual ensemble member can trigger an outcome-focused interpretation of that member, increasing its weight relative to the broader ensemble distribution.

**Evidence:** In point-based damage comparisons, the probability of choosing the closer-to-center location dropped substantially when the farther location lay on a single ensemble track, indicating overweighting of the intersecting member [@padillaEffectsEnsembleSummary2017]. This bias replicated when an “equal damage” option was added [@padillaEffectsEnsembleSummary2017].

**Notes:** The effect was demonstrated with forced-choice and with an added “equal” response option, suggesting robustness to response format.

## When this applies to ensemble uncertainty maps <!-- role: context -->

- **User Goal:** Decide which specific location will be more impacted.
- **Task:** Point-based comparison (A vs B) or evaluation of risk/damage at a specific site.
- **Data:** Track-based ensemble forecasts where individual members can intersect locations.
- **Chart Setting:** Static ensemble tracks over a map with highlighted point markers.
- **Audience:** Novice viewers making high-stakes or intuitive judgments.
- **Success Criterion:** Reduce overweighting of a single ensemble member due to visual intersection.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is explicitly to identify whether any ensemble member intersects a point (e.g., “is there at least one plausible track passing here?”). **Why:** Then the intersection is the intended signal, not a bias.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the transparency of showing individual members. **Risk:** Replacing tracks with a non-member-based depiction can reduce trust for users who want to see raw simulations. **Mitigation:** Provide access to individual members separately from the primary point-decision view.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Placing prominent point markers on top of ensemble tracks and asking “which point is more impacted?” **Why it fails:** The intersecting line becomes a categorical cue that competes with distributional reasoning.
- **Mistake:** Interpreting “line does not cross my point” as “zero chance.” **Why it fails:** The shown members are a sample and non-intersection does not imply negligible probability.

## Quick tests <!-- role: check -->

**Failure Sign:** Users switch their choice mainly when a single track crosses a location, even if overall spread/density suggests otherwise. **Quick Check:** Show two scenarios that differ only by whether one visible member crosses the point and see if judgments flip. **Stronger Test:** Run a small user test comparing point-based decisions under ensemble lines versus a non-member-based uncertainty depiction.

## What to do instead <!-- role: fix -->

- Replace individual tracks with an uncertainty depiction that communicates distribution without discrete member intersections for the decision view.
- Reframe the interaction to ask about areas or regions instead of single points when using ensemble tracks.
- Separate the decision layer (points) from the member layer so intersection is not visually emphasized at the moment of choice.
- Provide an explicit explanation that displayed tracks are samples and that intersection with a point should not be treated as a deterministic hit.

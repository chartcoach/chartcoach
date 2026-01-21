---
id: use-ensemble-displays-to-communicate-probabilistic-path-uncertainty
title: Use Ensemble Displays to Communicate Probabilistic Path Uncertainty
bibliography: references.bib
description: Prefer ensemble tracks over cone summaries when communicating geospatial
  path uncertainty to novices.
labels:
- chart:map
- chart:ensemble
- task:interpret
- visual:position
- impact:trust
- data:geospatial
- audience:novice
- domain:weather
---

## The Rule <!-- role: advice -->

Prefer ensemble track displays over cone-style summary displays when your goal is for novices to interpret geospatial path uncertainty rather than infer changes in storm size or intensity.

## The Logic <!-- role: reason -->

Cone summaries have salient boundaries that novices can misinterpret as physical growth; ensemble displays avoid that specific size-growth cue and lead to judgments more consistent with interpreting a distribution of possible tracks.

- **The Principle:** Mark salience shapes what viewers think the visualization “is about”
- **The Evidence:** Compared to ensembles, cone viewers more often judged that the hurricane grew in size and increased both size and intensity at the storm center; ensemble viewers were less likely to report size-growth interpretations and more likely to report increasing forecast uncertainty over time [@padillaEffectsEnsembleSummary2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding uncertainty in future paths (where it might go)
- **Data Type:** Ensembles of predicted tracks (multiple plausible futures)
- **Audience:** Novices / general public consuming forecasts

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user must make a decision about a single, specific point location (e.g., “my town”).
- **Reason:** Ensemble members can be overweighted when a point visually falls on a single track, biasing point-based judgments [@padillaEffectsEnsembleSummary2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Can introduce visual clutter/crowding as many tracks overlap.
- **The Risk:** Users may treat a single visible track as a deterministic path, especially for point-focused tasks [@padillaEffectsEnsembleSummary2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing an ensemble but encouraging “follow the line that hits you.”
- **Why it fails:** It reinforces overweighting of individual ensemble members instead of reading track density as probability [@padillaEffectsEnsembleSummary2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Users justify decisions by referencing one specific track (“this line goes right over it”).
- **The Test:** Ask users to explain what dense vs sparse regions mean; if they describe individual tracks as single predicted futures, the display is being read deterministically [@padillaEffectsEnsembleSummary2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reframe accompanying text/prompts so users consider the distribution (e.g., “consider how many tracks pass near a region”).
- **Best Fix:** Align the task with ensemble strengths by asking for area/pattern judgments rather than point-hit judgments when using ensemble displays [@padillaEffectsEnsembleSummary2017].

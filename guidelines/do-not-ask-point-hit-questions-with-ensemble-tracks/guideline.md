---
id: do-not-ask-point-hit-questions-with-ensemble-tracks
title: Avoid Point-Hit Decision Tasks with Ensemble Track Displays
bibliography: references.bib
description: Do not pair ensemble track displays with tasks that ask which specific
  point will be hit or damaged most.
labels:
- chart:ensemble
- chart:map
- task:decide
- visual:position
- impact:accuracy
- data:geospatial
- audience:novice
- domain:weather
---

## The Rule <!-- role: advice -->

Do not use ensemble track displays for tasks that require choosing outcomes for specific point locations (e.g., “which site gets more damage?”) when a point may coincide with an individual track.

## The Logic <!-- role: reason -->

When a point overlaps a single ensemble member, that member becomes a salient cue and can be overweighted, shifting judgments away from the intended probabilistic reading of the ensemble as a distribution.

- **The Principle:** Salient mark overlap can override distribution-based reasoning
- **The Evidence:** When the farther oil rig overlapped a single ensemble track, participants chose it far more often (reducing the “choose the closer-to-center” strategy from ~99.7% to ~64% in Experiment 2, and to ~55% in Experiment 3 after removing “equal damage” trials), showing strong bias from line-point colocation [@padillaEffectsEnsembleSummary2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Making a decision about a specific point location (facility, city, asset)
- **Data Type:** Ensemble paths rendered as distinct tracks/lines
- **Audience:** Novices interpreting forecast uncertainty

## When to Break It <!-- role: exceptions -->

- **Scenario:** The decision task is explicitly about identifying a particular ensemble member or a specific simulated trajectory.
- **Reason:** Then weighting individual tracks is the intended operation rather than a bias [@padillaEffectsEnsembleSummary2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less direct support for “my exact location” questions with ensemble visuals.
- **The Risk:** Switching away from point tasks may require reframing stakeholder requirements (e.g., from “will I be hit” to “how likely is my area”) [@padillaEffectsEnsembleSummary2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the point-based question but adding more ensemble members.
- **Why it fails:** More lines do not remove the salience of a point sitting exactly on one line; overlap remains a strong cue [@padillaEffectsEnsembleSummary2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Users pick a farther point because “a line goes through it,” even when other cues imply lower risk.
- **The Test:** Run a quick A/B with and without exact line-point overlap; if choices swing sharply, you have a colocation bias problem [@padillaEffectsEnsembleSummary2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Avoid placing point markers directly on ensemble lines in decision prompts (choose points that are not exactly colocalized).
- **Best Fix:** Redesign the task to be area-based (regional judgments) rather than point-hit based when presenting ensemble tracks [@padillaEffectsEnsembleSummary2017].

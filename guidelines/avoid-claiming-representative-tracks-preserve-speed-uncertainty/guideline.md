---
id: avoid-claiming-representative-tracks-preserve-speed-uncertainty
title: Do Not Rely on Representative Tracks to Convey Speed Uncertainty
bibliography: references.bib
description: Representative track subsets preserve directional spread but may not
  preserve uncertainty in forward speed/arrival time.
labels:
- chart:trajectory
- task:communicate-uncertainty
- visual:position
- impact:honesty
- data:temporal
- audience:novice
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

Do not present a small, time-parameterized representative track set as if it preserves uncertainty in storm forward speed (arrival time); treat it as primarily preserving directional/spatial spread.

## The Logic <!-- role: reason -->

The paper’s validation shows representative tracks match cross-track (perpendicular) spatial spread well but do not maintain the distribution along the forward direction, reflecting lost speed uncertainty; representing speed uncertainty with sparse time-parameterized tracks is inherently difficult without adding clutter [@liuVisualizingUncertainTropical2019].

- **The Principle:** Sampling limits what uncertainty dimensions remain visible
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Interpret likely landfall/strike timing in addition to location
- **Data Type:** Forecast ensembles with variability in storm speed/track length over time
- **Audience:** Operational users sensitive to timing (e.g., emergency planning)

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your ensemble has negligible speed variability (timing nearly fixed across members)
- **Reason:** Then the representative set’s median-speed depiction may be adequate [@liuVisualizingUncertainTropical2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** The visualization may understate or misstate arrival-time uncertainty
- **The Risk:** Decision makers may under/overestimate when impacts occur [@liuVisualizingUncertainTropical2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add many extra tracks solely to show varying track lengths
- **Why it fails:** Increasing track count to show speed uncertainty increases clutter and harms readability [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** At a given time slice, representative-track points cluster in a narrower range along-track than the full ensemble points
- **The Test:** Compare ensemble positions vs representative positions at the same forecast hour; if forward-direction spread collapses, speed uncertainty is not conveyed [@liuVisualizingUncertainTropical2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit note or separate element indicating that strike-time uncertainty is not fully represented
- **Best Fix:** Use an alternative point-based or dedicated approach to show speed uncertainty rather than overloading the track display (the paper illustrates that common add-ons like extra glyphs or dashed alternative tracks create clutter) [@liuVisualizingUncertainTropical2019]

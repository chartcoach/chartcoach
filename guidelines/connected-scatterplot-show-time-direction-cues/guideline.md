---
id: connected-scatterplot-show-time-direction-cues
title: Show the Direction of Time Explicitly
bibliography: references.bib
description: Prevent misreads by making the temporal direction unambiguous in connected
  scatterplots.
labels:
- chart:scatter
- task:interpret
- visual:annotation
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
---

## The Rule <!-- role: advice -->

Show an explicit, in-chart cue for the direction of time in a connected scatterplot (e.g., arrowheads or clearly marked start/end).

## The Logic <!-- role: reason -->

Viewers can reverse the intended temporal sequence even on simple tasks when time is encoded only by a connecting path; explicit cues reduce ambiguity about the reading direction.

- **The Principle:** Sequence disambiguation when time is implicit
- **The Evidence:** In translation/copy tasks, participants reversed time in connected scatterplots (including simple copying) and did so more often when translating between formats [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret the progression over time (what happened first/next).
- **Data Type:** Two paired time series shown as a connected path.
- **Audience:** General-public or first-time viewers of the technique.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A fully guided explanation accompanies the chart and explicitly states start/end and progression.
- **Reason:** Direction may be redundantly communicated elsewhere, reducing reliance on in-chart cues [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added visual clutter and less minimal aesthetics.
- **The Risk:** Direction markers may overlap in dense regions, reducing legibility.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming the audience will infer direction from an “obvious” left-to-right flow without explicit markers.
- **Why it fails:** Participants still reversed time even when working directly with a connected scatterplot [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** A viewer could plausibly read the path from either end with no contradiction.
- **The Test:** Cover any explanatory text; ask “where does time start?” If multiple answers seem plausible, you need stronger cues.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add arrowheads along the path and/or label “Start” and “End.”
- **Best Fix:** Combine start/end labeling with additional temporal encoding (e.g., clear progression markers) so direction remains clear in dense or looping sections [@harozConnectedScatterplotPresenting2016].

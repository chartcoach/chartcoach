---
id: add-playback-controls-and-frame-index-to-hops
title: Add Playback Controls and Frame Indexing to HOPs
bibliography: references.bib
description: Support counting and paced viewing by providing pause/step controls and
  visible frame numbering for HOPs.
labels:
- chart:animation
- task:estimate
- visual:interaction
- impact:usability
- data:uncertainty
- audience:novice
- uncertainty:hops
---

## The Rule <!-- role: advice -->

Provide pause/play plus step-forward/step-back controls and show a frame number in HOPs.

## The Logic <!-- role: reason -->

HOPs shift inference toward counting and integration across discrete draws; interactive controls let viewers slow down, step through frames, and keep track while counting occurrences (e.g., frames where B > A). The study’s HOPs implementation included these controls and frame numbering explicitly to support integration/counting.

- **The Principle:** Interaction scaffolds discrete-outcome integration
- **The Evidence:** [@hullmanHypotheticalOutcomePlots2015]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating probabilities as “x out of 100” by counting or sampling frames.
- **Data Type:** Animated HOPs for one or multiple variables.
- **Audience:** Viewers who differ in preferred pace or who may choose counting strategies.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A purely decorative animation where no inference is expected.
- **Reason:** If you don’t want viewers to infer frequencies from frames, controls can encourage over-interpretation. (No direct evidence for this in the paper, so avoid HOPs in that case.) [@hullmanHypotheticalOutcomePlots2015]

## The Price <!-- role: costs -->

- **The Sacrifice:** More UI complexity and space.
- **The Risk:** Some viewers may over-focus on manual stepping, increasing time-on-task without improving accuracy. [@hullmanHypotheticalOutcomePlots2015]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Autoplay-only HOPs with no way to pause or step.
- **Why it fails:** It removes user control needed for counting or careful comparison, undermining one of HOPs’ core interpretive advantages. [@hullmanHypotheticalOutcomePlots2015]

## How to Check <!-- role: check -->

- **Visual Sign:** Users attempt to count but lose their place or complain the animation is too fast/too slow.
- **The Test:** Ask users to estimate Pr(B > A); observe whether they try to pause/step—if they can’t, the design blocks common strategies described by HOPs’ rationale. [@hullmanHypotheticalOutcomePlots2015]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a pause button and a single-step forward control.
- **Best Fix:** Add pause/play, step forward/back, and a visible frame counter so users can count occurrences and estimate denominators. [@hullmanHypotheticalOutcomePlots2015]

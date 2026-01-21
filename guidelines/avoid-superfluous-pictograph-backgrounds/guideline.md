---
id: avoid-superfluous-pictograph-backgrounds
title: Avoid Superfluous Pictograph Backgrounds
bibliography: references.bib
description: Do not add decorative background images that are not part of the data
  encoding because they reduce recall and slow use.
labels:
- chart:bar
- task:recall
- visual:imagery
- impact:clarity
- data:categorical
- audience:general
- embellishment:background
- source:haroz-chi2015
---

## The Rule <!-- role: advice -->

Do not add superfluous (non-data) pictograph imagery as a background or decoration in charts.

## The Logic <!-- role: reason -->

Superfluous imagery competes for attention without providing usable cues for the values, increasing distraction during encoding and retrieval and slowing lookup.

- **The Principle:** Task-irrelevant visual competition harms performance
- **The Evidence:** Superfluous background pictographs increased recall error (Exp. 1) and increased response time in value-comparison tasks (Exp. 4) [@harozISOTYPEVisualizationWorking2015a].

## Where to Apply <!-- role: context -->

- **User Goal:** Remember recently viewed values; quickly answer “more/fewer” questions from a chart
- **Data Type:** Small categorical sets (e.g., 3 bars) with numeric magnitudes
- **Audience:** General viewers in time-limited or accuracy-critical contexts

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is purely decorative branding and performance/accuracy are not important
- **Reason:** The paper’s measured costs are specifically about speed and memory performance; if those are irrelevant, the tradeoff may be acceptable [@harozISOTYPEVisualizationWorking2015a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less decorative richness and thematic “infographic” styling
- **The Risk:** A plainer look may reduce initial visual appeal (even though embedded pictographs can still increase engagement) [@harozISOTYPEVisualizationWorking2015a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a faint/transparent background pictograph “so it won’t distract”
- **Why it fails:** Even when the image is not encoding data, it still adds competing structure and was associated with worse memory and slower responses in the tested tasks [@harozISOTYPEVisualizationWorking2015a].

## How to Check <!-- role: check -->

- **Visual Sign:** A large image behind the plotting area that does not correspond to any data mark
- **The Test:** Remove the background image and re-check whether the chart is faster to interpret and easier to recall (A/B test on the target tasks) [@harozISOTYPEVisualizationWorking2015a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the background illustration entirely.
- **Best Fix:** If you want pictographs, use them as the data marks (stacked or stretched pictographs) rather than as decoration [@harozISOTYPEVisualizationWorking2015a].

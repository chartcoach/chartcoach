---
id: choose-spatiotemporal-viz-for-direction-task
title: "Choose animated maps for speed or static maps for accuracy when tracking propagation direction"

tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - chart:map
  - chart:map.animated
  - chart:map.small-multiples
  - task:direction
  - task:trend
  - data:spatiotemporal
  - medium:animation
  - medium:interactive

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "The paper identified a speed-accuracy trade-off for the 'Direction' task. Animation was fastest but more error-prone, while static views (small multiples, glyphs) were slower but more accurate."

examples:
  - type: good
    description: "An animated map allows for rapid perception of movement, making it the fastest way to get a general sense of propagation direction."
  - type: bad
    description: "Relying solely on the speed of an animated map can lead to mistakes; the study found it to be the most error-prone method for determining direction."
  - type: good
    description: "A small-multiples view, while slower to process, allows for careful, deliberate comparison of consecutive frames, leading to higher accuracy in direction-finding."
---

## Guidance

When analyzing the direction of spatiotemporal propagation, choose your visualization based on the trade-off between speed and accuracy:
- For the **fastest** assessment, use an **animated map**.
- For the most **accurate** assessment, use a **static map** (like small multiples).

## Why

There is a speed-accuracy trade-off for this task. The human visual system is highly attuned to motion, which allows animated maps to provide a very fast, intuitive sense of direction. However, this speed can come at the cost of precision, leading to more errors. Static representations like small multiples force a more deliberate, side-by-side comparison, which is slower but less prone to error.

## When it applies

- When the task is to determine if a phenomenon is spreading in a consistent direction (e.g., north-to-south, outward from a central point).
- When deciding whether to prioritize quick insights or analytical rigor.

## Exceptions

- If the propagation is very slow or subtle, the motion cue in an animation may be too weak to be effective, diminishing its speed advantage.
- If the primary user is giving a presentation, the narrative quality and high user confidence associated with animation may outweigh the risk of minor inaccuracies.

## Trade-offs

- **Speed vs. Accuracy:** This is the central trade-off. Animated maps prioritize speed; static maps (small multiples) prioritize accuracy.
- **User Confidence:** Users report higher confidence with animation, even when they are less accurate. This can be a risk if a feeling of confidence is mistaken for correctness.

## Signs of Trouble

- **Frequent Errors with Animation:** When using an animated map, post-hoc analysis reveals that users frequently misidentify the primary direction of spread or miss secondary propagation fronts.
- **Slow Analysis with Static Maps:** When using small multiples, users complain that determining the overall direction takes too long or feels tedious.

## How to Improve

- **Prioritizing Speed:** If your current static map feels too slow for direction-finding, switch to an animated map but advise users to double-check their initial assessment.
- **Prioritizing Accuracy:** If your animated map is leading to errors, switch to a small-multiples layout. This will slow down the analysis but increase the reliability of the results.
- **Balanced Approach:** Use an animated map for an initial, quick assessment, and then switch to or supplement with a small-multiples view for confirmation and more detailed analysis.
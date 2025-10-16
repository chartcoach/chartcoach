---
id: avoid-map-glyphs-for-spatial-jumps
title: "Avoid using maps with glyphs to detect spatial jumps in propagation"

tags:
  - impact:cognitive
  - impact:perceptual
  - impact:performance
  - chart:map
  - chart:map.glyphs
  - task:find-anomalies
  - data:spatiotemporal
  - medium:interactive
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "The study found that maps with glyphs were significantly slower and less preferred for detecting 'Hops' (spatial jumps), as they impose a high cognitive load for this task."

examples:
  - type: bad
    description: "In a map with glyphs, to see if a jump occurred from time T to T+1, a user must find the cell for T in one glyph and the cell for T+1 in another, distant glyph, and compare their context. This is cognitively very difficult."
  - type: good
    description: "In an animated or small-multiples map, the entire map for time T is replaced by the map for T+1. A new, non-adjacent colored region 'pops' into view, making the spatial jump immediately obvious."
---

## Guidance

Do not use a map with glyphs when the task is to detect non-contiguous propagation (i.e., "spatial jumps"). Use an animated map or a small-multiples layout instead.

## Why

Detecting a spatial jump requires comparing the state of the entire map between two consecutive time-steps. A map with glyphs fundamentally breaks this comparison apart; the information for time `T` and time `T+1` is fragmented across dozens of separate, tiny glyphs. Re-assembling this information mentally is cognitively demanding and highly inefficient. In contrast, both animation and small multiples preserve the spatial integrity of the map for each time-step, making a sudden appearance in a non-adjacent region a salient "pop-out" visual event.

## When it applies

- The analytical task is to identify anomalies in propagation, specifically when a phenomenon spreads to a non-adjacent geographical region between time-steps.
- Examples include a disease outbreak jumping a country due to air travel or a viral meme appearing in a disconnected social group.

## Exceptions

- There are no known exceptions where a map with glyphs would be effective for this task. The cognitive mismatch between the visualization's structure and the task's requirements is a fundamental limitation.

## Trade-offs

- The main trade-off is choosing between animation and small multiples, both of which are effective for this task. Maps with glyphs are simply the wrong tool for the job and should be avoided.

## Signs of Trouble

- **Missed Jumps:** Users completely fail to notice when the phenomenon jumps to a distant, non-adjacent location.
- **Extreme Slowness:** Users take an exceptionally long time to answer questions about spatial jumps, often having to manually check many glyphs.
- **Low Confidence:** Users report very low confidence in their answers about whether or not jumps occurred.

## How to Improve

- **Comprehensive Redesign: Replace the Glyph Map.** The most effective fix is to replace the map with glyphs entirely.
    - **Use an animated map** to show the temporal progression. Spatial jumps will appear as sudden onsets in new locations.
    - **Use a small-multiples layout** to present all time-steps statically. Jumps will be visible by scanning from one map to the next in the sequence.
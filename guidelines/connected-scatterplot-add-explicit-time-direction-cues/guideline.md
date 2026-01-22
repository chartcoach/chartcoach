---
id: connected-scatterplot-add-explicit-time-direction-cues
title: Add explicit cues for time direction in connected scatterplots
bibliography: references.bib
description: Prevent time-order reversals by explicitly encoding the direction of
  time in connected scatterplots.
labels:
- chart:scatter
- task:interpret
- visual:annotation
- impact:clarity
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Encode time direction explicitly in a connected scatterplot <!-- role: advice -->

Add an explicit, always-visible cue that shows which way time moves along the connected line. Make the cue readable without relying on surrounding article text.

## Time-order is not self-evident when time is encoded by a connecting line <!-- role: reason -->

When time is not mapped to a dedicated axis, viewers must infer temporal order from secondary cues on the path, which is error-prone even for simple shapes. Misreading time direction changes the story of the data because the same geometric shape can imply opposite temporal narratives.

**Mechanism:** External direction cues reduce ambiguity about sequence, preventing viewers from mentally “playing” the path in the wrong direction.

**Evidence:** Viewers reversed the temporal ordering of points in connected scatterplots, including when simply copying a connected scatterplot (about 5% of trials) and more often when translating between formats (about 13% of trials) [@harozConnectedScatterplotPresenting2016].

**Notes:** Arrows were commonly used in real examples but were not sufficient to eliminate reversals in the measured tasks.

## Situations where time-direction cues matter most <!-- role: context -->

- **User Goal:** Understand how the relationship between two variables evolves over time.
- **Task:** Determine “what happens next,” identify phases, or compare earlier vs later segments.
- **Data:** Paired time series rendered as a connected path; direction is not obvious from monotonic movement.
- **Chart Setting:** Static graphics, thumbnails, or any view where the reader may not read accompanying explanatory text.
- **Audience:** Viewers unfamiliar with the connected scatterplot format.
- **Success Criterion:** Readers consistently identify start vs end and do not tell the story backward.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart uses an alternative unambiguous encoding of time direction (for example, clearly marked start/end points that are always visible at the viewing size). **Why:** Additional direction cues may be redundant and add visual clutter.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional marks and visual complexity on an otherwise simple path. **Risk:** Over-annotation can clutter the path and compete with labels or highlights. **Mitigation:** Keep the cue lightweight and consistently applied across the entire path.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming that a reader will infer time direction from the path’s overall left-to-right progression. **Why it fails:** Viewers still reversed time, even in tasks where the connected scatterplot only needed to be copied [@harozConnectedScatterplotPresenting2016].
- **Mistake:** Relying on surrounding prose to explain direction instead of encoding it in the chart. **Why it fails:** The visualization becomes non-self-contained, especially in thumbnails or skimming contexts [@harozConnectedScatterplotPresenting2016].

## Quick tests for time-direction clarity <!-- role: check -->

**Failure Sign:** A viewer can describe two opposite temporal stories from the same connected shape. **Quick Check:** Ask a colleague to point to the start and end without reading any text. **Stronger Test:** Run a small pilot where viewers translate or summarize the chart; measure time-order reversals.

## What to do instead <!-- role: fix -->

- Add start and end markers that remain visible at small sizes.
- Add repeated directional indicators along the path so direction remains clear in dense or looping segments.
- If direction still confuses viewers, switch to a dual-axis line chart where time is explicitly mapped to an axis.

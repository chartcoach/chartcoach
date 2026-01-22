---
id: test-trend-understanding-with-analysis-level-questions
title: Test trend understanding with an analysis question that names a series and
  asks how it changes over time
bibliography: references.bib
description: Assess whether viewers can correctly characterize trends by prompting
  a focused trend description.
labels:
- chart:time-series
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:general
- method:user-study
---

## Ask a focused trend-description question for a named entity or series <!-- role: advice -->

Include an analysis-level prompt that names a specific series (such as a county or category) and asks how its values changed over time.

## Why focused trend questions expose structural misreadings <!-- role: reason -->

Trend understanding requires relating parts of the display in sequence; if the structure prevents correct sequencing, viewers may confidently report the wrong trend. A targeted trend prompt reveals whether the chart supports temporal reasoning rather than only value reading.

**Mechanism:** Trend description forces viewers to integrate multiple marks in order, making mis-ordering or misleading layout more likely to surface as incorrect qualitative descriptions.

**Evidence:** When dates were not in chronological order, participants more often mischaracterized the trend direction and were far less likely to notice distribution shape (e.g., bi-modality) than with a chronological redesign, even though both charts displayed the same underlying values [@burnsHowEvaluateData2020]. In another case, different encodings led to different likelihood of describing immigration as increasing, indicating that analysis-level prompts can detect design effects missed at other levels [@burnsHowEvaluateData2020].

**Notes:** Coding can tag whether responses mention trend direction, shape features, or other pre-defined descriptors.

## When a trend-analysis prompt applies <!-- role: context -->

- **User Goal:** Determine whether the chart supports correct “over time” understanding.
- **Task:** Describe direction, changes, and notable shapes (peaks, multiple modes) for a named series.
- **Data:** Temporal or ordered data where sequence matters.
- **Chart Setting:** Static displays where ordering is a key part of the encoding.
- **Audience:** General readers who may not scrutinize axis ordering.
- **Success Criterion:** Correct qualitative characterization of trend direction and shape.

## When not to rely on a trend-analysis prompt <!-- role: exceptions -->

**Break it when:** The chart is not intended to communicate sequence (e.g., sorted-by-value displays where time is not the semantic x-axis). **Why:** A trend question will test an interpretation the design does not aim to support.

## Tradeoffs of trend-description evaluation <!-- role: costs -->

**Sacrifice:** Requires qualitative coding to decide what counts as a “trend mention” or “shape mention.” **Risk:** Participants may give underspecified answers (“it changed a lot”). **Mitigation:** Keep the prompt specific about the entity and timeframe.

## Common mistakes with trend prompts <!-- role: mistakes -->

- **Mistake:** Asking for “the trend” without naming the series. **Why it fails:** Participants may describe different subsets, making results incomparable.
- **Mistake:** Scoring only whether a response is positive/negative. **Why it fails:** It can miss important differences in noticing shape features that affect interpretation.

## Quick checks for trend-support problems <!-- role: check -->

**Failure Sign:** Many participants describe a monotonic increase/decrease when the data has reversals or multiple peaks.\
**Quick Check:** Verify participants can correctly name the earliest and latest time points from the axis labels.\
**Stronger Test:** Compare coded trend descriptions across two designs that differ only in ordering or grouping.

## What to do instead if trend understanding is unreliable <!-- role: fix -->

- Re-encode the x-axis to enforce chronological order when time is the intended reading.
- Separate or group series to reduce the need for mental reordering.
- Add explicit annotations that clarify the intended temporal sequence.
- Use small multiples or faceting by category if overplotting or grouping hides within-series change.

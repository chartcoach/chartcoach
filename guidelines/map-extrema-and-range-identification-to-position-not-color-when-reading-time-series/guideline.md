---
id: map-extrema-and-range-identification-to-position-not-color-when-reading-time-series
title: Map extrema and range identification to position encodings rather than color
  encodings (when scanning time-series values)
bibliography: references.bib
description: Position encodings can support more accurate extraction of extrema and
  range than color encodings in time-series aggregation tasks.
labels:
- chart:time-series
- task:identify
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Use position to find minima, maxima, and range in time-series displays <!-- role: advice -->

Map values to position when you expect viewers to locate minima/maxima or estimate the range over time or across series. Treat color encodings as secondary for these identification tasks.

## Why position helps extrema/range identification <!-- role: reason -->

Extrema and range are defined by boundary values, and positional encodings preserve boundary shapes in a way that supports locating and comparing endpoints across many marks.

**Mechanism:** Position supports visually identifying boundary properties (highest/lowest and span), which aligns with identification tasks that depend on detecting endpoints rather than averaging.

**Evidence:** In aggregation tasks on time-series visualizations, extrema and range were estimated more accurately from positional encodings than from color encodings, even though mean/variance showed the opposite pattern [@szafirFourTypesEnsemble2016a].

**Notes:** This is about extracting extremes across many values, not reading a single labeled value.

## When you should apply this mapping choice <!-- role: context -->

- **User Goal:** Quickly find highs/lows and assess the spread of values.
- **Task:** Identify minimum, maximum, outlier-like extremes, or overall range across time windows/groups.
- **Data:** Temporal series or multiple series where extremes matter operationally.
- **Chart Setting:** Line charts, stacked small multiples, or aggregated time-series overviews.
- **Audience:** Analysts or general readers who need fast identification of peaks/troughs.
- **Success Criterion:** Faster and more accurate agreement on which time window/series contains the extremes and widest range.

## When not to follow this guideline <!-- role: exceptions -->

- **Break it when:** The primary questions are mean or variance comparisons across subsets. **Why:** Color encodings can better support mean/variance extraction than positional encodings in the studied aggregation context.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Position-based displays can make aggregate summaries like mean/variance harder than color-based summaries for the same data. **Risk:** Viewers may over-focus on prominent peaks and miss overall distributional context. **Mitigation:** Pair the positional view with a summary-oriented encoding when both tasks are required.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding the key “extreme-sensitive” variable only with color in a dense time-series overview. **Why it fails:** Extrema and range judgments are less accurate from color than from position in the evaluated aggregation tasks.

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot reliably answer “which month has the highest peak?” or “which period has the widest range?” without prolonged searching. **Quick Check:** Time a few people answering extrema/range questions from the chart; long times and inconsistent answers indicate mismatch. **Stronger Test:** Compare accuracy on extrema/range questions between a position-encoded and color-encoded prototype.

## What to do instead when this fails <!-- role: fix -->

- Switch the primary encoding of the extreme-sensitive measure to position (e.g., height or vertical location).
- Add a second view that uses color for mean/variance summaries if summary tasks are also important.
- Reduce visual clutter by splitting series into small multiples so positional extremes remain legible.

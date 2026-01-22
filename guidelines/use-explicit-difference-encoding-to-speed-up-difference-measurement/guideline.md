---
id: use-explicit-difference-encoding-to-speed-up-difference-measurement
title: "Use explicit difference encoding to reduce time when measuring a specific\
  \ category\u2019s change"
bibliography: references.bib
description: For measuring the change for a given category between two series, explicit
  difference encodings reduce completion time compared to grouped bars.
labels:
- chart:bar
- task:aggregate
- task:compare
- visual:position
- impact:speed
- data:categorical
- audience:novice
- comparison:multi-series
---

## Use explicit differences to measure a category’s change faster <!-- role: advice -->

When the task is to report the change for a specific category between two series, use a chart that explicitly encodes the difference (difference chart or difference overlays) rather than only a grouped bar chart. This reduces task completion time.

## Why explicit differences reduce time for difference measurement <!-- role: reason -->

When differences are encoded directly, viewers can read the change without computing it from two separate bars.

**Mechanism:** Explicit difference marks remove the need for per-category subtraction, reducing cognitive steps and speeding up responses.

**Evidence:** For measuring the difference for a category, the difference chart and the difference-overlay charts ranked faster than the grouped bar chart, with significant effects of chart design on completion time reported for this task across conditions [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about time; the structured evidence does not show a clear accuracy separation among designs for this task.

## When difference measurement applies <!-- role: context -->

- **User Goal:** Determine the size of change for a specified category (not just identify which is largest).
- **Task:** Measure a specific difference between series for one category.
- **Data:** Two-series categorical/ordinal categories with numeric values (change may be positive or negative).
- **Chart Setting:** Dashboard-style view where users answer targeted questions quickly.
- **Audience:** Mixed literacy; readers who benefit from reduced mental arithmetic.
- **Success Criterion:** Lower time to produce the correct numeric difference.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Differences are not meaningful or should not be emphasized relative to original values. **Why:** Explicit difference marks can shift attention away from original magnitudes.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More visual encodings increase chart complexity. **Risk:** Users may confuse the meaning of the difference marks if they are not visually distinct from the value marks. **Mitigation:** Use a clearly different mark type for differences than for values.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using grouped bars and expecting quick, precise difference entry. **Why it fails:** The viewer must compute differences mentally, which slows response.

## Quick tests <!-- role: check -->

**Failure Sign:** People pause to subtract values before responding. **Quick Check:** Ask a reader to state the change for one category aloud; if they start calculating from two bars, the chart is not optimized for this task. **Stronger Test:** Compare median completion time for the same difference-measurement prompts across chart designs.

## What to do instead <!-- role: fix -->

- Use a difference chart when the dashboard question is primarily about changes.
- Use grouped bars with difference overlays when users also need to reference both original values.
- Provide a companion table of exact differences if the task demands precise numeric reporting under time pressure.

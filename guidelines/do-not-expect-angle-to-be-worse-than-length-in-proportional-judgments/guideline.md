---
id: do-not-expect-angle-to-be-worse-than-length-in-proportional-judgments
title: Do not assume angle is less accurate than length for proportional judgments
bibliography: references.bib
description: Angle encodings did not underperform length encodings in the tested proportional
  judgment format.
labels:
- chart:pie
- task:estimate
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Do not treat angle as automatically worse than length for proportional estimates <!-- role: advice -->

When choosing between angle and length for proportional estimation, do not assume angle will be less accurate than length without testing in your specific task format.

## Why angle can match length in this task format <!-- role: reason -->

Relative performance among non-position encodings can be task- and stimulus-format dependent, and the expected theoretical ordering is not guaranteed under a given judgment protocol.

**Mechanism:** Both angle and length require normalization to infer a percentage; depending on how comparisons are cued and presented, these demands can be comparable.

**Evidence:** In proportional-judgment stimuli designed to be comparable across encodings, angle judgments did not perform worse than length judgments, consistent with prior findings that also did not show angle underperforming length in comparable tasks [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** This does not imply angle is best-in-class; position on a common scale still outperformed both.

## When this guideline applies <!-- role: context -->

- **User Goal:** Estimate proportional differences, not just identify larger/smaller.
- **Task:** Percentage judgment between two marked values.
- **Data:** Quantitative values displayed as either length marks or angle sectors.
- **Chart Setting:** Considering a pie/angle-based design vs bar/length-based design for ratio estimation.
- **Audience:** General audiences with variable visualization literacy.
- **Success Criterion:** Avoid unjustified encoding choices based on assumed rankings.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your intended task is not proportional estimation (e.g., scanning for extremes across many categories). **Why:** This evidence is specific to proportional-judgment accuracy, not all chart-reading tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Testing multiple encodings adds evaluation overhead. **Risk:** Taking this as license to prefer angle widely can still harm accuracy relative to position encodings. **Mitigation:** Treat this as a warning against assumptions, not a blanket endorsement.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Rejecting angle encodings solely because of a presumed “angle < length” accuracy rule. **Why it fails:** The tested proportional-judgment results did not show angle performing worse than length.

## Quick tests <!-- role: check -->

**Failure Sign:** Encoding decisions are justified only by generic ranking lore rather than task-fit evidence. **Quick Check:** Create one angle and one length version and ask a few users for percentage estimates; compare absolute errors. **Stronger Test:** Run a small crowdsourced proportional-judgment study with verifiable checks and compare error distributions.

## What to do instead <!-- role: fix -->

- Prefer position on a common scale if you can support it.
- If constrained to non-position encodings, prototype both angle and length and measure proportional error with your actual data ranges.
- Add labels or reference cues to reduce normalization effort for either encoding.
- Use redundant cues (e.g., label + mark) when the consequence of misestimation is high.

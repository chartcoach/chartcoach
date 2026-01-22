---
id: avoid-encoding-secondary-quantitative-with-size-when-primary-is-on-position
title: Prefer color over size for the secondary quantitative field when the primary
  quantitative field is on position
bibliography: references.bib
description: When a primary quantitative field is encoded on x or y in trivariate
  point plots, encoding the secondary quantitative field with size can slow value
  tasks more than using color.
labels:
- chart:scatter
- task:retrieve-value
- visual:size
- impact:speed
- data:quantitative
- audience:general
- complexity:advanced
---

## Use color instead of size for the secondary quantitative field in value-focused point plots <!-- role: advice -->

When the primary quantitative field is encoded on x or y, encode the secondary quantitative field with color rather than size if users are doing value-reading or value-comparison tasks.

## Why size can interfere with position-based value reading <!-- role: reason -->

A varying-size channel can act as a distractor when users are trying to decode a position-encoded primary value, increasing the time required to answer value questions.

**Mechanism:** Size variation adds an additional perceptual dimension that competes for attention and can hinder efficient lookup of positional values.

**Evidence:** For value tasks, designs with the secondary quantitative field encoded as size were slower than comparable designs with the secondary field encoded as color (e.g., Q2:size vs Q2:color) while the primary field remained position-encoded; this timing penalty appears consistently in the reported task-focused rankings [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

**Notes:** This is a speed-focused guideline; accuracy patterns may differ by task and condition.

## When you should apply this <!-- role: context -->

- **User Goal:** Answer questions primarily about the primary quantitative field while still seeing a secondary quantitative field.
- **Task:** retrieve-value, sort (as used for value comparisons), find-extremum (when framed around primary-field maxima).
- **Data:** One categorical field plus two quantitative fields in a point-based plot.
- **Chart Setting:** Dense scatter-like display where marks are simultaneously visible.
- **Audience:** General audiences under time pressure (dashboards, monitoring, quick checks).
- **Success Criterion:** Faster completion time without giving up the ability to see the secondary field.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s task is to decode the secondary quantitative field itself (not merely keep it visible). **Why:** The evidence addresses time costs when the task focus is on the primary field.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Encoding the secondary quantitative field with color may reduce the precision of decoding that secondary field compared to size in some contexts. **Risk:** Using color for Q2 may introduce interpretability issues if users expect color to represent categories. **Mitigation:** Use clear legends and keep the categorical field on a distinct channel (e.g., position-based grouping or faceting) when feasible.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Defaulting to “size for quantitative” for the secondary field whenever x and y are already used. **Why it fails:** It can make value-focused tasks slower when users must read the primary value from position while ignoring size variation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users take noticeably longer on simple value questions even though the primary value is on an axis. **Quick Check:** Temporarily switch Q2 from size to color and see if the plot becomes faster to read for “which is larger?” questions about the primary field. **Stronger Test:** A/B test Q2:size vs Q2:color with timed retrieve-value questions.

## What to do instead <!-- role: fix -->

- Encode the secondary quantitative field with color (and keep the primary quantitative field on x or y).
- If color is already reserved for categories, move the categorical field to another channel used in the study designs (e.g., positional grouping or row faceting) and free color for the secondary quantitative field.
- Remove the secondary quantitative encoding entirely when the user’s questions do not require it.

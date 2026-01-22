---
id: prefer-position-along-a-common-scale-for-proportional-judgments
title: Prefer position along a common scale for proportional judgments
bibliography: references.bib
description: Position on a shared axis yields more accurate proportional estimates
  than length, angle, or area encodings.
labels:
- chart:comparative
- task:estimate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:foundational
---

## Prefer position on a shared axis for proportional estimates <!-- role: advice -->

Use position along a common scale when viewers must estimate one value as a percentage of another. Avoid switching that task to length, angle, or area encodings if accuracy matters.

## Why shared-axis position improves proportional accuracy <!-- role: reason -->

Position on a common axis supports direct spatial comparison with minimal intermediate inference, while length, angle, and area require additional perceptual/mental transformations that increase error.

**Mechanism:** A shared reference frame reduces the need to normalize marks mentally, improving proportional decoding accuracy.

**Evidence:** In proportional judgment tasks replicated via crowdsourcing, position encodings (types using a common scale) produced lower log absolute error than length, and both outperformed area; results preserved the same ranking pattern observed in prior lab findings [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** Crowdsourced results showed higher variance, but the relative ordering across encodings remained stable.

## When proportional-position encodings are the right fit <!-- role: context -->

- **User Goal:** Compare two quantities as a percent of the larger (or similar proportional relationship).
- **Task:** Quick visual judgment of proportional differences.
- **Data:** Two highlighted quantitative values (or two values among many).
- **Chart Setting:** Static or lightly interactive charts where accurate decoding matters.
- **Audience:** Mixed or unknown audiences, including non-experts.
- **Success Criterion:** Lower estimation error for proportional comparisons.

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You cannot allocate a shared axis due to severe space constraints or the need to emphasize part-to-whole composition. **Why:** The design constraint may force non-position encodings even if they are less accurate.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Shared-axis position encodings can consume more layout space than compact area or angle displays. **Risk:** Forcing a shared axis into a cramped layout may reduce legibility overall. **Mitigation:** Consider reducing the number of compared items or using interaction to reveal details on demand.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using angle or area marks for ratio comparisons because they look visually “intuitive.” **Why it fails:** These encodings produce larger proportional judgment error than position on a common scale in the tested tasks.

## Quick tests <!-- role: check -->

**Failure Sign:** People give noticeably inconsistent percentage estimates for the same comparisons. **Quick Check:** Ask a few readers to estimate a simple percentage (e.g., “smaller as % of larger”) and compare spread across encodings. **Stronger Test:** Run a small proportional-judgment pilot with your candidate encodings and compare absolute or log error.

## What to do instead if you cannot use shared-axis position <!-- role: fix -->

- Use a length encoding with a shared baseline as a fallback when position on a shared axis is not feasible.
- Add explicit reference guides (ticks or labels) to reduce mental normalization demands.
- Reduce reliance on proportional estimation by directly labeling values or differences.
- Reframe the question to a simpler comparison (e.g., which is larger) if the display cannot support accurate ratio judgments.

---
id: expect-non-round-truncation-starts-to-increase-value-estimation-error
title: Expect Non-Round Truncation Starts to Increase Value Estimation Error
bibliography: references.bib
description: Starting a y-axis at an awkward value (e.g., 25%) can make individual
  value estimation harder.
labels:
- chart:bar
- task:estimate
- visual:axis
- impact:accuracy
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

Avoid truncation start points that make mental conversion difficult (e.g., 25%); if you must truncate, prefer start points that are easier to anchor and interpolate.

## The Logic <!-- role: reason -->

Some truncation baselines are harder for viewers to mentally map back to the original 0–100% frame, increasing error in estimating individual values.

- **The Principle:** Hard-to-anchor scales increase cognitive conversion load and estimation error.
- **The Evidence:** In Experiment 3, magnitude/value estimation error (Emagnitude) differed significantly by truncation level, with the 25% start producing higher error than other levels; participants reported difficulty interpreting that scale [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Reading or estimating individual values from bars.
- **Data Type:** Percent-like scales or other bounded quantitative ranges where users expect intuitive anchors.
- **Audience:** General viewers doing quick read-offs rather than careful calculation [@correllTruncatingYAxisThreat2020a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is qualitative severity judgment rather than numeric read-off.
- **Reason:** The paper’s main finding is that severity inflation persists regardless; avoiding “awkward” baselines addresses value estimation error, not severity bias [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a preferred tight framing if it requires an awkward baseline.
- **The Risk:** Choosing a “convenient” baseline might still inflate severity; it only reduces one kind of error [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking an arbitrary non-zero start (like 25%) just because it creates a desired visual spread.
- **Why it fails:** It can increase value estimation error due to harder anchoring and conversion [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Reviewers hesitate or disagree when reading bar values off the chart.
- **The Test:** Ask a few people to estimate specific bar values; if errors spike at certain baselines (notably 25% in the study), the baseline is likely hard to use [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change the truncation start to a more readily anchored value.
- **Best Fix:** If value read-off matters, avoid truncation levels that force constant mental conversion; choose a scale that supports estimation while acknowledging truncation still affects perceived severity [@correllTruncatingYAxisThreat2020a].

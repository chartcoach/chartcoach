---
id: assume-y-axis-truncation-inflates-perceived-effect-size
title: Assume Y-Axis Truncation Inflates Perceived Effect Size
bibliography: references.bib
description: "Treat raising the y-axis baseline as a reliable way to increase viewers\u2019\
  \ perceived severity of differences."
labels:
- chart:bar
- chart:line
- task:judge
- task:compare
- visual:axis
- visual:position
- impact:integrity
- impact:clarity
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

Assume that starting the y-axis above zero will make viewers judge differences as more severe, even when the underlying numbers are unchanged.

## The Logic <!-- role: reason -->

Axis truncation visually magnifies differences by expanding a narrower range to fill the same vertical space, which increases subjective severity judgments.

- **The Principle:** Visual magnification drives qualitative effect-size judgments.
- **The Evidence:** Across three crowdsourced experiments, increasing y-axis truncation increased perceived severity ratings, robustly and significantly [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging how big/important a difference or change “feels.”
- **Data Type:** Quantitative values shown on a continuous y-axis (including percent-like scales).
- **Audience:** General audiences or mixed-statistical-literacy audiences making qualitative judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your explicit intent is to emphasize small-but-meaningful variations within a narrow range.
- **Reason:** The paper argues there is no universal “correct” perceived severity; designers may legitimately choose a range that matches the meaningful effect size they intend to communicate [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a “neutral” presentation; viewers’ severity impressions become more sensitive to your scale choice.
- **The Risk:** Viewers may over-weight minor differences and infer greater importance than warranted for the situation [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “nothing is falsified” so perception won’t change.
- **Why it fails:** The paper shows perception shifts persist even when values are readable and when viewers can accurately report numbers [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Small numeric differences look like large vertical separations or steep slopes.
- **The Test:** Re-render the same chart with a lower y-axis start (e.g., to 0) and see whether the perceived “story” changes dramatically while the numbers don’t [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Expand the y-axis range (reduce truncation) until the visual prominence better matches the importance you intend to convey.
- **Best Fix:** Choose and justify an axis range based on the magnitude of *meaningful* effect sizes for the task, rather than relying on default or aesthetically “tight” scaling [@correllTruncatingYAxisThreat2020a].

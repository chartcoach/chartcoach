---
id: avoid-truncating-y-axis-when-effect-size-judgment-matters
title: Avoid truncating the y-axis when you want viewers to judge effect size fairly
bibliography: references.bib
description: Axis truncation increases perceived effect severity even when viewers
  can read values accurately.
labels:
- chart:bar
- chart:line
- task:compare
- visual:position
- visual:length
- impact:trust
- data:ordered
- audience:general
- topic:axis-scale
---

## Use a full y-axis scale when effect-size severity should not be inflated <!-- role: advice -->

Avoid starting the y-axis above zero when you want subjective judgments of “how big” a difference or change is to be comparable across charts. Keep the y-axis start consistent across comparable views.

## Axis-range compression magnifies perceived severity <!-- role: reason -->

Truncating a y-axis reduces the plotted value range, which visually magnifies changes (steeper slopes in lines and larger apparent differences in bar heights). That visual magnification persists as a subjective impression, even when viewers can correctly report the underlying numeric values.

**Mechanism:** A narrower y-range increases the visual salience of differences, which biases viewers’ qualitative severity judgments upward.

**Evidence:** Increasing the y-axis starting point increased perceived severity, and the effect appeared for both bar charts (length) and line charts (position) under both value- and trend-framed questions [@correllTruncatingYAxisThreat2020]. This finding is included as collated graphical-perception knowledge for recommendation settings [@zengReviewCollationGraphical2023].

**Notes:** The subjective inflation persisted even when participants were prompted to estimate values, suggesting the effect is not only a failure to read axis labels.

## Where subjective effect-size judgments are the goal <!-- role: context -->

- **User Goal:** Judge how severe, important, or large a change/difference is.
- **Task:** Compare endpoints or trends (e.g., “how quickly values are changing” or “how different first vs last is”).
- **Data:** Ordered categories on x with quantitative y; small-to-moderate changes where scale choice meaningfully alters apparent magnitude.
- **Chart Setting:** Static bar or line charts where viewers make qualitative severity judgments.
- **Audience:** General audiences, including viewers who may or may not attend to axis labels.
- **Success Criterion:** Minimize bias in perceived severity while preserving interpretability.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your purpose is to intentionally emphasize small differences as more severe than they would appear under a full-range scale. **Why:** Truncation predictably increases perceived severity, so it is not neutral for effect-size communication.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose visual resolution for small differences when the y-axis spans a larger range. **Risk:** Small but meaningful changes can become harder to see, potentially reducing sensitivity for some analytic uses. **Mitigation:** Consider whether the goal is detecting small changes or judging their magnitude fairly.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Truncating the y-axis to “improve readability” without accounting for subjective severity inflation. **Why it fails:** The design change systematically increases perceived severity across bar and line charts.
- **Mistake:** Assuming that prompting viewers to read values (or that they are graph-literate) eliminates truncation bias. **Why it fails:** Severity inflation persisted even when viewers estimated values and could answer truncation-related literacy checks.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe changes as “dramatic” or “extreme” for datasets where the numeric differences are modest. **Quick Check:** Re-render the same chart with a lower y-axis start and see if the perceived “severity” changes substantially. **Stronger Test:** Run a small internal A/B test asking viewers to rate perceived severity with different y-axis start points.

## What to do instead <!-- role: fix -->

- Use a y-axis start that preserves a stable interpretive frame across comparable charts, rather than tightening the range to amplify differences.
- Present multiple views with different y-axis ranges (e.g., a context view and a focus view) when both small changes and fair severity judgment matter.
- Add explicit textual framing that states the actual numeric change (e.g., “increase from A to B”) when viewers may otherwise rely on visual magnitude.
- Switch the presentation to a form where the question focuses on numeric differences directly (e.g., emphasizing reported deltas) if subjective severity should be anchored in numbers.

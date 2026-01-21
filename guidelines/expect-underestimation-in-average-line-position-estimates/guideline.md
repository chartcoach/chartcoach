---
id: expect-underestimation-in-average-line-position-estimates
title: Anticipate Underestimation in Average Line Position Judgments
bibliography: references.bib
description: Average position judgments from line charts can be systematically underestimated,
  even though position is generally precise.
labels:
- chart:line
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- phenomenon:systematic-bias
---

## The Rule <!-- role: advice -->

Anticipate that viewers will underestimate the average vertical position of a line when they report an average from a line chart.

## The Logic <!-- role: reason -->

- **The Principle:** Systematic bias in positional averaging for lines (underestimation).
- **The Evidence:** The collated graphical perception record in [@zengReviewCollationGraphical2023] includes experimental evidence that average position reports for a single line (PY encoding with a line mark) are biased toward underestimation [@xiongBiasedAveragePosition2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating or recalling an average level (“on average, how high is this series?”).
- **Data Type:** Quantitative values encoded by vertical position (positionY) in a line chart.
- **Audience:** Any audience doing quick perceptual averaging (e.g., dashboard viewers).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is not to report an average (e.g., reading an exact labeled value, or comparing labeled endpoints).
- **Reason:** This guideline is grounded specifically in an average-position (aggregate) estimation context from the collated study record [@xiongBiasedAveragePosition2020], as summarized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional communication or validation steps if you want viewers to take away an unbiased “average” impression.
- **The Risk:** Over-correcting for a bias that may not be relevant if your users are not doing average estimation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “position is always unbiased” because it is a high-precision channel.
- **Why it fails:** The reported evidence shows systematic underestimation can occur even for positional encoding of averages in line charts [@xiongBiasedAveragePosition2020], as collated by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ takeaway about the series’ “typical level” skews lower than what the data’s average supports.
- **The Test:** Ask a small sample of users to estimate the series’ average level; compare their responses to the true mean (or intended “average” reference).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit visual reference for the average you want users to perceive (e.g., a clearly indicated average level).
- **Best Fix:** Redesign the display so the intended average is not inferred solely from remembering/estimating average line position (keeping in mind the underestimation bias reported in [@xiongBiasedAveragePosition2020] and summarized in [@zengReviewCollationGraphical2023]).

---
id: avoid-wide-bubble-size-ranges-for-mean-estimation-when-correlated
title: Avoid wide point-area ranges in bubble scatterplots when point size correlates
  with position and viewers must estimate the mean
bibliography: references.bib
description: When size is correlated with position, widening bubble-size ranges increases
  mean-position bias and produces the worst-performing conditions.
labels:
- chart:scatter
- task:aggregate
- visual:area
- impact:bias
- data:quantitative
- audience:general
- data-characteristic:correlation
---

## Correlated size + position: do not widen bubble ranges for mean judgments <!-- role: advice -->

Avoid using a wide point-area (bubble size) range in a scatterplot when the size variable is correlated with x/y position and viewers need to estimate the mean position. Keep size ranges narrow if you must use area in this correlated setting.

## Wide size ranges amplify mean-position bias under correlation <!-- role: reason -->

When size varies strongly and is correlated with position, the perceived mean position shifts toward larger marks more strongly, increasing systematic bias in mean estimates.

**Mechanism:** Correlation clusters larger marks in particular regions, and widening the size range increases their perceptual pull, producing larger directional bias in where viewers place the mean.

**Evidence:** For area-encoded designs, higher-correlation and wider-range conditions rank as the most biased, with the wide-range/high-correlation bubble condition (E-18) ranking worst on bias and the high-correlation bubble conditions (E-15, E-18) appearing at the bottom of the bias ranking. [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023]

**Notes:** This is about bias (systematic directional shift), not just overall error magnitude.

## Applies when bubble size is correlated with position in mean-estimation tasks <!-- role: context -->

- **User Goal:** Use the mean as a reference threshold (e.g., decide which points are above/below average).
- **Task:** Aggregate (mean position estimation).
- **Data:** Quantitative x/y plus a third quantitative variable mapped to area; the third variable has medium/high correlation with position.
- **Chart Setting:** Static bubble scatterplot (area-circle marks).
- **Audience:** General audiences.
- **Success Criterion:** Lower directional bias in mean estimates.

## When not to use this rule <!-- role: exceptions -->

**Break it when:** The size variable is not correlated with position (or correlation is not present/meaningful for the intended reading). **Why:** The amplified bias pattern in this guideline is tied to correlation conditions in the evidence.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** A narrower size range reduces visual separation of the third variable. **Risk:** Differences in the third variable become harder to perceive. **Mitigation:** Use another channel for the third variable or provide an auxiliary view for reading the third dimension.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Increasing the bubble-size range to “make the third variable pop” in a mean-based scatterplot reading. **Why it fails:** Wider size ranges under correlation align with the most biased mean-estimation conditions.

## Quick tests <!-- role: check -->

**Failure Sign:** The perceived mean shifts noticeably toward the region containing the largest points when you widen the size scale. **Quick Check:** Toggle between narrow and wide size ranges while holding data constant and observe whether the implied “average” location moves. **Stronger Test:** Collect a small set of click-the-mean responses for narrow vs wide size ranges and compare directional bias.

## What to do instead <!-- role: fix -->

- Use a narrow size range if you must keep area encoding while viewers estimate the mean position.
- Replace area encoding with a lightness-based encoding for the third variable in mean-estimation contexts.
- Decouple the third variable from the mean-estimation view by using a separate chart or interaction to reveal it on demand.
- Provide an explicit computed mean marker so judgments do not depend on perceptual averaging.

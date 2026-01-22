---
id: measure-prediction-with-synthesis-level-extrapolation-question
title: Measure prediction by asking viewers to extrapolate a specific future value
  from the chart
bibliography: references.bib
description: Use a synthesis-level prediction question to evaluate how chart design
  affects extrapolation and uncertainty.
labels:
- chart:time-series
- task:predict
- visual:position
- impact:decision
- data:temporal
- audience:general
- method:user-study
---

## Ask a single-value prediction question beyond the displayed range <!-- role: advice -->

Include a synthesis-level prompt that asks for a specific numeric prediction at a defined future point (or unobserved point), based on the data shown.

## Why predictions reveal affordances beyond description <!-- role: reason -->

Extrapolation requires viewers to transform observed values into a forecast, which can be sensitive to what patterns the design makes salient and how confidently viewers commit to a number. Comparing prediction distributions can reveal differences in mean or variance even when other measures look similar.

**Mechanism:** Prediction tasks elicit constructive reasoning (extending patterns), allowing evaluation of both central tendency (average forecast) and dispersion (how much forecasts vary) across designs.

**Evidence:** Prediction questions sometimes showed no difference in mean or variance between original and redesigned charts even when earlier levels differed, indicating that design effects can be level-specific [@burnsHowEvaluateData2020]. In other cases, redesigns shifted the mean prediction and/or changed the variance of predictions, showing that synthesis-level measures can detect affordance differences missed by retrieval or summary questions [@burnsHowEvaluateData2020].

**Notes:** Analyzing both mean and variance of predictions can reveal changes in consensus as well as direction.

## When prediction questions apply <!-- role: context -->

- **User Goal:** Understand how viewers extrapolate from a visualization to a future or missing value.
- **Task:** Provide a numeric forecast for a specified entity and time.
- **Data:** Ordered sequences where extrapolation is plausible (time, rank, progression).
- **Chart Setting:** Static charts without interactivity; text response collection.
- **Audience:** Viewers expected to reason about what comes next (planning, policy, projections).
- **Success Criterion:** Differences in predicted values or dispersion that reflect changed interpretation.

## When not to use a prediction prompt <!-- role: exceptions -->

**Break it when:** There is no meaningful basis for extrapolation in the data (highly irregular sequences without an implied generative process). **Why:** Predictions will reflect guessing rather than chart-supported reasoning.

## Tradeoffs of prediction-based evaluation <!-- role: costs -->

**Sacrifice:** Some responses may be non-numeric (ranges or verbal trends) and require exclusion or separate handling. **Risk:** Predictions can be driven by prior beliefs rather than the chart alone. **Mitigation:** Keep the prompt tightly anchored to the displayed pattern and specify the exact target point.

## Common mistakes with prediction questions <!-- role: mistakes -->

**Mistake:** Allowing unconstrained prediction formats without planning analysis. **Why it fails:** Mixed formats (single numbers, ranges, text) reduce comparability and can bias which responses you analyze.

## Quick checks for prediction-task quality <!-- role: check -->

**Failure Sign:** Many participants answer with “0” or repeat the last visible value without indicating any reasoning from the trend.\
**Quick Check:** Confirm the asked-for point is clearly outside the displayed range and uniquely specified.\
**Stronger Test:** Compare both average prediction and prediction variance between designs.

## What to do instead if prediction responses are unusable <!-- role: fix -->

- Restrict the response format to a single numeric value.
- Ask for a prediction plus a short justification referencing a visible pattern.
- Change the synthesis task from forecasting to “create a new representation” when prediction is not meaningful.
- Use a nearer interpolation target (between existing points) if extrapolation is too unconstrained.

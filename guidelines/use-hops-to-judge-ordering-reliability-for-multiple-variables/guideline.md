---
id: use-hops-to-judge-ordering-reliability-for-multiple-variables
title: Use Hypothetical Outcome Plots to Judge Reliability of Variable Ordering When
  Comparing Two or More Variables
bibliography: references.bib
description: Animated Hypothetical Outcome Plots (HOPs) improve accuracy for judging
  how often one variable exceeds another in multi-variable uncertainty displays.
labels:
- chart:uncertainty
- task:compare
- visual:position
- impact:accuracy
- data:multivariate
- audience:novice
- method:hops
---

## Use HOPs for ordering probabilities across variables <!-- role: advice -->

Use Hypothetical Outcome Plots (HOPs) when the key question is how reliably one variable is larger than another (or the largest among several). Show synchronized draws per frame so viewers can directly see which variable wins on each draw.

## Why HOPs support ordering judgments <!-- role: reason -->

HOPs present uncertainty as a sequence of concrete outcomes, enabling viewers to infer ordering reliability by perceptual comparison and simple frequency estimation across frames rather than decoding abstract distribution encodings.

**Mechanism:** Viewing repeated joint draws turns a probabilistic comparison (for example, whether B exceeds A) into an observable event per frame, which supports counting/accumulating wins across frames.

**Evidence:** Viewers estimated Pr(B > A) far more accurately with HOPs than with error bars or violin plots across multiple bivariate settings, including a correlated case where static plots did not encode correlation. [@hullmanHypotheticalOutcomePlots2015]\
Viewers also estimated Pr(B > A and B > C) more accurately with HOPs than with error bars or violin plots in a trivariate setting. [@hullmanHypotheticalOutcomePlots2015]

**Notes:** This advantage held even under study conditions favorable to static summaries (normal distributions), suggesting the gain is tied to the outcome-by-outcome comparison affordance rather than distribution shape. [@hullmanHypotheticalOutcomePlots2015]

## When ordering-reliability judgments are the goal <!-- role: context -->

- **User Goal:** Decide how reliable a ranking or ordering is (for example, “How often is B larger than A?”).
- **Task:** Estimate Pr(B > A), Pr(B > A and B > C), or similar ordering probabilities.
- **Data:** Two or more uncertain quantities; may be independent or correlated.
- **Chart Setting:** Digital medium where animation/interaction is feasible.
- **Audience:** Readers without strong statistical training; mixed numeracy.
- **Success Criterion:** Lower absolute error in estimated ordering probabilities.

## When not to rely on HOPs for this <!-- role: exceptions -->

**Break it when:** The comparison depends on correlation structure but you cannot generate/show synchronized joint draws (for example, you only have independent marginal draws). **Why:** The ordering frequency depends on joint behavior, and HOPs need aligned draws per frame to faithfully convey it. [@hullmanHypotheticalOutcomePlots2015]

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Viewers must integrate information over time, which can take attention and time.\
**Risk:** Because HOPs show a finite number of frames, sampling variability can add imprecision to perceived probabilities.\
**Mitigation:** Ensure viewers can view many frames and keep the visual mapping stable across frames so comparisons remain easy. [@hullmanHypotheticalOutcomePlots2015]

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using static error bars or violin plots and expecting viewers to accurately infer Pr(B > A) by “reading overlap.” **Why it fails:** Viewers showed very large errors on bivariate and trivariate ordering probability estimates with these static summaries. [@hullmanHypotheticalOutcomePlots2015]

## Quick tests <!-- role: check -->

**Failure Sign:** People give ordering-probability answers that are wildly inconsistent with the displayed means (for example, many answers below 50% when B’s mean exceeds A’s).\
**Quick Check:** Ask a few readers to estimate “times out of 100 B > A” from the display; large spread and extreme errors indicate the encoding is not supporting the inference.\
**Stronger Test:** Run a small controlled comparison of absolute error for Pr(B > A) between your static design and a HOPs version using the same draws. [@hullmanHypotheticalOutcomePlots2015]

## What to do instead <!-- role: fix -->

- Implement HOPs by animating frames of synchronized draws and letting users pause and step through frames.
- If you must stay static, avoid claiming that viewers can accurately infer ordering reliability from error bars alone.
- Provide an explicit ordering-probability annotation when animation is not possible and ordering reliability is central.
- Reduce cognitive load by keeping axes and scales fixed across frames to preserve visual stability. [@hullmanHypotheticalOutcomePlots2015]

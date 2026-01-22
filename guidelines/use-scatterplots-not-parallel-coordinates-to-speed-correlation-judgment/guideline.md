---
id: use-scatterplots-not-parallel-coordinates-to-speed-correlation-judgment
title: Use a scatterplot (not parallel coordinates) to make correlation judgments
  faster
bibliography: references.bib
description: For the correlation task, scatterplots enable faster judgments than parallel
  coordinate plots.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:correlate
- visual:position
- impact:speed
- data:quantitative
- audience:general
- comparison:chart-type
---

## Prefer scatterplots over parallel coordinates to reduce time for correlation judgments <!-- role: advice -->

Use a scatterplot rather than a parallel coordinate plot when the user needs to judge correlation quickly between two quantitative variables. This preference applies even when the user has sufficient time to inspect the view.

## Scatterplots reduce the time needed to interpret correlation patterns <!-- role: reason -->

Time to judgment reflects how quickly viewers can extract the relevant visual cue and map it to a decision. For correlation, scatterplots present a direct spatial pattern in 2D that viewers can interpret faster than the parallel-line versus crossing-line patterns in parallel coordinate plots, which can increase cognitive effort.

**Mechanism:** A single 2D spatial pattern can be scanned and categorized faster than interpreting many line segments between two axes.

**Evidence:** In a controlled comparison for the correlate task, scatterplots ranked faster than parallel coordinate plots, with a statistically significant difference reported. [@zengReviewCollationGraphical2023; @liJudgingCorrelationScatterplots2010]

**Notes:** This guideline concerns decision time for correlation judgments and does not cover other tasks like clustering or range finding.

## When this applies: time-constrained correlation estimation <!-- role: context -->

- **User Goal:** Make a quick decision about correlation direction/strength.
- **Task:** Correlate.
- **Data:** Two quantitative variables; the user is comparing multiple pairs or operating under time pressure.
- **Chart Setting:** Static charts in reports, dashboards, or quick-look exploratory views.
- **Audience:** General audiences who can interpret scatterplots.
- **Success Criterion:** Shorter time to reach a correlation judgment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user is not performing a correlation judgment between two quantitative variables. **Why:** The evidence only supports time differences for the correlate task.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce consistency with a workflow built around parallel coordinate plots for scanning many variables. **Risk:** Over-optimizing for speed can encourage superficial correlation judgments when deeper analysis is needed. **Mitigation:** Use scatterplots for the initial correlation screen, and allow follow-up inspection as needed.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming a parallel coordinate plot is equally quick for bivariate correlation because it uses a simple two-axis layout. **Why it fails:** Time to judge correlation is slower than with scatterplots for this task.

## Quick tests <!-- role: check -->

**Failure Sign:** Users hesitate or take noticeably longer to decide correlation sign/strength in the parallel coordinate view than in a scatterplot.\
**Quick Check:** Time a few representative users on the same correlation questions using both views.\
**Stronger Test:** A/B test scatterplot-first versus parallel-coordinates-first flows and compare time-to-answer on correlation questions.

## What to do instead <!-- role: fix -->

- Use a scatterplot as the default view for bivariate correlation checks.
- Add a scatterplot preview when users select two axes/dimensions from a parallel coordinate interface.
- Provide both views but route correlation-specific prompts (e.g., “Are these correlated?”) to the scatterplot.

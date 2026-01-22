---
id: connected-scatterplot-do-not-use-for-primary-correlation-takeaway-with-novices
title: Do not rely on connected scatterplots to communicate correlation as the primary
  takeaway for novice audiences
bibliography: references.bib
description: Dual-axis line charts cue correlational interpretations more readily
  than connected scatterplots for naive viewers.
labels:
- chart:scatter
- task:infer
- visual:orientation
- impact:clarity
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Use a dual-axis line chart when the main message is positive vs negative correlation for novices <!-- role: advice -->

If your key takeaway is that two time series move together or move in opposite directions, prefer a dual-axis line chart over a connected scatterplot for general audiences. Use a connected scatterplot only if you add support that makes the correlation reading explicit.

## Correlation cues are more conventional in dual-axis line charts than in connected scatterplots <!-- role: reason -->

Viewers have learned associations between patterns in dual-axis line charts and correlation (for example, parallel movement vs X-shaped crossings). Connected scatterplots require learning new mappings between diagonal segment directions and correlation, so naive viewers may not spontaneously describe relationships in correlational terms even when they can describe increases and decreases.

**Mechanism:** Familiar visual metaphors and learned pattern-language reduce the inference burden for correlation judgments.

**Evidence:** In qualitative descriptions, viewers used correlational language far more often for dual-axis line charts than for connected scatterplots depicting the same datasets (a large imbalance in frequency of correlation-related terms) [@harozConnectedScatterplotPresenting2016].

**Notes:** This does not mean connected scatterplots cannot support correlation inference, but it may be less salient without learned conventions.

## Situations where correlation salience is required <!-- role: context -->

- **User Goal:** Conclude “these move together” vs “these move oppositely.”
- **Task:** Make an overall relationship judgment rather than narrate phases.
- **Data:** Paired time series where correlation framing is the intended takeaway.
- **Chart Setting:** Explanatory communication where readers may only glance briefly.
- **Audience:** Novices or general readers with limited exposure to connected scatterplots.
- **Success Criterion:** Readers use correct “positive/negative relationship” language without prompting.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The intended takeaway is about time shifts, loops, or phase structure rather than overall correlation. **Why:** Connected scatterplots can surface time-offset dynamics that are not as visually distinctive in dual-axis line charts [@harozConnectedScatterplotPresenting2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose engagement and distinctive features like loops that attract attention. **Risk:** Using only a dual-axis line chart can reduce visibility of time-offset patterns. **Mitigation:** Use annotations or complementary views if time-offset structure matters.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Publishing a connected scatterplot expecting readers to immediately infer correlation from diagonal directions. **Why it fails:** Naive readers may not naturally map connected-scatterplot geometry to correlation concepts [@harozConnectedScatterplotPresenting2016].

## Quick tests for correlation comprehension <!-- role: check -->

**Failure Sign:** Readers describe only individual series changes (“one goes up, the other goes down”) without summarizing the relationship. **Quick Check:** Ask readers to label the overall relationship as “together” or “opposite” after a brief glance. **Stronger Test:** Compare a connected scatterplot and dual-axis line chart in an A/B test for correct correlation judgments.

## What to do instead <!-- role: fix -->

- Use a dual-axis line chart when correlation is the headline conclusion.
- Pair the connected scatterplot with a short annotation that explicitly names the relationship in key segments.
- Provide both views (connected scatterplot and dual-axis line chart) when you need both engagement and conventional correlation cues.

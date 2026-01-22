---
id: use-dot-plots-over-filled-bars-for-multi-value-average-comparisons
title: Use dot plots instead of filled bars to support multi-value average comparisons
bibliography: references.bib
description: Dot plots keep values as positions, which can better support average
  comparisons than bar fills that encourage extent-based proxies.
labels:
- chart:dot
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:general
- statistic:mean
---

## Prefer dot plots for comparing averages across sets of values <!-- role: advice -->

Use a dot plot (points positioned on a common axis) rather than filled bars when viewers need to compare averages across sets of multiple values. Keep the encoding focused on position so the judgment target is the same feature the viewer compares.

## Why dot plots can reduce extent-based interference <!-- role: reason -->

Dot plots present values as spatial positions without a filled extent that can be summed. When bars are used, viewers tend to treat each bar as an object and aggregate by total extent, which yields low-precision average judgments and becomes especially problematic when set sizes differ; position-only encodings can be less impaired in those cases.

**Mechanism:** Removing bar extent reduces the salience of “total mass,” decreasing the chance that viewers substitute a sum proxy for the intended average judgment.

**Evidence:** In multi-value comparisons, performance for normal bar charts matched misaligned bars, consistent with reliance on extent rather than bar-top position, while dot plots sometimes showed less impairment when set sizes differed (an interaction suggested better performance for dots than normal bars in unequal-size comparisons) [@yuanPerceptualProxiesExtracting2019]. Across experiments, unequal set sizes reduced performance strongly, consistent with interference from irrelevant set-size/area cues that dot plots can partially avoid compared to bars [@yuanPerceptualProxiesExtracting2019].

**Notes:** This rule is about average comparisons across multiple points per group, not single-value comparisons.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Compare which of two (or more) groups has a higher average.
- **Task:** Make a forced-choice or ranking judgment about group means from multiple observations.
- **Data:** Multiple observations per category; potentially unequal group sizes.
- **Chart Setting:** Any display where you might otherwise use multiple bars per group (small multiples of bars, grouped bars, or bar-per-observation layouts).
- **Audience:** Broad audiences who may default to intuitive visual proxies.
- **Success Criterion:** Higher discrimination precision (lower just-noticeable difference) for mean comparisons.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is a single-value comparison (one value per group) and the bar chart already provides aligned baselines. **Why:** For single-value comparisons, bar charts can support position-based judgments with high precision similar to dot plots [@yuanPerceptualProxiesExtracting2019].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Dot plots can require more explanation for audiences expecting bar charts.\
**Risk:** If dots overlap or become too dense, position comparisons may degrade and other proxies may emerge.\
**Mitigation:** Maintain legibility of individual points (spacing/jitter) so positions remain readable.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Switching to dots but still emphasizing group “mass” via heavy fills or large markers that create a salient area. **Why it fails:** Strong extent cues can reintroduce sum-like proxies and set-size interference [@yuanPerceptualProxiesExtracting2019].
- **Mistake:** Using misaligned bars (stack-like parts) for average comparisons across groups. **Why it fails:** Misalignment removes position comparability and encourages extent-based extraction that is low-precision for averages [@yuanPerceptualProxiesExtracting2019].

## Quick tests before you ship <!-- role: check -->

**Failure Sign:** Viewers do well on 1-vs-1 judgments but accuracy collapses when you move to 2-vs-2 or larger set comparisons.\
**Quick Check:** Re-encode the same values as dots and see whether the average comparison feels visually clearer without relying on total filled area.\
**Stronger Test:** Compare just-noticeable differences for bars vs dots in a small study using equal-size and unequal-size groups.

## What to do instead <!-- role: fix -->

- Replace per-observation bars with per-observation dots on a shared axis.
- Add a clear mean marker on top of the dot distribution for each group.
- If you must keep bars for familiarity, remove filled area emphasis by reducing area salience (for example, using outlines) and add explicit mean marks.
- When group sizes differ, provide a dedicated mean comparison view rather than relying on aggregate perception from many marks.

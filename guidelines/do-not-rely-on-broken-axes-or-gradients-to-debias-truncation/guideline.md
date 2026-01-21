---
id: do-not-rely-on-broken-axes-or-gradients-to-debias-truncation
title: Do Not Rely on Broken Axes or Gradients to De-bias Truncation
bibliography: references.bib
description: Visual cues for truncated axes do not reliably reduce inflated severity
  judgments.
labels:
- chart:bar
- task:judge
- visual:axis
- visual:annotation
- impact:integrity
- data:categorical
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

If you truncate a y-axis, do not expect a broken-axis mark or under-bar gradient to meaningfully reduce exaggeration in viewers’ severity judgments.

## The Logic <!-- role: reason -->

People’s severity judgments are driven by the visually magnified differences created by truncation; making truncation “obvious” with common visual indicators did not reliably reduce this subjective inflation.

- **The Principle:** Warning cues do not neutralize the perceptual impact of rescaled vertical space.
- **The Evidence:** Experiments 2 and 3 found no consistent reduction in perceived severity for broken-axis bar charts or gradient bar charts versus standard truncated bar charts [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Forming an intuitive impression of how large differences are.
- **Data Type:** Bar charts where a designer is tempted to truncate for narrow ranges.
- **Audience:** Crowdsourced/general audiences (and, by implication, many real-world viewers) [@correllTruncatingYAxisThreat2020a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your goal is disclosure/legibility (making truncation detectable), not de-biasing perceived severity.
- **Reason:** The paper does not claim these cues are useless for transparency—only that they did not measurably reduce severity inflation [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may add visual complexity without improving interpretive neutrality.
- **The Risk:** You create a false sense of “we fixed it” while the subjective exaggeration remains [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a broken-axis glyph and assuming the chart is now perceptually “honest.”
- **Why it fails:** Severity ratings remained similar across standard, broken-axis, and gradient designs at the same truncation levels [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Despite a prominent break/gradient, the difference still “looks huge.”
- **The Test:** Show reviewers two truncated versions (standard vs. broken/gradient) and see if severity impressions materially change; if not, the cue isn’t de-biasing [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the truncation level (expand the y-axis range) rather than adding cue marks.
- **Best Fix:** Treat axis-range choice as the primary control on perceived effect size; use cues for disclosure, but manage severity through scale decisions aligned to meaningful effects [@correllTruncatingYAxisThreat2020a].

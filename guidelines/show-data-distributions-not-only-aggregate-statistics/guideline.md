---
id: show-data-distributions-not-only-aggregate-statistics
title: Show the underlying data distribution, not only aggregate statistics, when
  viewers must judge variability or shape
bibliography: references.bib
description: Replacing data with summary statistics hides distribution structure and
  can bias inference, so include distributional views when possible.
labels:
- chart:distribution
- task:infer
- visual:aggregation
- impact:transparency
- data:quantitative
- audience:analyst
- risk:hidden-structure
---

## Include distribution context instead of only means and error bars when interpreting samples <!-- role: advice -->

When communicating sample comparisons, include a visualization of the data distribution rather than showing only aggregate statistics like means with error bars. Use a distribution-revealing design that makes variance and shape visible alongside any summary values.

## Why summaries alone can mislead <!-- role: reason -->

Aggregating to a single statistic removes context needed to evaluate uncertainty, shape, and outliers, reducing flexibility in interpretation. Some common aggregate encodings also bias inference: viewers treat values “within the bar” as more likely than values outside it, even when the bar is only a mean indicator.

**Mechanism:** Viewers use ensemble perception to estimate distributional properties from visible sets; hiding the set and showing only a summary prevents accurate judgments and can introduce within-the-mark biases.

**Evidence:** Bar charts used for means can induce within-the-bar bias, where viewers infer higher likelihood for values inside the bar than outside, despite the bar not representing a distribution [@szafirGoodBadBiased2018]. Distribution-revealing summaries (for example, violin plots) surface meaningful differences in shape (normal, bimodal, skewed) that aggregate statistics obscure [@szafirGoodBadBiased2018].

**Notes:** This is not an argument against statistics; it is about providing enough visible context to evaluate what the statistics mean.

## When this applies <!-- role: context -->

- **User Goal:** Compare groups while understanding variability, uncertainty, or distribution shape.
- **Task:** Judge overlap, spread, skew, multimodality, or outliers across samples.
- **Data:** Sampled measurements per group (not just a single known constant per group).
- **Chart Setting:** Scientific figures, evaluations, A/B test summaries, benchmark comparisons.
- **Audience:** Analysts, reviewers, and decision makers who may question validity.
- **Success Criterion:** Readers can see both central tendency and distributional structure.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Aggregate statistics are sufficient for the decision and the distribution shape is irrelevant to the question being asked. **Why:** Showing full distributions can add complexity without improving the specific judgment [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Distribution plots take more space and can be harder for some audiences to learn than a simple bar. **Risk:** Very large datasets can create clutter if every point is drawn. **Mitigation:** Use visual summaries that reduce clutter while preserving key distribution properties.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using mean bars with error bars as the only depiction of group differences. **Why it fails:** It hides distribution shape and can trigger within-the-bar bias in how viewers interpret likelihood [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** Two groups have similar means but could plausibly have very different spreads or multimodality, yet the chart offers no way to tell. **Quick Check:** Ask what the distribution might look like; if the chart cannot support an answer, it is likely over-aggregated. **Stronger Test:** Add a distribution view and see whether the qualitative story changes.

## What to do instead <!-- role: fix -->

- Use a distribution-revealing summary (such as a violin plot) alongside a central tendency marker.
- When feasible, show more of the underlying data rather than only computed aggregates.
- If the dataset is too large, construct visual summaries that preserve important distribution properties.
- Reduce clutter by filtering, clustering, or subsampling while maintaining the overall distributional pattern.

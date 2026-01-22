---
id: use-continuous-uncertainty-encodings-to-reduce-binary-interpretation
title: Use continuous uncertainty encodings to discourage binary 'inside/outside'
  interpretations
bibliography: references.bib
description: Continuous uncertainty displays reduce all-or-nothing reasoning and overconfident
  effect-size judgments.
labels:
- chart:gradient
- chart:violin
- task:infer
- task:compare
- visual:transparency
- visual:width
- impact:calibration
- data:uncertainty
- audience:novice
---

## Show uncertainty as a continuous field rather than a binary interval marker <!-- role: advice -->

For inferential tasks, encode uncertainty with a continuous visual cue (such as transparency or width) so plausibility changes gradually away from the mean. Avoid encodings that visually collapse uncertainty into a single “inside the interval vs. outside” decision.

## Why continuous encodings better calibrate inference and confidence <!-- role: reason -->

Discrete interval markers encourage viewers to treat uncertainty as a hard boundary, which supports threshold-driven judgments and inflated confidence in comparisons. Continuous encodings better reflect that plausibility typically decreases smoothly with distance from the mean and can support more nuanced reasoning beyond a single confidence level.

**Mechanism:** A continuous mapping (for example, fading opacity or narrowing width) provides graded evidence about unlikely outcomes and reduces the tendency to treat uncertainty as an all-or-nothing filter.

**Evidence:** In one-sample tasks, encodings that provided more detail about the distribution (gradient and violin) produced higher reported confidence aligned with the inferential task compared to binary encodings (bar charts and modified box plots) [@correllErrorBarsConsidered2014]. In two-sample tasks, bar charts produced higher confidence and larger predicted effects than alternatives, including when differences were not statistically significant, consistent with boundary-driven overconfidence [@correllErrorBarsConsidered2014].

**Notes:** The paper’s gradient plot design uses a solid region for a 95% confidence interval with “fuzzy” edges to communicate graded uncertainty beyond that interval.

## When graded uncertainty is needed <!-- role: context -->

- **User Goal:** Make a decision that depends on both effect size and uncertainty, not just whether an interval overlaps.
- **Task:** Compare groups, assess confidence in a predicted winner, or judge magnitude of an uncertain difference.
- **Data:** Means with margins of error where different standards of evidence might be relevant.
- **Chart Setting:** Side-by-side group comparison displays used for inference “by eye.”
- **Audience:** General or mixed-expertise readers.
- **Success Criterion:** Confidence and effect-size judgments change smoothly with increasing/decreasing uncertainty.

## When a binary boundary is acceptable <!-- role: exceptions -->

**Break it when:** The only intended message is membership in a single, explicitly defined interval category (for example, a fixed operational cutoff), and you do not want viewers to interpolate beyond it. **Why:** A continuous display invites interpolation and gradation that may be outside the intended categorical message [@correllErrorBarsConsidered2014].

## Tradeoffs of continuous uncertainty encodings <!-- role: costs -->

**Sacrifice:** Continuous uncertainty displays can be harder to read precisely than a single interval endpoint. **Risk:** Transparency in particular can be reproduced inconsistently across displays. **Mitigation:** Treat the goal as conveying graded plausibility rather than exact numeric decoding.

## Common ways continuous encodings go wrong <!-- role: mistakes -->

**Mistake:** Showing only an error bar endpoint and assuming viewers will infer gradual changes in likelihood. **Why it fails:** The visual design still promotes binary thinking about “within vs. outside” and can inflate effect-size judgments [@correllErrorBarsConsidered2014].

## Quick checks for binary-interpretation risk <!-- role: check -->

**Failure Sign:** The uncertainty depiction has a single crisp boundary that visually dominates the reading. **Quick Check:** Ask whether the chart visually supports answering “how much less likely is this value?” rather than only “is it inside the interval?” **Stronger Test:** Compare predicted effect size and confidence across encodings for the same stimuli and look for inflated responses in the crisp-boundary condition.

## What to do instead of a crisp boundary-only uncertainty marker <!-- role: fix -->

- Use a gradient plot that fades away from the mean to represent decreasing plausibility continuously.
- Use a violin plot whose width narrows away from the mean to represent the probability density used for inference.
- Pair a discrete interval (such as 95%) with a graded outer region so viewers can reason beyond a single threshold.

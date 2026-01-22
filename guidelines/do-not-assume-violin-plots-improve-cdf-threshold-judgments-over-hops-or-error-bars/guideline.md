---
id: do-not-assume-violin-plots-improve-cdf-threshold-judgments-over-hops-or-error-bars
title: Do Not Assume Violin Plots Improve CDF Threshold Judgments Over HOPs or Error
  Bars
bibliography: references.bib
description: Violin plots were not consistently more accurate than HOPs or error bars
  for estimating probabilities above or between thresholds.
labels:
- chart:violin
- task:estimate
- visual:area
- impact:accuracy
- data:univariate
- audience:novice
- method:violin
---

## Validate violin plots for probability-above/between-threshold tasks <!-- role: advice -->

Do not treat violin plots as a guaranteed best choice for estimating probabilities above a threshold or between two thresholds; test them against alternatives such as HOPs or error bars for your specific parameter ranges.

## Why violin plots are not reliably superior for these tasks <!-- role: reason -->

Although violin plots encode probability density via width (area), viewers may still struggle to integrate area into cumulative probabilities, and performance can vary with how compressed or expanded the distribution appears.

**Mechanism:** Cumulative judgments from density encodings require mental integration of area, which can be sensitive to scale and the perceptual difficulty of mapping widths to totals.

**Evidence:** Across multiple univariate tasks estimating Pr(A > k) and Pr(k2 ≤ A ≤ k3), violin plots were not consistently more accurate than HOPs or error bars, and in at least one condition violin plots produced significantly higher error than the other representations. [@hullmanHypotheticalOutcomePlots2015]

**Notes:** Performance differences varied by variance and threshold placement, indicating that “best” may depend on the specific distribution and query. [@hullmanHypotheticalOutcomePlots2015]

## When this warning applies <!-- role: context -->

- **User Goal:** Estimate how often values exceed a threshold or fall within an interval.
- **Task:** Probability estimation from a univariate distribution depiction.
- **Data:** Continuous univariate uncertainty (for example, approximately normal in the study).
- **Chart Setting:** Static or interactive; thresholds/intervals are visually marked.
- **Audience:** General readers who may not know how to interpret density encodings.
- **Success Criterion:** Lower absolute error in probability estimates.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** You have direct evidence from your own evaluation that your audience can accurately read the relevant cumulative probabilities from your violin design. **Why:** The observed accuracy varied by condition, so local validation can override the general uncertainty in performance. [@hullmanHypotheticalOutcomePlots2015]

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Running validation takes time compared with choosing a default plot type.\
**Risk:** Using a violin plot without validation can lead to confidently wrong probability interpretations.\
**Mitigation:** Use small pilots with the target questions (above/between thresholds) before standardizing the encoding. [@hullmanHypotheticalOutcomePlots2015]

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing violin plots solely because they “show the full distribution” and assuming this ensures accurate probability judgments. **Why it fails:** Showing more distribution detail did not reliably translate into lower error on threshold-based probability questions. [@hullmanHypotheticalOutcomePlots2015]

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ estimated “times out of 100” for a threshold/interval are systematically too high or too low across repeated questions.\
**Quick Check:** Ask users to answer two or three threshold/interval probability questions from the same design; inconsistent or extreme answers indicate poor decoding.\
**Stronger Test:** Compare mean absolute error for your key probability questions across violin plots, HOPs, and error-bar variants using the same sampled draws. [@hullmanHypotheticalOutcomePlots2015]

## What to do instead <!-- role: fix -->

- Use HOPs when probability judgments involve comparisons across variables or when you want frequency-style reasoning.
- Use error bars with clear coverage wording when the primary need is a simple static summary rather than detailed probability reading.
- Add direct numeric annotations for the specific probability of interest when readers must answer a known threshold/interval query accurately.
- Pilot-test threshold/interval questions with your target audience before adopting violin plots as the default uncertainty encoding. [@hullmanHypotheticalOutcomePlots2015]

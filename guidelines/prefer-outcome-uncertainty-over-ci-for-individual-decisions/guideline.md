---
id: prefer-outcome-uncertainty-over-ci-for-individual-decisions
title: Prefer outcome-uncertainty displays over 95% CIs for individual-level treatment
  decisions
bibliography: references.bib
description: When readers must judge how a treatment will affect an individual outcome,
  show outcome uncertainty rather than only inferential uncertainty.
labels:
- chart:errorbar
- task:decide
- visual:length
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:scientific-reporting
---

## Use 95% prediction intervals or hypothetical outcome plots for individual outcome judgments <!-- role: advice -->

Use a visualization that encodes outcome uncertainty—such as 95% Prediction Intervals (PIs) or Hypothetical Outcome Plots (HOPs)—when readers are deciding whether a treatment is worth it for them personally.

## Outcome-uncertainty encodings avoid inflated effect impressions <!-- role: reason -->

When uncertainty is shown only as inferential uncertainty around the mean (e.g., 95% Confidence Intervals (CIs)), readers can mistake the narrow interval as implying that individual outcomes are tightly clustered and that the treatment is reliably superior. Displays that directly encode variation in individual outcomes make overlap and variability perceptually available, which reduces overconfidence about treatment effectiveness.

**Mechanism:** Narrow mean-focused intervals visually compress uncertainty, encouraging readers to underestimate outcome variability and overestimate how often the treatment “wins” for an individual.

**Evidence:** Across two randomized experiments, viewers shown 95% CIs overstated willingness to pay and probability of superiority more than viewers shown 95% PIs or HOPs, and they also understated outcome variability more than PI/HOP viewers [@hofmanHowVisualizingInferential2020]. Responses were closest to normatively correct answers when the visualization encoded variation in individual outcomes (95% PIs or HOPs) rather than inferential uncertainty alone [@hofmanHowVisualizingInferential2020].

**Notes:** This guideline targets judgments about individual outcomes (e.g., “Will it help me?”), not whether an average difference is statistically distinguishable from zero.

## When readers need to judge how often the treatment helps an individual <!-- role: context -->

- **User Goal:** Decide whether to pay for or adopt a treatment/intervention for personal benefit.
- **Task:** Estimate probability of superiority, decide willingness to pay, or reason about likely individual outcomes under treatment vs control.
- **Data:** Two-group outcomes with substantial within-group variability; effect sizes may be small.
- **Chart Setting:** Scientific result figure or explanatory graphic in text where a single chart must carry the main message.
- **Audience:** Lay readers or mixed audiences who may not distinguish sampling variability from outcome variability.
- **Success Criterion:** Calibrated beliefs about effect magnitude, variability, and probability of being better off under treatment.

## When not to treat outcome-uncertainty displays as sufficient <!-- role: exceptions -->

**Break it when:** The primary goal is to communicate inferential uncertainty about the mean difference itself (e.g., precision of an estimated mean). **Why:** Outcome-uncertainty views (PIs/HOPs) can obscure how precisely the mean was estimated, which is a different uncertainty construct [@hofmanHowVisualizingInferential2020].

## Tradeoffs of outcome-uncertainty-first displays <!-- role: costs -->

**Sacrifice:** Fine visual discriminability of small mean differences can be reduced when axes must span the full range of outcomes. **Risk:** Readers may miss that the mean difference is precisely estimated even when outcomes are variable. **Mitigation:** Use accompanying text to clarify what uncertainty is shown without relying on mean-only intervals to carry the decision message.

## Common ways this goes wrong in practice <!-- role: mistakes -->

- **Mistake:** Showing only 95% CIs to support individual-level claims like “the treatment works for most people.” **Why it fails:** Viewers interpret narrow CIs as implying low variability in individual outcomes and overestimate treatment effectiveness [@hofmanHowVisualizingInferential2020].
- **Mistake:** Treating a mean-and-CI plot as an effect-size display. **Why it fails:** It emphasizes sampling distribution properties rather than outcome distribution overlap, biasing perceived probability of superiority upward [@hofmanHowVisualizingInferential2020].

## Quick checks for calibrated individual-level interpretation <!-- role: check -->

**Failure Sign:** Readers’ implied or stated probability of superiority clusters near certainty even for small effects. **Quick Check:** Ask a colleague “Out of 100 people, about how many would do better with treatment?”; if answers jump toward ~90%+ for a small mean shift, the display likely overemphasizes inferential uncertainty. **Stronger Test:** Run a small between-subjects check comparing CI vs PI/HOP versions and measure probability-of-superiority estimates for the same underlying data.

## What to do instead of CI-only when decisions are individual-level <!-- role: fix -->

- Show 95% Prediction Intervals (PIs) to visualize variability in individual outcomes around each mean.
- Use Hypothetical Outcome Plots (HOPs) to depict repeated draws from the outcome distributions when probability-of-superiority judgments matter.
- Pair mean markers with an outcome-uncertainty encoding so the central tendency is still visible without implying low variability.
- If constrained to one plot, prioritize outcome uncertainty over inferential uncertainty when the decision is about an individual’s expected result.

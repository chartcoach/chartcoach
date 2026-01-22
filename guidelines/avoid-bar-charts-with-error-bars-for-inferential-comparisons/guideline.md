---
id: avoid-bar-charts-with-error-bars-for-inferential-comparisons
title: Avoid bar charts with error bars for inferential comparisons of means
bibliography: references.bib
description: Bar charts with error bars systematically bias judgments about uncertain
  means in inferential tasks.
labels:
- chart:bar
- task:compare
- task:infer
- visual:position
- impact:accuracy
- data:uncertainty
- audience:novice
- evidence:crowdsourced
---

## Prefer non-bar encodings for mean-plus-uncertainty inference <!-- role: advice -->

Avoid bar charts with error bars when the viewer must reason from sample means and uncertainty to a real-world inference or choice. Use a visually symmetric encoding that represents uncertainty continuously instead.

## Why bar charts distort uncertainty judgments in inference tasks <!-- role: reason -->

A bar is a filled, asymmetric container that visually implies “values inside the bar are more plausible,” even when the chart is meant to communicate uncertainty around a mean. This metaphor pushes viewers toward binary, threshold-like interpretations (inside vs. outside) and inflates perceived effect size and confidence in comparisons.

**Mechanism:** The filled bar creates a containment cue that makes outcomes on the bar-filled side of the mean seem more likely; discrete error bars also encourage all-or-nothing reasoning about uncertainty rather than gradual changes in plausibility.

**Evidence:** In one-sample inference tasks, outcomes positioned within the filled bar region were judged more likely than equally distant outcomes outside it (within-the-bar bias), but this asymmetry disappeared for symmetric encodings [@correllErrorBarsConsidered2014]. In two-sample comparisons, bar charts led to larger predicted effect sizes and higher confidence than alternative encodings, including for cases that were not statistically significant [@correllErrorBarsConsidered2014].

**Notes:** The observed differences occurred for a general audience and held across multiple problem framings (polling, weather, finance).

## When you are asking readers to infer from mean and error <!-- role: context -->

- **User Goal:** Decide what will happen in a population or future outcome using sample means plus uncertainty.
- **Task:** Infer direction, confidence, or effect size from uncertain group means.
- **Data:** Sample means with margins of error or confidence intervals (for example, t-confidence intervals).
- **Chart Setting:** Static charts in reports, slides, or articles where viewers make “by eye” inferences.
- **Audience:** Mixed or general audiences without deep statistical training.
- **Success Criterion:** Viewer judgments and confidence track the implications of uncertainty rather than the bar’s visual metaphor.

## When a bar chart is not the primary problem <!-- role: exceptions -->

**Break it when:** The task is not inferential (for example, you are not asking viewers to reason from uncertainty to outcomes) and the bar’s magnitude comparison is the only intended reading. **Why:** The documented harms are tied to inferential judgments about uncertainty and likelihood rather than simple magnitude lookup [@correllErrorBarsConsidered2014].

## Tradeoffs of avoiding bar charts with error bars <!-- role: costs -->

**Sacrifice:** You may give up the familiarity of the common “bar + error bar” convention. **Risk:** Less familiar uncertainty encodings may require brief onboarding text or captions. **Mitigation:** Use consistent legends and short descriptions of what the uncertainty band/shape represents.

## Common ways people fail to fix bar-chart inference bias <!-- role: mistakes -->

**Mistake:** Keeping the bar chart and assuming the error bars alone will prevent misinterpretation. **Why it fails:** Viewers still show within-the-bar bias and overconfident effect-size judgments in inferential tasks [@correllErrorBarsConsidered2014].

## Quick checks for bar-chart-driven misinference <!-- role: check -->

**Failure Sign:** Viewers treat outcomes on the filled-bar side of the mean as more likely than equally distant outcomes on the other side. **Quick Check:** Ask a colleague whether an outcome equally far above and below the mean seems equally likely; asymmetry indicates bias risk. **Stronger Test:** Run a small A/B test comparing the bar chart to a symmetric continuous uncertainty encoding and measure predicted effect size and confidence.

## What to do instead of bar charts with error bars for inference <!-- role: fix -->

- Replace the bar-and-error-bar design with a gradient plot that encodes uncertainty continuously and symmetrically.
- Replace the bar-and-error-bar design with a violin plot that uses width to show the distribution used for inference.
- If you must show a bar for other reasons, add an additional symmetric uncertainty display alongside it for the inferential judgment task.

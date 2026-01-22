---
id: avoid-95-ci-errorbars-as-effectiveness-cue
title: Avoid using 95% CI error bars as the primary cue for treatment effectiveness
bibliography: references.bib
description: Do not rely on 95% confidence-interval error bars alone to communicate
  how effective a treatment is likely to be.
labels:
- chart:errorbar
- task:compare
- visual:length
- impact:bias-reduction
- data:uncertainty
- audience:novice
- domain:scientific-reporting
---

## Do not use 95% CI error bars alone to convey “how big” or “how reliable” an effect feels <!-- role: advice -->

Do not use a mean-with-95%-Confidence-Interval (CI) error bar plot as the sole visual evidence for how effective a treatment is.

## CI-focused plots invite overconfidence about treatment wins <!-- role: reason -->

A 95% CI plot visualizes uncertainty in estimating the mean (sampling uncertainty), which can be much smaller than the spread of individual outcomes. Readers can misread the narrowness of CIs as “tight outcomes,” inflating perceived superiority and willingness to invest.

**Mechanism:** The visual prominence of narrow intervals anchors judgments to precision-of-mean rather than overlap of outcomes, causing an exaggerated mental model of treatment impact.

**Evidence:** In randomized experiments using identical underlying data, CI-based visualizations produced higher willingness to pay and higher probability-of-superiority estimates than PI-based or HOP-based visualizations, indicating systematic overestimation of treatment effectiveness from CI-focused displays [@hofmanHowVisualizingInferential2020]. CI-based visualizations also led to underestimation of outcome variability as elicited through participant-constructed distributions [@hofmanHowVisualizingInferential2020].

**Notes:** This problem is especially concerning for small effects, where the mean difference is visually small but CI bars can still look “decisive.”

## When a single chart is used to justify a treatment effect to readers <!-- role: context -->

- **User Goal:** Understand whether an intervention is meaningfully better than a baseline.
- **Task:** Judge strength of effect; infer “how often” treatment helps; decide whether to adopt/pay.
- **Data:** Two conditions/groups with overlapping outcome distributions; potentially small effect size.
- **Chart Setting:** Papers, reports, or summaries where readers may only see the figure and caption.
- **Audience:** Lay readers (and mixed audiences) who may not separate mean estimation uncertainty from outcome variability.
- **Success Criterion:** Readers do not overestimate probability of superiority or undervalue within-group variability.

## When CI-only may be acceptable <!-- role: exceptions -->

**Break it when:** The communication goal is strictly about precision of the estimated mean (not individual outcomes or “wins”). **Why:** The CI is the uncertainty construct being communicated, so outcome spread is not the primary target [@hofmanHowVisualizingInferential2020].

## Tradeoffs of avoiding CI-only plots <!-- role: costs -->

**Sacrifice:** You may lose a compact, familiar encoding of inferential precision that some scientific audiences expect. **Risk:** Replacing CI-only with wider outcome-focused intervals can make mean differences appear visually smaller and harder to read. **Mitigation:** Keep the mean clearly marked while shifting the uncertainty encoding toward outcomes.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a CI plot to imply “the treatment is reliably better for most individuals.” **Why it fails:** CI width reflects sample size and mean estimation precision, not the variability of individual outcomes [@hofmanHowVisualizingInferential2020].
- **Mistake:** Assuming explanatory caption text will neutralize CI-driven overconfidence. **Why it fails:** Adding extra text about PIs did not eliminate the overestimation patterns induced by CI-focused visualizations [@hofmanHowVisualizingInferential2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers interpret small CI overlap/non-overlap as “near-certain advantage” in head-to-head outcomes. **Quick Check:** Ask readers to estimate “out of 100 trials, how many times does treatment beat control?”; if estimates jump far above the implied probability of superiority for the data, CI-only is likely driving inflation. **Stronger Test:** Swap CI-only with PI/HOP and re-test probability-of-superiority estimates in a small pilot.

## What to do instead <!-- role: fix -->

- Replace CI-only error bars with 95% Prediction Intervals (PIs) when readers need to reason about individual outcomes.
- Use HOPs to support probability-of-superiority judgments via repeated outcome samples.
- If you must show CIs, pair them with an outcome-uncertainty encoding in the same figure or an adjacent view.
- Add an elicitation or interpretive prompt (e.g., probability-of-superiority framing) that forces attention to outcomes rather than mean precision.

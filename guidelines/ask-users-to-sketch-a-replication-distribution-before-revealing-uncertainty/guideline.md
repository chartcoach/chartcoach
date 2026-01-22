---
id: ask-users-to-sketch-a-replication-distribution-before-revealing-uncertainty
title: Ask Users to Sketch the Replication Distribution Before Revealing the Uncertainty
  Visualization
bibliography: references.bib
description: Having people graphically predict replication outcomes before seeing
  the true distribution improves their later uncertainty estimation for a new study.
labels:
- chart:distribution
- task:estimate
- visual:interaction
- impact:learning
- data:uncertainty
- audience:novice
- interaction:elicitation
---

## Graphically elicit a replication distribution before showing the true sampling distribution <!-- role: advice -->

Before displaying the sampling distribution for a study result, require the reader to sketch their prediction of the distribution of effects from replications. Then reveal the true sampling distribution so the reader can compare their guess to the observed uncertainty.

## Prediction-before-reveal strengthens transfer to new uncertainty judgments <!-- role: reason -->

Making a concrete prediction forces the reader to externalize assumptions about variability and center, creating a clear discrepancy signal when the true distribution is revealed. That comparison can recalibrate intuitions about replication uncertainty and improve later estimation in a new-but-similar scenario.

**Mechanism:** Prediction prompts deeper processing of uncertainty and makes error feedback salient by showing the “gap” between belief and evidence.

**Evidence:** A controlled experiment found that participants who graphically predicted replication uncertainty for one experiment produced more accurate uncertainty estimates in a transfer task for a new experiment (lower divergence from the replication prediction distribution) than those who did not predict first [@hullmanImaginingReplicationsGraphical2018].

**Notes:** The same study did not find a clear improvement from prediction on short-term recall of the original sampling distribution, so the benefit is strongest for transfer rather than memorization.

## When prediction-first elicitation fits the job <!-- role: context -->

- **User Goal:** Form an intuition for how much an observed effect might vary across exact replications.
- **Task:** Estimate a distribution of possible replication effects for a new study based on summary results.
- **Data:** Experimental results summarized by sample mean, standard deviation, and sample size; uncertainty expressed as a distribution.
- **Chart Setting:** Interactive report, explorable article, or analysis tool where the viewer can input a distribution before seeing the “answer.”
- **Audience:** Non-statisticians or mixed audiences likely to have weak intuitions about sampling variation.
- **Success Criterion:** Better-calibrated replication uncertainty estimates on a subsequent, similar study.

## When not to force prediction-first <!-- role: exceptions -->

**Break it when:** The setting cannot support interaction (e.g., static figure-only delivery) or the audience cannot reasonably perform a sketch task. **Why:** The technique depends on eliciting a user-generated distribution and then contrasting it with the true distribution.

## Tradeoffs of adding a prediction step <!-- role: costs -->

**Sacrifice:** Additional time and interaction cost before the viewer can see results. **Risk:** Some users may respond with noisy or default-shaped sketches, reducing benefit and adding variance. **Mitigation:** Keep the elicitation lightweight and immediately show the comparison to make the feedback value obvious.

## Common ways prediction-first goes wrong <!-- role: mistakes -->

**Mistake:** Letting users skip directly to the revealed distribution without committing a prediction. **Why it fails:** The “gap” signal that drives recalibration is weakened when no explicit prior is recorded.

**Mistake:** Treating prediction as a quiz with no visual comparison to the true distribution. **Why it fails:** The benefit relies on seeing one’s prediction against the actual sampling distribution, not only making a guess.

## Quick checks for whether prediction-first is working <!-- role: check -->

**Failure Sign:** Users’ later transfer estimates show no improvement over baseline despite completing predictions. **Quick Check:** Confirm the interface requires a committed sketch and always displays the sketch overlaid or juxtaposed with the revealed sampling distribution. **Stronger Test:** Run a small A/B test measuring divergence of users’ transfer-task distributions from an appropriate replication prediction distribution.

## Alternatives when prediction-first is not feasible <!-- role: fix -->

- Provide the sampling distribution first but add a follow-up “adjust the distribution to match what you think replications would look like” task.
- Replace free-form sketching with a constrained distribution-adjustment interaction (e.g., adjust center and spread) to reduce effort.
- Use a short interactive prompt that asks users to place a few representative outcomes for replications before showing the full distribution.
- If interaction is impossible, separate the report into “Your expectation” text prompts followed by the revealed uncertainty visualization to approximate commitment.

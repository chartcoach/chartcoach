---
id: separate-evidence-uncertainty-from-value-thresholds-in-binary-advice
title: Separate evidence uncertainty from value thresholds in categorical recommendations
bibliography: references.bib
description: "When issuing binary calls to action, disclose both the uncertainty in\
  \ discrimination and the decision rule\u2019s tradeoffs."
labels:
- chart:annotation
- task:decide
- visual:text
- impact:trust
- data:uncertainty
- audience:public
- domain:risk-communication
---

## Disclose both evidence strength and decision threshold in binary advice <!-- role: advice -->

When you present a categorical recommendation (do/act vs don’t/wait), explicitly communicate both how well the evidence discriminates the underlying state and how cautious the recommendation rule is. Put these as two separate message elements rather than a single blended conclusion.

## Why separating d′ from β reduces misinterpretation <!-- role: reason -->

Blended calls to action combine uncertainty about facts with tradeoffs among outcomes, so audiences cannot tell whether an “unnecessary” action reflects weak evidence or a conservative threshold. Separating these components helps readers evaluate performance fairly and avoids distrust driven by outcome bias and hindsight bias.

**Mechanism:** Distinguishing discrimination ability (d′) from the decisional threshold (β) lets people attribute errors to evidence limits vs chosen tradeoffs, instead of inferring incompetence or bad faith.

**Evidence:** Categorical recommendations inherently reflect both discrimination ability and decision thresholds, and miscommunication arises when recipients treat advice as pure evidence rather than evidence filtered through a decision rule [@fischhoffCommunicatingScientificUncertainty2014]. People’s retrospective evaluations are also shaped by outcome and hindsight biases, increasing the need for transparent separation [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** If you cannot quantify d′ and β, communicate them qualitatively as distinct concepts (e.g., “weak signal” vs “high caution”) rather than merging them.

## When you are issuing a binary recommendation <!-- role: context -->

- **User Goal:** Decide whether to act now based on an alert, guideline, or signal.
- **Task:** Accept/reject a recommended action under uncertainty.
- **Data:** Evidence with false positives/false negatives; uncertain base rates; limited observations.
- **Chart Setting:** Alerts, dashboards, public advisories, clinical summaries, push notifications, headlines with supporting detail.
- **Audience:** Mixed literacy; may not know scientific norms; may judge quality from outcomes.
- **Success Criterion:** Users understand why advice could be wrong sometimes and still be rational; trust is maintained.

## When not to follow the separation literally <!-- role: exceptions -->

**Break it when:** The recommendation is purely descriptive (no implied action) and no decision threshold is being applied. **Why:** Presenting a threshold implies a value-laden rule that is not part of the communication goal.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You spend extra space and attention budget to explain two components instead of one conclusion. **Risk:** Readers may overfocus on the threshold statement and interpret it as self-protective hedging. **Mitigation:** Keep the threshold description concrete by naming the outcomes being traded off.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Presenting a single “yes/no” recommendation without stating the decision rule behind it. **Why it fails:** Users cannot distinguish weak evidence from conservative caution and may feel misled by outcomes [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Treating disagreement as evidence of ignorance rather than different thresholds/values. **Why it fails:** Observers may overestimate scientific uncertainty or misattribute motives [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “Why were you wrong?” after an event, with no grasp of tradeoffs.\
**Quick Check:** Can a reader restate, in their own words, both “how strong the signal is” and “how cautious the rule is”?\
**Stronger Test:** User test two versions (blended vs separated) and measure understanding of why false alarms/misses occur.

## What to do instead when you cannot quantify it <!-- role: fix -->

- Write two labeled sentences: one about evidence discrimination and one about the tradeoff embedded in the action threshold.
- Add a short note describing what an error would look like (false alarm vs miss) in the current situation.
- Provide an example scenario illustrating the same evidence leading to different actions under different values.
- If space is tight, link to a “How we decide” explainer that separates evidence from thresholds.

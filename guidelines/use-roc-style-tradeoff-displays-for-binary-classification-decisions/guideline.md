---
id: use-roc-style-tradeoff-displays-for-binary-classification-decisions
title: Use ROC-style tradeoff summaries for categorical decision signals
bibliography: references.bib
description: Summarize binary recommendations with explicit false-alarm vs miss tradeoffs
  tied to discrimination ability.
labels:
- chart:curve
- task:choose
- visual:position
- impact:clarity
- data:uncertainty
- audience:expert
- domain:risk-communication
---

## Show false-alarm versus miss tradeoffs for binary signals <!-- role: advice -->

When communicating a binary signal (e.g., warn vs reassure), visualize or state the achievable tradeoff between false alarms and misses for the current evidence quality. Make clear that different operating points reflect different thresholds rather than different underlying evidence.

## Why ROC tradeoffs communicate uncertainty in categorical signals <!-- role: reason -->

Binary outputs hide a continuum of confidence and the costs of errors. A receiver operating characteristic framing makes explicit what outcomes are possible given discrimination ability and how changing the threshold shifts error rates, preventing users from imputing certainty to a categorical label.

**Mechanism:** A tradeoff representation links decision thresholds to observable performance (hits, false alarms), separating “how well you can discriminate” from “how cautious you choose to be.”

**Evidence:** Receiver operating curves are described as the standard summary of uncertainty underlying categorical messages because they show the tradeoffs possible with a given discrimination ability [@fischhoffCommunicatingScientificUncertainty2014]. Misinterpretation occurs when people do not realize categorical advice reflects both discrimination and threshold choices [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** If you cannot draw a curve, report a small set of operating points (e.g., “at this caution level, expect X% false alarms and Y% misses”).

## When a binary message is masking continuous uncertainty <!-- role: context -->

- **User Goal:** Decide whether to take an action triggered by an alert.
- **Task:** Choose an operating point (more cautious vs less cautious) or interpret one chosen for them.
- **Data:** Binary classification with known/estimable outcomes; historical outcomes or validation set.
- **Chart Setting:** Monitoring dashboards, forecast products, clinical screening summaries, quality reports.
- **Audience:** Decision makers who can tolerate quantitative tradeoffs; intermediaries translating to public guidance.
- **Success Criterion:** Users can anticipate error patterns and understand threshold changes without losing trust.

## When not to use ROC-style summaries <!-- role: exceptions -->

**Break it when:** Outcomes cannot be defined consistently or observed (no clear ground truth). **Why:** Tradeoff estimates depend on clear event definitions and evaluable outcomes [@fischhoffCommunicatingScientificUncertainty2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More analytical and design work to estimate and present tradeoffs. **Risk:** Users may treat the displayed tradeoff as fixed even when the environment shifts. **Mitigation:** Pair the tradeoff with the conditions under which it was estimated.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Reporting only accuracy or “confidence” without distinguishing false alarms from misses. **Why it fails:** Users cannot map performance to their own values and thresholds [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Changing thresholds over time without indicating that the operating point moved. **Why it fails:** Users may infer the evidence quality changed when only the decision rule did [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users interpret a warning label as meaning “near certainty,” then feel betrayed by false alarms.\
**Quick Check:** Does the display/message include both kinds of errors (false alarms and misses) in terms users can recognize?\
**Stronger Test:** Ask users to choose between two thresholds given stated costs and see if they can justify the tradeoff.

## What to do instead <!-- role: fix -->

- Report expected false-alarm and miss rates for the current operating point in plain terms.
- Add a small “more cautious / less cautious” comparison showing how error rates shift.
- Provide a brief definition of what counts as the target event so performance is interpretable.
- If the ground truth is indirect, explain what proxy is used and that it adds uncertainty.

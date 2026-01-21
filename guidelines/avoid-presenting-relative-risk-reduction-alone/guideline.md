---
id: avoid-presenting-relative-risk-reduction-alone
title: Never Present Relative Risk Reduction Without Baseline Risk or Absolute Change
bibliography: references.bib
description: If you use relative risk reduction, always include baseline risk or absolute
  risk change to prevent misleading interpretations.
labels:
- chart:table
- task:explain
- visual:text
- impact:integrity
- data:probabilistic
- audience:novice
- domain:health-risk-communication
---

## The Rule <!-- role: advice -->

If you present a relative risk reduction (RRR), also present baseline risk and/or the absolute risk reduction (ARR); do not show RRR alone.

## The Logic <!-- role: reason -->

RRR tends to be perceived as a larger effect and is more persuasive than absolute formats, which can shift decisions without improving understanding—especially when baseline risk is low—so pairing with baseline/absolute values mitigates misinterpretation.

- **The Principle:** Relative-format inflation of perceived effect size
- **The Evidence:** Compared with ARR, RRR increased perceived effectiveness (SMD 0.41) and persuasiveness (SMD 0.66) with little/no difference in understanding overall (SMD 0.02) in [@aklUsingAlternativeStatistical2011]. The authors caution that RRR without baseline risk is likely to misinform decisions, particularly when baseline risk is low [@aklUsingAlternativeStatistical2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether to adopt an intervention based on its risk reduction.
- **Data Type:** Treatment/intervention effect messages that include (or could include) RRR.
- **Audience:** Health consumers and health professionals (overall patterns were similar in [@aklUsingAlternativeStatistical2011]).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are explicitly comparing proportional effects across groups where baseline risk is already clearly displayed elsewhere in the same view.
- **Reason:** The rule’s intent is to prevent RRR being interpreted without baseline context; if baseline risk is already unambiguously present in the same display, the core failure mode is reduced (while still consistent with the caution in [@aklUsingAlternativeStatistical2011]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra numbers and explanation increase layout complexity.
- **The Risk:** Users may focus on one metric (e.g., RRR) and ignore the others unless the layout is clear.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting “50% risk reduction” without stating “from what to what.”
- **Why it fails:** RRR alone hides baseline risk; [@aklUsingAlternativeStatistical2011] notes this can make small absolute benefits look large.

## How to Check <!-- role: check -->

- **Visual Sign:** A statement like “reduces risk by X%” appears with no baseline risk and no absolute difference.
- **The Test:** Try to compute ARR or NNT from what’s shown; if you can’t, the presentation is missing required context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add baseline risk alongside RRR (e.g., “50% relative reduction from 10% baseline”).
- **Best Fix:** Present both group risks (control and intervention) and the absolute difference, and treat RRR as secondary (consistent with concerns raised in [@aklUsingAlternativeStatistical2011]).

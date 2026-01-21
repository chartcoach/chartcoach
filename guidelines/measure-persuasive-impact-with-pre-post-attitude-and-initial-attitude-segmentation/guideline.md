---
id: measure-persuasive-impact-with-pre-post-attitude-and-initial-attitude-segmentation
title: Measure Persuasion With Pre/Post Attitude and Initial-Attitude Segmentation
bibliography: references.bib
description: Use a pre/post attitude measure and analyze results by initial attitude
  to detect whether a visualization format persuades.
labels:
- task:evaluate
- impact:persuasion
- data:survey
- audience:researchers
- method:pre-post
- attitude:segmentation
---

## The Rule <!-- role: advice -->

When evaluating persuasive visualizations, record attitude before and after exposure and analyze effects separately for initial-attitude groups (negative, neutral/weak, positive).

## The Logic <!-- role: reason -->

The study defines persuasion as attitude change (post minus pre) and shows that the direction of the format effect depends on initial attitude: charts helped more for neutral/weakly polarized participants, while tables helped more for negatively polarized participants. Without segmentation, you can miss or misinterpret the effect.

- **The Principle:** Initial attitude moderates persuasion; aggregate-only results can hide opposing subgroup effects.
- **The Evidence:** [@pandeyPersuasivePowerData2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Determine whether a chart/table format actually shifts opinions.
- **Data Type:** Any persuasion study where participants can start with different prior beliefs.
- **Audience:** Practitioners and researchers testing message formats. [@pandeyPersuasivePowerData2014]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot ask pre-treatment attitude because it would bias exposure or is operationally impossible.
- **Reason:** The method relies on having a baseline to compute change and classify initial attitude; without it, you can’t reproduce the paper’s moderation analysis. [@pandeyPersuasivePowerData2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** More survey steps and participant time.
- **The Risk:** Small subgroup sizes (e.g., few strongly negative participants) increase uncertainty; the paper notes higher uncertainty in NP due to fewer participants. [@pandeyPersuasivePowerData2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only overall mean attitude change without looking at who started opposed vs neutral.
- **Why it fails:** You can average away meaningful, opposite-direction effects across subgroups. [@pandeyPersuasivePowerData2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Conflicting or “no effect” results despite strong changes in some participants.
- **The Test:** Plot persuasion likelihood as (+) change / no change / (-) change by initial attitude bucket and treatment, as in the paper’s analysis. [@pandeyPersuasivePowerData2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a single-item pre-attitude question aligned to the claim (same wording used post-treatment).
- **Best Fix:** Plan recruitment/assignment so you have enough participants in each initial-attitude bucket to estimate treatment effects with acceptable uncertainty. [@pandeyPersuasivePowerData2014]

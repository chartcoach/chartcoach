---
id: include-number-needed-to-treat-for-primary-prevention
title: Include Number Needed to Treat for Key Outcomes
bibliography: references.bib
description: Add number needed to treat to communicate the concrete effort required
  to prevent one event.
labels:
- chart:table
- task:decide
- visual:text
- impact:decision-support
- data:risk
- audience:expert
- domain:clinical-trials
---

## The Rule <!-- role: advice -->

For each key binary clinical endpoint, report the **number needed to treat (NNT)** over a stated time horizon alongside risk reductions.

## The Logic <!-- role: reason -->

NNT converts risk differences into an action-focused quantity (how many patients must be treated for how long to prevent one event). In the study, presenting the same myocardial infarction outcome as NNT led to lower perceived effectiveness and reduced inclination to treat compared with presenting it as risk reduction, indicating NNT meaningfully changes interpretation and decisions [@bucherInfluenceMethodReporting1994].

- **The Principle:** Converting probability changes into “patients treated per event prevented” anchors perceived impact in concrete effort.
- **The Evidence:** Ratings of effectiveness and treatment inclination were lower when the endpoint was presented as NNT rather than as relative (and also absolute) risk reduction [@bucherInfluenceMethodReporting1994].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether the benefit justifies starting therapy (especially in primary prevention).
- **Data Type:** Randomized trial results with event rates and a defined follow-up duration (so ARR and NNT can be computed).
- **Audience:** Physicians making prescribing decisions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The report does not define a time horizon or has highly variable follow-up without a clear way to express NNT over a consistent period.
- **Reason:** NNT is time-dependent; without a defined duration, it can be misleading [@bucherInfluenceMethodReporting1994] (the study’s NNT was explicitly tied to “five years”).

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires additional computation and clear specification of duration (and sometimes assumptions).
- **The Risk:** If the time horizon is omitted, readers may treat NNT as universal rather than duration-specific.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing NNT without stating “over X years” (or the follow-up period).
- **Why it fails:** The study’s questionnaire anchored NNT to “five years,” and interpretability depends on that framing [@bucherInfluenceMethodReporting1994].

## How to Check <!-- role: check -->

- **Visual Sign:** Outcomes are shown only as percentages, with no “N patients treated for T years to prevent one event.”
- **The Test:** Verify each key endpoint includes an NNT and that the duration is stated in the same sentence/row.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a single NNT line for the primary endpoint with the study’s follow-up duration.
- **Best Fix:** For each endpoint, provide ARR and NNT together with an explicit time horizon, mirroring the paired presentation tested in [@bucherInfluenceMethodReporting1994].

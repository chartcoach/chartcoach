---
id: report-absolute-risk-alongside-relative-risk
title: Report Absolute Risk Alongside Relative Risk
bibliography: references.bib
description: Always present absolute risk change together with relative risk change
  to prevent overestimation of treatment effects.
labels:
- chart:table
- task:compare
- visual:text
- impact:clarity
- data:risk
- audience:expert
- domain:clinical-trials
---

## The Rule <!-- role: advice -->

Report treatment effects as **absolute risk reduction (or absolute risk increase)** whenever you report **relative risk reduction**, rather than using relative risk alone.

## The Logic <!-- role: reason -->

Relative risk can make an intervention feel more impactful because it omits the baseline event rate; absolute risk forces the reader to account for the denominator and the “what happens without treatment” level. In a randomized survey experiment, physicians rated lipid-lowering drugs as more effective and were more inclined to treat when outcomes were presented as relative rather than absolute risk reduction, despite identical underlying data [@bucherInfluenceMethodReporting1994].

- **The Principle:** Denominator visibility changes perceived magnitude.
- **The Evidence:** Physicians’ effectiveness ratings and treatment inclination shifted downward when absolute risk reduction replaced relative risk reduction for myocardial infarction outcomes [@bucherInfluenceMethodReporting1994].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge practical clinical benefit and decide whether to treat.
- **Data Type:** Binary event outcomes from trials (e.g., myocardial infarction, mortality) where baseline risk may be low (primary prevention).
- **Audience:** Clinicians and decision-makers interpreting trial reports, summaries, or promotional materials.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You truly cannot compute absolute risks because event rates (or sufficient denominators/time horizon) are not available.
- **Reason:** Absolute risk reduction requires baseline event risk over a defined period; without it, you cannot present ARR faithfully.

## The Price <!-- role: costs -->

- **The Sacrifice:** Takes more space and requires reporting baseline risks and a time horizon.
- **The Risk:** If baseline risk is not clearly defined (population/time), ARR can be misread or misapplied.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only “X% relative risk reduction” as the headline number.
- **Why it fails:** It systematically increases perceived effectiveness and willingness to treat compared with presenting absolute effects for the same result [@bucherInfluenceMethodReporting1994].

## How to Check <!-- role: check -->

- **Visual Sign:** The results section (or figure/table) contains a relative risk reduction percentage but no “per N patients over T years” absolute change.
- **The Test:** Ask, “Could a reader infer how many events are prevented per 1000 (or per 100) over the study period?” If not, the rule is broken.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a line under each relative risk statement giving the corresponding **absolute change** (e.g., “14 fewer events per 1000 over 5 years”).
- **Best Fix:** Present both measures side-by-side for each endpoint so readers can compare consistently [@bucherInfluenceMethodReporting1994].

---
id: use-icon-arrays-even-with-absolute-risk-reduction
title: Use Icon Arrays Even When You Already Use Absolute Risk Reduction
bibliography: references.bib
description: Even with transparent numeric formats like absolute risk reduction, adding
  icon arrays further improves understanding.
labels:
- chart:icon-array
- task:communicate-risk
- task:explain-risk-reduction
- impact:comprehension
- impact:accessibility
- data:probability
- audience:general-public
- audience:low-numeracy
- custom:numeric-format:absolute-risk-reduction
- domain:health
---

## The Rule <!-- role: advice -->

When communicating treatment effects, use absolute risk reduction (ARR) and still add icon arrays as a visual supplement.

## The Logic <!-- role: reason -->

ARR improves understanding compared to relative risk reduction, but icon arrays provide additional independent gains in accuracy beyond the numeric framing. In the study, icon arrays increased comprehension in both ARR and RRR conditions (no meaningful interaction), indicating additive benefit.

- **The Principle:** Redundant, congruent encoding improves accuracy
- **The Evidence:** [@galesicUsingIconArrays2009]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly infer risk reduction from “risk without treatment” vs “risk with treatment”
- **Data Type:** Two risks (baseline and treated) meant to be compared precisely
- **Audience:** Mixed-numeracy audiences where you cannot assume strong quantitative skills

## When to Break It <!-- role: exceptions -->

- **Scenario:** The display must be extremely compact (e.g., tiny label space) and you can include only one representation.
- **Reason:** ARR alone already improves comprehension; the incremental gain from icon arrays may not justify the space in constrained layouts, though the paper does not quantify a space–benefit tradeoff [@galesicUsingIconArrays2009].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional layout space for a paired pictorial display
- **The Risk:** Users may rely on approximate visual impression rather than reading exact ARR numbers

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming ARR is “good enough” and skipping visuals for low-numeracy groups
- **Why it fails:** The study found icon arrays improved accuracy even when ARR was used [@galesicUsingIconArrays2009].

## How to Check <!-- role: check -->

- **Visual Sign:** People interpret ARR text correctly but still fail to compute or explain the implied change in a “per 1,000” question.
- **The Test:** A/B test ARR-only vs ARR+icon arrays on a simple comprehension item (counts out of 1,000).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small paired icon array next to the ARR statement.
- **Best Fix:** Keep ARR text and show two matched arrays (without/with treatment) using the same denominator and highlighting affected individuals [@galesicUsingIconArrays2009].

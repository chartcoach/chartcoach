---
id: quantify-pre-study-odds-before-testing
title: Quantify Pre-Study Odds Before Testing
bibliography: references.bib
description: Estimate the pre-study odds (R) that a relationship is true before running
  or interpreting a study.
labels:
- task:evaluate
- impact:trust
- audience:expert
- custom:research-interpretation
- custom:bayesian-thinking
---

## The Rule <!-- role: advice -->

Quantify and state the pre-study odds (R) for the relationship you are testing before you run the study or interpret its p-value.

## The Logic <!-- role: reason -->

Research findings’ truth depends not just on statistical significance, but on prior plausibility; with low R, even “significant” results have low probability of being true. The paper formalizes this using PPV as a function of R, power, and α.

- **The Principle:** Low prior odds dominate post-study credibility
- **The Evidence:** [@ioannidisWhyMostPublished2005]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge whether a claimed “positive” finding is likely true
- **Data Type:** Hypothesis-testing results (p-values/significance claims)
- **Audience:** Researchers, peer reviewers, editors

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are conducting a strictly confirmatory test of a well-established relationship with high plausibility
- **Reason:** R is already effectively high and may be less contested, though it should still be made explicit. [@ioannidisWhyMostPublished2005]

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires subjective judgment and explicit assumptions
- **The Risk:** Different stakeholders may disagree on R and debate may shift to priors. [@ioannidisWhyMostPublished2005]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating p < 0.05 as sufficient proof regardless of context
- **Why it fails:** PPV can remain low when R is low, even with “significance.” [@ioannidisWhyMostPublished2005]

## How to Check <!-- role: check -->

- **Visual Sign:** A claim is presented as “discovered” with only a p-value and no discussion of plausibility or hypothesis space
- **The Test:** Ask: “What is R for this field/question, and is it stated?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit sentence estimating whether the tested relationship is common or rare among those probed (high vs low R)
- **Best Fix:** Provide a structured justification of R (e.g., based on prior evidence and how many hypotheses are being tested in the field), and interpret the result through PPV logic. [@ioannidisWhyMostPublished2005]

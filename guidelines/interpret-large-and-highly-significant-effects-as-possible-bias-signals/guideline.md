---
id: interpret-large-and-highly-significant-effects-as-possible-bias-signals
title: Treat Extremely Strong Effects as Potential Bias Signals
bibliography: references.bib
description: In low-PPV fields, unusually large or highly significant effects may
  reflect bias more than truth.
labels:
- task:evaluate
- impact:trust
- audience:expert
- custom:bias-detection
---

## The Rule <!-- role: advice -->

In fields with low pre-study odds or high bias risk, treat unusually large and highly significant effects as prompts to investigate bias, not as automatic proof of discovery.

## The Logic <!-- role: reason -->

The paper argues that in “null fields” (or fields with very low PPV), claimed effect sizes can become accurate measures of prevailing bias; very strong/significant effects may therefore indicate large bias rather than true relationships.

- **The Principle:** In low-PPV environments, extreme significance can be a bias artifact
- **The Evidence:** [@ioannidisWhyMostPublished2005]

## Where to Apply <!-- role: context -->

- **User Goal:** Sanity-check “too good to be true” results
- **Data Type:** Literatures dominated by small effects, many tests, flexible analyses, or strong incentives
- **Audience:** Critical readers, meta-researchers, peer reviewers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Domains where large effects are biologically/plausibly expected and designs are tightly controlled
- **Reason:** Large true effects can exist; the warning is context-dependent on PPV and bias conditions. [@ioannidisWhyMostPublished2005]

## The Price <!-- role: costs -->

- **The Sacrifice:** Greater scrutiny and slower acceptance of dramatic results
- **The Risk:** May dampen attention to real breakthroughs. [@ioannidisWhyMostPublished2005]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Equating “very small p-value” with “no bias”
- **Why it fails:** Bias (u) and selective reporting can generate strong-looking results. [@ioannidisWhyMostPublished2005]

## How to Check <!-- role: check -->

- **Visual Sign:** Effect sizes that seem surprisingly large relative to what the field usually supports
- **The Test:** Ask whether the field is low-R/high-flexibility/high-incentive; if yes, treat extremity as a bias audit trigger

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit bias and flexibility checks (outcome switching, subgrouping, selective reporting risk) in interpretation
- **Best Fix:** Demand replication and stronger, more standardized confirmatory designs before concluding the effect is real. [@ioannidisWhyMostPublished2005]

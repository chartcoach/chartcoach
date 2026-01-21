---
id: discount-isolated-findings-in-hot-fields
title: Discount Isolated Findings in Hot Fields
bibliography: references.bib
description: Treat single significant results as less reliable when many teams test
  the same question.
labels:
- task:evaluate
- impact:trust
- audience:expert
- custom:replication
---

## The Rule <!-- role: advice -->

In “hot” fields with many competing teams, assume isolated significant findings are less likely to be true unless supported by the total evidence.

## The Logic <!-- role: reason -->

The paper models multiple independent testing and shows PPV of an isolated finding tends to decrease as more teams conduct studies, because the probability that at least one study reports significance increases even when no true relationship exists.

- **The Principle:** Multiple independent shots increase the chance of at least one false “hit” being published/emphasized
- **The Evidence:** [@ioannidisWhyMostPublished2005]

## Where to Apply <!-- role: context -->

- **User Goal:** Evaluate headline “breakthrough” claims
- **Data Type:** Literatures with many parallel studies and rapid publication cycles
- **Audience:** Journalists, reviewers, funders, researchers surveying a field

## When to Break It <!-- role: exceptions -->

- **Scenario:** Coordinated, preplanned multi-study programs where all results are synthesized and nulls are visible
- **Reason:** The distortion from “at least one significant” emphasis is reduced when total evidence is considered. [@ioannidisWhyMostPublished2005]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less excitement about early results
- **The Risk:** May undervalue genuine early discoveries. [@ioannidisWhyMostPublished2005]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating the first significant study as decisive
- **Why it fails:** With many teams, “someone will find p < 0.05” becomes likely even under null. [@ioannidisWhyMostPublished2005]

## How to Check <!-- role: check -->

- **Visual Sign:** A field with many papers on the same question, but attention focuses on the one positive result
- **The Test:** Ask: “How many independent teams have tested this, and is the claim based on the totality or one outlier?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Require corroboration from additional studies before treating the claim as established
- **Best Fix:** Synthesize across studies and interpret the claim in light of the whole research record, not the most significant paper. [@ioannidisWhyMostPublished2005]

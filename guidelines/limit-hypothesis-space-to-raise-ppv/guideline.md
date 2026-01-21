---
id: limit-hypothesis-space-to-raise-ppv
title: Limit the Hypothesis Space to Raise PPV
bibliography: references.bib
description: Reduce the number of tested relationships or increase preselection to
  improve the chance that significant findings are true.
labels:
- task:plan
- impact:trust
- audience:expert
- custom:multiplicity
---

## The Rule <!-- role: advice -->

Narrow and preselect the set of tested relationships to keep pre-study odds (R) from collapsing.

## The Logic <!-- role: reason -->

PPV depends strongly on R, the ratio of true to non-true relationships among those tested. When many relationships are tested with little preselection (discovery-oriented work), R becomes very small and PPV becomes extremely low for each claimed finding.

- **The Principle:** Massive testing lowers the fraction of true hypotheses, reducing PPV
- **The Evidence:** [@ioannidisWhyMostPublished2005]

## Where to Apply <!-- role: context -->

- **User Goal:** Design studies where “positive” findings are likely real
- **Data Type:** High-dimensional or many-hypothesis research programs
- **Audience:** Investigators planning exploratory vs confirmatory work

## When to Break It <!-- role: exceptions -->

- **Scenario:** The explicit goal is hypothesis generation/screening
- **Reason:** Broad testing can be appropriate, but findings should not be treated as established without follow-up. [@ioannidisWhyMostPublished2005]

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced breadth; may miss unexpected true relationships
- **The Risk:** Overly narrow preselection may reinforce existing prejudices. [@ioannidisWhyMostPublished2005]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Testing thousands of relationships and highlighting whichever crosses p < 0.05 as “discovered”
- **Why it fails:** Very low R makes most “discoveries” false even without overt bias. [@ioannidisWhyMostPublished2005]

## How to Check <!-- role: check -->

- **Visual Sign:** Many endpoints/contrasts tested with only a few reported “hits”
- **The Test:** Ask: “How many relationships were probed, and what is the plausible ratio of true to non-true (R)?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Separate exploratory screens from confirmatory claims in reporting
- **Best Fix:** Predefine a smaller, theory-driven hypothesis set when the goal is establishing truth; treat wide screens as provisional leads. [@ioannidisWhyMostPublished2005]

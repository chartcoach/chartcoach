---
id: do-not-assume-iconic-symbols-improve-accuracy-in-aggregate-uncertainty-tasks
title: Do Not Assume Iconic Symbols Improve Accuracy in Aggregate Uncertainty Tasks
bibliography: references.bib
description: Iconic symbols do not reliably increase correctness when comparing regional
  uncertainty.
labels:
- chart:map
- task:compare
- visual:iconicity
- impact:accuracy
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Do not choose iconic uncertainty symbols expecting a consistent accuracy improvement in regional/aggregate comparison tasks.

## The Logic <!-- role: reason -->

In Experiment #2, pooled accuracy across Series #2–10 showed no significant difference between abstract and iconic symbol sets, and within-series advantages were inconsistent (sometimes abstract was significantly more accurate; sometimes iconic was) [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Iconicity affects speed more reliably than correctness in aggregation
- **The Evidence:** Experiment #2 accuracy results pooled and by series [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Selecting which region is least certain overall
- **Data Type:** Multiple points per region with ordinal uncertainty levels
- **Audience:** Users performing repeated comparisons

## When to Break It <!-- role: exceptions -->

- **Scenario:** A specific uncertainty condition in your context matches one where iconic helped in the study (e.g., some series showed iconic accuracy gains).
- **Reason:** The paper found condition-dependent differences; you should validate in-context rather than generalize [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need testing rather than relying on intuition.
- **The Risk:** Picking icons without testing can slow users without improving correctness.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Make it more pictorial so people get it right.”
- **Why it fails:** The study’s aggregation task did not show a reliable accuracy lift from iconicity overall [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Accuracy remains unchanged while response time increases after switching to icons.
- **The Test:** A/B test abstract vs iconic using the same region configurations and measure both accuracy and RT.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Revert to the abstract winner for the uncertainty condition.
- **Best Fix:** Use iconicity only where it demonstrably improves your users’ accuracy for your specific uncertainty condition and task [@maceachrenVisualSemioticsUncertainty2012].

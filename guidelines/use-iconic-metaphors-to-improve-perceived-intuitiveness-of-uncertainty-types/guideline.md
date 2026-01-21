---
id: use-iconic-metaphors-to-improve-perceived-intuitiveness-of-uncertainty-types
title: Use Iconic Metaphors to Improve Perceived Intuitiveness of Uncertainty Types
bibliography: references.bib
description: Prefer iconic symbol sets when the goal is for users to feel a logical
  match between symbol and uncertainty category.
labels:
- chart:map
- task:learn
- visual:iconicity
- impact:interpretability
- data:categorical
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

When you need users to distinguish qualitatively different uncertainty conditions (e.g., spatial vs temporal vs attribute; accuracy vs precision vs trustworthiness), use iconic symbol sets that prompt a metaphor aligned to that condition.

## The Logic <!-- role: reason -->

In Experiment #1, iconic symbol sets were rated slightly higher in intuitiveness than abstract ones when pooling Series #2–10, indicating that metaphor-driven sign vehicles can strengthen the perceived logical link between symbol and uncertainty category [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Metaphor-driven signification (iconic sign vehicles)
- **The Evidence:** Experiment #1 pooled difference in intuitiveness between iconic vs abstract sets [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly associating a symbol family with a specific uncertainty condition
- **Data Type:** Multiple uncertainty conditions that must be differentiated (9 conditions tested)
- **Audience:** Users who can read legends and conceptual definitions (as provided in the experiments)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary task is fast visual aggregation or scanning across dense displays.
- **Reason:** Iconic symbols generally took longer to interpret in both experiments, which can slow map-reading tasks [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Speed of interpretation.
- **The Risk:** If the metaphor is not understood, iconic symbols can confuse rather than clarify.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a clever metaphor without confirming users share it.
- **Why it fails:** The paper notes iconic symbols only work well if users understand both the uncertainty aspect and the metaphor; mismatches occurred for some designed icons [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask what the icon “stands for” or confuse uncertainty types.
- **The Test:** Run a quick matching test: show the icon set and ask users to pick which uncertainty condition it represents.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit labeling near the legend for the uncertainty condition.
- **Best Fix:** Replace the icon with a simpler metaphor or revert to an abstract encoding and rely on text/legend for the uncertainty type [@maceachrenVisualSemioticsUncertainty2012].

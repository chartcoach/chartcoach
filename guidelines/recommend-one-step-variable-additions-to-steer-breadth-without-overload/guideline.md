---
id: recommend-one-step-variable-additions-to-steer-breadth-without-overload
title: Recommend Only One Additional Variable Beyond the Selection
bibliography: references.bib
description: "Expand the user\u2019s selection by a single variable at a time to keep\
  \ recommendations interpretable and navigable."
labels:
- chart:gallery
- task:explore
- visual:faceting
- impact:comprehension
- data:multivariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

When generating suggested views, “look ahead” by adding only one non-selected variable to the user’s selected set at a time.

## The Logic <!-- role: reason -->

Restricting suggestions to one-step expansions reduces combinatorial explosion, keeps users oriented, and lowers the risk of irrelevant displays while still broadening coverage—Voyager does this by constructing variable sets U and U∪{v} for each remaining variable v [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Controlled expansion of the search space
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan plausible relationships around a current variable or pair
- **Data Type:** Tables with many columns where exhaustive combinations are infeasible
- **Audience:** Analysts browsing recommendations

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user explicitly requests higher-order interactions (e.g., exploring 4–5 variables together).
- **Reason:** One-step additions can miss multi-variable patterns unless the user repeatedly steers selections.

## The Price <!-- role: costs -->

- **The Sacrifice:** Slower access to higher-dimensional relationships.
- **The Risk:** Users may need multiple clicks to reach a desired multi-variable view.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Recommending many multi-variable combinations at once.
- **Why it fails:** It can overwhelm the gallery and make it hard for users to understand what changed between views [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Suggested charts vary across too many variables simultaneously, making the gallery feel chaotic.
- **The Test:** Ask a user to explain how two adjacent recommendations differ; if they can’t quickly say “it added X,” the step size is too large.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Generate suggestions as U∪{v} for each non-selected v and present them in a predictable order.
- **Best Fix:** Pair one-step suggestions with interactive steering (include/exclude variables and transformations) so users can iteratively walk toward more complex views [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

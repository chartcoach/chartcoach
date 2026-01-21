---
id: visualize-policy-impact-and-performance-as-scenario-comparisons
title: Visualize Policy Impact and Performance Through Scenario Comparison
bibliography: references.bib
description: Support impact analysis by visualizing policy outcomes across scenarios
  so users can evaluate and improve policies.
labels:
- task:compare
- task:evaluate
- impact:decision-making
- data:scenario
- audience:analyst
- domain:policy-modeling
- stage:impact-analysis
---

## The Rule <!-- role: advice -->

In impact analysis, visualize a policy’s potential or actual impact and performance as comparable scenarios to support iterative improvement.

## The Logic <!-- role: reason -->

The paper defines impact analysis as evaluating a designed policy’s “potential or actual impact and performance,” which “must be adequately visualized to support the policy’s further improvement” [@kohlhammerVisualizationPolicyModeling2012]. This implies scenario-based comparison as the mechanism for deciding what to adjust next.

## Where to Apply <!-- role: context -->

- **User Goal:** Assess consequences of policy options and refine the policy based on observed outcomes.
- **Data Type:** Outputs from simulation, optimization, opinion mining, and monitoring indicators.
- **Audience:** Analysts supporting decision-makers and subsequent policy revisions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** No scenario variability exists (only one fixed implementation path and one measured outcome).
- **Reason:** Comparison adds little; emphasis should be on clear reporting of the single outcome.

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires consistent scenario definitions and comparable metrics.
- **The Risk:** Poorly specified scenarios can produce misleading comparisons.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing one “best” result without exposing alternative scenarios or sensitivity.
- **Why it fails:** It blocks the iterative improvement loop implied by impact analysis in the paper [@kohlhammerVisualizationPolicyModeling2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot tell what changed between runs or options, or cannot trace outcomes back to scenario settings.
- **The Test:** Ask users to explain why scenario A differs from scenario B using only the visualization; if they can’t, comparisons aren’t supported.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add side-by-side or selectable scenario views with consistent measures.
- **Best Fix:** Couple scenario visualization to interactive analysis controls so users can adjust parameters and immediately see impact differences for refinement [@kohlhammerVisualizationPolicyModeling2012].

---
id: match-visual-approach-to-human-vs-computer-roles
title: Match the Visual Approach to Human vs. Computer Roles
bibliography: references.bib
description: Choose between information design, information visualization, semantics
  visualization, visual analytics, and KDD based on how much automation and interaction
  the task needs.
labels:
- task:choose-method
- impact:efficiency
- data:heterogeneous
- audience:analyst
- domain:policy-modeling
- complexity:variable
---

## The Rule <!-- role: advice -->

Select the visualization discipline by explicitly deciding the human vs. computer role: information design, information visualization, semantics visualization, visual analytics, or KDD—then build the system accordingly.

## The Logic <!-- role: reason -->

The paper separates methods by “the human’s and computer’s roles in the transformation from data to insight,” noting the computer’s role increases from information design to KDD while the human’s role decreases [@kohlhammerVisualizationPolicyModeling2012]. Making that choice up front prevents mismatches (for example, fully automatic KDD when interactive reasoning is needed).

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether the task is communication (briefing), interactive exploration, semantic relationship understanding, or automated discovery.
- **Data Type:** From curated summaries to massive data requiring automatic aggregation.
- **Audience:** Teams designing tools for analysts and stakeholders across a policy workflow.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single tool must cover multiple user groups and stages with different automation needs.
- **Reason:** You may need a hybrid, but still must make the role split explicit per feature, not per product.

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires clearer product scoping and may reduce “one-size-fits-all” feature bundling.
- **The Risk:** Over-segmentation can create a fragmented user experience if transitions between roles aren’t designed.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating KDD outputs as sufficient “visual analytics” because a GUI exists.
- **Why it fails:** The paper distinguishes VA as interactive visual control of analysis, while KDD uses visualization only in restricted ways such as parameter GUIs [@kohlhammerVisualizationPolicyModeling2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users either (a) only consume static results for tasks needing interaction, or (b) must manually do work the computer should automate.
- **The Test:** For each feature, answer: “Who is doing the transforming—human or computer?” If unclear, the role split is missing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Classify each view/feature into one of the five disciplines and remove or redesign mismatched interactions.
- **Best Fix:** Provide coordinated capabilities: communication artifacts (info design), interactive browsing (info vis), semantic relation views (semantics vis), interactive model steering (VA), and bounded automation where appropriate (KDD) [@kohlhammerVisualizationPolicyModeling2012].

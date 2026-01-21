---
id: analyze-rhetoric-by-editorial-layer
title: Audit Rhetorical Choices Across Editorial Layers
bibliography: references.bib
description: Evaluate framing effects by systematically checking data, visual representation,
  annotation, and interactivity decisions.
labels:
- task:review
- impact:clarity
- impact:trust
- custom:rhetoric:editorial-layers
- audience:designer
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Audit rhetoric separately at the **data**, **visual representation**, **textual annotations**, and **interactivity** layers, and document what each layer **adds, omits, or implies**.

## The Logic <!-- role: reason -->

Narrative visualizations “tell a story” through a sequence of design choices, and rhetorical effects can enter from multiple paths; separating layers makes omissions and emphases visible and analyzable.

- **The Principle:** Layered editorial judgment shapes interpretation
- **The Evidence:** [@hullmanVisualizationRhetoricFraming2011a]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how a visualization prioritizes certain interpretations
- **Data Type:** Any; especially multi-variable, high-context topics (news, policy)
- **Audience:** Designers, editors, reviewers of narrative visualization

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are doing a purely perceptual encoding check (e.g., color distinguishability only)
- **Reason:** Layer separation is overkill when the task is narrowly perceptual and not interpretive.

## The Price <!-- role: costs -->

- **The Sacrifice:** More time and documentation overhead
- **The Risk:** You may over-attribute intentionality if you treat every effect as deliberate.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reviewing only the chart encoding and ignoring annotations or interaction defaults
- **Why it fails:** The paper shows rhetoric often depends on cross-layer interaction, not a single encoding [@hullmanVisualizationRhetoricFraming2011a].

## How to Check <!-- role: check -->

- **Visual Sign:** Interpretations hinge on titles, defaults, menus, or missing context rather than the data marks
- **The Test:** List (1) what data was selected/transformed, (2) what encodings imply, (3) what annotations assert, (4) what interaction constrains—then see which interpretation becomes “most probable.”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short layer-by-layer “editorial notes” checklist to your review process.
- **Best Fix:** Produce an explicit layer map (what is omitted/emphasized at each layer) and revise the highest-impact layer first (often defaults/annotations).

---
id: design-for-bottom-up-attention
title: Design Saliency to Highlight Task-Critical Data
bibliography: references.bib
description: Use visual salience intentionally so viewers' automatic attention lands
  on task-relevant information.
labels:
- chart:general
- task:scan
- visual:salience
- impact:accuracy
- data:general
- audience:novice
- mechanism:type-1
---

## The Rule <!-- role: advice -->

Make the task-critical elements the most visually salient parts of the visualization.

## The Logic <!-- role: reason -->

Salient features capture bottom-up attention automatically (Type 1), which can either help or harm decisions depending on what is salient. The review documents that viewers fixate on salient features and may miss less-salient but crucial context, leading to biased or incorrect judgments [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Quick judgments, detection, triage, or “what should I look at?” tasks
- **Data Type:** Any visualization where some elements are more decision-relevant than others
- **Audience:** Non-experts and time-pressured decision makers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Exploratory analysis where users must freely discover patterns without being steered
- **Reason:** Over-salient cues can over-direct attention and suppress discovery of non-salient patterns [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less visual neutrality; more designer-imposed emphasis
- **The Risk:** If you misidentify what is “critical,” you will systematically bias decisions [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making the “important” area salient without confirming the task’s true decision-relevant variable
- **Why it fails:** Bottom-up attention will lock onto the wrong cue and distort downstream reasoning [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ eyes are pulled to borders, decorations, or icons rather than the data needed for the decision.
- **The Test:** Ask, “If someone looks for 1 second, what will they notice first?” If it isn’t decision-critical, you’ve likely broken the rule [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce salience of non-critical marks (e.g., soften edges/lines that are not decision-relevant).
- **Best Fix:** Redesign the encoding so the decision-relevant variable is what visually “pops” first [@padillaDecisionMakingVisualizations2018].

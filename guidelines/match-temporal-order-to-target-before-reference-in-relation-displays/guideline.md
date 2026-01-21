---
id: match-temporal-order-to-target-before-reference-in-relation-displays
title: Match Temporal Order to Target Before Reference in Relation Displays
bibliography: references.bib
description: When using staged reveals, show the target object before the reference
  to speed relation judgments.
labels:
- chart:animation
- task:match
- visual:motion
- impact:speed
- data:categorical
- audience:general
- concept:spatial-relations
---

## The Rule <!-- role: advice -->

If your design reveals two related objects sequentially (animation or progressive disclosure), reveal the object that will be the linguistic target before revealing the reference object.

## The Logic <!-- role: reason -->

Across both experiments, responses were faster when the target appeared first and the reference appeared second, matching the “target … of reference” sentence order in a sentence–picture verification task. This indicates that temporal ordering can bias attention and thus the asymmetric perceptual encoding used to verify the relation [@rothAsymmetricCodingCategorical2012].

- **The Principle:** Order-of-attention compatibility with target/reference framing
- **The Evidence:** [@rothAsymmetricCodingCategorical2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly decide whether the displayed relation matches a remembered/verbalized query
- **Data Type:** Two-object displays where one element can appear slightly before the other (staged reveal)
- **Audience:** Users doing repeated checks where milliseconds matter (high-trial tasks)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The design’s sequential reveal is used primarily to prime a response identity (e.g., “choose red/green”) rather than encode a relation.
- **Reason:** The paper cautions that for some question types, early appearance may prime identity-based responding rather than relational processing, complicating interpretation [@rothAsymmetricCodingCategorical2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to animate “for aesthetics” or to mirror other transitions.
- **The Risk:** If the sentence frame changes (target/reference swapped) but the reveal order stays fixed, you may systematically harm performance for half the prompts [@rothAsymmetricCodingCategorical2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always revealing the left/top object first regardless of the prompted target.
- **Why it fails:** The strongest, most robust effect in the paper was target-first relative to sentence target, not a fixed left/top priority [@rothAsymmetricCodingCategorical2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Performance drops specifically when the prompt’s first-mentioned object is not the first revealed object.
- **The Test:** Swap reveal order while holding everything else constant; if verification times change in the target-first direction, order is a key driver as predicted [@rothAsymmetricCodingCategorical2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Tie your reveal order to the currently active prompt/template (target-first).
- **Best Fix:** Make the reveal order adaptive to the user’s task framing (e.g., if the prompt changes from “A left of B” to “B right of A,” flip reveal order accordingly) so attention and sentence roles remain compatible [@rothAsymmetricCodingCategorical2012].

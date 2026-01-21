---
id: make-spatial-relations-target-ground-explicit
title: Make Target and Reference Roles Explicit in Spatial Relations
bibliography: references.bib
description: Treat categorical spatial relations as asymmetric by explicitly encoding
  a target (figure) and a reference (ground).
labels:
- chart:diagram
- task:describe
- visual:position
- impact:clarity
- data:categorical
- audience:general
- concept:spatial-relations
---

## The Rule <!-- role: advice -->

Assign one object as the target and the other as the reference whenever you depict or describe a categorical spatial relation (e.g., “A is left of B”), and keep that role assignment consistent across the design.

## The Logic <!-- role: reason -->

Categorical spatial relations are role-dependent: swapping the roles changes the meaning (“A above B” ≠ “B above A”). The paper argues that this asymmetry exists not only in language but also in perceptual representations of relations, likely tied to where attention is allocated [@rothAsymmetricCodingCategorical2012].

- **The Principle:** Asymmetric (target/reference) coding of relations
- **The Evidence:** [@rothAsymmetricCodingCategorical2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Determine or verify a left/right or above/below relation between two items
- **Data Type:** Two-item categorical spatial relations (left/right, above/below)
- **Audience:** Any audience interpreting relation statements or relation diagrams

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task genuinely requires a symmetric summary (e.g., only “these two are horizontally arranged,” not “which is left”).
- **Reason:** The paper’s effect is about role-based relation verification; if roles are irrelevant, enforcing them can add unnecessary structure [@rothAsymmetricCodingCategorical2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility in phrasing/labeling (you must choose a “figure” and “ground”).
- **The Risk:** If you pick an unintuitive target/reference assignment, users may experience slower verification due to a mismatch with their attention strategy [@rothAsymmetricCodingCategorical2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Alternating between “A is left of B” and “B is right of A” within the same view as if they were interchangeable.
- **Why it fails:** The paper shows role order interacts with attention and verification speed; swapping roles can disrupt compatibility between what’s cued/attended and what’s being verified [@rothAsymmetricCodingCategorical2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or re-scan between the two objects before answering “which is where.”
- **The Test:** Rewrite all relation text in one consistent role direction (same target position in the sentence) and see if the design becomes easier to follow in a quick verification pass [@rothAsymmetricCodingCategorical2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize all relation statements to one target-first form (e.g., always “Target is [direction] of Reference”).
- **Best Fix:** Add a persistent visual cue that marks the target object as the one the user should start with (see also attention-cue guideline) so perceptual encoding aligns with the linguistic framing [@rothAsymmetricCodingCategorical2012].

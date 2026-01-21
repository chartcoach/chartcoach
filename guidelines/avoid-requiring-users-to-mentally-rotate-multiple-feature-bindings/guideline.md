---
id: avoid-requiring-users-to-mentally-rotate-multiple-feature-bindings
title: Avoid Requiring Users to Mentally Rotate Multiple Feature-Part Bindings
bibliography: references.bib
description: Do not rely on users maintaining multiple feature-to-part bindings during
  mental rotation; assume capacity is about one.
labels:
- chart:diagram
- task:compare
- visual:color
- impact:accuracy
- data:categorical
- audience:novice
- domain:spatial-reasoning
- evidence:lab-study
---

## The Rule <!-- role: advice -->

Do not design tasks where users must mentally rotate an object and simultaneously keep track of which multiple visual features (e.g., colors/labels) stay attached to which parts.

## The Logic <!-- role: reason -->

- **The Principle:** Feature–part binding during mental rotation has extremely low capacity.
- **The Evidence:** In a feature-swap detection task with a rotating multi-part object, participants could maintain only ~1 feature-part correspondence (K≈1) during mental rotation, versus ~2 when the object stayed static; similar impairment occurred even when rotation was on a separate “needle” while the colored object stayed static [@xuCapacityVisualFeatures2015].

## Where to Apply <!-- role: context -->

- **User Goal:** Verify whether parts/features match after a transformation (e.g., “Is the same configuration shown after rotation?”).
- **Data Type:** Diagrams with multiple parts where identity depends on feature bindings (colors, symbols, part labels).
- **Audience:** General audiences and learners (especially in STEM-like spatial tasks).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user only needs to track a single critical feature-part binding.
- **Reason:** The paper’s results suggest one binding can be reliably maintained during rotation [@xuCapacityVisualFeatures2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less reliance on compact “rotate-in-your-head” presentations.
- **The Risk:** You may need additional views/space or interaction to avoid mental rotation demands.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more distinctive colors/symbols and still expecting users to mentally rotate and keep all attachments correct.
- **Why it fails:** The bottleneck is the ability to keep multiple bindings attached during rotation, not just discriminability of features [@xuCapacityVisualFeatures2015].

## How to Check <!-- role: check -->

- **Visual Sign:** Correctness depends on remembering “which feature was on which arm/segment” after rotation.
- **The Test:** Ask a user to answer after a brief occlusion/transition; if they often miss feature swaps except those involving one salient part, you’re overloading rotation binding capacity [@xuCapacityVisualFeatures2015].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide the post-rotation view explicitly (don’t make users imagine it).
- **Best Fix:** Avoid mental rotation entirely by showing aligned orientations (e.g., side-by-side already rotated versions) so users only compare static feature-part bindings [@xuCapacityVisualFeatures2015].

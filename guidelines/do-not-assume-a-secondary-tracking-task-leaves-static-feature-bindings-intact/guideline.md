---
id: do-not-assume-a-secondary-tracking-task-leaves-static-feature-bindings-intact
title: Do Not Combine Feature-Binding Judgments With Concurrent Spatial Tracking
bibliography: references.bib
description: "If users must track a moving element, do not expect accurate memory\
  \ for feature-to-part bindings\u2014even on a static object."
labels:
- chart:diagram
- task:monitor
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- domain:attention
- interaction:animation
---

## The Rule <!-- role: advice -->

If a task includes attentional tracking of motion (e.g., following a moving pointer/needle), do not require users to also maintain multiple feature-to-part bindings for an object at the same time.

## The Logic <!-- role: reason -->

- **The Principle:** Attentional tracking disrupts feature binding even when the bound object is static.
- **The Evidence:** When participants rotated an independent “needle” while the colored multi-part object remained static, capacity for remembering which colors belonged to which parts still collapsed to ~1 (K≈0.9), comparable to rotating the object itself [@xuCapacityVisualFeatures2015].

## Where to Apply <!-- role: context -->

- **User Goal:** Track a moving indicator and also verify identities/attachments in a diagram (e.g., “watch the pointer, and also notice if parts swapped”).
- **Data Type:** Static multi-part diagrams with features that must remain attached (colors/labels) plus any concurrently moving element.
- **Audience:** Learners and general users in interactive/animated explanations.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The binding task is trivial because there are only two parts/features (so a “swap” is always obvious).
- **Reason:** With only two parts, swap detection can be near perfect even with mental rotation demands [@xuCapacityVisualFeatures2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced ability to “teach by animation” while simultaneously testing detailed feature mappings.
- **The Risk:** You may need to separate steps (track first, bind second), which can lengthen the interaction.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the object static and assuming that eliminates the binding problem while a different element moves.
- **Why it fails:** The attentional demands of tracking (even of an unrelated moving element) are enough to degrade binding capacity [@xuCapacityVisualFeatures2015].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must watch motion and also answer questions about which features belong to which parts.
- **The Test:** Temporarily remove motion; if binding accuracy jumps, your motion/tracking component is likely consuming the needed attentional resource [@xuCapacityVisualFeatures2015].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pause motion before asking feature-binding questions.
- **Best Fix:** Split the interaction into phases: (1) motion/tracking phase, then (2) static comparison phase for feature-part bindings [@xuCapacityVisualFeatures2015].

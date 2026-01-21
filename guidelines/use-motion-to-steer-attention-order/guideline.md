---
id: use-motion-to-steer-attention-order
title: Use Motion to Steer Visual Attention Order
bibliography: references.bib
description: Use the onset and path of motion to draw gaze to key objects and control
  viewing order.
labels:
- task:guide
- visual:motion
- impact:attention
- audience:novice
- content:multimedia
- source:faraday-1997
---

## The Rule <!-- role: advice -->

Use the onset of motion to pull attention to the right object, and use the object’s motion path to control the viewing order and where viewers look next.

## The Logic <!-- role: reason -->

Motion onset captures attention and viewers tend to track moving objects; fixations are also biased toward the motion endpoint. This lets you “script” attention through the scene (e.g., users rapidly aligned to the photolyase when it appeared and tracked it).

- **The Principle:** Attentional capture and tracking by motion
- **The Evidence:** [@faradayDesigningEffectiveMultimedia1997]

## Where to Apply <!-- role: context -->

- **User Goal:** Follow a process/sequence; notice a specific object at the right moment.
- **Data Type:** Stepwise procedural/causal explanations using animated objects.
- **Audience:** Especially useful for low domain knowledge viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The moving element is not important.
- **Reason:** Viewers may track it and miss other critical information [@faradayDesigningEffectiveMultimedia1997].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced opportunity for viewers to read or inspect static elements.
- **The Risk:** Motion can “steal” attention from newly revealed labels or key state changes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding motion everywhere to make the screen feel dynamic.
- **Why it fails:** Tracking consumes attention and can suppress attention to static or newly revealed text [@faradayDesigningEffectiveMultimedia1997].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ gaze (or their descriptions) follow the moving object while they miss the intended label/state.
- **The Test:** Pause the animation at key moments and ask viewers what changed; if they can’t name the intended element, motion likely dominated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or slow non-essential motion during reading/label moments.
- **Best Fix:** Use motion only for key objects, with a planned path that ends near the next item you want viewed [@faradayDesigningEffectiveMultimedia1997].

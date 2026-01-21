---
id: do-not-hide-critical-information-in-non-top-parts-during-mental-rotation
title: Do Not Hide Critical Information in Non-Top Parts During Mental Rotation
bibliography: references.bib
description: When users must mentally rotate, assume they will track one salient part
  (often the top) and miss changes elsewhere.
labels:
- chart:diagram
- task:detect-change
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- domain:attention
- bias:top-part
---

## The Rule <!-- role: advice -->

If mental rotation is unavoidable, place the most critical feature-binding information on the single part users are most likely to track—typically the object’s top—and do not rely on users noticing changes among other parts.

## The Logic <!-- role: reason -->

- **The Principle:** During mental rotation, attention and gaze tend to “glue” to one selected part, creating a strong asymmetry in what is encoded.
- **The Evidence:** Participants detected feature swaps far better when the swap involved the top part; when swaps did not involve the top, performance was near chance in rotation and needle-rotation conditions. Eye-tracking showed participants preferentially fixated the topmost part before rotation and then tracked its imagined path [@xuCapacityVisualFeatures2015].

## Where to Apply <!-- role: context -->

- **User Goal:** Detect whether a rotated object is the “same” (no swaps/mismatches).
- **Data Type:** Multi-part objects/diagrams where parts can swap or be confused after rotation.
- **Audience:** Anyone performing mental rotation under time/attention constraints.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can externalize the rotation (animate or show aligned views) so users don’t mentally rotate.
- **Reason:** The top-part bias and single-part tracking are tied to mental rotation demands; removing mental rotation removes the need for that strategy [@xuCapacityVisualFeatures2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less balanced visual emphasis across parts.
- **The Risk:** Overemphasizing the “top” could mislead users about overall structure importance.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Evenly distributing critical labels/features across all parts while expecting equal attention during mental rotation.
- **Why it fails:** Users tend to allocate attention to one part (often the top) and may miss swaps elsewhere [@xuCapacityVisualFeatures2015].

## How to Check <!-- role: check -->

- **Visual Sign:** Users reliably answer correctly when changes touch one salient part, but miss changes elsewhere.
- **The Test:** Create two swap types—swaps involving the top vs not; if detection collapses for non-top swaps, your design depends on attention users won’t have during rotation [@xuCapacityVisualFeatures2015].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the most important discriminating feature/label to the top part (or the part you explicitly cue users to track).
- **Best Fix:** Remove the need for mental rotation by presenting the rotated result explicitly or by aligning orientations for direct static comparison [@xuCapacityVisualFeatures2015].

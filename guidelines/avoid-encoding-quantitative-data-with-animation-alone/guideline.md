---
id: avoid-encoding-quantitative-data-with-animation-alone
title: Avoid Encoding Quantitative Change with Animation Alone
bibliography: references.bib
description: Prefer static comparison designs over animations when users must accurately
  detect or compare changes across time.
labels:
- chart:temporal
- task:compare
- visual:motion
- impact:accuracy
- data:temporal
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not rely on animation as the only way to communicate change over time; provide a direct, viewable comparison of time points.

## The Logic <!-- role: reason -->

Animation can induce change blindness and overload attention and memory, causing viewers to miss important changes outside the focal area and to forget precise differences, as discussed in [@szafirGoodBadBiased2018].

- **The Principle:** Change blindness + limited attentional tracking in motion
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect and compare changes across multiple time points
- **Data Type:** Time series or repeated measures shown as successive frames
- **Audience:** Any audience, especially when the viewer is not explicitly guided

## When to Break It <!-- role: exceptions -->

- **Scenario:** A presenter actively narrates and directs attention to specific changes
- **Reason:** Guided attention can mitigate what viewers miss in animations, as implied by the discussion of narrated animated examples in [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced “wow factor” and cinematic storytelling
- **The Risk:** Static alternatives can take more space and may require careful layout to avoid clutter

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Speeding up/slowing down the animation to “make it clearer”
- **Why it fails:** The core issue is limited attention and recall, not just playback speed, per [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers disagree on what changed, or can’t recall differences after watching
- **The Test:** Ask a viewer to report at least two notable changes outside the most salient moving element—if they can’t, the animation is likely hiding changes (consistent with [@szafirGoodBadBiased2018])

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add small multiples (juxtaposition) of key time points
- **Best Fix:** Replace the animation with one of: juxtaposition (small multiples), superposition (overlaid time points), or explicit encoding of change (e.g., trajectories), selecting based on how many time points and what comparisons matter, as recommended in [@szafirGoodBadBiased2018]

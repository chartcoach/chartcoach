---
id: treat-bad-3d-implementation-as-a-primary-risk-and-validate-encoding-interaction-and-lighting
title: Treat bad 3D implementation as a primary risk and validate encoding, interaction,
  and lighting
bibliography: references.bib
description: Because it is easy to build misleading or unusable 3D, explicitly validate
  encoding choice, interaction model, lighting, and text readability.
labels:
- chart:3d
- task:design
- visual:interaction
- impact:quality
- data:any
- audience:any
- custom:implementation
---

## Validate the full 3D design, not just the chart type <!-- role: advice -->

When you choose 3D, explicitly validate that the encoding, interaction model, lighting, and text/label strategy together produce a real benefit rather than a degraded experience.

## Why 3D amplifies the cost of poor design decisions <!-- role: reason -->

3D introduces additional failure points—lighting, depth cues, navigation, occlusion, and text rendering—so a weak implementation can negate any theoretical representational advantage.

**Mechanism:** Each added degree of freedom increases the ways users can become disoriented, misread values, or fail to interact effectively; overall success depends on the coordinated quality of multiple design components.

**Evidence:** It is often easier to create a bad 3D implementation than a bad 2D one, including failures in encoding, interaction paradigms, lighting, and font readability, so extra care is required to ensure 3D provides net benefit [@brath3DInfoVisHere2014].

**Notes:** This guideline is about design validation, not discouraging 3D categorically.

## When this applies <!-- role: context -->

- **User Goal:** Trust and use a 3D visualization for analysis or communication.
- **Task:** Any task where 3D is considered for encoding or layout.
- **Data:** Any.
- **Chart Setting:** Interactive or static 3D renderings.
- **Audience:** Any, especially mixed-experience audiences.
- **Success Criterion:** The 3D version demonstrably improves comprehension or capability relative to feasible 2D alternatives.

## When not to follow it <!-- role: exceptions -->

This guideline has no practical exception when 3D is used. **Why:** The identified risks arise from the nature of 3D implementation itself [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More design time and iteration than a straightforward 2D chart. **Risk:** Without validation, the result may be attractive but less usable. **Mitigation:** Evaluate the visualization in the same consumption modes users will face (static exports, shared viewing, interactive use).

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Treating “make it 3D” as a simple toggle without redesigning interaction and cues. **Why it fails:** Navigation, occlusion, and depth perception issues can make the result less readable than 2D [@brath3DInfoVisHere2014].
- **Mistake:** Using poor lighting or unreadable labels in 3D. **Why it fails:** The scene loses the very cues needed to interpret 3D structure [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users prefer a screenshot of a 2D alternative for doing the task. **Quick Check:** Compare the 3D view to a 2D baseline on a representative task and see which supports faster, correct answers. **Stronger Test:** Run a small task-based evaluation covering navigation, selection, and value comparison.

## What to do instead <!-- role: fix -->

- Produce a 2D baseline and require the 3D version to outperform it on a defined task.
- Add a 3D+2D linked design so users can fall back to precise 2D reading.
- Constrain the 3D interaction model so the default view is immediately interpretable.
- Remove 3D if the primary benefit is only visceral appeal rather than analytic effectiveness.
